# Daily Operations SOP

## Purpose

This SOP defines the daily operating rhythm for the personal AI factory after the personal Feishu gateway reaches P5 formal deployment acceptance.

Core operating principle:

```text
Human decides.
Feishu receives.
OpenClaw routes.
Codex executes approved engineering work.
GitHub records.
NAS is reserved for a later phase and is not connected yet.
```

## Current Scope

Active scope:

- Personal Feishu DM entry.
- OpenClaw gateway as a macOS LaunchAgent.
- Local Codex / OpenClaw model route through the `xbai` relay/intermediary provider.
- GitHub as the current source of truth for project files, docs, logs, and commits.

Reserved but not active:

- P6 NAS knowledge base.
- NAS paths, mounts, credentials, indexing, and retrieval workflows.

Out of scope unless separately approved:

- Feishu group chats.
- Expanded DM allowlist.
- Public gateway exposure.
- Model provider or base URL changes.
- Secret handling or credential rotation.
- Company `cc-connect` / Feishu reuse.

## Daily Health Check

Run these as read-only checks. Do not print secrets.

```bash
openclaw gateway status --json --require-rpc
```

Expected:

- LaunchAgent loaded/running.
- RPC OK.
- Port `18789` listening only on `127.0.0.1` and `[::1]`.
- Gateway version has no drift.

```bash
openclaw channels status --channel feishu --probe --json
```

Expected:

- Feishu channel configured.
- Feishu channel running.
- Probe OK.
- Groups remain disabled by policy.

```bash
openclaw config get agents.defaults.model --json
```

Expected:

- Primary model remains `xbai/gpt-5.5`.

```bash
git status --short
```

Expected:

- Working tree is clean, unless active work is in progress.

## Message Entry Rules

Allowed low-risk message types:

- Ask for current project phase.
- Ask for latest deployment status.
- Ask for gateway health summary.
- Ask for next step.
- Ask for a non-secret document or log summary.

Requires confirmation before execution:

- File edits.
- Git commits or pushes.
- LaunchAgent stop/start/restart/unload/remove.
- Feishu app, allowlist, group, or channel changes.
- Model provider, model name, base URL, or API shape changes.
- Any paid API usage beyond routine approved operation.
- Any task that may expose, move, edit, or rotate secrets.

Blocked unless separately approved:

- Feishu group enablement.
- Public network exposure.
- Company `cc-connect` / Feishu reuse.
- Destructive Git operations.
- Secret printing, copying into logs, or committing to Git.

## Task Forwarding Rules

Every real task passed from Feishu / OpenClaw to Codex should use this packet shape:

```text
task_id: YYYY-MM-DD_short-task-name
source: personal-feishu-dm
repo: /Users/duckulacissy/Duci-s-AI-Factory
phase: P5-MNO or later
risk_level: L0 | L1 | L2 | L3
approval_status: approved | needs_confirmation
request: <user request>
expected_output: summary, changed_files, verification, next_step
```

Risk levels:

| Level | Meaning | Action |
|---|---|---|
| L0 | Read-only status or summary | Can answer after inspection |
| L1 | Documentation/log/script edits without secrets | Can proceed after task direction is approved |
| L2 | Services, gateway, Git commit/push, external messages, paid API use | Ask before execution |
| L3 | Secrets, public exposure, destructive changes, company channel reuse | Block until explicit exact approval |

Codex return shape:

```text
status: completed | blocked | needs_confirmation
changed_files:
verification:
risks:
next_step:
```

## Logs And Git

Daily rules:

- Important project state changes go into `logs/YYYY-MM-DD.md`.
- Architecture, phase, and boundary changes go into `docs/AI_FACTORY_MANUAL.md`.
- Operational procedures go into `docs/*_SOP.md`.
- Commit and push after milestone changes, once verification passes.
- Chat history is not the source of truth.

Git checks before commit:

```bash
git diff --check
git status --short
```

Secret-pattern scans should be run before committing deployment records.

## Security Boundaries

Never record these in Git, docs, logs, screenshots, or chat:

- API keys.
- Feishu app secrets.
- Verification tokens.
- Encrypt keys.
- Gateway tokens.
- `.env` contents.
- Private SSH keys.

The non-secret model route can be recorded:

```text
provider: xbai
model: gpt-5.5
api shape: openai-responses / responses
base URL label: https://api.xbai.top/v1
```

## Incident Handling

If Feishu does not reply:

1. Check gateway status.
2. Check Feishu channel probe.
3. Check recent gateway log lines without copying secrets.
4. Check model route.
5. Ask before restarting services.

If gateway is down:

1. Record the status output summary.
2. Confirm whether LaunchAgent is loaded.
3. Confirm whether port `18789` is listening.
4. Ask before start/restart/unload actions.

If model request fails:

1. Record non-secret error summary.
2. Confirm model route is still `xbai/gpt-5.5`.
3. Do not print API keys.
4. Ask before changing provider, auth profile, or base URL.

If Git working tree is dirty:

1. Run `git status --short`.
2. Inspect diffs.
3. Do not overwrite user changes.
4. Commit only scoped, reviewed changes.

## Rollback Policy

Soft rollback requires user confirmation:

- Stop or unload the LaunchAgent.
- Confirm port `18789` is closed.
- Keep config and auth stores intact for audit.
- Record the rollback in logs and manual.

Hard rollback requires separate confirmation after soft rollback:

- Remove channel config.
- Delete LaunchAgent files.
- Rotate or remove credentials.
- Delete local auth profiles or env files.

Hard rollback is not a routine troubleshooting step.

## Weekly Maintenance

Recommended weekly checks:

- Confirm gateway and Feishu probe are healthy.
- Confirm Git working tree is clean.
- Confirm docs/manual/logs agree on current phase.
- Review gateway log size.
- Review whether any SOP drift exists.
- Defer OpenClaw upgrades unless separately approved.

## P6 NAS Placeholder

P6 NAS knowledge base is reserved but inactive.

Do not yet:

- Mount NAS paths.
- Store credentials.
- Configure indexers.
- Move project memory to NAS.
- Change retrieval workflows.

When P6 starts, it must define path layout, access policy, backup rules, retrieval scope, and secret boundaries before any technical connection.

## Completion Standard

Daily operations are healthy when:

- Gateway is running and loopback-only.
- Feishu probe is OK.
- Model route remains `xbai/gpt-5.5`.
- Working tree is clean or intentionally in progress.
- No secrets are exposed.
- Logs/manual are updated for milestone changes.
