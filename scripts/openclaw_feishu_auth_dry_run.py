#!/usr/bin/env python3
"""Dry-run a future personal Feishu channel authorization plan.

This script is intentionally non-connecting. It does not read App ID, App
Secret, verification tokens, encryption keys, or OpenClaw config files. It does
not call OpenClaw channel commands, write config, start the gateway, install
services, or send messages. It only describes the minimum personal-only Feishu
credential and authorization plan that a human may review later.
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
from dataclasses import asdict, dataclass
from pathlib import Path


PHASE = "P5-F"
DEFAULT_ACCOUNT = "personal-feishu-bot"
DEFAULT_NAME = "Personal Feishu Bot"
DEFAULT_APP_ID_ENV = "OPENCLAW_FEISHU_APP_ID"
DEFAULT_APP_SECRET_ENV = "OPENCLAW_FEISHU_APP_SECRET"
DEFAULT_DOMAIN = "feishu"


@dataclass
class Decision:
    status: str
    reason: str
    connection_allowed_now: bool
    may_read_credentials: bool
    may_write_openclaw_config: bool
    requires_separate_channel_config_draft: bool


def normalize_list(values: list[str] | None) -> list[str]:
    if not values:
        return []
    normalized = []
    for value in values:
        cleaned = value.strip()
        if cleaned and cleaned not in normalized:
            normalized.append(cleaned)
    return normalized


def normalize_optional(value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def is_valid_env_name(value: str) -> bool:
    return re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value) is not None


def has_company_reference(values: list[str]) -> bool:
    haystack = " ".join(values).lower()
    return any(term in haystack for term in ["company", "cc-connect", "work-feishu", "corp", "tenant", "公司", "企业"])


def credential_config_preview(args: argparse.Namespace) -> dict:
    if args.credential_source == "env-secretref":
        return {
            "channels": {
                "feishu": {
                    "enabled": True,
                    "domain": args.domain,
                    "connectionMode": args.connection_mode,
                    "defaultAccount": args.account,
                    "accounts": {
                        args.account: {
                            "appId": {"source": "env", "provider": "default", "id": args.app_id_env},
                            "appSecret": {"source": "env", "provider": "default", "id": args.app_secret_env},
                            "domain": args.domain,
                            "name": args.name,
                        }
                    },
                    "dmPolicy": args.dm_policy,
                    "allowFrom": normalize_list(args.allow_user),
                    "groupPolicy": args.group_policy,
                    "groupAllowFrom": normalize_list(args.allow_group),
                    "requireMention": True,
                    "streaming": False,
                    "dynamicAgentCreation": {"enabled": False},
                }
            }
        }
    if args.credential_source == "secret-file":
        return {
            "channels": {
                "feishu": {
                    "enabled": True,
                    "domain": args.domain,
                    "connectionMode": args.connection_mode,
                    "defaultAccount": args.account,
                    "accounts": {
                        args.account: {
                            "appId": {"source": "file", "provider": "personal-feishu", "id": "app_id"},
                            "appSecret": {"source": "file", "provider": "personal-feishu", "id": "app_secret"},
                            "domain": args.domain,
                            "name": args.name,
                        }
                    },
                    "dmPolicy": args.dm_policy,
                    "allowFrom": normalize_list(args.allow_user),
                    "groupPolicy": args.group_policy,
                    "groupAllowFrom": normalize_list(args.allow_group),
                    "requireMention": True,
                    "streaming": False,
                    "dynamicAgentCreation": {"enabled": False},
                }
            },
            "secrets": {
                "providers": {
                    "personal-feishu": {
                        "source": "file",
                        "path": args.secret_file,
                        "mode": "json",
                    }
                }
            },
        }
    return {
        "channels": {
            "feishu": {
                "enabled": True,
                "domain": args.domain,
                "connectionMode": args.connection_mode,
                "defaultAccount": args.account,
                "accounts": {
                    args.account: {
                        "appId": "<PERSONAL_FEISHU_APP_ID>",
                        "appSecret": "<PERSONAL_FEISHU_APP_SECRET>",
                        "domain": args.domain,
                        "name": args.name,
                    }
                },
                "dmPolicy": args.dm_policy,
                "allowFrom": normalize_list(args.allow_user),
                "groupPolicy": args.group_policy,
                "groupAllowFrom": normalize_list(args.allow_group),
                "requireMention": True,
                "streaming": False,
                "dynamicAgentCreation": {"enabled": False},
            }
        }
    }


def future_command_preview(args: argparse.Namespace) -> dict:
    if args.credential_source == "env-secretref":
        commands = [
            [
                "openclaw",
                "config",
                "set",
                f"channels.feishu.accounts.{args.account}.appId",
                "--ref-source",
                "env",
                "--ref-provider",
                "default",
                "--ref-id",
                args.app_id_env,
                "--dry-run",
            ],
            [
                "openclaw",
                "config",
                "set",
                f"channels.feishu.accounts.{args.account}.appSecret",
                "--ref-source",
                "env",
                "--ref-provider",
                "default",
                "--ref-id",
                args.app_secret_env,
                "--dry-run",
            ],
            [
                "openclaw",
                "channels",
                "status",
                "--channel",
                "feishu",
                "--json",
            ],
        ]
    elif args.credential_source == "secret-file":
        commands = [
            [
                "openclaw",
                "config",
                "set",
                "secrets.providers.personal-feishu",
                "--provider-source",
                "file",
                "--provider-path",
                args.secret_file,
                "--provider-mode",
                "json",
                "--dry-run",
            ],
            [
                "openclaw",
                "channels",
                "status",
                "--channel",
                "feishu",
                "--json",
            ],
        ]
    else:
        commands = [
            [
                "openclaw",
                "channels",
                "login",
                "--channel",
                "feishu",
                "--account",
                args.account,
            ]
        ]
    return {
        "command_args": commands,
        "shell_preview": [" ".join(shlex.quote(part) for part in command) for command in commands],
        "execution_allowed_now": False,
    }


def decide(args: argparse.Namespace, allow_users: list[str], allow_groups: list[str]) -> Decision:
    if args.personal_only != "confirmed":
        return Decision(
            status="hold",
            reason="personal_only_boundary_not_confirmed",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    if has_company_reference([args.account, args.name, *allow_users, *allow_groups]):
        return Decision(
            status="hold",
            reason="company_feishu_or_cc_connect_reference_detected",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    if args.credential_source == "inline-placeholder":
        return Decision(
            status="hold",
            reason="inline_credentials_are_not_allowed_in_project_records",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    if args.credential_source == "env-secretref":
        if not is_valid_env_name(args.app_id_env) or not is_valid_env_name(args.app_secret_env):
            return Decision(
                status="hold",
                reason="env_secretref_names_must_be_valid_environment_variable_names",
                connection_allowed_now=False,
                may_read_credentials=False,
                may_write_openclaw_config=False,
                requires_separate_channel_config_draft=True,
            )
        if args.app_id_env == args.app_secret_env:
            return Decision(
                status="hold",
                reason="app_id_and_app_secret_must_use_distinct_env_names",
                connection_allowed_now=False,
                may_read_credentials=False,
                may_write_openclaw_config=False,
                requires_separate_channel_config_draft=True,
            )
    if args.credential_source == "secret-file":
        if not args.secret_file:
            return Decision(
                status="hold",
                reason="secret_file_path_required_for_secret_file_source",
                connection_allowed_now=False,
                may_read_credentials=False,
                may_write_openclaw_config=False,
                requires_separate_channel_config_draft=True,
            )
        if not Path(args.secret_file).is_absolute():
            return Decision(
                status="hold",
                reason="secret_file_path_must_be_absolute",
                connection_allowed_now=False,
                may_read_credentials=False,
                may_write_openclaw_config=False,
                requires_separate_channel_config_draft=True,
            )
    if args.dm_policy == "allowlist" and not allow_users:
        return Decision(
            status="needs_allowlist",
            reason="dm_allowlist_requires_at_least_one_personal_feishu_open_id",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    if args.dm_policy == "open":
        return Decision(
            status="hold",
            reason="open_dm_policy_is_not_allowed_for_first_personal_feishu_entry",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    if args.group_policy != "disabled":
        return Decision(
            status="hold",
            reason="first_personal_feishu_entry_must_keep_group_policy_disabled",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    if allow_groups:
        return Decision(
            status="hold",
            reason="group_allowlist_must_be_empty_when_group_policy_is_disabled",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
            requires_separate_channel_config_draft=True,
        )
    return Decision(
        status="draft_ready",
        reason="personal_feishu_credential_and_authorization_plan_ready_for_review",
        connection_allowed_now=False,
        may_read_credentials=False,
        may_write_openclaw_config=False,
        requires_separate_channel_config_draft=True,
    )


def build_plan(args: argparse.Namespace) -> dict:
    allow_users = normalize_list(args.allow_user)
    allow_groups = normalize_list(args.allow_group)
    decision = decide(args, allow_users, allow_groups)
    config_preview = credential_config_preview(args)

    return {
        "mode": "feishu_auth_dry_run_only",
        "phase": PHASE,
        "script_boundary": [
            "does_not_read_app_id",
            "does_not_read_app_secret",
            "does_not_read_verification_token",
            "does_not_read_encrypt_key",
            "does_not_read_openclaw_config",
            "does_not_write_openclaw_config",
            "does_not_run_openclaw_channel_commands",
            "does_not_start_gateway",
            "does_not_connect_channel",
            "does_not_send_messages",
            "does_not_install_daemon",
            "does_not_call_codex_exec",
        ],
        "local_basis": {
            "openclaw_version_minimum_from_local_docs": "2026.5.29",
            "observed_openclaw_cli_version": "2026.6.8",
            "channel_supported_by_local_cli_help": True,
            "local_docs_path": "/opt/homebrew/lib/node_modules/openclaw/docs/channels/feishu.md",
            "default_event_transport_in_local_docs": "websocket",
            "credential_fields_from_local_docs": [
                "channels.feishu.accounts.<id>.appId",
                "channels.feishu.accounts.<id>.appSecret",
            ],
            "access_control_fields_from_local_docs": [
                "channels.feishu.dmPolicy",
                "channels.feishu.allowFrom",
                "channels.feishu.groupPolicy",
                "channels.feishu.groupAllowFrom",
                "channels.feishu.requireMention",
            ],
        },
        "personal_only_boundary": {
            "status": args.personal_only,
            "company_cc_connect_reuse_allowed": False,
            "company_app_or_tenant_reuse_allowed": False,
            "restore_retired_company_runtime_allowed": False,
        },
        "channel": {
            "provider": "feishu",
            "account": args.account,
            "display_name": args.name,
            "domain": args.domain,
            "connection_mode": args.connection_mode,
            "recommended_first_mode": "manual_self_built_personal_app",
        },
        "credential_plan": {
            "source": args.credential_source,
            "app_id_env_name": args.app_id_env if args.credential_source == "env-secretref" else None,
            "app_secret_env_name": args.app_secret_env if args.credential_source == "env-secretref" else None,
            "secret_file_path": args.secret_file if args.credential_source == "secret-file" else None,
            "secret_material_present_in_output": False,
            "credential_will_be_read_now": False,
            "recommended_storage": "env SecretRef in OpenClaw config preview; real values stay only in local runtime env",
        },
        "authorization_plan": {
            "dm_policy": args.dm_policy,
            "allow_from_open_ids": allow_users,
            "default_policy": "deny",
            "unknown_sender_policy": "ignore_and_log_metadata_only_or_pairing_request_only",
            "group_policy": args.group_policy,
            "group_allow_from": allow_groups,
            "require_mention": True,
            "dynamic_agent_creation_enabled": False,
            "streaming_enabled_initially": False,
        },
        "required_personal_feishu_prework_later": [
            "Create or confirm a personal self-built Feishu/Lark bot app.",
            "Enable bot capability and required message event subscription later, after explicit approval.",
            "Use persistent connection/WebSocket as the first event transport.",
            "Collect the user's Feishu open_id through a separately approved pairing/log step; do not infer it from company data.",
        ],
        "future_config_preview": {
            "json5_shape": config_preview,
            "execution_allowed_now": False,
            "contains_real_secret_material": False,
        },
        "future_command_preview": future_command_preview(args),
        "decision": asdict(decision),
        "operator_next_step": next_step(decision),
    }


def next_step(decision: Decision) -> str:
    if decision.status == "draft_ready":
        return "Review P5-F. Real Feishu setup still requires a separate P5-G minimal channel configuration draft and explicit approval."
    if decision.status == "needs_allowlist":
        return "Add one personal Feishu open_id later, after a separately approved ID discovery/pairing step."
    return "Hold. Adjust the personal-only, credential, or access-control plan before preparing any real setup draft."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draft a personal Feishu channel credential and allowlist plan without connecting it.")
    parser.add_argument("--account", default=DEFAULT_ACCOUNT, help="Future OpenClaw account id.")
    parser.add_argument("--name", default=DEFAULT_NAME, help="Future OpenClaw display name.")
    parser.add_argument("--domain", choices=["feishu", "lark"], default=DEFAULT_DOMAIN, help="Future API domain.")
    parser.add_argument("--connection-mode", choices=["websocket", "webhook"], default="websocket", help="Future event transport.")
    parser.add_argument(
        "--credential-source",
        choices=["env-secretref", "secret-file", "inline-placeholder"],
        default="env-secretref",
        help="Where future app credentials would come from. This script never reads them.",
    )
    parser.add_argument("--app-id-env", default=DEFAULT_APP_ID_ENV, help="Environment variable name for env-backed App ID.")
    parser.add_argument("--app-secret-env", default=DEFAULT_APP_SECRET_ENV, help="Environment variable name for env-backed App Secret.")
    parser.add_argument("--secret-file", help="Absolute future JSON secret file path. The file is not read.")
    parser.add_argument("--dm-policy", choices=["pairing", "allowlist", "open", "disabled"], default="allowlist", help="Future direct-message policy.")
    parser.add_argument("--allow-user", action="append", help="Allowed personal Feishu open_id, usually ou_xxx. May be repeated.")
    parser.add_argument("--group-policy", choices=["allowlist", "open", "disabled"], default="disabled", help="Future group-message policy.")
    parser.add_argument("--allow-group", action="append", help="Allowed Feishu chat_id, usually oc_xxx. Initial plan should leave this empty.")
    parser.add_argument("--personal-only", choices=["confirmed", "unconfirmed"], default="confirmed", help="Whether the personal-only boundary is confirmed.")
    parser.add_argument("--examples", action="store_true", help="Emit built-in dry-run examples.")
    return parser.parse_args()


def example_args(**overrides: object) -> argparse.Namespace:
    base = {
        "account": DEFAULT_ACCOUNT,
        "name": DEFAULT_NAME,
        "domain": DEFAULT_DOMAIN,
        "connection_mode": "websocket",
        "credential_source": "env-secretref",
        "app_id_env": DEFAULT_APP_ID_ENV,
        "app_secret_env": DEFAULT_APP_SECRET_ENV,
        "secret_file": None,
        "dm_policy": "allowlist",
        "allow_user": ["ou_personal_open_id_placeholder"],
        "group_policy": "disabled",
        "allow_group": None,
        "personal_only": "confirmed",
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
            example_args(personal_only="unconfirmed"),
            example_args(group_policy="allowlist", allow_group=["oc_group_placeholder"]),
        ]
        print(json.dumps([build_plan(example) for example in examples], ensure_ascii=False, indent=2))
        return 0

    args.secret_file = normalize_optional(args.secret_file)
    print(json.dumps(build_plan(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
