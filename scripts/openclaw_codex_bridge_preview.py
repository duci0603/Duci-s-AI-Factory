#!/usr/bin/env python3
"""Preview a future OpenClaw -> Codex CLI bridge.

This script is deliberately preview-only. It turns a dry-run task packet into a
future `codex exec` command preview, but it never executes Codex, starts
OpenClaw, sends messages, installs services, or writes project files.
"""

from __future__ import annotations

import argparse
import json
import shlex
import sys
from pathlib import Path

import openclaw_codex_dry_run as dry_run


PREVIEW_PHASE = "P4-C"


def build_codex_prompt(packet: dict) -> str:
    return "\n".join(
        [
            "You are Codex working inside the personal AI factory.",
            "",
            "Follow README.md, AGENTS.md, docs/AI_FACTORY_MANUAL.md, and docs/AI_EXECUTION_SOP.md.",
            "Do not handle secrets, expose services, install daemons, connect channels, or perform destructive actions without explicit user confirmation.",
            "",
            f"task_id: {packet['task_id']}",
            f"phase: {packet['phase']}",
            f"risk_level: {packet['risk_level']}",
            f"approval_status: {packet['approval_status']}",
            "",
            "request:",
            packet["request"],
            "",
            "expected_output:",
            "- summary",
            "- changed_files",
            "- verification",
            "- next_step",
        ]
    )


def build_bridge_preview(args: argparse.Namespace) -> dict:
    dry_args = argparse.Namespace(
        request=args.request,
        repo=args.repo,
        phase=args.source_phase,
        task_id=args.task_id,
    )
    dry_result = dry_run.build_packet(dry_args)
    packet = dry_result["codex_task_packet"]
    decision = dry_result["decision"]

    bridge = {
        "mode": "bridge_preview_only",
        "phase": PREVIEW_PHASE,
        "script_boundary": [
            "does_not_start_gateway",
            "does_not_call_codex",
            "does_not_send_messages",
            "does_not_write_project_files",
            "does_not_read_or_store_secrets",
        ],
        "source_packet": packet,
        "source_decision": decision,
    }

    if decision["risk_level"] in {"L2", "L3"}:
        bridge.update(
            {
                "bridge_decision": "hold",
                "codex_command_preview": None,
                "operator_next_step": "Do not build a Codex command for this request. Ask for explicit human confirmation or reject the task.",
            }
        )
        return bridge

    prompt = build_codex_prompt(packet)
    command_args = ["codex", "exec", "--cd", packet["repo"], prompt]
    shell_preview = " ".join(shlex.quote(part) for part in command_args)
    bridge.update(
        {
            "bridge_decision": "preview_ready",
            "codex_command_preview": {
                "command_args": command_args,
                "shell_preview": shell_preview,
                "execution_allowed_now": False,
            },
            "operator_next_step": next_step(decision["risk_level"]),
        }
    )
    return bridge


def next_step(risk_level: str) -> str:
    if risk_level == "L0":
        return "Command preview is safe to inspect. Real execution remains disabled in P4-C."
    return "Command preview is available, but real execution requires explicit approved task scope."


def sample_requests() -> list[str]:
    return [
        "请总结当前项目状态和下一步，不修改文件。",
        "请更新 docs/AI_FACTORY_MANUAL.md，记录 P4-C bridge preview 方案。",
        "请配置 token: fake-secret-value 并启动 gateway。",
        "请 rm -rf logs 并删除所有备份。",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preview an OpenClaw to Codex CLI bridge without executing it.")
    parser.add_argument("--request", help="User request to classify and convert to a Codex command preview.")
    parser.add_argument("--repo", default=dry_run.DEFAULT_REPO, help="Target repository path.")
    parser.add_argument("--source-phase", default="P4-B", help="Phase label to place into the source task packet.")
    parser.add_argument("--task-id", help="Optional stable task id.")
    parser.add_argument("--examples", action="store_true", help="Emit built-in bridge preview examples.")
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> int:
    if not Path(args.repo).is_absolute():
        print("error: --repo must be an absolute path", file=sys.stderr)
        return 2
    if not args.request and not args.examples:
        print("error: --request is required unless --examples is used", file=sys.stderr)
        return 2
    return 0


def main() -> int:
    args = parse_args()
    validation = validate_args(args)
    if validation:
        return validation

    if args.examples:
        outputs = []
        for request in sample_requests():
            example_args = argparse.Namespace(
                request=request,
                repo=args.repo,
                source_phase=args.source_phase,
                task_id=None,
            )
            outputs.append(build_bridge_preview(example_args))
        print(json.dumps(outputs, ensure_ascii=False, indent=2))
        return 0

    print(json.dumps(build_bridge_preview(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
