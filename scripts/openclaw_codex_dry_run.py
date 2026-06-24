#!/usr/bin/env python3
"""OpenClaw -> Codex dry-run packet builder.

This script is intentionally non-executing. It creates a proposed Codex handoff
packet and risk decision for future OpenClaw routing tests, but it never starts
OpenClaw, never invokes Codex, never sends messages, and never writes project
files other than its own stdout.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_REPO = "/Users/duckulacissy/Duci-s-AI-Factory"
DEFAULT_PHASE = "P4-B"


SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_\-=]{12,}"),
    re.compile(r"(OPENAI|ANTHROPIC|OPENCLAW|API)_?[A-Z_]*KEY\s*=\s*\S+", re.I),
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE) KEY"),
    re.compile(r"(password|token|secret)\s*[:=]\s*\S+", re.I),
]

RISK_RULES = [
    (
        "L3",
        "blocked",
        "destructive_or_public_exposure",
        re.compile(
            r"rm\s+-rf|git\s+reset\s+--hard|force[- ]?push|强制推送|重置仓库|"
            r"删除.*(仓库|日志|备份|目录|文件)|清空|公网|路由器|端口暴露|"
            r"公开.*(gateway|ssh|vnc)|恢复公司|cc-connect|公司.*飞书",
            re.I,
        ),
    ),
    (
        "L2",
        "needs_confirmation",
        "secret_service_or_channel",
        re.compile(
            r"api\s*key|密钥|私钥|token|password|\.env|安装|升级|npm\s+install|"
            r"brew\s+install|daemon|launchagent|启动服务|重启服务|kill|"
            r"gateway\s+(install|start|run)|channels?\s+add|接入.*(微信|telegram|slack|飞书)|"
            r"发送消息|message\s+send|付费|模型授权",
            re.I,
        ),
    ),
    (
        "L1",
        "approved_scope_only",
        "project_edit",
        re.compile(
            r"修改|更新|写入|新增|创建|编辑|提交|推送|commit|push|"
            r"docs/|logs/|scripts/|README|AGENTS\.md",
            re.I,
        ),
    ),
]


@dataclass
class Decision:
    risk_level: str
    approval_status: str
    route: str
    reason: str
    allowed_in_p4b: bool
    may_execute_codex: bool


def redact(text: str) -> tuple[str, bool]:
    redacted = text
    found = False
    for pattern in SECRET_PATTERNS:
        if pattern.search(redacted):
            found = True
            redacted = pattern.sub("[REDACTED_SECRET]", redacted)
    return redacted, found


def slugify(text: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", text.lower())
    if not words:
        return "manual-review"
    return "-".join(words[:6])


def remove_negative_safety_phrases(text: str) -> str:
    """Avoid treating explicit safety limits as requested actions."""
    phrases = [
        "不修改文件",
        "不改文件",
        "不写文件",
        "不自动修改文件",
        "不执行真实任务",
        "不调用 Codex",
        "不调用codex",
        "不启动 gateway",
        "不启动gateway",
        "不发送消息",
    ]
    normalized = text
    for phrase in phrases:
        normalized = normalized.replace(phrase, "")
    return normalized


def classify(request: str, repo: str) -> Decision:
    if not Path(repo).is_absolute():
        return Decision("L2", "needs_confirmation", "hold", "repo_path_not_absolute", False, False)

    redacted, has_secret = redact(request)
    if has_secret:
        return Decision("L2", "needs_confirmation", "hold", "secret_like_input_redacted", False, False)

    risk_text = remove_negative_safety_phrases(redacted)
    for level, status, reason, pattern in RISK_RULES:
        if pattern.search(risk_text):
            return Decision(
                risk_level=level,
                approval_status=status,
                route="hold" if level in {"L2", "L3"} else "codex_packet_preview",
                reason=reason,
                allowed_in_p4b=level == "L1",
                may_execute_codex=False,
            )

    return Decision("L0", "dry_run_allowed", "codex_packet_preview", "read_only_or_question", True, False)


def build_packet(args: argparse.Namespace) -> dict:
    redacted_request, secret_like_input = redact(args.request)
    decision = classify(args.request, args.repo)
    today = dt.date.today().isoformat()
    task_id = args.task_id or f"{today}_{slugify(redacted_request)}"

    packet = {
        "task_id": task_id,
        "repo": args.repo,
        "phase": args.phase,
        "request": redacted_request,
        "risk_level": decision.risk_level,
        "approval_status": decision.approval_status,
        "expected_output": ["summary", "changed_files", "verification", "next_step"],
    }

    return {
        "mode": "dry_run_only",
        "script_boundary": [
            "does_not_start_gateway",
            "does_not_call_codex",
            "does_not_send_messages",
            "does_not_write_project_files",
            "does_not_read_or_store_secrets",
        ],
        "secret_like_input_redacted": secret_like_input,
        "decision": asdict(decision),
        "codex_task_packet": packet,
        "operator_next_step": next_step(decision),
    }


def next_step(decision: Decision) -> str:
    if decision.risk_level == "L0":
        return "Safe for P4-B packet preview. Keep as dry-run unless a human explicitly approves execution."
    if decision.risk_level == "L1":
        return "Project-edit packet preview only. Real Codex execution requires approved task scope."
    if decision.risk_level == "L2":
        return "Hold. Ask the user for explicit confirmation before any real action."
    return "Block by default. Only proceed if the user specifically directs this exact high-risk action."


def sample_requests() -> list[str]:
    return [
        "请总结当前项目状态和下一步，不修改文件。",
        "请更新 docs/AI_FACTORY_MANUAL.md，记录 P4-B dry-run 方案。",
        "请 rm -rf logs 并删除所有备份。",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a dry-run OpenClaw to Codex task packet.")
    parser.add_argument("--request", help="User request to classify and package.")
    parser.add_argument("--repo", default=DEFAULT_REPO, help="Target repository path.")
    parser.add_argument("--phase", default=DEFAULT_PHASE, help="Project phase label.")
    parser.add_argument("--task-id", help="Optional stable task id.")
    parser.add_argument("--examples", action="store_true", help="Emit three built-in dry-run examples.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.examples:
        outputs = []
        for request in sample_requests():
            example_args = argparse.Namespace(
                request=request,
                repo=args.repo,
                phase=args.phase,
                task_id=None,
            )
            outputs.append(build_packet(example_args))
        print(json.dumps(outputs, ensure_ascii=False, indent=2))
        return 0

    if not args.request:
        print("error: --request is required unless --examples is used", file=sys.stderr)
        return 2

    print(json.dumps(build_packet(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
