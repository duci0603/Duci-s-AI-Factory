#!/usr/bin/env python3
"""Draft a future personal Feishu channel configuration sequence.

This script is preview-only. It does not run OpenClaw commands, read
credentials, write config, start the gateway, install services, probe Feishu, or
send messages. It turns the P5-F credential and authorization plan into a P5-G
setup checklist that a human may review before a separately approved real setup
step.
"""

from __future__ import annotations

import argparse
import json
import shlex
from dataclasses import asdict, dataclass

import openclaw_feishu_auth_dry_run as auth_dry_run


PHASE = "P5-G"
DEFAULT_PATCH_PATH = "/private/tmp/openclaw-personal-feishu.patch.json5"


@dataclass
class Decision:
    status: str
    reason: str
    configuration_allowed_now: bool
    may_read_credentials: bool
    may_write_openclaw_config: bool
    may_probe_provider: bool
    requires_separate_real_setup_confirmation: bool


def preview(command_args: list[str]) -> dict:
    return {
        "command_args": command_args,
        "shell_preview": " ".join(shlex.quote(part) for part in command_args),
        "execution_allowed_now": False,
    }


def auth_args_from(args: argparse.Namespace) -> argparse.Namespace:
    return argparse.Namespace(
        account=args.account,
        name=args.name,
        domain=args.domain,
        connection_mode=args.connection_mode,
        credential_source=args.credential_source,
        app_id_env=args.app_id_env,
        app_secret_env=args.app_secret_env,
        secret_file=args.secret_file,
        dm_policy=args.dm_policy,
        allow_user=args.allow_user,
        group_policy=args.group_policy,
        allow_group=args.allow_group,
        personal_only=args.personal_only,
    )


def decide(auth_plan: dict) -> Decision:
    auth_status = auth_plan["decision"]["status"]
    if auth_status != "draft_ready":
        return Decision(
            status="hold",
            reason=f"p5f_auth_plan_not_ready:{auth_status}",
            configuration_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            may_probe_provider=False,
            requires_separate_real_setup_confirmation=True,
        )
    return Decision(
        status="draft_ready",
        reason="minimal_personal_feishu_channel_configuration_sequence_ready_for_review",
        configuration_allowed_now=False,
        may_read_credentials=False,
        may_write_openclaw_config=False,
        may_probe_provider=False,
        requires_separate_real_setup_confirmation=True,
    )


def build_patch_preview(auth_plan: dict) -> dict:
    config_shape = auth_plan["future_config_preview"]["json5_shape"]
    return {
        "patch_path_preview": DEFAULT_PATCH_PATH,
        "json5_shape": config_shape,
        "contains_real_secret_material": False,
        "write_patch_file_allowed_now": False,
        "notes": [
            "This script does not write the patch file.",
            "If P5-H approves real setup, create the patch file in a controlled shell from this reviewed shape.",
            "The reviewed shape uses SecretRef placeholders only; real credentials remain in local environment variables.",
        ],
    }


def build_config_sequence(args: argparse.Namespace) -> dict:
    account = args.account
    patch_path = args.patch_path
    return {
        "preflight_command_previews": [
            preview(["openclaw", "config", "file"]),
            preview(["openclaw", "config", "validate", "--json"]),
            preview(["openclaw", "gateway", "status", "--deep", "--no-probe", "--json"]),
            preview(["openclaw", "channels", "status", "--channel", "feishu", "--json"]),
        ],
        "patch_validation_preview": preview(["openclaw", "config", "patch", "--file", patch_path, "--dry-run", "--json"]),
        "future_config_apply_preview": {
            "command": preview(["openclaw", "config", "patch", "--file", patch_path]),
            "requires_separate_confirmation": True,
            "reason": "writes_openclaw_config",
        },
        "post_config_local_verification_previews": [
            preview(["openclaw", "config", "validate", "--json"]),
            preview(["openclaw", "channels", "status", "--channel", "feishu", "--json"]),
        ],
        "credential_probe_command_preview": {
            "command": preview(["openclaw", "channels", "status", "--channel", "feishu", "--json", "--probe"]),
            "requires_separate_confirmation": True,
            "reason": "credential_probe_may_contact_feishu_provider",
        },
        "gateway_start_preview": {
            "command": preview(["openclaw", "gateway", "run", "--bind", "loopback"]),
            "requires_separate_confirmation": True,
            "reason": "starts_gateway_foreground_runtime",
        },
        "message_test_preview": {
            "description": "Send one DM from the approved personal Feishu account to the bot and verify metadata-only handling.",
            "execution_allowed_now": False,
            "requires_separate_confirmation": True,
            "reason": "contacts_real_feishu_and_sends_or_receives_messages",
        },
        "rollback_command_previews": {
            "soft_disable_channel": preview(["openclaw", "channels", "remove", "--channel", "feishu", "--account", account]),
            "delete_config": {
                "command": preview(["openclaw", "channels", "remove", "--channel", "feishu", "--account", account, "--delete"]),
                "requires_separate_confirmation": True,
                "reason": "delete_config_removes_channel_entries",
            },
        },
    }


