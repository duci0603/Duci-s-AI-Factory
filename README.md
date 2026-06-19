# Duci-s-AI-Factory

Personal AI factory repository.

## Goal

Build a long-running, remotely managed, auditable personal AI factory.

Infrastructure route:

```text
MacBook Air
↓
Tailscale / SSH
↓
Mac mini
↓
GitHub
↓
NAS
```

Target AI workflow:

```text
Personal message entry
↓
OpenClaw / Longxia gateway
↓
Codex App / Codex CLI / tmux
↓
Tool Chain
↓
GitHub + NAS
```

Core principle: humans make decisions; AI executes.

## Current Phase

P4: OpenClaw / Longxia trial deployment preparation, restored to the V3.4.1 manual stage.

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
- OpenClaw / Longxia: future personal message gateway, task intake, scheduling, memory carrier, and handoff layer
- Codex: engineering execution layer
- GitHub: versioned project record
- NAS: long-term knowledge and backup store

## Architecture Boundary

The host architecture is `MacBook Air -> Tailscale/SSH -> Mac mini -> GitHub -> NAS`.

OpenClaw / Longxia is not an extra host in that chain. It is the future personal gateway workflow layer that may run on the Mac mini and hand engineering tasks to Codex after approval.

The retired company-side `cc-connect` / Feishu channel must not be restored or reused. Any future gateway work must use separate personal configuration, credentials, logs, sessions, and approval rules.

See `docs/AI_FACTORY_MANUAL.md` and `docs/AI_EXECUTION_SOP.md`.

## Repository Layout

```text
Duci-s-AI-Factory/
├── AGENTS.md
├── README.md
├── .gitignore
├── agents/
├── docs/
│   ├── AI_FACTORY_MANUAL.md
│   ├── AI_EXECUTION_SOP.md
│   ├── CODEX_PERSONAL_ENTRY.md
│   └── TMUX_SOP.md
├── logs/
├── prompts/
├── scripts/
├── tools/
└── workflows/
```

## Rules

- Do not store secrets in Git.
- Do not expose SSH, VNC, personal gateways, retired company channels, or local dev ports to the public internet.
- Use Tailscale for private network access.
- Run long tasks inside tmux.
- Update logs and documentation at milestones.
- Follow `AGENTS.md` and `docs/AI_EXECUTION_SOP.md` for AI execution rules.
