# AI Execution SOP

## Purpose

This SOP defines how AI work should be executed inside the personal AI factory.

Core principle:

```text
Human decides. OpenClaw receives. Codex executes. GitHub records. Mac mini stays online.
```

## Roles

| Role | Responsibility | Boundary |
|---|---|---|
| Human | Decides goals, approves risk, confirms direction. | Does not need to remember every detail. |
| OpenClaw / Longxia | Future personal gateway for message intake, task classification, memory, scheduling, and handoff to Codex. | Not the main engineering agent; must not reuse company `cc-connect` / Feishu. |
| Codex App / CLI | Reads project context, edits files, runs commands, verifies results, updates logs, prepares commits. | Must follow approval and safety rules. |
| GitHub | Stores code, docs, logs, commits, and recoverable history. | Must not store secrets. |
| Mac mini | Always-on execution host. | Should run long tasks inside tmux. |
| NAS | Long-term memory, knowledge, backups, and large files. | Does not replace Git history. |

## Architecture Boundary

The host route is:

```text
MacBook Air -> Tailscale/SSH -> Mac mini -> GitHub -> NAS
```

The AI workflow route is:

```text
Personal message entry -> OpenClaw / Longxia -> Codex -> Tool Chain -> GitHub / NAS
```

OpenClaw / Longxia is a future personal gateway layer, not a separate host between Mac mini and GitHub.

The retired company-side `cc-connect` / Feishu runtime is not part of this workflow and must not be restored or reused.

## Required Start Checklist

Before every engineering task:

1. Read `README.md`.
2. Read `AGENTS.md`.
3. Read `docs/AI_FACTORY_MANUAL.md`.
4. Read the latest relevant file under `logs/`.
5. Read `docs/DAILY_OPERATIONS_SOP.md` when the task is operational or deployment-related.
6. Run `git status --short`.
7. Identify user-owned or uncommitted changes.
8. Confirm current phase, task, risk, and next step.

## Approval Levels

### Level 0: Read-Only

Allowed without extra approval:

- Inspect files.
- Inspect Git status and diffs.
- Inspect tmux sessions.
- Inspect installed tool versions.
- Read logs and documentation.

Examples:

```bash
git status --short
tmux ls
codex --version
```

### Level 1: Low-Risk Project Edits

Allowed after the user has approved the task direction:

- Edit docs, logs, prompts, scripts, and non-secret project files.
- Create project SOP files.
- Commit and push agreed project changes.
- Create non-destructive tmux windows or sessions.

Examples:

```text
Update docs/TMUX_SOP.md
Add logs/YYYY-MM-DD.md
Commit and push a documentation update
```

### Level 2: Requires Explicit Confirmation

Ask before doing:

- Delete files or directories.
- Kill tmux sessions or processes.
- Install or upgrade dependencies, CLIs, daemons, or launch agents.
- Start, stop, or restart long-running services.
- Change SSH, Tailscale, VNC, firewall, reverse proxy, public URL, or port exposure.
- Change Git remotes, branch strategy, or repository visibility.
- Handle secrets, tokens, API keys, private keys, passwords, or `.env` files.
- Start paid API usage, auto-sending messages, scheduled jobs, or background automations.

### Level 3: Prohibited Unless Specifically Directed

Do not do unless the user explicitly requests the exact action:

- `git reset --hard`
- Force push.
- Rewrite shared Git history.
- Expose SSH, VNC, OpenClaw gateway, retired company channels, or local dev ports to the public internet.
- Commit secrets.
- Replace the agreed architecture or main agent/tool roles.
- Remove backups or logs.

## Standard Execution Flow

1. Confirm phase and task.
2. Inspect current state.
3. Decide approval level.
4. If needed, ask for explicit confirmation.
5. Make the smallest useful change.
6. Verify the result.
7. Update logs and documentation.
8. Commit with a short English imperative message.
9. Push to GitHub when appropriate.
10. Report result, changed files, verification, risk, and next step.

## Codex Report Format

Use this format for deployment, infrastructure, and milestone work:

```text
【当前阶段】
【已完成】
【进行中】
【本次执行】
【风险/需确认】
【下一步】
```

## OpenClaw To Codex Task Packet

When a task is handed to Codex through a future approved personal OpenClaw / Longxia gateway, use this shape:

```text
task_id: YYYY-MM-DD_short-task-name
repo: /Users/duckulacissy/Duci-s-AI-Factory
phase: P4
request: <user request>
risk_level: L0 | L1 | L2 | L3
approval_status: approved | needs_confirmation
expected_output: summary, changed_files, verification, next_step
```

Current personal gateway route is approved only for personal Feishu DM allowlist intake and must keep the local Codex `xbai` relay model route unless the user separately approves a change.

P6 NAS knowledge base is reserved but not connected yet. Do not mount NAS paths, configure retrieval, or move memory assets into NAS without a separate P6 approval.

## Codex Return Summary

Codex should return:

```text
status: completed | blocked | needs_confirmation
changed_files:
verification:
risks:
next_step:
```

## Logging Rules

- Every milestone updates `logs/YYYY-MM-DD.md`.
- Every architecture or rule change updates `docs/AI_FACTORY_MANUAL.md`.
- Every operational SOP change updates the corresponding `docs/*_SOP.md`.
- Logs should record completed work, issues, verification, and next steps.

## Git Rules

- Run `git status --short` before edits.
- Review `git diff` before commit.
- Do not include secrets.
- Use short English imperative commit messages.
- Push only after relevant verification.

Examples:

```text
Add AI execution SOP
Update OpenClaw task packet format
Document approval rules
```

## tmux Rules

- Use `ai-factory` as the only default session.
- Use fixed windows:
  - `control`
  - `codex`
  - `gateway`
  - `logs`
  - `dev`
  - `monitor`
- Treat `gateway` as the future personal OpenClaw / Longxia gateway window; it remains inactive until explicitly approved.
- Never run company `cc-connect` / Feishu in `gateway`.
- Run long tasks inside the appropriate named window.
- Do not leave long-running services in unnamed shells.

## Secret Handling

- Never print private keys, tokens, passwords, or `.env` contents into logs.
- Public SSH keys may be displayed when needed.
- Private SSH keys must not be read or copied into the project.
- If a secret is encountered, stop and ask the user how to proceed.

## Completion Standard

A task is complete only when:

- The requested work is done.
- Verification has run or the limitation is stated.
- Logs/docs are updated when project state changed.
- Git status is clean when a commit/push was expected.
- The next step is clear.
