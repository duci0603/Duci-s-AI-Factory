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
| 0 | control | Project control, Git status, temporary commands, and phase checks. |
| 1 | codex | Codex CLI execution for engineering work, file edits, and command runs. |
| 2 | gateway | Future personal OpenClaw / Longxia gateway or message bridge window. It stays inactive until explicitly approved. Never run company `cc-connect` / Feishu here. |
| 3 | logs | OpenClaw, Codex, Git, and system service log watching. |
| 4 | dev | npm, Python, skill, script testing, and temporary development tasks. |
| 5 | monitor | htop, disk, network, service status, and health checks. |

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

Final active session:

```text
ai-factory
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

Old sessions removed after user confirmation:

```text
factory
codex
openclaw
monitor
```

Use `ai-factory` as the default working session.

## Safety Rules

- Do not kill sessions with running commands.
- Do not run deployment, gateway, company-channel, paid API, or auto-send tasks without explicit confirmation.
- Record tmux layout changes in `logs/YYYY-MM-DD.md`.
- Keep long-running services in named windows, not unnamed shells.
