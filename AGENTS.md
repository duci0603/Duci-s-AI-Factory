# AGENTS.md

## Project Positioning

This repository belongs to the personal AI factory project.

Core principle: humans make decisions; AI executes.

## Current Phase

P1: GitHub standardization.

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

## OpenClaw And Codex Roles

OpenClaw/Longxia receives work. Codex does the engineering work. GitHub records results. Mac mini stays online.

OpenClaw/Longxia is a gateway and memory carrier, not the main engineering agent. It should receive messages, classify tasks, trigger scripts or `codex exec`, and return summaries.

Codex is the engineering execution layer. It should read project context, edit files, run commands, inspect results, update logs, and prepare Git commits.

## Recommended Workflow

1. Read `README.md`, `docs/AI_FACTORY_MANUAL.md`, and recent files under `logs/`.
2. Run `git status --short`.
3. Identify user-owned changes and avoid overwriting them.
4. Make the smallest useful change.
5. Run relevant verification.
6. Update logs when the task changes project state.
7. Report changed files, verification, risks, and next step.

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
