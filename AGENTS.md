# AGENTS.md

## Project Positioning

This repository belongs to the personal AI factory project.

Core principle: humans make decisions; AI executes.

## Current Phase

P3: AI execution rules.

The next planned phases are:

1. P0: Infrastructure acceptance
2. P1: GitHub standardization
3. P2: tmux standardization
4. P3: AI execution rules
5. P4: OpenClaw trial deployment
6. P5: OpenClaw formal deployment
7. P6: NAS knowledge base
8. P7: Daily operations SOP

## Execution Rules

- Before each task, confirm the current phase, completed items, current task, risk, and next step.
- Do not rely on chat history or model memory as the source of truth.
- Important changes must update `docs/AI_FACTORY_MANUAL.md` or `logs/`.
- Do not change the core architecture without explicit approval.
- Do not introduce an alternative agent framework or execution engine without approval.
- Do not delete files, reset Git history, force-push, or overwrite user changes unless explicitly approved.
- Do not commit API keys, SSH keys, tokens, passwords, `.env` files, or private credentials.
- Any deployment, permission change, secret handling, network exposure, or destructive command requires user confirmation.

## Approval Rules

Allowed without extra approval:

- Read repository files.
- Run read-only inspection commands.
- Edit project documentation, logs, prompts, scripts, and non-secret project files within the agreed task scope.
- Commit and push changes after the user has approved the work direction.

Requires explicit user confirmation:

- Delete files or directories.
- Kill processes or tmux sessions.
- Reset, rebase, force-push, or rewrite Git history.
- Install or upgrade dependencies, CLIs, services, launch agents, or background daemons.
- Change SSH, Tailscale, VNC, firewall, reverse proxy, public URL, or port exposure.
- Handle secrets, API keys, tokens, passwords, private keys, or `.env` files.
- Start paid API usage, auto-sending messages, scheduled jobs, or long-running services.
- Change the core architecture or replace Codex/OpenClaw/GitHub/NAS roles.

Never do:

- Commit secrets or private credentials.
- Expose SSH, VNC, OpenClaw gateway, or local dev ports to the public internet.
- Revert or overwrite user changes without explicit instruction.
- Claim a task is complete without verification or a stated limitation.

## OpenClaw And Codex Roles

OpenClaw/Longxia receives work. Codex does the engineering work. GitHub records results. Mac mini stays online.

OpenClaw/Longxia is a gateway and memory carrier, not the main engineering agent. It should receive messages, classify tasks, trigger scripts or `codex exec`, and return summaries.

Codex is the engineering execution layer. It should read project context, edit files, run commands, inspect results, update logs, and prepare Git commits.

## Recommended Workflow

1. Read `README.md`, `docs/AI_FACTORY_MANUAL.md`, and recent files under `logs/`.
2. Run `git status --short`.
3. Identify user-owned changes and avoid overwriting them.
4. Confirm risk level and approval needs.
5. Make the smallest useful change.
6. Run relevant verification.
7. Update logs when the task changes project state.
8. Commit and push when appropriate.
9. Report changed files, verification, risks, and next step.

## Standard Report Format

Use this structure for milestone or deployment work:

```text
【当前阶段】
【已完成】
【进行中】
【本次执行】
【风险/需确认】
【下一步】
```

## Repository Standards

- Keep important project files in GitHub.
- Keep temporary experiments out of GitHub unless promoted intentionally.
- Preserve empty directories with `.gitkeep`.
- Keep large knowledge assets and backups in NAS, not in the Git repository.
- Keep the Word manual and `docs/AI_FACTORY_MANUAL.md` aligned at each milestone.

## Naming Rules

- Use `Duci-s-AI-Factory` as the GitHub repository name and long-term local project directory name.
- Use lowercase English plural names for repository directories: `agents/`, `docs/`, `logs/`, `prompts/`, `scripts/`, `tools/`, `workflows/`.
- Keep the machine-readable manual at `docs/AI_FACTORY_MANUAL.md`.
- Name project logs as `logs/YYYY-MM-DD.md`.
- Name scripts with lowercase English and underscores, such as `check_environment.sh`, `run_codex_task.sh`, and `build_manual.py`.
- Use `ai-factory` as the long-running tmux session name.
- Use these tmux window names when practical: `control`, `codex`, `gateway`, `logs`, `dev`, `monitor`.
- Use lowercase hyphenated Git branch names, such as `p1-github-standardization` or `docs-naming-rules`.
- Use short English imperative commit messages, such as `Add naming rules to manual`.
- Name OpenClaw/Codex engineering tasks as `YYYY-MM-DD_short-task-name`, without secrets, private account data, or long natural-language sentences.
