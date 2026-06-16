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

P1: GitHub standardization.

Current local standardization tasks:

- Add `AGENTS.md`
- Add `.gitignore`
- Add `logs/`
- Add `tools/`
- Sync `docs/AI_FACTORY_MANUAL.md` to V3.4
- Fix GitHub SSH authentication before pushing

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