def build_draft(args: argparse.Namespace) -> dict:
    auth_plan = auth_dry_run.build_plan(auth_args_from(args))
    decision = decide(auth_plan)
    result = {
        "mode": "feishu_channel_config_draft_only",
        "phase": PHASE,
        "script_boundary": [
            "does_not_run_openclaw_commands",
            "does_not_read_app_id",
            "does_not_read_app_secret",
            "does_not_read_verification_token",
            "does_not_read_encrypt_key",
            "does_not_read_openclaw_config",
            "does_not_write_openclaw_config",
            "does_not_write_patch_file",
            "does_not_start_gateway",
            "does_not_connect_channel",
            "does_not_probe_provider",
            "does_not_send_messages",
            "does_not_install_daemon",
            "does_not_call_codex_exec",
        ],
        "auth_plan": auth_plan,
        "decision": asdict(decision),
        "operator_next_step": next_step(decision),
    }
    if decision.status == "draft_ready":
        result["config_patch_preview"] = build_patch_preview(auth_plan)
        result["configuration_sequence"] = build_config_sequence(args)
    else:
        result["config_patch_preview"] = None
        result["configuration_sequence"] = None
    return result


def next_step(decision: Decision) -> str:
    if decision.status == "draft_ready":
        return "Review P5-G. Real Feishu channel setup remains disabled until a separate P5-H approval checklist is confirmed."
    return "Hold. Fix the P5-F credential and authorization draft before preparing real Feishu setup."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draft a personal Feishu channel setup sequence without executing it.")
    parser.add_argument("--account", default=auth_dry_run.DEFAULT_ACCOUNT, help="Future OpenClaw account id.")
    parser.add_argument("--name", default=auth_dry_run.DEFAULT_NAME, help="Future OpenClaw display name.")
    parser.add_argument("--domain", choices=["feishu", "lark"], default=auth_dry_run.DEFAULT_DOMAIN, help="Future API domain.")
    parser.add_argument("--connection-mode", choices=["websocket", "webhook"], default="websocket", help="Future event transport.")
    parser.add_argument(
        "--credential-source",
        choices=["env-secretref", "secret-file", "inline-placeholder"],
        default="env-secretref",
        help="Where future app credentials would come from. This script never reads them.",
    )
    parser.add_argument("--app-id-env", default=auth_dry_run.DEFAULT_APP_ID_ENV, help="Environment variable name for env-backed App ID.")
    parser.add_argument("--app-secret-env", default=auth_dry_run.DEFAULT_APP_SECRET_ENV, help="Environment variable name for env-backed App Secret.")
    parser.add_argument("--secret-file", help="Absolute future JSON secret file path. The file is not read.")
    parser.add_argument("--dm-policy", choices=["pairing", "allowlist", "open", "disabled"], default="allowlist", help="Future direct-message policy.")
    parser.add_argument("--allow-user", action="append", help="Allowed personal Feishu open_id, usually ou_xxx. May be repeated.")
    parser.add_argument("--group-policy", choices=["allowlist", "open", "disabled"], default="disabled", help="Future group-message policy.")
    parser.add_argument("--allow-group", action="append", help="Allowed Feishu chat_id, usually oc_xxx. Initial plan should leave this empty.")
    parser.add_argument("--personal-only", choices=["confirmed", "unconfirmed"], default="confirmed", help="Whether the personal-only boundary is confirmed.")
    parser.add_argument("--patch-path", default=DEFAULT_PATCH_PATH, help="Future reviewed config patch path. The file is not written.")
    parser.add_argument("--examples", action="store_true", help="Emit built-in setup draft examples.")
    return parser.parse_args()


def example_args(**overrides: object) -> argparse.Namespace:
    base = {
        "account": auth_dry_run.DEFAULT_ACCOUNT,
        "name": auth_dry_run.DEFAULT_NAME,
        "domain": auth_dry_run.DEFAULT_DOMAIN,
        "connection_mode": "websocket",
        "credential_source": "env-secretref",
        "app_id_env": auth_dry_run.DEFAULT_APP_ID_ENV,
        "app_secret_env": auth_dry_run.DEFAULT_APP_SECRET_ENV,
        "secret_file": None,
        "dm_policy": "allowlist",
        "allow_user": ["ou_personal_open_id_placeholder"],
        "group_policy": "disabled",
        "allow_group": None,
        "personal_only": "confirmed",
        "patch_path": DEFAULT_PATCH_PATH,
    }
    base.update(overrides)
    return argparse.Namespace(**base)


def main() -> int:
    args = parse_args()
    if args.examples:
        examples = [
            example_args(),
            example_args(allow_user=[]),
            example_args(credential_source="inline-placeholder"),
            example_args(group_policy="allowlist", allow_group=["oc_group_placeholder"]),
        ]
        print(json.dumps([build_draft(example) for example in examples], ensure_ascii=False, indent=2))
        return 0

    args.secret_file = auth_dry_run.normalize_optional(args.secret_file)
    print(json.dumps(build_draft(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
