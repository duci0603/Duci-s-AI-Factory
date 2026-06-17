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
Codex
↓
OpenClaw gateway / tools
↓
GitHub + NAS
```

Core principle: humans make decisions; AI executes.

## Current Phase

P3: AI execution rules.

Completed foundation:

- P1 GitHub standardization
- P2 tmux standardization
- Default GitHub SSH authentication
- Standard `ai-factory` tmux session

## Core Roles

- MacBook Air: cockpit and remote control surface
- Mac mini: always-on AI factory host
- Codex: engineering execution layer
- OpenClaw/Longxia: message gateway, scheduler, old memory carrier, task forwarder
- GitHub: versioned project record
- NAS: long-term knowledge and backup store

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
│   └── TMUX_SOP.md
├── logs/
├── prompts/
├── scripts/
├── tools/
└── workflows/
```

## Rules

- Do not store secrets in Git.
- Do not expose SSH, VNC, OpenClaw gateway, or local dev ports to the public internet.
- Use Tailscale for private network access.
- Run long tasks inside tmux.
- Update logs and documentation at milestones.
- Follow `AGENTS.md` and `docs/AI_EXECUTION_SOP.md` for AI execution rules.
