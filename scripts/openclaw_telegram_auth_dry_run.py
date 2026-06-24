#!/usr/bin/env python3
"""Dry-run a future Telegram channel authorization plan.

This script is intentionally non-connecting. It does not read bot tokens, write
OpenClaw config, start the gateway, call OpenClaw channel commands, or send
messages. It only describes the minimum credential and allowlist plan that a
human may approve later.
"""

from __future__ import annotations

import argparse
import json
import shlex
from dataclasses import asdict, dataclass
from pathlib import Path


PHASE = "P5-B"
DEFAULT_ACCOUNT = "personal-telegram-bot"
DEFAULT_ENV_NAME = "OPENCLAW_TELEGRAM_BOT_TOKEN"


@dataclass
class Decision:
    status: str
    reason: str
    connection_allowed_now: bool
    may_read_credentials: bool
    may_write_openclaw_config: bool


def normalize_allowlist(values: list[str] | None) -> list[str]:
    if not values:
        return []
    normalized = []
    for value in values:
        cleaned = value.strip()
        if cleaned and cleaned not in normalized:
            normalized.append(cleaned)
    return normalized


def build_command_preview(args: argparse.Namespace) -> list[str]:
    command = [
        "openclaw",
        "channels",
        "add",
        "--channel",
        "telegram",
        "--account",
        args.account,
        "--name",
        args.name,
    ]
    if args.credential_source == "env":
        command.append("--use-env")
    elif args.credential_source == "token-file":
        command.extend(["--token-file", args.token_file])
    else:
        command.extend(["--token", "<TELEGRAM_BOT_TOKEN>"])
    return command


def decide(args: argparse.Namespace, allowlist: list[str]) -> Decision:
    if args.credential_source == "inline-placeholder":
        return Decision(
            status="hold",
            reason="inline_tokens_are_not_allowed_in_project_records",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
        )
    if args.credential_source == "token-file" and not args.token_file:
        return Decision(
            status="hold",
            reason="token_file_path_required_for_token_file_source",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
        )
    if args.credential_source == "token-file" and not Path(args.token_file).is_absolute():
        return Decision(
            status="hold",
            reason="token_file_path_must_be_absolute",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
        )
    if not allowlist:
        return Decision(
            status="needs_allowlist",
            reason="dm_only_requires_at_least_one_explicit_allowed_user",
            connection_allowed_now=False,
            may_read_credentials=False,
            may_write_openclaw_config=False,
        )
    return Decision(
        status="draft_ready",
        reason="credential_source_and_allowlist_are_defined_for_review",
        connection_allowed_now=False,
        may_read_credentials=False,
        may_write_openclaw_config=False,
    )


def build_plan(args: argparse.Namespace) -> dict:
    allowlist = normalize_allowlist(args.allow_user)
    decision = decide(args, allowlist)
    command_args = build_command_preview(args)

    return {
        "mode": "telegram_auth_dry_run_only",
        "phase": PHASE,
        "script_boundary": [
            "does_not_read_bot_token",
            "does_not_write_openclaw_config",
            "does_not_start_gateway",
            "does_not_connect_channel",
            "does_not_send_messages",
            "does_not_install_daemon",
        ],
        "channel": {
            "provider": "telegram",
            "account": args.account,
            "display_name": args.name,
            "mode": "dm_only",
            "groups_enabled": False,
        },
        "credential_plan": {
            "source": args.credential_source,
            "env_name": args.env_name if args.credential_source == "env" else None,
            "token_file_path": args.token_file if args.credential_source == "token-file" else None,
            "secret_material_present_in_output": False,
            "credential_will_be_read_now": False,
        },
        "authorization_plan": {
            "allowlist": allowlist,
            "default_policy": "deny",
            "unknown_sender_policy": "ignore_and_log_metadata_only",
            "group_message_policy": "disabled",
        },
        "future_openclaw_command_preview": {
            "command_args": command_args,
            "shell_preview": " ".join(shlex.quote(part) for part in command_args),
            "execution_allowed_now": False,
        },
        "decision": asdict(decision),
        "operator_next_step": next_step(decision),
    }


def next_step(decision: Decision) -> str:
    if decision.status == "draft_ready":
        return "Review the draft. Real channel setup still requires explicit human confirmation and a separate P5-C step."
    if decision.status == "needs_allowlist":
        return "Add at least one explicit allowed Telegram user id or handle before any future channel setup."
    return "Hold. Adjust the credential source plan before any future channel setup."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draft a Telegram channel credential and allowlist plan without connecting it.")
    parser.add_argument("--account", default=DEFAULT_ACCOUNT, help="Future OpenClaw account id.")
    parser.add_argument("--name", default="Personal Telegram Bot", help="Future OpenClaw display name.")
    parser.add_argument(
        "--credential-source",
        choices=["env", "token-file", "inline-placeholder"],
        default="env",
        help="Where the future bot token would come from. This script never reads it.",
    )
    parser.add_argument("--env-name", default=DEFAULT_ENV_NAME, help="Environment variable name for env-backed credentials.")
    parser.add_argument("--token-file", help="Absolute future token file path. The file is not read.")
    parser.add_argument("--allow-user", action="append", help="Allowed Telegram user id or handle. May be repeated.")
    parser.add_argument("--examples", action="store_true", help="Emit built-in dry-run examples.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.examples:
        examples = [
            argparse.Namespace(
                account=DEFAULT_ACCOUNT,
                name="Personal Telegram Bot",
                credential_source="env",
                env_name=DEFAULT_ENV_NAME,
                token_file=None,
                allow_user=["@your_telegram_handle"],
            ),
            argparse.Namespace(
                account=DEFAULT_ACCOUNT,
                name="Personal Telegram Bot",
                credential_source="env",
                env_name=DEFAULT_ENV_NAME,
                token_file=None,
                allow_user=[],
            ),
            argparse.Namespace(
                account=DEFAULT_ACCOUNT,
                name="Personal Telegram Bot",
                credential_source="inline-placeholder",
                env_name=DEFAULT_ENV_NAME,
                token_file=None,
                allow_user=["@your_telegram_handle"],
            ),
        ]
        print(json.dumps([build_plan(example) for example in examples], ensure_ascii=False, indent=2))
        return 0

    print(json.dumps(build_plan(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
