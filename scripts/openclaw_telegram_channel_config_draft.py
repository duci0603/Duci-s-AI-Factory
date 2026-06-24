#!/usr/bin/env python3
"""Draft a future Telegram channel configuration sequence.

This script is intentionally preview-only. It does not run OpenClaw channel
commands, read credentials, start the gateway, install services, or send
messages. It turns the P5-B credential plan into a P5-C setup checklist that a
human may review before a separately approved real setup step.
"""

from __future__ import annotations

import argparse
import json
import shlex
from dataclasses import asdict, dataclass

import openclaw_telegram_auth_dry_run as auth_dry_run


PHASE = "P5-C"


@dataclass
class Decision:
    status: str
    reason: str
    configuration_allowed_now: bool
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
        credential_source=args.credential_source,
        env_name=args.env_name,
        token_file=args.token_file,
        allow_user=args.allow_user,
    )


def decide(auth_plan: dict) -> Decision:
    auth_status = auth_plan["decision"]["status"]
    if auth_status != "draft_ready":
        return Decision(
            status="hold",
            reason=f"p5b_auth_plan_not_ready:{auth_status}",
            configuration_allowed_now=False,
            requires_separate_real_setup_confirmation=True,
        )
    return Decision(
        status="draft_ready",
        reason="minimal_channel_configuration_sequence_ready_for_review",
        configuration_allowed_now=False,
        requires_separate_real_setup_confirmation=True,
    )


def build_config_sequence(account: str) -> dict:
    return {
        "preflight_command_previews": [
            preview(["openclaw", "channels", "list", "--json"]),
            preview(["openclaw", "gateway", "status", "--deep", "--no-probe"]),
        ],
        "post_config_command_previews": [
            preview(["openclaw", "channels", "list", "--json"]),
            preview(["openclaw", "channels", "status", "--channel", "telegram", "--json"]),
        ],
        "credential_probe_command_preview": {
            "command": preview(["openclaw", "channels", "status", "--channel", "telegram", "--json", "--probe"]),
            "requires_separate_confirmation": True,
            "reason": "credential_probe_may_contact_channel_provider",
        },
        "rollback_command_previews": {
            "soft_disable": preview(["openclaw", "channels", "remove", "--channel", "telegram", "--account", account]),
            "delete_config": {
                "command": preview(["openclaw", "channels", "remove", "--channel", "telegram", "--account", account, "--delete"]),
                "requires_separate_confirmation": True,
                "reason": "delete_config_removes_channel_entries",
            },
        },
    }


def build_draft(args: argparse.Namespace) -> dict:
    auth_plan = auth_dry_run.build_plan(auth_args_from(args))
    decision = decide(auth_plan)
    result = {
        "mode": "telegram_channel_config_draft_only",
        "phase": PHASE,
        "script_boundary": [
            "does_not_run_openclaw_channel_commands",
            "does_not_read_bot_token",
            "does_not_write_openclaw_config",
            "does_not_start_gateway",
            "does_not_connect_channel",
            "does_not_send_messages",
            "does_not_install_daemon",
        ],
        "auth_plan": auth_plan,
        "decision": asdict(decision),
        "operator_next_step": next_step(decision),
    }
    if decision.status == "draft_ready":
        result["config_command_preview"] = auth_plan["future_openclaw_command_preview"]
        result["verification_and_rollback"] = build_config_sequence(args.account)
    else:
        result["config_command_preview"] = None
        result["verification_and_rollback"] = None
    return result


def next_step(decision: Decision) -> str:
    if decision.status == "draft_ready":
        return "Review the P5-C setup sequence. Real Telegram channel setup remains disabled until a separate explicit confirmation."
    return "Hold. Fix the P5-B credential and allowlist draft before preparing a real setup step."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draft a Telegram channel setup sequence without executing it.")
    parser.add_argument("--account", default=auth_dry_run.DEFAULT_ACCOUNT, help="Future OpenClaw account id.")
    parser.add_argument("--name", default="Personal Telegram Bot", help="Future OpenClaw display name.")
    parser.add_argument(
        "--credential-source",
        choices=["env", "token-file", "inline-placeholder"],
        default="env",
        help="Where the future bot token would come from. This script never reads it.",
    )
    parser.add_argument("--env-name", default=auth_dry_run.DEFAULT_ENV_NAME, help="Environment variable name for env-backed credentials.")
    parser.add_argument("--token-file", help="Absolute future token file path. The file is not read.")
    parser.add_argument("--allow-user", action="append", help="Allowed Telegram user id or handle. May be repeated.")
    parser.add_argument("--examples", action="store_true", help="Emit built-in setup draft examples.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.examples:
        examples = [
            argparse.Namespace(
                account=auth_dry_run.DEFAULT_ACCOUNT,
                name="Personal Telegram Bot",
                credential_source="env",
                env_name=auth_dry_run.DEFAULT_ENV_NAME,
                token_file=None,
                allow_user=["@your_telegram_handle"],
            ),
            argparse.Namespace(
                account=auth_dry_run.DEFAULT_ACCOUNT,
                name="Personal Telegram Bot",
                credential_source="env",
                env_name=auth_dry_run.DEFAULT_ENV_NAME,
                token_file=None,
                allow_user=[],
            ),
        ]
        print(json.dumps([build_draft(example) for example in examples], ensure_ascii=False, indent=2))
        return 0

    print(json.dumps(build_draft(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
