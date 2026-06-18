# Codex Personal Entry SOP

## Purpose

This document defines how Codex belongs to the personal AI factory after separating the company messaging channel.

Codex is the engineering execution layer for the personal AI factory. It does not depend on the company `cc-connect` / Feishu channel.

## Current Personal Entry Points

| Entry | Purpose | Notes |
|---|---|---|
| Codex App | Interactive engineering work, document work, browser or desktop verification. | Current primary personal entry. |
| Codex CLI | SSH, terminal tasks, scripts, and future automation. | Use inside the project repository and tmux. |
| tmux `ai-factory` | Durable terminal workspace. | Use fixed windows: `control`, `codex`, `gateway`, `logs`, `dev`, `monitor`. |
| GitHub | Project state, docs, logs, commits, and recovery history. | Do not store secrets. |

## Company Channel Separation

The company-side `cc-connect` runtime has been isolated outside the personal AI factory flow.

Isolated location:

```text
/Users/duckulacissy/Documents/Codex/2026-06-15/files-mentioned-by-the-user-ai/公司使用通道/
```

The isolated company channel may contain Feishu configuration, logs, sessions, or credentials. Do not copy it into this repository.

## Personal AI Factory Rule

Use this route for personal project work:

```text
User
↓
Codex App / Codex CLI
↓
tmux ai-factory
↓
/Users/duckulacissy/Duci-s-AI-Factory
↓
GitHub
↓
NAS later
```

Do not use the company `cc-connect` / Feishu channel as the default personal AI factory gateway.

## Future Personal Gateway

If a message gateway is needed later, create a new personal gateway configuration rather than reusing the company channel.

Future gateway requirements:

- Separate config directory.
- Separate platform credentials.
- Separate logs and sessions.
- No company contacts, app IDs, app secrets, tokens, or chat history.
- Explicit approval before install, daemon setup, cron setup, or auto-sending messages.

Suggested future path:

```text
~/.ai-factory-gateway/
```

This path is only a proposal. Do not create or start it without approval.
