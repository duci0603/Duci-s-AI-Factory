# OpenClaw Gateway SOP

## Purpose

This SOP records the daily operation, health checks, and rollback boundaries for the personal OpenClaw / Longxia gateway.

For the broader daily operating rhythm, use `docs/DAILY_OPERATIONS_SOP.md`.

Current approved shape:

```text
Personal Feishu DM
-> personal Feishu bot
-> OpenClaw gateway
-> xbai/gpt-5.5 relay model route
-> Feishu reply
```

The local Codex API route uses the `xbai` relay/intermediary provider. OpenClaw must stay aligned with that route unless the user explicitly approves a model-provider change.

## Current Service

| Item | Current value |
|---|---|
| Service manager | macOS LaunchAgent |
| LaunchAgent label | `ai.openclaw.gateway` |
| LaunchAgent file | `~/Library/LaunchAgents/ai.openclaw.gateway.plist` |
| Gateway log | `~/Library/Logs/openclaw/gateway.log` |
| Gateway port | `18789` |
| Bind boundary | loopback / local host only |
| Entry channel | personal Feishu |
| Entry scope | personal DM allowlist only |
| Groups | disabled |
| Company channel | retired; do not reuse `cc-connect` / company Feishu |

## Read-Only Health Check

Use these checks for routine observation. They must not print secrets.

```bash
openclaw gateway status --json --require-rpc
```

Expected result:

- Gateway is loaded/running.
- RPC is reachable.
- Port `18789` is listening on loopback.
- No public bind is introduced.

```bash
openclaw channels status --channel feishu --probe --json
```

Expected result:

- Feishu channel is configured.
- Feishu channel is running.
- Probe returns OK.

```bash
openclaw config get agents.defaults.model --json
```

Expected result:

- Primary model remains `xbai/gpt-5.5`.

## Log Check

Use the gateway log only for status and error inspection:

```bash
tail -n 120 ~/Library/Logs/openclaw/gateway.log
```

Do not copy secrets from local auth stores, `.env` files, or launch environment files into Git, logs, or chat.

Useful expected non-secret signals:

- `provider=xbai`
- `api=openai-responses`
- `model=gpt-5.5`
- `baseUrl=https://api.xbai.top/v1`
- HTTP `200` for successful model requests
- Feishu dispatch with `replies=1` for successful reply delivery

## Approval Boundaries

Allowed after the user approves the task direction:

- Read-only health checks.
- Git diff review.
- Documentation and log updates.
- Commit and push documentation changes.

Requires separate explicit confirmation:

- Stop, start, restart, install, unload, or remove the LaunchAgent.
- Change Feishu app credentials, app identity, DM allowlist, group policy, or event mode.
- Enable Feishu groups.
- Change model provider, model name, base URL, API shape, or auth profile.
- Read, print, move, or rewrite API keys, app secrets, verification tokens, encrypt keys, gateway secrets, or `.env` values.
- Expose the gateway outside loopback or add public networking.
- Restore or reuse company `cc-connect` / Feishu.

Never do:

- Commit secrets.
- Print secret values into manual, logs, chat, or Git.
- Reuse company Feishu configuration or old company runtime files.
- Force-push or rewrite Git history for deployment records.

## Soft Rollback

Soft rollback means disable the entry path or stop the gateway without deleting history or credentials. It requires user confirmation before execution.

Candidate soft rollback actions:

```text
1. Stop or unload the LaunchAgent.
2. Confirm port 18789 is no longer listening.
3. Confirm Feishu channel is no longer reachable through the gateway.
4. Keep config and auth stores intact for audit unless the user explicitly asks to remove them.
5. Record the rollback in logs/YYYY-MM-DD.md and docs/AI_FACTORY_MANUAL.md.
```

## Hard Rollback

Hard rollback is destructive or credential-affecting and requires a separate confirmation after soft rollback.

Examples:

- Remove Feishu channel configuration.
- Delete or rotate local gateway secrets.
- Delete LaunchAgent files.
- Remove local auth profiles.
- Remove local environment files.

Do not perform hard rollback as part of routine troubleshooting.

## Incident Notes

If a health check fails:

1. Record the command and non-secret error summary.
2. Do not print secrets.
3. Check whether the gateway is running and whether port `18789` is loopback-only.
4. Check whether the model route still says `xbai/gpt-5.5`.
5. Ask before restarting services or changing config.

## Completion Standard

A gateway operation is complete only when:

- The requested check or change is done.
- Verification has run or the limitation is stated.
- No secrets were exposed.
- Manual/log records are updated when project state changed.
- Git status is reviewed before commit.
