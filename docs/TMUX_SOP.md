# tmux SOP

## Purpose

tmux keeps long-running AI factory work alive when SSH disconnects.

Use one durable session for the AI factory:

```text
ai-factory
```

## Standard Layout

| Window | Name | Purpose |
|---|---|---|
| 0 | control | Project control, Git status, temporary commands. |
| 1 | codex | Codex CLI execution window. |
| 2 | gateway | OpenClaw gateway or message bridge. |
| 3 | logs | OpenClaw, Codex, and system log watching. |
| 4 | dev | npm, Python, skill, and temporary development tasks. |
| 5 | monitor | htop, disk, network, and service status checks. |

## Daily Commands

Create or enter the standard session:

```bash
tmux new -As ai-factory
```

Attach to the standard session:

```bash
tmux attach -t ai-factory
```

List sessions:

```bash
tmux ls
```

Rename the current window:

```bash
tmux rename-window control
```

Create a new named window:

```bash
tmux new-window -n codex
```

## Current Migration Status

Existing sessions found during P2 read-only check:

```text
ai-factory
factory
codex
openclaw
monitor
```

`ai-factory` has been created as the standard session with six windows:

```text
0 control
1 codex
2 gateway
3 logs
4 dev
5 monitor
```

All `ai-factory` windows currently start in:

```text
/Users/duckulacissy/Duci-s-AI-Factory
```

Old sessions still exist as rollback:

```text
factory
codex
openclaw
monitor
```

Each old session currently has one `zsh` window and no active long-running command.

Do not kill old sessions until the user confirms consolidation.

## Proposed Consolidation

1. Use `ai-factory` as the default working session.
2. Keep old sessions temporarily as rollback.
3. After confirming the new layout works, close old empty sessions.

## Safety Rules

- Do not kill sessions with running commands.
- Do not run deployment, gateway, or paid API tasks without explicit confirmation.
- Record tmux layout changes in `logs/YYYY-MM-DD.md`.
- Keep long-running services in named windows, not unnamed shells.
