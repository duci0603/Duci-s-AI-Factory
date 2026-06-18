# Duci-s-AI-Factory

Personal AI factory repository.

## Goal

Build a long-running, remotely managed, auditable personal AI factory:

```text
MacBook Air
↓
Tailscale / SSH
↓
Mac mini
↓
Codex App / Codex CLI / tmux
↓
GitHub + NAS
```

Core principle: humans make decisions; AI executes.

## Current Phase

P4: retire company channel and continue with Codex-only personal AI factory.

Completed foundation:

- P1 GitHub standardization
- P2 tmux standardization
- P3 AI execution rules
- Default GitHub SSH authentication
- Standard `ai-factory` tmux session
- Company-side `cc-connect` / Feishu runtime retired and removed from the personal flow

## Core Roles

- MacBook Air: cockpit and remote control surface
- Mac mini: always-on AI factory host
- Codex: engineering execution layer
- GitHub: versioned project record
- NAS: long-term knowledge and backup store

## Personal Codex Entry

Codex belongs to the personal AI factory through Codex App, Codex CLI, tmux, and GitHub.

The company-side `cc-connect` / Feishu channel has been retired from the personal AI factory. Its old runtime, sessions, logs, and sync script were deleted after user confirmation, and it must not be used as a personal entry point.

See `docs/CODEX_PERSONAL_ENTRY.md`.

## Repository Layout

```text
Duci-s-AI-Factory/
├── AGENTS.md
├── README.md
├── .gitignore
├── agents/
├── docs/
│   └── AI_FACTORY_MANUAL.md
│   └── AI_EXECUTION_SOP.md
│   └── CODEX_PERSONAL_ENTRY.md
│   └── TMUX_SOP.md
├── logs/
├── prompts/
├── scripts/
├── tools/
└── workflows/
```

## Rules

- Do not store secrets in Git.
- Do not expose SSH, VNC, retired company channels, future message gateways, or local dev ports to the public internet.
- Use Tailscale for private network access.
- Run long tasks inside tmux.
- Update logs and documentation at milestones.
- Follow `AGENTS.md` and `docs/AI_EXECUTION_SOP.md` for AI execution rules.
