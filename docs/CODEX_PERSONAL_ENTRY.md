# Codex Personal Entry SOP

## Purpose

This document defines how Codex belongs to the personal AI factory after retiring the company messaging channel.

Codex is the engineering execution layer for the personal AI factory. It does not depend on the company `cc-connect` / Feishu channel.

## Current Personal Entry Points

| Entry | Purpose | Notes |
|---|---|---|
| Codex App | Interactive engineering work, document work, browser or desktop verification. | Current primary personal entry. |
| Codex CLI | SSH, terminal tasks, scripts, and future automation. | Use inside the project repository and tmux. |
| tmux `ai-factory` | Durable terminal workspace. | Use fixed windows: `control`, `codex`, `gateway`, `logs`, `dev`, `monitor`; `gateway` is reserved and inactive. |
| GitHub | Project state, docs, logs, commits, and recovery history. | Do not store secrets. |

## Company Channel Retirement

The company-side `cc-connect` runtime has been retired from the personal AI factory flow.

Local retirement note:

```text
/Users/duckulacissy/Documents/Codex/2026-06-15/files-mentioned-by-the-user-ai/公司使用通道/
```

The former runtime, sessions, logs, LaunchAgent, and old sync script were permanently deleted after user confirmation on 2026-06-18. The remaining local folder is only a non-secret note that the company channel was retired.

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

Do not use the company `cc-connect` / Feishu channel as a personal AI factory gateway.

## Future Personal Gateway

There is no active personal gateway in the current official workflow. If a message gateway is needed later, create a new personal gateway configuration rather than reusing the company channel.

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
