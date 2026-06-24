# 个人AI工厂建设手册 V3.4.2（仓库同步版）

本文件在 `个人AI工厂建设手册_V3.4.1_正式版.docx` 回滚同步基础上更新，用于 Codex、OpenClaw、Git 和日常执行。

| 文档定位 | 项目唯一真相来源（SSOT） |
| --- | --- |
| 基础设施主线 | MacBook Air → Tailscale/SSH → Mac mini → GitHub → NAS |
| AI 工作流主线 | 个人消息入口 → OpenClaw/龙虾 → Codex → Tool Chain → GitHub/NAS |
| 核心分工 | 人负责决策，AI负责执行 |
| 本版更新 | GitHub SSH修复、标准tmux会话、AI执行SOP、窗口分工、目录文件说明、P4官方资料核对、OpenClaw CLI安装记录、P4-A本地沙盒链路验证、A1-A6执行结果、A7收尾记录、P4-A收尾评估、P4-B dry-run方案与脚本、P4-C桥接预览脚本、P5-A入口选择策略、P5-B Telegram凭证授权dry-run、P5-C最小channel配置草案、P5-D真实配置审批清单、P5-E入口转向个人飞书、P5-F个人飞书凭证授权dry-run、Word手册导出记录 |
| 更新日期 | 2026-06-24 |

使用原则：不依赖聊天记录，不依赖模型记忆；所有关键状态、决策、经验、故障和下一步必须写入本手册或仓库中的同步手册。

## 第一章：文档管理原则

本手册是项目唯一真相来源（SSOT）。不再创建平行规划书。所有架构、决策、经验、故障、日志统一记录于本手册。项目推进不得依赖聊天记录或模型记忆。

从 V3.3 起，建议同时维护仓库中的 Markdown 同步版：docs/AI_FACTORY_MANUAL.md。Word 文档用于正式保存，Markdown 用于 Codex、OpenClaw、Git 版本管理和自动化读取。V3.4 进一步补充 Mac mini 常驻主机规范、OpenClaw gateway 定位、命令速查和故障排查库初版。

```text
SSOT 执行规则
任何重要变更必须至少落在一个可追溯位置：Word 正式手册、Markdown 同步手册、项目日志、Git 提交记录。聊天记录只能作为临时讨论，不作为项目状态依据。
```

## 第二章：项目目标

打造长期在线、可持续成长、可远程管理、可自主执行的个人AI工厂。原则：人负责决策，AI负责执行。

最终目标是构建真正属于自己的 AI 员工体系：消息入口负责接单，OpenClaw 负责调度，Codex 负责工程执行，工具链负责具体动作，GitHub 与 NAS 负责沉淀和追溯。

```text
V3.4 核心分工
OpenClaw/龙虾负责接活，Codex 负责干活，GitHub 负责记录，Mac mini 负责常驻。OpenClaw 不再作为复杂工程任务的主 Agent，而是消息 gateway、定时任务入口、旧记忆承载和任务转发层。
```

## 第三章：总体架构

```text
MacBook Air（驾驶舱）
↓
Tailscale
↓
SSH（主控制通道）
↓
Mac mini（AI工厂）
↓
GitHub（项目仓库与版本记录）
↓
NAS（长期记忆库与资料沉淀）
```

架构核心不是“装更多工具”，而是建立稳定的远程控制、工程执行、状态记录、知识沉淀和故障恢复闭环。

需要特别区分两条线：主机链路是 MacBook Air → Tailscale/SSH → Mac mini → GitHub → NAS；AI 工作流是 OpenClaw/龙虾 → Codex → Tool Chain。OpenClaw/龙虾不是夹在 Mac mini 和 GitHub 之间的一台主机，而是未来运行在个人体系里的 gateway 和记忆/转发层。

### 主机级架构

```text
MacBook Air：驾驶舱 / 遥控器 / 日常操作入口
Tailscale：专线网络，不暴露 SSH、VNC、gateway 和本地调试端口到公网
SSH：主控制通道
Mac mini：机房 / AI 常驻主机 / Codex 与未来 gateway 的运行环境
GitHub：版本记录与成果沉淀
NAS：长期资料、知识库、备份和大文件沉淀
```

### AI 组件架构

```text
OpenClaw/龙虾：个人消息前台与 gateway，负责微信/Telegram/Slack/个人飞书等入口、定时任务、旧记忆和任务转发
Codex：工程执行层，负责读项目、改文件、跑命令、生成 skill、维护代码
Tool Chain：脚本、CLI、skills、自动化工具和外部服务连接器
```

## 第四章：项目治理规则

本手册是唯一真相来源（SSOT）。

不依赖聊天记录推进项目。

不依赖模型记忆判断项目状态。

所有重要决策必须写入手册。

每完成一个阶段必须更新状态。

每完成一个里程碑必须记录日志。

涉及核心架构、权限、安全、密钥、远程服务暴露的变更必须先获得用户确认。

AI 可以建议修改路线，但必须说明变更内容、原因、收益、风险和迁移成本。

## 第五章：技术路线锁定机制

### 基础设施路线

```text
MacBook Air
↓
Tailscale
↓
SSH
↓
Mac mini
↓
GitHub
↓
NAS
```

### Agent 路线

```text
OpenClaw
↓
Codex
↓
Tool Chain
```

未经批准不得修改核心架构、引入替代 Agent 框架、引入替代执行引擎或改变项目主线。如建议变更，必须说明变更内容、原因、收益、风险、迁移成本，并等待批准。


### 公司通道退役说明

本次回滚恢复的是 V3.4.1 的项目阶段与目标架构：OpenClaw/龙虾作为个人 AI 工厂的目标 gateway 和记忆承载层，Codex 作为工程主执行层。

这不等于恢复公司侧 `cc-connect` / Feishu 通道。公司侧通道已经废除，旧运行目录、会话、日志、LaunchAgent 和旧同步脚本已按用户确认删除。后续如执行 P4 OpenClaw 试部署，必须使用个人专用配置、个人凭证、个人日志和独立会话，不复用公司通道。

因此，手册中出现的“飞书”只表示未来可能接入的个人消息入口类型，不代表公司 `cc-connect` / Feishu 流程。

## 第六章：项目当前状态

### 已完成

- Node.js
- Git
- Codex CLI
- Tailscale
- SSH 远程控制
- VNC 远程桌面
- GitHub 账号
- GitHub SSH 认证
- Duci-s-AI-Factory 仓库
- 本地项目骨架
- P1 GitHub 标准化
- P2 tmux 标准化
- P3 AI 执行规范固化
- 默认 GitHub SSH Key 已恢复为 ~/.ssh/id_ed25519
- 备用 GitHub SSH Key 保留为 ~/.ssh/id_ed25519_codex
- 标准 tmux session 已统一为 ai-factory
- AI 执行 SOP 已写入 docs/AI_EXECUTION_SOP.md 并推送到 GitHub
### 进行中

- P4 OpenClaw 试部署准备
- P4 安装前只读可用性检查已完成：当时未发现 `openclaw` 或 `longxia` 命令
- 官方资料核对已完成：OpenClaw 是自托管 gateway；推荐安装入口为 `npm install -g openclaw@latest`，官方 onboarding 会配置模型、workspace、Gateway、channels、daemon 和 health check
- OpenClaw CLI 已安装：`/opt/homebrew/bin/openclaw`，版本 `2026.6.8 (844f405)`
- gateway 当前未启动；A4 已完成手动启动、loopback 监听、安全关闭验证
- P4-A 本地沙盒链路验证策略已确认：先验证流程是否能安全走通，不用真实项目测试，不接真实消息入口，不自动修改文件
- A1 前置只读检查已完成；A2 沙盒边界已确认；A3 最小化本地 onboarding 已完成；A4 手动启动 gateway 已完成
- A5 只读健康检查已完成：gateway 停止、端口关闭、无 daemon / LaunchAgent、channels 未配置
- A6 最小本地安全测试已完成：gateway 可前台启动，只监听 loopback；health/status 因无 token / device identity 安全失败；测试后已 clean shutdown，端口关闭
- A7 收尾记录已完成：A6 结果写入手册和 2026-06-24 项目日志
- P4-A 收尾评估已完成：本地沙盒链路验证通过，可以关闭
- P4-B dry-run 方案已写入：先定义 OpenClaw 到 Codex 的任务包、风险分级和拦截规则
- P4-B 最小脚本已准备：`scripts/openclaw_codex_dry_run.py` 只生成 dry-run JSON，不执行 Codex、不启动 gateway、不发送消息
- P4-B smoke verification 已完成：L0/L1/L2/L3 风险分级与脱敏行为符合预期
- P4-C 本地桥接预览脚本已准备：`scripts/openclaw_codex_bridge_preview.py` 只生成未来 `codex exec` 命令预览，不执行
- P4-C 初步预演已完成：L0/L1 生成命令预览且 `execution_allowed_now=false`，L2/L3 被 hold
- P4-C 收尾评估已完成：最小桥接预览通过，可以关闭
- P5-A 入口选择策略已完成：建议首个真实个人入口采用 Telegram 个人 bot，DM-only + allowlist，不启用群聊
- P5-B Telegram 凭证与授权 dry-run 已准备：只生成 env/token-file/allowlist 方案预览，不读取 token、不接 channel
- P5-C 最小 Telegram channel 配置草案已准备：只生成 preflight、配置、验收与回滚命令预览，不执行
- P5-D 真实 Telegram channel 配置审批清单已准备：明确凭证输入、allowlist、执行窗口、验收和回滚门禁
- P5-E 入口决策已变更：用户明确不选择 Telegram 作为 gateway 入口，当前路线改为个人飞书；Telegram P5-B/C/D 保留为历史 dry-run，不进入真实配置
- P5-F 个人飞书凭证与授权 dry-run 已准备：只生成 env SecretRef、DM allowlist、groups disabled 和未来配置预览，不读取 app id / app secret、不写配置、不接 channel
- Word 手册已按当前 Markdown 同步版导出为可下载版本；导出动作不改变 OpenClaw / Telegram / 飞书真实接入状态
- 后续进入真实接入前仍不接真实消息入口、不配置模型/API授权、不安装 daemon
- 补齐 NAS 长期记忆库路径与资料分类
### 后续路线

```text
已完成：P0 基础设施验收
已完成：P1 GitHub 标准化
已完成：P2 tmux 标准化
已完成：P3 AI 执行规范固化
↓
下一步：P5-G 最小个人飞书 channel 配置草案
↓
OpenClaw 正式部署
↓
Codex 工作流
↓
NAS 长期记忆库
↓
日常运维 SOP
```

## 第七章：部署阶段与验收关卡

本手册将后续部署拆成可验收关卡。每个关卡必须有完成标准，不能只用“已经装好”作为完成判断。

| 阶段 | 目标 | 完成标准 |
| --- | --- | --- |
| P0 | 基础设施验收 | SSH、Tailscale、VNC、GitHub SSH、Codex CLI 可用；记录主机名、IP、路径和版本。 |
| P1 | GitHub 标准化 | README、.gitignore、.gitkeep、docs、logs、AGENTS.md 基础版存在；完成一次规范提交。 |
| P2 | tmux 标准化 | 固定 session 名称、窗口命名、重连方式、日志窗口和执行窗口。 |
| P3 | AI 执行规范固化 | AGENTS.md 明确安全边界、执行流程、日志规则、禁止动作和审批规则。 |
| P4 | OpenClaw 试部署 | OpenClaw 可启动，可接收测试消息，可调用本地脚本，不自动执行高风险任务。 |
| P5 | OpenClaw 正式部署 | 接入消息入口，能将工程任务转交 Codex，并回传摘要。 |
| P6 | NAS 知识库接入 | 资料分类、路径规范、备份策略和检索方式明确。 |
| P7 | 日常运维 SOP | 形成启动、停止、升级、故障排查、日志归档和恢复流程。 |

### P4 官方资料核对

官方资料来源：

- OpenClaw 官方站：https://openclaw.ai/
- OpenClaw 官方文档：https://docs.openclaw.ai/
- OpenClaw GitHub：https://github.com/openclaw/openclaw

核对结论：

- OpenClaw 定位是自托管 Gateway，连接消息入口、agent、CLI、Web Control UI 和移动节点。
- 官方要求 Node 24 推荐，Node 22.19+ 兼容；本机 Node.js 为 v26.3.0，满足版本方向，但正式安装前仍需注意包兼容性。
- 官方快速路径包括 `npm install -g openclaw@latest` 和 `openclaw onboard --install-daemon`。
- `openclaw onboard` 会涉及模型/API 授权、workspace、Gateway 端口与绑定、认证、channels、daemon、health check 和 skills。
- 官方默认 Gateway 端口为 18789；远程访问建议使用 Tailscale、trusted LAN/tailnet 或 SSH tunnel，不应公网暴露。
- 官方安全文档强调 one trusted operator boundary per gateway；个人 AI 工厂应坚持一个个人 gateway、一个个人配置边界，不复用公司通道。

保守执行策略：

1. 不使用 `curl | bash` 作为首选安装方式；优先使用更可控的 `npm install -g openclaw@latest`。
2. 安装 CLI 之前必须获得明确确认，因为它会写入全局 npm 路径。
3. 安装后先执行 `openclaw --version`、`openclaw --help`、`openclaw onboard --help`，不立即启动 gateway。
4. onboarding 前确认模型/API 授权方式、个人配置目录、Gateway 绑定方式、token 认证和是否安装 daemon。
5. P4 第一版只允许 loopback/Tailscale/SSH tunnel，不允许公网暴露，不允许自动发送消息，不允许接入公司 Feishu/cc-connect。

### P4 CLI 安装结果

已完成：

- 安装命令：`npm install -g openclaw@latest`
- 安装路径：`/opt/homebrew/bin/openclaw`
- 安装版本：`OpenClaw 2026.6.8 (844f405)`
- `openclaw --help` 可正常显示命令列表。
- `openclaw onboard --help` 可正常显示 onboarding 参数。
- `openclaw status` 显示 Gateway 为 local loopback 目标 `ws://127.0.0.1:18789`，但当前 `unreachable`。
- `openclaw gateway status` 显示 LaunchAgent not loaded / service not installed。
- `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出，说明 18789 端口未监听。
- channels 未配置，sessions 为 0。

注意：

- 仅执行 `openclaw onboard --help` 时，OpenClaw 自动创建了本地状态目录 `~/.openclaw/state/openclaw.sqlite`。这不是 gateway 启动，也不是 channel 配置，但说明 CLI 已开始使用 `~/.openclaw` 作为本地状态目录。
- CLI 输出提示 `~/.openclaw/state` 权限加固 chmod 被 macOS/Codex 沙箱拒绝，但文件权限当前为用户私有目录/文件。后续 onboarding 前应再次检查权限与配置路径。
- npm 安装提示部分 install scripts 处于 allow-scripts 待审批状态；当前未执行 `npm approve-scripts`。
- 本阶段未运行 `openclaw onboard`，未安装 daemon，未启动 gateway，未接入消息通道，未写入模型/API 密钥。

### P4-A 本地沙盒链路验证决策

日期：2026-06-20。用户确认采用 A 方案：本地沙盒模式。

目标：P4-A 验证的是 OpenClaw 本地沙盒链路能否安全走通，不是用真实项目测试 OpenClaw 或 Codex 的工程能力。

边界：

- 使用个人专用 `~/.openclaw`。
- gateway 只绑定 `127.0.0.1:18789`。
- 暂不安装 daemon / LaunchAgent。
- 暂不接微信、Telegram、Slack、个人飞书等 channels。
- 不使用公司 `cc-connect`，不复用任何公司配置。
- 不公网暴露，不打开路由器端口。
- 只使用个人 API/模型授权。
- 手动启动，测试后可停止。
- 不让 OpenClaw 自动调用 Codex 修改文件。

任务 Tree：

```text
P4-A 本地沙盒链路验证
├─ A0 决策确认：已确认采用本地沙盒模式
├─ A1 前置检查：路径、版本、端口、~/.openclaw、cc-connect 清理状态
├─ A2 沙盒边界确认：loopback、无 daemon、无 channels、无公网、无公司配置
├─ A3 onboarding：只建立个人本地配置；API/模型授权由用户确认或输入
├─ A4 手动启动 gateway：在 tmux gateway 窗口启动，不设开机自启
├─ A5 健康检查：status、gateway status、lsof、channels、sessions
├─ A6 最小安全测试：只测本地请求和状态，不执行真实工程任务
└─ A7 收尾记录：停止 gateway、确认端口关闭、更新手册和日志
```

节点确认与检测：

| 节点 | 成功标准 | 禁止事项 |
| --- | --- | --- |
| A1 前置检查 | OpenClaw CLI 可用，18789 端口未被占用或状态明确，`~/.openclaw` 状态明确，公司 `cc-connect` 不可执行。 | 不运行 `openclaw onboard`，不启动 gateway。 |
| A2 边界确认 | 明确 loopback、无 daemon、无 channels、无公网、无公司配置。 | 不改变核心边界，不接入公司通道。 |
| A3 onboarding | 只生成个人本地配置；API/模型授权由用户确认或输入。 | 不安装 daemon，不接 channels，不写入公司凭证。 |
| A4 手动启动 gateway | gateway 可由人工命令启动，运行窗口可见。 | 不设开机自启，不后台静默常驻。 |
| A5 健康检查 | `openclaw status`、`openclaw gateway status`、`lsof`、channels、sessions 状态可读。 | 不发送真实外部消息。 |
| A6 最小安全测试 | 本地测试请求或状态检查能完成，且不会自动修改文件。 | 不执行真实工程任务，不自动调用 Codex 改文件。 |
| A7 收尾记录 | gateway 可停止，端口关闭，手册和日志更新。 | 不留下未记录的后台服务。 |

执行规则：

- 只读检查可以直接执行并记录结果。
- 会写配置、启动服务、涉及 API/模型授权、安装 daemon、接入 channels 的动作，必须先再次获得用户确认。
- 本阶段验收标准是“本地沙盒链路验证完成”，不是“真实项目自动执行成功”。


### P4-A A1-A4 执行记录与手动启动结果

日期：2026-06-20 至 2026-06-23。

A1 前置只读检查结果：

| 检查项 | 结果 |
| --- | --- |
| OpenClaw 路径 | `/opt/homebrew/bin/openclaw` |
| OpenClaw 版本 | `OpenClaw 2026.6.8 (844f405)` |
| Node / npm | Node `v26.3.0`，npm `11.16.0` |
| 18789 端口 | 未监听，gateway 未启动 |
| `cc-connect` | 命令不可执行，全局包已卸载；npm 缓存仍可能保留下载记录，但不影响运行边界 |
| `~/.openclaw` | 已存在，仅个人目录 |
| `~/.openclaw/openclaw.json` | A1 时不存在；A3 后已生成 |
| LaunchAgent / daemon | 未安装 |
| channels | 未配置 |
| sessions | A1 时为 0；A3 后 session 目录为空 |

A1 结论：通过。系统具备进入本地沙盒初始化的条件，但 A2 必须确认 gateway 只允许 loopback。

A2 沙盒边界确认：

| 项目 | 决策 |
| --- | --- |
| 模式 | `local` |
| gateway 绑定 | `loopback`，只允许本机访问 |
| 端口 | `18789` |
| Tailscale | `off` |
| daemon / LaunchAgent | 跳过，不安装 |
| channels | 跳过，不接微信、Telegram、Slack、个人飞书 |
| 认证方式 | token，不允许无认证 |
| API/模型授权 | 只用个人授权；A3 最小化执行时暂时跳过模型授权 |
| workspace | 使用个人 OpenClaw workspace |
| 公司通道 | 不使用 `cc-connect`，不复用公司配置 |
| Codex 自动执行 | A 阶段不允许自动改文件 |

A3 最小化 onboarding 执行结果：

已完成：

- 生成个人本地配置：`~/.openclaw/openclaw.json`。
- 创建个人 workspace：`~/.openclaw/workspace`。
- 创建个人 session 目录：`~/.openclaw/agents/main/sessions`。
- 配置 gateway：`mode=local`、`bind=loopback`、`port=18789`、`tailscale=off`。
- 配置 gateway auth：`token`，token 使用环境变量引用 `OPENCLAW_GATEWAY_TOKEN`，配置文件不保存明文 token。

未执行：

- 未启动 gateway。
- 未安装 daemon / LaunchAgent。
- 未接 channels。
- 未写入模型 API key。
- 未复用公司配置。
- 未让 OpenClaw 自动调用 Codex 修改文件。

A3 后配置核对：

| 项目 | 结果 |
| --- | --- |
| `gateway.mode` | `local` |
| `gateway.bind` | `loopback` |
| `gateway.port` | `18789` |
| `gateway.tailscale.mode` | `off` |
| `gateway.auth.mode` | `token` |
| token 保存方式 | SecretRef 环境变量引用：`OPENCLAW_GATEWAY_TOKEN` |
| workspace | `/Users/duckulacissy/.openclaw/workspace` |
| daemon | 未安装 |
| channels | 未配置 |
| sessions | 空 |
| 18789 端口 | 未监听 |

注意：

- A3 生成的 token 是临时环境变量。A4 启动前，需要重新由用户设置或生成 `OPENCLAW_GATEWAY_TOKEN`。
- 当前不把 token 写入手册、聊天记录、GitHub 或命令历史。
- `openclaw status` 在 Codex 环境里曾出现 `unable to open database file`；`openclaw gateway status` 可读配置。A4 如遇同类问题，优先在用户普通终端或授权环境执行。

A4 手动启动 gateway 方案：

目标：临时前台启动本地 gateway，只验证监听和状态；不安装 daemon，不设开机自启，不接 channels，不做真实项目。

推荐在 `tmux` 的 `gateway` 窗口执行：

```bash
export OPENCLAW_GATEWAY_TOKEN="$(openssl rand -hex 32)"
openclaw gateway run --bind loopback --port 18789 --auth token --tailscale off
```

含义：

| 命令参数 | 含义 |
| --- | --- |
| `OPENCLAW_GATEWAY_TOKEN` | 当前窗口临时 token；不写入手册，不提交 GitHub |
| `gateway run` | 前台手动启动，关闭窗口或 `Ctrl+C` 即停止 |
| `--bind loopback` | 只允许本机访问 |
| `--port 18789` | 使用默认本地测试端口 |
| `--auth token` | 需要 token 认证 |
| `--tailscale off` | 不启用 Tailscale 暴露 |

另开窗口检测：

```bash
lsof -nP -iTCP:18789 -sTCP:LISTEN
openclaw gateway status
```

停止方式：

```text
在运行 gateway 的窗口按 Ctrl+C
```

停止后复查：

```bash
lsof -nP -iTCP:18789 -sTCP:LISTEN
```

A4 禁止事项：

- 不运行 `openclaw gateway install`。
- 不运行 `openclaw gateway start`。
- 不安装 daemon / LaunchAgent。
- 不接 channels。
- 不公网暴露。
- 不使用公司 `cc-connect`。
- 不让 OpenClaw 自动调用 Codex 改文件。

A4 实测结果（2026-06-23）：

已完成：

- 在 `tmux` 的 `gateway` 窗口中手动前台启动 OpenClaw gateway。
- 启动命令使用 `--bind loopback --port 18789 --auth token --tailscale off`。
- gateway 达到 ready 状态。
- `lsof` 确认仅监听 `127.0.0.1:18789` 与 `[::1]:18789`。
- 未监听公网地址，未发现 `0.0.0.0` 对外开放监听。
- `openclaw gateway status` 确认 LaunchAgent not loaded、service not installed。
- `launchctl list` 未发现 OpenClaw / cc-connect / claw 相关后台项。
- 使用 `Ctrl+C` 停止 gateway。
- 停止日志显示 clean shutdown。
- 停止后 `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出，确认端口已关闭。

预期内现象：

- gateway 运行期间出现 `No API key found for provider "openai"`。
- 原因是 A3 按安全策略故意没有写入模型 API key。
- 该报错不影响 A4 的 gateway 启动与监听验证结论，但说明当前还不能执行真实模型任务。

A4 结论：通过。OpenClaw gateway 可以在本地沙盒模式下手动启动、只监听本机、无后台服务残留，并可干净关闭。

A5 进入条件：

- 只做只读健康检查。
- 不接真实消息入口。
- 不发送真实外部消息。
- 不运行真实工程任务。
- 在模型 API key 未配置前，不做模型调用链路验收。


A5 只读健康检查结果（2026-06-23）：

已执行：

- `openclaw status`。
- `openclaw gateway status`。
- `openclaw channels status`。
- `openclaw sessions list`。
- `lsof -nP -iTCP:18789 -sTCP:LISTEN`。
- `launchctl list` 过滤 OpenClaw / cc-connect / claw 后台项。

结果：

- Gateway 状态：local loopback，目标 `ws://127.0.0.1:18789`，当前 unreachable / `ECONNREFUSED`，符合 A4 后已停止的预期。
- Dashboard 地址仍为 `http://127.0.0.1:18789/`，但 gateway 未运行。
- Tailscale exposure：off。
- Gateway service：LaunchAgent not installed / not loaded。
- Node service：LaunchAgent not installed。
- `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出，确认 18789 端口未监听。
- `launchctl list` 未发现 OpenClaw / cc-connect / claw 相关后台项。
- Channels：No channels configured。
- Sessions：存在 1 个本地 direct session：`agent:main:main`，模型显示 `gpt-5.5`，runtime 为 OpenAI Codex；这是本地 OpenClaw session 记录，不代表接入了真实消息通道。
- Gateway auth token 为 SecretRef，当前命令路径未设置 `OPENCLAW_GATEWAY_TOKEN`，因此 status 显示 degraded read-only config；未写入或暴露 token。

限制与结论：

- 在 Codex 沙盒内直接运行部分 OpenClaw CLI 状态命令时，会出现 SQLite 只读数据库 / chmod 权限限制；授权环境中重跑后可正常读取状态。
- A5 通过：gateway 已停止、端口关闭、无后台服务、无 channels、无公网暴露、无公司 `cc-connect` 通道。
- 下一步如进入 A6，只允许做本地最小安全测试，不接真实消息入口，不运行真实工程任务，不配置模型 API key，除非再次获得用户明确确认。


### A6 最小本地安全测试方案（待执行）

目标：A6 只验证 OpenClaw gateway 在本地 loopback 模式下的最小请求 / 状态路径是否可安全测试；不验证模型能力，不执行真实工程任务，不接真实消息入口。

前置条件：

- A4 已通过，gateway 可手动启动并可干净关闭。
- A5 已通过，当前 gateway 已停止，18789 端口无监听，channels 未配置，daemon / LaunchAgent 未安装。
- 用户再次明确确认后，才允许进入 A6-Run。

执行边界：

- 只允许在 `tmux` 的 `gateway` 窗口中前台临时启动 gateway。
- 只允许绑定 loopback：`127.0.0.1:18789` / `[::1]:18789`。
- 只允许使用临时环境变量 `OPENCLAW_GATEWAY_TOKEN`，不把 token 写入手册、日志、Git、命令历史或聊天记录。
- 不配置模型 API key。
- 不接微信、Telegram、Slack、个人飞书等 channels。
- 不安装 daemon / LaunchAgent。
- 不公网暴露，不打开 Tailscale 暴露。
- 不让 OpenClaw 自动调用 Codex 修改文件。
- 不运行真实项目任务，不发送真实外部消息。

建议命令草案（仅供 A6-Run 确认后执行）：

```bash
export OPENCLAW_GATEWAY_TOKEN="$(openssl rand -hex 32)"
openclaw gateway run --bind loopback --port 18789 --auth token --tailscale off
```

另开窗口只读检查：

```bash
openclaw gateway status
openclaw status
lsof -nP -iTCP:18789 -sTCP:LISTEN
openclaw channels status
openclaw sessions list
```

最小安全测试范围：

- 允许：gateway status / status / health / probe 类本地状态读取。
- 允许：确认本地 loopback 连接、认证缺失或 SecretRef 未解析时的安全失败。
- 不允许：`openclaw agent` 执行真实任务。
- 不允许：`openclaw message send` 或任何外部消息发送。
- 不允许：`openclaw channels add` 或登录任何 channel。
- 不允许：`openclaw gateway install`、`gateway start`、daemon / LaunchAgent 操作。
- 不允许：写入模型 API key 或触发付费模型调用。

成功标准：

- gateway 可手动前台启动。
- 监听地址仍只限 loopback，未出现 `0.0.0.0` 公网监听。
- status / gateway status / lsof 等本地状态可读，或以可解释的安全失败结束。
- channels 仍未配置。
- 未发送外部消息。
- 未调用 Codex 修改文件。
- 停止后 `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出。
- `launchctl list` 未出现 OpenClaw / cc-connect / claw 后台项。

收尾要求：

- A6-Run 完成后必须停止 gateway。
- 必须记录命令、结果、失败原因、端口关闭状态和下一步。
- 若出现任何超出边界的提示或风险，立即停止并回到人工确认。


### A6 最小本地安全测试结果（2026-06-24）

执行结果：通过。

已执行：

- 在 `tmux` 的 `gateway` 窗口中以前台方式临时启动 gateway。
- 启动命令使用 `--bind loopback --port 18789 --auth token --tailscale off`。
- token 使用一次性环境变量生成，未写入手册、日志、Git 或聊天记录。
- 通过 `lsof -nP -iTCP:18789 -sTCP:LISTEN` 确认监听地址仅为 `127.0.0.1:18789` 和 `[::1]:18789`。
- 执行 `openclaw gateway status`、`openclaw status`、`openclaw health`、`openclaw channels status`、`openclaw sessions list`。
- 使用 `Ctrl+C` 停止 gateway。
- 停止日志显示 clean shutdown。
- 停止后 `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出，确认端口关闭。
- 停止后 `launchctl list` 未发现 OpenClaw / cc-connect / claw 后台项。

检查结果：

- Gateway 可手动前台启动。
- Gateway 只监听 loopback，未出现 `0.0.0.0` 公网监听。
- `openclaw gateway status` 能识别本地 gateway 进程和端口占用，但因当前命令路径没有 gateway token / paired device identity，连接探测以安全认证失败结束。
- `openclaw status` 显示 gateway local loopback，但 unreachable 原因为 `device identity required`；Gateway service 和 Node service 仍为 LaunchAgent not installed。
- `openclaw health` 显示 Gateway reachable，但 CLI 没有 token/password 或 paired device token，无法执行 read-scope health RPC。该结果符合 A6 允许的安全失败范围。
- Channels 仍未配置。
- Sessions 仍为 1 个本地 direct session：`agent:main:main`，不代表接入真实消息通道。
- 运行期间仍出现 `No API key found for provider "openai"`，这是未配置模型 API key 的预期结果；未触发真实模型任务验收。

未执行：

- 未配置模型 API key。
- 未接微信、Telegram、Slack、个人飞书等 channels。
- 未安装 daemon / LaunchAgent。
- 未发送外部消息。
- 未运行真实工程任务。
- 未让 OpenClaw 调用 Codex 修改文件。

A7 收尾：

- gateway 已停止。
- 18789 端口已关闭。
- 未留下后台服务。
- 结果已写入手册和项目日志。

结论：P4-A 本地沙盒链路验证到 A6 为止已完成安全闭环。下一步不应直接接入真实消息入口或模型 API key，应先做 P4-A 收尾评估，并确认 P4-B 的目标、边界和授权策略。


### P4-A 收尾评估（2026-06-24）

结论：P4-A 通过，可以关闭。

验收对照：

- OpenClaw CLI 已安装并可执行，版本为 `2026.6.8 (844f405)`。
- gateway 已在 A4/A6 中完成手动前台启动验证。
- gateway 启动时只监听 loopback：`127.0.0.1:18789` 与 `[::1]:18789`。
- Tailscale exposure 保持 off，未出现公网监听。
- daemon / LaunchAgent 未安装，`launchctl list` 未发现 OpenClaw / cc-connect / claw 后台项。
- channels 未配置，未接微信、Telegram、Slack、个人飞书或任何公司通道。
- 未配置模型 API key，未触发真实模型任务。
- 未发送外部消息，未运行真实工程任务，未让 OpenClaw 调用 Codex 修改文件。
- 测试后 gateway 已停止，18789 端口关闭。

当前状态复核：

- `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出。
- `openclaw gateway status` 显示 local loopback 目标，连接结果为 `ECONNREFUSED`，符合 gateway 已停止的预期。
- `openclaw status` 显示 Gateway service / Node service 均为 LaunchAgent not installed。
- `openclaw channels status` 为 config-only，无 channels configured。
- `openclaw sessions list` 仍只有 1 个本地 direct session：`agent:main:main`；这不是消息入口接入。

遗留限制：

- 当前 CLI 命令路径没有 gateway token / paired device identity，部分 read-scope RPC 会以安全认证失败结束。
- 当前没有模型 API key，不能验收真实模型调用能力。
- 当前没有 channel，不能验收真实消息收发。
- 当前没有 daemon / LaunchAgent，不能验收长期自启动。

关闭条件：P4-A 的目标是验证本地沙盒链路是否能安全启动、检查、失败和关闭；该目标已完成。下一阶段必须先定义 OpenClaw 如何安全转交任务给 Codex，不能直接进入真实消息入口、模型 API key 或 daemon 部署。


### P4-B OpenClaw 到 Codex 转交合约 dry-run 方案（2026-06-24）

目标：定义未来 OpenClaw 将消息任务转交 Codex 的最小合约，并用本地 dry-run 验证任务分类、风险拦截和任务包格式。不接真实消息入口，不配置模型 API key，不启动 gateway，不安装 daemon，不执行 Codex。

本阶段边界：

- 只做本地 dry-run。
- 不启动 OpenClaw gateway。
- 不连接微信、Telegram、Slack、个人飞书等 channels。
- 不发送外部消息。
- 不配置或读取模型 API key。
- 不安装 daemon / LaunchAgent。
- 不调用 `codex exec` 执行真实任务。
- 不自动修改项目文件。

任务包字段：

```text
task_id: YYYY-MM-DD_short-task-name
repo: /Users/duckulacissy/Duci-s-AI-Factory
phase: P4-B
request: <用户请求，发现疑似密钥时必须脱敏>
risk_level: L0 | L1 | L2 | L3
approval_status: dry_run_allowed | approved_scope_only | needs_confirmation | blocked
expected_output: summary, changed_files, verification, next_step
```

风险分级：

| 等级 | 含义 | P4-B 行为 |
| --- | --- | --- |
| L0 | 只读查询、总结、状态说明 | 允许生成任务包预览，不执行 Codex。 |
| L1 | 文档、日志、脚本等低风险项目编辑 | 允许生成任务包预览；真实执行仍需任务范围已获确认。 |
| L2 | 安装、启动服务、处理密钥、配置 API、接 channels、发送消息、付费调用 | 阻断并要求用户明确确认。 |
| L3 | 删除、重置、强推、公网暴露、恢复公司通道、破坏性操作 | 默认阻断，除非用户明确指定该精确动作。 |

最小脚本：

- 路径：`scripts/openclaw_codex_dry_run.py`
- 输入：`--request`、`--repo`、`--phase`、可选 `--task-id`。
- 输出：JSON dry-run 结果，包括边界声明、风险判定、Codex 任务包和下一步。
- 明确不做：不启动 gateway、不调用 Codex、不发送消息、不写项目文件、不读取或保存密钥。

建议测试用例：

```bash
python3 scripts/openclaw_codex_dry_run.py --request "请总结当前项目状态和下一步，不修改文件。"
python3 scripts/openclaw_codex_dry_run.py --request "请更新 docs/AI_FACTORY_MANUAL.md，记录 P4-B dry-run 方案。"
python3 scripts/openclaw_codex_dry_run.py --request "请 rm -rf logs 并删除所有备份。"
python3 scripts/openclaw_codex_dry_run.py --examples
```

成功标准：

- L0 任务被识别为 `dry_run_allowed`。
- L1 任务被识别为 `approved_scope_only`，只生成任务包预览。
- L2/L3 任务被阻断，不给出真实执行许可。
- 输出中不包含真实密钥；疑似密钥必须脱敏。
- 脚本运行期间不产生外部消息、不启动服务、不改变 gateway 状态、不调用 Codex。

P4-B 完成后，才可以讨论 P4-C 本地脚本桥接；在 P4-C 前仍不接真实消息入口、不配置模型 API key、不安装 daemon。


### P4-C 本地脚本桥接预览（2026-06-24）

目标：在 P4-B 任务包和风险判定基础上，验证未来 OpenClaw 如何把允许进入预览的任务转换成 Codex CLI 命令草案。P4-C 只生成命令预览，不执行 `codex exec`。

本阶段边界：

- 不启动 OpenClaw gateway。
- 不连接任何 channels。
- 不配置或读取模型 API key。
- 不安装 daemon / LaunchAgent。
- 不发送外部消息。
- 不调用真实 `codex exec`。
- 不自动修改项目文件。

脚本：

- 路径：`scripts/openclaw_codex_bridge_preview.py`
- 输入：`--request`、`--repo`、`--source-phase`、可选 `--task-id`。
- 依赖：复用 `scripts/openclaw_codex_dry_run.py` 的风险分类与脱敏逻辑。
- 输出：JSON bridge preview，包括 source packet、source decision、bridge decision、未来 Codex command preview 和 operator next step。

桥接规则：

| 风险 | P4-C 行为 |
| --- | --- |
| L0 | 生成 `codex exec --cd <repo> <prompt>` 命令预览；`execution_allowed_now=false`。 |
| L1 | 生成命令预览，但标记真实执行需要已获确认的任务范围；`execution_allowed_now=false`。 |
| L2 | hold，不生成 Codex 命令预览。 |
| L3 | hold，不生成 Codex 命令预览。 |

命令预览中的 Codex prompt 必须包含：

- 读取 `README.md`、`AGENTS.md`、`docs/AI_FACTORY_MANUAL.md`、`docs/AI_EXECUTION_SOP.md`。
- 不处理密钥、不暴露服务、不安装 daemon、不接 channels、不执行破坏性动作，除非用户明确确认。
- 任务包字段：`task_id`、`phase`、`risk_level`、`approval_status`、`request`、`expected_output`。

初步预演：

```bash
python3 -B scripts/openclaw_codex_bridge_preview.py --request "请总结当前项目状态和下一步，不修改文件。"
python3 -B scripts/openclaw_codex_bridge_preview.py --request "请更新 docs/AI_FACTORY_MANUAL.md，记录 P4-C bridge preview 方案。"
python3 -B scripts/openclaw_codex_bridge_preview.py --request "请配置 token: fake-secret-value 并启动 gateway。"
python3 -B scripts/openclaw_codex_bridge_preview.py --request "请 rm -rf logs 并删除所有备份。"
```

预演结果：

- 只读总结请求：L0，`bridge_decision=preview_ready`，生成命令预览，`execution_allowed_now=false`。
- 文档更新请求：L1，`bridge_decision=preview_ready`，生成命令预览，但真实执行仍需确认任务范围。
- 假 token-like + 启动 gateway 请求：L2，疑似密钥被脱敏，`bridge_decision=hold`，不生成命令预览。
- 删除日志请求：L3，`bridge_decision=hold`，不生成命令预览。

结论：P4-C 最小桥接预览通过。当前仍然没有真实执行链路，OpenClaw 不会调用 Codex；下一步可以做 P4-C 收尾评估，并准备 P5-A 入口选择策略。


### P5-A 个人消息入口选择策略（2026-06-24）

目标：在进入真实 OpenClaw 部署前，先选定第一个个人消息入口的方向和安全边界。P5-A 只做入口策略，不连接 channel，不写凭证，不启动 gateway，不安装 daemon，不配置模型 API key。

P4-C 收尾评估：

- P4-C 目标已达成：本地桥接预览可以把 L0/L1 dry-run 任务包转换为未来 `codex exec` 命令草案。
- 所有预览仍保持 `execution_allowed_now=false`。
- L2/L3 任务仍被 hold，不生成 Codex 命令预览。
- 当前没有真实执行链路：OpenClaw 不会调用 Codex，不会发送外部消息，也不会自动修改项目文件。
- 因此 P4-C 可以关闭，后续进入 P5 前必须先确认真实入口和授权方案。

候选入口对比：

| 入口 | 优点 | 风险 / 成本 | P5-A 结论 |
| --- | --- | --- | --- |
| Telegram 个人 bot | OpenClaw 官方支持成熟；个人 bot 配置相对轻；可先使用 DM-only + allowlist；适合作为最小真实个人入口。 | 仍涉及 bot token、用户白名单和消息入口授权，必须在 P5-B 单独设计凭证与权限方案。 | 推荐作为第一个真实入口。 |
| Slack | OpenClaw 官方支持成熟，适合团队与工作区流程。 | workspace / app / permission 配置更重；个人 AI 工厂第一阶段不需要团队协作入口。 | 可作为后续扩展，不作为首选。 |
| 个人飞书 | 理论上可作为个人消息入口。 | 容易与已废除的公司 `cc-connect` / Feishu 流程混淆；审批、机器人和租户边界更复杂。 | 暂不作为首选；不得复用公司通道。 |
| 微信 | 贴近日常使用。 | 当前更依赖外部插件或 private-chat 支持，稳定性、合规边界和长期维护成本更高。 | 暂不作为首选。 |
| 无 channel / 本地 CLI | 最安全，适合继续做本地验证。 | 不是实际个人消息入口，无法验证消息到任务的真实闭环。 | 可保留为回退路径。 |

推荐方案：

- 第一个真实个人入口选择 Telegram 个人 bot。
- 初始模式只允许私聊：DM-only。
- 初始访问控制使用 allowlist，只允许用户本人或明确授权的账号。
- 初始阶段不启用群聊，不接团队 workspace，不接公司 Feishu / `cc-connect`。
- P5-A 不写入 bot token，不创建 channel 配置，不启动 gateway，不安装 daemon。
- P5-B 再单独设计凭证来源、白名单字段、日志脱敏、回滚方式和最小验证命令。

P5-B 前置确认：

1. 用户确认是否采用 Telegram 个人 bot 作为首个真实入口。
2. 若确认 Telegram，再设计 P5-B 凭证与授权方案。
3. P5-B 仍先做配置草案与 dry-run，不直接进入长期运行。


### P5-B Telegram 凭证与授权 dry-run（2026-06-24）

目标：在不接入 Telegram、不读取 token、不写 OpenClaw 配置的前提下，定义未来 Telegram 个人 bot 的凭证来源、授权边界、allowlist 策略和最小命令预览。

本阶段依据：

- `openclaw channels --help` 显示 OpenClaw 支持 `channels add`、`channels status`、`channels list` 等 channel 管理命令。
- `openclaw channels add --help` 显示 Telegram 位于 `--channel` 可选项中，且存在 `--token`、`--bot-token`、`--token-file`、`--use-env` 等凭证参数。
- P5-A 已确认首选入口为 Telegram 个人 bot，模式为 DM-only + allowlist。

本阶段边界：

- 不调用 `openclaw channels add`。
- 不读取、生成、粘贴或保存 Telegram bot token。
- 不写 `~/.openclaw` channel 配置。
- 不启动 OpenClaw gateway。
- 不安装 daemon / LaunchAgent。
- 不发送 Telegram 消息。
- 不启用群聊。
- 不复用公司 `cc-connect` / Feishu。

脚本：

- 路径：`scripts/openclaw_telegram_auth_dry_run.py`
- 输入：`--credential-source`、`--env-name`、`--token-file`、`--allow-user`、`--account`、`--name`。
- 默认凭证策略：未来使用环境变量名 `OPENCLAW_TELEGRAM_BOT_TOKEN`，但脚本当前不读取该变量。
- 默认授权策略：DM-only、groups disabled、allowlist only、unknown sender deny。
- 输出：JSON 方案预览，包括 channel、credential plan、authorization plan、未来 OpenClaw command preview 和 decision。

凭证策略：

| 方案 | P5-B 结论 |
| --- | --- |
| env-backed | 首选。未来由用户在一次性 shell / tmux gateway 窗口设置环境变量，配置记录只引用环境变量名，不记录 token。 |
| token-file | 备选。只允许绝对路径，文件不得进入 Git；P5-B 脚本不读取文件。 |
| inline token | 禁止。真实 token 不得出现在命令行、日志、聊天记录、手册或 Git。 |

授权策略：

- 只允许私聊入口。
- allowlist 必须至少包含一个明确授权的 Telegram 用户 ID 或 handle。
- 未在 allowlist 内的发送者默认拒绝，只记录最小元信息，不记录消息正文。
- 群聊默认关闭；如果未来要启用群聊，必须重新进入单独审批阶段。

预演命令：

```bash
python3 -B scripts/openclaw_telegram_auth_dry_run.py --examples
python3 -B scripts/openclaw_telegram_auth_dry_run.py --allow-user "@your_telegram_handle"
```

预演结果：

- env-backed + allowlist 示例返回 `status=draft_ready`，但 `connection_allowed_now=false`。
- 缺少 allowlist 示例返回 `status=needs_allowlist`。
- inline placeholder 示例返回 `status=hold`，说明 inline token 路径不进入项目记录。
- 所有输出均不包含真实 secret，且不执行 OpenClaw channel 配置。

结论：P5-B 已形成 Telegram 凭证与授权 dry-run。下一步仍不应直接连接 Telegram；应先由用户审阅凭证来源、allowlist 字段和未来验证路径，再决定是否进入 P5-C 最小 channel 配置草案。


### P5-C 最小 Telegram channel 配置草案（2026-06-24）

目标：在不执行真实 channel 配置的前提下，把未来最小 Telegram channel 配置拆成可审阅的 preflight、配置、验收、probe 和回滚步骤。P5-C 仍然是草案和 dry-run，不接 Telegram。

本阶段依据：

- `openclaw channels status --help` 支持 `--channel telegram`、`--json`、`--probe` 和 `--timeout`。
- `openclaw channels list --help` 支持 `--json` 和 `--all`。
- `openclaw channels remove --help` 支持 `--channel telegram`、`--account` 和 `--delete`。
- `openclaw gateway status --help` 支持 `--deep`、`--json`、`--no-probe`、`--token` 和 `--url`。
- P5-B 已定义 env-backed 凭证、DM-only、allowlist only、groups disabled。

本阶段边界：

- 不执行 `openclaw channels add`。
- 不执行 `openclaw channels remove`。
- 不执行 `openclaw channels status --probe`。
- 不读取 Telegram bot token。
- 不写 `~/.openclaw` channel 配置。
- 不启动 OpenClaw gateway。
- 不安装 daemon / LaunchAgent。
- 不发送 Telegram 消息。

脚本：

- 路径：`scripts/openclaw_telegram_channel_config_draft.py`
- 依赖：复用 `scripts/openclaw_telegram_auth_dry_run.py` 的 P5-B 凭证与 allowlist 方案。
- 输入：`--credential-source`、`--env-name`、`--token-file`、`--allow-user`、`--account`、`--name`。
- 输出：JSON 配置草案，包括 P5-B auth plan、未来配置命令预览、preflight 检查、post-config 验收、credential probe 预览和 rollback 预览。

未来真实配置顺序草案：

1. preflight：只读确认 channels 列表和 gateway 状态。
2. config：在用户明确批准且凭证只存在于运行时环境后，执行最小 `openclaw channels add --channel telegram ... --use-env`。
3. verify：先执行不带 probe 的 list/status，只确认本地配置可见。
4. probe：如果需要验证 Telegram 凭证，`--probe` 必须再次单独确认，因为它可能联系 channel provider。
5. rollback：优先 soft remove；`--delete` 删除配置项需要再次单独确认。

预演命令：

```bash
python3 -B scripts/openclaw_telegram_channel_config_draft.py --examples
python3 -B scripts/openclaw_telegram_channel_config_draft.py --allow-user "@your_telegram_handle"
```

预演结果：

- env-backed + allowlist 示例返回 `status=draft_ready`，但 `configuration_allowed_now=false`。
- 缺少 allowlist 示例返回 `status=hold`，不生成配置序列。
- 所有配置、验收、probe 和回滚命令都只是 command preview，`execution_allowed_now=false`。
- 脚本不读取 token，不执行 OpenClaw 命令，不写配置，不发送消息。

结论：P5-C 已完成最小 Telegram channel 配置草案。下一步不能直接配置 Telegram；应由用户审阅 P5-C 草案，并在 P5-D 中单独决定是否进入真实配置审批。


### P5-D 真实 Telegram channel 配置审批清单（2026-06-24）

目标：在任何真实 Telegram channel 配置前，建立逐项审批门禁。P5-D 只写审批清单，不执行真实配置，不读取 token，不连接 Telegram。

P5-D 必须确认的五件事：

| 审批项 | 必须确认的内容 | 默认建议 | 未确认时状态 |
| --- | --- | --- | --- |
| 是否进入真实配置 | 是否允许未来执行 `openclaw channels add --channel telegram ...` | 暂不执行，先审阅清单 | block |
| 凭证输入方式 | Telegram bot token 如何进入运行环境 | 仅使用 `OPENCLAW_TELEGRAM_BOT_TOKEN` 环境变量，由用户现场输入 | block |
| allowlist 值 | 允许哪个 Telegram 用户 ID 或 handle 触发 bot | 只允许用户本人，必须明确写入审批记录，但不写私人敏感信息 | block |
| 最小验收范围 | 真实配置后先做哪些检查 | 只做本地 `channels list/status`；不 probe、不发消息 | block |
| 回滚方式 | 配置不符合预期时如何撤回 | 先 soft remove；`--delete` 需再次确认 | block |

允许动作（仅在 P5-D 逐项确认后，且进入下一阶段时才可执行）：

- 只读 preflight：`openclaw channels list --json`。
- 只读 preflight：`openclaw gateway status --deep --no-probe`。
- 在用户现场设置环境变量后执行最小 Telegram channel 配置。
- 配置后只读检查：`openclaw channels list --json`。
- 配置后只读检查：`openclaw channels status --channel telegram --json`。
- 必要时执行 soft rollback：`openclaw channels remove --channel telegram --account personal-telegram-bot`。

禁止动作（P5-D 不允许，后续也必须单独审批）：

- 不在聊天记录、手册、日志、Git、命令历史中写入真实 token。
- 不使用 inline token 命令。
- 不执行 `openclaw channels status --channel telegram --json --probe`，除非单独确认。
- 不发送 Telegram 测试消息，除非单独确认。
- 不启用群聊。
- 不安装 daemon / LaunchAgent。
- 不启动长期 gateway。
- 不配置模型 API key。
- 不执行 `openclaw channels remove --delete`，除非单独确认。
- 不复用公司 `cc-connect` / Feishu。

建议的真实配置窗口：

- 在 tmux `gateway` 或临时受控 shell 中执行。
- 开始前确认 Git 工作区干净。
- 开始前记录当前 `openclaw channels list --json` 输出摘要。
- token 只由用户在本地 shell 输入到环境变量，不由 Codex 打印、读取、保存或复述。
- 执行完成后立即清理当前 shell 中的 token 环境变量，或关闭该 shell。

P5-E 进入条件：

1. 用户明确说“进入 P5-E 真实 Telegram channel 配置执行”。
2. 用户确认凭证输入方式为 env-backed。
3. 用户提供 allowlist 的非敏感标识，或在本地执行时确认该值。
4. 用户确认本阶段只做本地配置可见性验收，不 probe、不发消息。
5. 用户确认如需回滚，先 soft remove。

结论：P5-D 是真实配置前的审批闸门。清单未逐项确认前，不得执行任何真实 Telegram channel 配置。


### P5-E 入口决策变更：改选个人飞书（2026-06-24）

用户新决策：不要选择 Telegram 作为 gateway 的入口，改选飞书。

本决策含义：

- 当前真实消息入口路线从 Telegram 切换为个人飞书。
- Telegram P5-B / P5-C / P5-D 保留为历史 dry-run、配置草案和审批清单记录，但不再作为当前执行路线。
- 不进入 Telegram P5-E 真实配置执行。
- 后续如继续，应进入个人飞书的资料核对、凭证与授权 dry-run、最小配置草案和审批清单。

必须再次强调的边界：

- 这里的“飞书”只允许是个人飞书 / 个人专用配置。
- 不得复用公司 `cc-connect` / Feishu。
- 不恢复旧公司运行目录、会话、日志、LaunchAgent 或同步脚本。
- 不使用任何公司 app id、app secret、tenant、群组、联系人或历史消息。
- 不直接进入真实飞书配置，不读取或写入真实 app secret / token。
- 不启动 gateway，不安装 daemon，不发送消息，不让 OpenClaw 调用 Codex。

本地依据：

- `openclaw channels add --help` 的 channel 列表包含 `feishu`。
- `openclaw channels status --help` 的 channel 列表包含 `feishu`。
- 这只说明 OpenClaw CLI 支持 Feishu channel 类型；不代表当前已经配置飞书，也不代表可以复用公司 Feishu。

下一步建议：

1. P5-F 只读核对 Feishu channel 的 OpenClaw 参数形态和官方资料。
2. 定义个人飞书凭证来源、权限范围、allowlist / 可触达对象边界。
3. 准备个人飞书 dry-run 脚本，只生成 JSON 方案，不读取 secret、不写配置。
4. 再决定是否进入最小个人飞书 channel 配置草案。

结论：当前入口方向改为个人飞书；Telegram 路线暂停并归档为历史备选。


### P5-F 个人飞书凭证与授权 dry-run（2026-06-24）

目标：在不连接飞书、不读取或写入真实 app id / app secret、不写 OpenClaw 配置的前提下，核对个人飞书 channel 的参数形态，并形成可审阅的凭证来源、访问控制和最小 dry-run 脚本。

本阶段依据：

- `openclaw --version` 当前为 `2026.6.8 (844f405)`，满足本地 Feishu 文档要求的 OpenClaw 2026.5.29 以上版本。
- `openclaw channels add --help` 和 `openclaw channels status --help` 的 channel 列表包含 `feishu`。
- OpenClaw 本地文档 `/opt/homebrew/lib/node_modules/openclaw/docs/channels/feishu.md` 说明 Feishu/Lark channel 支持 bot DM 与 group chats，默认事件传输为 WebSocket，配置字段包含 `appId`、`appSecret`、`dmPolicy`、`allowFrom`、`groupPolicy`、`groupAllowFrom`、`requireMention`。
- OpenClaw 本地实现支持 Feishu `appId` / `appSecret` 使用 SecretRef；因此 P5-F 首选 env SecretRef，而不是把真实凭证写入命令、日志或配置草案。

必须维持的边界：

- P5-F 只做资料核对、脚本和 JSON 方案预览。
- 不执行 `openclaw channels login --channel feishu`。
- 不执行真实 `openclaw channels add`。
- 不执行 `openclaw channels status --channel feishu --probe`。
- 不读取、生成、粘贴、保存或复述真实 Feishu app id / app secret / verification token / encrypt key。
- 不写 `~/.openclaw` 配置，不启动 gateway，不安装 daemon / LaunchAgent，不发送飞书消息，不调用真实 `codex exec`。
- 不复用公司 `cc-connect` / Feishu；不恢复旧公司运行目录、会话、日志、LaunchAgent 或同步脚本；不使用公司 app、tenant、群组、联系人或历史消息。

脚本：

- 路径：`scripts/openclaw_feishu_auth_dry_run.py`
- 输入：`--credential-source`、`--app-id-env`、`--app-secret-env`、`--allow-user`、`--dm-policy`、`--group-policy`、`--account`、`--name`、`--domain`、`--connection-mode`。
- 默认凭证策略：未来使用 env SecretRef，变量名为 `OPENCLAW_FEISHU_APP_ID` 与 `OPENCLAW_FEISHU_APP_SECRET`；脚本当前不读取这两个变量。
- 默认授权策略：`dmPolicy=allowlist`、`groupPolicy=disabled`、`requireMention=true`、`dynamicAgentCreation.enabled=false`、`streaming=false`。
- 输出：JSON 方案预览，包括本地依据、个人边界、credential plan、authorization plan、未来 config JSON5 shape、未来 command preview 和 decision。

凭证策略：

| 方案 | P5-F 结论 |
| --- | --- |
| env SecretRef | 首选。未来 OpenClaw 配置只记录 `{source:"env", provider:"default", id:"OPENCLAW_FEISHU_APP_ID"}` 与 `{source:"env", provider:"default", id:"OPENCLAW_FEISHU_APP_SECRET"}`，真实值只存在于用户本地运行时环境。 |
| secret-file | 备选。只允许绝对路径，文件不得进入 Git；P5-F 脚本不读取文件。 |
| inline credential | 禁止。真实 app id / app secret 不得出现在聊天记录、命令历史、手册、日志或 Git。 |

授权策略：

- 第一版只允许个人 DM allowlist。
- `allowFrom` 未来应使用用户个人飞书 `open_id`，通常形如 `ou_xxx`；该值必须通过后续单独审批的 pairing / 日志发现步骤获得，不能从公司数据推断。
- 未在 allowlist 内的发送者默认拒绝，只记录最小元信息或进入 pairing 请求，不记录消息正文。
- 群聊默认关闭：`groupPolicy=disabled`，`groupAllowFrom=[]`。
- 第一版不启用 public DM，不启用 groups，不启用 dynamic agent creation，不启用长期 gateway。

预演命令：

```bash
python3 -B scripts/openclaw_feishu_auth_dry_run.py --examples
python3 -B scripts/openclaw_feishu_auth_dry_run.py --allow-user ou_personal_open_id_placeholder
python3 -B scripts/openclaw_feishu_auth_dry_run.py --personal-only unconfirmed --allow-user ou_personal_open_id_placeholder
python3 -B scripts/openclaw_feishu_auth_dry_run.py --group-policy allowlist --allow-group oc_group_placeholder --allow-user ou_personal_open_id_placeholder
```

预演结果：

- env SecretRef + 个人 open_id placeholder 示例返回 `status=draft_ready`，但 `connection_allowed_now=false`、`may_read_credentials=false`、`may_write_openclaw_config=false`。
- 缺少 allowlist 示例返回 `status=needs_allowlist`。
- inline credential 示例返回 `status=hold`。
- personal-only 未确认示例返回 `status=hold`。
- 尝试启用 group allowlist 示例返回 `status=hold`，因为第一版个人飞书入口必须保持 groups disabled。
- 所有输出均不包含真实 secret，且不执行 OpenClaw channel 配置。

未来配置预览：

```json5
{
  channels: {
    feishu: {
      enabled: true,
      domain: "feishu",
      connectionMode: "websocket",
      defaultAccount: "personal-feishu-bot",
      accounts: {
        "personal-feishu-bot": {
          appId: { source: "env", provider: "default", id: "OPENCLAW_FEISHU_APP_ID" },
          appSecret: { source: "env", provider: "default", id: "OPENCLAW_FEISHU_APP_SECRET" },
          domain: "feishu",
          name: "Personal Feishu Bot",
        },
      },
      dmPolicy: "allowlist",
      allowFrom: ["ou_personal_open_id_placeholder"],
      groupPolicy: "disabled",
      groupAllowFrom: [],
      requireMention: true,
      streaming: false,
      dynamicAgentCreation: { enabled: false },
    },
  },
}
```

未来命令预览：

```bash
openclaw config set channels.feishu.accounts.personal-feishu-bot.appId --ref-source env --ref-provider default --ref-id OPENCLAW_FEISHU_APP_ID --dry-run
openclaw config set channels.feishu.accounts.personal-feishu-bot.appSecret --ref-source env --ref-provider default --ref-id OPENCLAW_FEISHU_APP_SECRET --dry-run
openclaw channels status --channel feishu --json
```

以上命令在 P5-F 只是预览，`execution_allowed_now=false`。P5-F 不执行这些命令，也不进入真实配置。

结论：P5-F 已完成个人飞书资料核对与凭证授权 dry-run 方案。下一步不能直接连接飞书；应进入 P5-G 最小个人飞书 channel 配置草案，继续只做 preflight、配置、验收和回滚的命令预览。


## 第八章：OpenClaw 与 Codex 的角色分工

OpenClaw 不替代 Codex。V3.4 明确将 OpenClaw/龙虾降级为 gateway 和记忆承载层：负责消息接入、定时任务、旧 agent 记忆、任务转发和结果回传。Codex 才是工程主执行层，负责进入仓库、读规则、改文件、跑命令、检查结果并记录日志。

| 组件 | 职责 | 不应承担 |
| --- | --- | --- |
| 用户 | 提出目标、批准关键变更、判断方向。 | 不负责记住所有细节。 |
| OpenClaw/龙虾 | 接收微信/Telegram/Slack/个人飞书等入口消息，承载旧会话记忆，处理定时任务，识别任务类型，调用 Codex CLI、skill CLI 或脚本，并汇报结果。 | 不作为复杂工程任务的主 Agent，不直接承担大规模代码修改，不绕过审批执行高风险操作。 |
| Codex | 在项目仓库中执行工程任务：读 AGENTS.md、改文件、写脚本、跑命令、生成日志、准备提交。 | 不擅自改变核心架构，不处理未经授权的密钥与破坏性操作。 |
| GitHub | 保存代码、文档、日志、提交记录，是工程状态的版本账本。 | 不保存密钥和私有凭证。 |
| NAS | 保存长期资料、经验库、知识库、备份和大文件。 | 不替代 GitHub 的版本记录。 |

## 第九章：OpenClaw + Codex 完整工作流

```text
你
↓
微信 / Telegram / Slack / 个人飞书等入口
↓
OpenClaw
↓
任务判断与权限检查
↓
Codex
↓
本地仓库 / 命令行 / 文件系统 / 工具链
↓
GitHub 提交记录
↓
NAS 长期记忆
↓
OpenClaw 汇报结果
↓
你确认 / 追问 / 批准下一步
```

### 标准执行步骤

用户通过消息入口提出任务。

OpenClaw 判断任务类型：普通问答、资料查询、日程消息、工程任务或高风险任务。

如果是普通问答，OpenClaw 可直接回答；如果是工程任务，转交 Codex。

OpenClaw 调用本地脚本或工具入口，把任务、仓库路径、执行限制传给 Codex。

Codex 进入仓库，读取 AGENTS.md、README、docs/AI_FACTORY_MANUAL.md 和 logs。

Codex 执行任务前确认当前阶段、已完成事项、当前任务和风险点。

Codex 执行必要文件修改、命令检查、脚本生成或部署动作。

Codex 输出执行摘要，更新项目日志，必要时准备 Git 提交。

OpenClaw 将结果压缩成可读汇报，发回给用户。

用户确认下一步，或者要求回滚、补充、暂停。

### 最小可行调用方式

第一版不追求全自动，建议让 OpenClaw 调用一个本地脚本，再由脚本调用 Codex CLI。示例：

```text
codex exec --cd ~/Duci-s-AI-Factory "请检查项目状态，补齐 AGENTS.md，并更新项目日志"
```

后续如果 OpenClaw 支持更正式的工具协议，可以升级为 run_codex_task 工具，输入 repo、task、approval_policy，输出 summary、changed_files、status、next_step。

## 第十章：任务路由规则

| 任务类型 | OpenClaw 处理方式 | 是否交给 Codex |
| --- | --- | --- |
| 普通问答 | 直接回答，必要时引用 NAS/知识库。 | 否 |
| 资料查询 | 搜索或检索 NAS，生成摘要。 | 视情况 |
| 消息与日程 | 调用对应平台工具。 | 否 |
| 工程修改 | 创建任务请求，转交 Codex 执行。 | 是 |
| 部署与服务 | 先请求用户确认，再交给 Codex 执行。 | 是 |
| 删除、重置、密钥、权限 | 必须阻断并请求明确确认。 | 仅确认后 |
| 路线变更 | 要求说明原因、收益、风险和迁移成本。 | 确认后 |

## 第十一章：Codex 三种形态

Codex 不只有一种入口。不同入口适合不同任务，后续部署和日常使用时应按任务类型选择。

| 形态 | 适合任务 | 建议使用场景 |
| --- | --- | --- |
| Codex App | 完整项目开发、浏览器验证、图形界面、Computer Use、复杂多文件任务。 | 远程桌面进入 Mac mini 后使用；适合需要看页面、操作浏览器、处理可视化结果的任务。 |
| Codex CLI | SSH、脚本、自动化、改文件、跑命令、日志检查、`codex exec` 非交互任务。 | OpenClaw 调用 Codex 的主要方式；也是 tmux 常驻窗口中的主力执行工具。 |
| Codex IDE 插件 | 在 VS Code / Cursor 内直接协作编辑代码。 | 人在 MacBook 上开发时使用；适合近距离编辑和代码审阅。 |

选择规则：能用 CLI 稳定完成的任务，优先交给 Codex CLI；需要浏览器、桌面或视觉确认的任务，使用 Codex App；人在 IDE 中直接写代码时，用 Codex IDE 插件。

## 第十二章：Mac mini 常驻主机规范

Mac mini 是 AI 工厂的机房，不是临时工作电脑。它应长期在线、尽量不休眠、不随意关机，并具备断线恢复和服务重启能力。

### 常驻要求

- Mac mini 尽量固定放置，保持供电稳定。
- 关闭自动睡眠，避免 Codex、OpenClaw gateway、tmux 长任务中断。
- Tailscale 保持登录同一账号，并确认 MacBook、iPhone、Mac mini 在同一个 tailnet 内。
- SSH 作为主控制通道，VNC/屏幕共享作为图形备用通道。
- 所有长期任务必须运行在 tmux 内，避免 SSH 断线导致任务丢失。
- OpenClaw gateway、日志观察、Codex CLI、开发命令应拆分到不同 tmux 窗口。
### 重启后检查

| 检查项 | 命令或动作 | 通过标准 |
| --- | --- | --- |
| Tailscale | tailscale status | Mac mini 在线，能看到同一 tailnet 设备。 |
| SSH | 从 MacBook 执行 ssh 用户名@Tailscale-IP | 可登录 Mac mini。 |
| tmux | tmux ls | 能看到 ai-factory 或 codex/gateway/logs 等会话。 |
| Codex CLI | codex --version | 命令可用，版本可显示。 |
| OpenClaw | openclaw gateway status --deep | gateway 正常或能明确看到错误原因。 |
| GitHub | git -C ~/dev/github/Duci-s-AI-Factory status | 仓库可读，状态可检查。 |

## 第十三章：AI 执行规范固化

P3 已完成：AGENTS.md、docs/AI_EXECUTION_SOP.md、README.md、docs/AI_FACTORY_MANUAL.md 已同步，AI 执行边界、审批等级、任务包、回传格式和日志规则已写入仓库并推送。

每次工程任务开始前必须执行以下检查。此规则适用于 Codex，也适用于通过 OpenClaw 调度的工程任务。

读取 README.md。

读取 AGENTS.md。

读取 docs/AI_FACTORY_MANUAL.md。

读取最近的 logs/YYYY-MM-DD.md。

执行 git status --short。

识别用户未提交修改，避免覆盖。

确认当前阶段、任务、风险等级和下一步。

### 固定汇报格式

```text
【当前阶段】
【已完成】
【进行中】
【本次执行】
【风险/需确认】
【下一步】
```

### 审批等级

| 等级 | 含义 | 示例 |
| --- | --- | --- |
| L0 | 只读检查，无需额外确认。 | 查看文件、Git 状态、tmux 状态、工具版本。 |
| L1 | 低风险项目编辑，用户确认方向后可执行。 | 更新文档、日志、SOP、非密钥项目文件、提交并推送。 |
| L2 | 必须明确确认。 | 删除文件、kill session、安装依赖、改 SSH/Tailscale/VNC、防火墙、处理密钥、启动长期服务。 |
| L3 | 除非用户明确指定，否则禁止。 | git reset --hard、force push、暴露公网端口、提交密钥、替换核心架构。 |

### OpenClaw 转交 Codex 的任务包

```text
task_id: YYYY-MM-DD_short-task-name
repo: /Users/duckulacissy/Duci-s-AI-Factory
phase: P4
request: <用户请求>
risk_level: L0 \| L1 \| L2 \| L3
approval_status: approved \| needs_confirmation
expected_output: summary, changed_files, verification, next_step
```

### Codex 回传格式

```text
status: completed \| blocked \| needs_confirmation
changed_files:
verification:
risks:
next_step:
```

## 第十四章：AGENTS.md 当前规则

AGENTS.md 是 Codex 在仓库中的持久执行规则。当前版本已经从基础建议升级为可执行规则，和 docs/AI_EXECUTION_SOP.md 共同约束 Codex 与 OpenClaw 的工程任务。

```text
# AGENTS.md

## 项目定位
本仓库属于个人AI工厂项目。人负责决策，AI负责执行。

## 执行规则
- 每次任务先确认当前阶段、已完成事项、当前任务、风险和下一步。
- 所有重要变更必须更新 docs/AI_FACTORY_MANUAL.md 或 logs/。
- 不依赖聊天记录或模型记忆推进项目。
- 不得擅自修改核心架构或更换主技术路线。
- 不得删除文件、重置仓库、覆盖用户修改，除非用户明确批准。
- 不得把 API Key、SSH Key、Token、密码写入仓库。
- 涉及部署、权限、密钥、网络暴露、破坏性命令时必须请求用户确认。

## OpenClaw And Codex Roles
OpenClaw/Longxia receives work. Codex does the engineering work.
GitHub records results. Mac mini stays online.

## 推荐流程
1. 读取 README.md、AGENTS.md、docs/AI_FACTORY_MANUAL.md、logs/。
2. 检查 git status。
3. 执行最小必要修改。
4. 运行必要验证。
5. 更新日志。
6. 汇报变更、风险和下一步。
```

## 第十五章：GitHub 标准化收尾

GitHub 标准化的目标是让仓库成为项目的工程账本。所有文件结构、执行规则、日志、文档同步版都应在仓库中可见。

### 当前目录结构

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
├── workflows/
└── tools/
```

### Mac mini 主机级目录结构

项目仓库结构和主机级目录结构要分开。仓库内只放该项目需要版本管理的文件；Mac mini 主机级目录负责承载多个项目、实验、Codex 配置和 OpenClaw 工作区。

```text
~/dev/github/           # 正式 GitHub 项目目录
~/dev/lab/              # 临时实验目录，不承诺长期保存
~/.codex/               # Codex 配置、skills、用户级规则
~/.openclaw/            # OpenClaw/龙虾配置、workspace、agents、memory
~/.openclaw/workspace/  # OpenClaw 工作区，谨慎纳入 Git
NAS                     # 长期资料、知识库、大文件、备份
```

| 目录 | 用途 | 规则 |
| --- | --- | --- |
| ~/dev/github/ | 正式项目与可追溯工程资产。 | 重要项目进入 GitHub；每个项目应有 README、AGENTS.md、logs 或 docs。 |
| ~/dev/lab/ | 临时实验、测试 skill、一次性输出。 | 不作为长期真相来源；有价值内容及时迁移到正式仓库。 |
| ~/.codex/ | Codex 配置、skills、全局偏好和用户级规则。 | 不要混入具体项目产物；敏感配置不得提交。 |
| ~/.openclaw/ | OpenClaw gateway、旧工作流、memory、workspace。 | 不要整体上传 GitHub；只抽取需要版本管理的配置样例。 |
| NAS | 长期资料、知识库、大文件、备份。 | 大文件不随便进 git；按公开/私有/密钥/备份分类。 |

### 完成标准

- 远程仓库可正常 push/pull。
- 本地目录结构完整。
- 空目录使用 .gitkeep 保留。
- README.md 存在并说明项目定位。
- AGENTS.md 存在并说明 AI 执行规则。
- .gitignore 存在并排除 .env、密钥、缓存、日志临时文件。
- docs/AI_FACTORY_MANUAL.md 与 Word 手册保持同步。
- logs/ 中存在项目日志。
- 至少完成一次规范提交。
## 第十六章：命名规范

命名规范的目标是降低未来自动化和多 Agent 协作成本。名称应当稳定、可读、可搜索，并能被脚本安全处理。

### 项目与仓库命名

| 类型 | 规则 | 示例 |
| --- | --- | --- |
| 中文项目名 | 用于正式说明、人类阅读和手册标题。 | 个人 AI 工厂 |
| GitHub 仓库名 | 使用英文、短横线连接，保持与远程仓库一致。 | Duci-s-AI-Factory |
| 本地正式项目目录 | 建议长期放入 ~/dev/github/，目录名与仓库名一致。 | ~/dev/github/Duci-s-AI-Factory |
| 临时实验目录 | 放入 ~/dev/lab/，不得作为长期真相来源。 | ~/dev/lab/openclaw-test |

当前实际仓库路径仍是 /Users/duckulacissy/Duci-s-AI-Factory，后续可迁移或软链接到 ~/dev/github/Duci-s-AI-Factory。

### 仓库目录命名

仓库内目录统一使用小写英文复数，避免中文目录、空格和特殊符号。空目录统一用 .gitkeep 保留。

```text
agents/
docs/
logs/
prompts/
scripts/
tools/
workflows/
```

### 核心文件命名

| 文件 | 作用 | 规则 |
| --- | --- | --- |
| README.md | GitHub 首页和人工说明。 | 保持简洁，说明目标、架构、目录和当前阶段。 |
| AGENTS.md | AI 执行规则。 | 给 Codex/OpenClaw 读取，写清权限、安全、日志和流程。 |
| .gitignore | Git 忽略规则。 | 必须覆盖密钥、环境变量、缓存和临时输出。 |
| docs/AI_FACTORY_MANUAL.md | 手册仓库同步版。 | 与 Word 正式版在里程碑时保持一致。 |
| logs/YYYY-MM-DD.md | 项目日志。 | 用日期命名，记录当天状态、问题、经验和下一步。 |

### 当前仓库结构说明

以下结构是当前应保留并推送到 GitHub 的完整结构。它同时覆盖原有目录、P1 新增文件、P2 tmux SOP、P3 AI 执行 SOP 和 V3.4.1 回滚说明。

```text
Duci-s-AI-Factory/
├── .gitignore
├── AGENTS.md
├── README.md
├── agents/
│   └── .gitkeep
├── docs/
│   ├── .gitkeep
│   ├── AI_FACTORY_MANUAL.md
│   ├── AI_EXECUTION_SOP.md
│   ├── CODEX_PERSONAL_ENTRY.md
│   └── TMUX_SOP.md
├── logs/
│   ├── 2026-06-15.md
│   ├── 2026-06-16.md
│   ├── 2026-06-17.md
│   ├── 2026-06-18.md
│   ├── 2026-06-19.md
│   ├── 2026-06-20.md
│   ├── 2026-06-23.md
│   └── 2026-06-24.md
├── prompts/
│   └── .gitkeep
├── scripts/
│   ├── .gitkeep
│   ├── openclaw_codex_bridge_preview.py
│   ├── openclaw_codex_dry_run.py
│   ├── openclaw_telegram_auth_dry_run.py
│   └── openclaw_telegram_channel_config_draft.py
├── tools/
│   └── .gitkeep
└── workflows/
    └── .gitkeep
```

| 路径 | 来源 | 说明 |
| --- | --- | --- |
| .gitignore | P1 新增 | 防止 .DS_Store、.env、密钥、缓存和临时输出进入 GitHub。 |
| AGENTS.md | P1 新增 | AI 执行规则文件，供 Codex/OpenClaw 进入仓库时读取。 |
| README.md | 原有，P1 更新 | GitHub 首页说明，面向人类阅读。 |
| agents/ | 原有，保留 | 未来放 Agent 定义、角色配置和任务模板。 |
| agents/.gitkeep | 原有，保留 | 保留空的 agents/ 目录。 |
| docs/ | 原有，保留 | 项目文档目录。 |
| docs/.gitkeep | 原有，暂时保留 | 保留空目录的占位文件；已有真实文件后可在后续清理。 |
| docs/AI_FACTORY_MANUAL.md | P1 新增 | 手册 Markdown 同步版，供 GitHub、Codex、OpenClaw 读取。 |
| docs/AI_EXECUTION_SOP.md | P3 新增 | AI 执行 SOP，记录启动检查、审批等级、OpenClaw 任务包和 Codex 回传格式。 |
| docs/CODEX_PERSONAL_ENTRY.md | P4 边界说明 | 说明 Codex 当前入口、未来个人 gateway 接入方式和公司通道退役边界。 |
| docs/TMUX_SOP.md | P2 新增 | tmux 标准化 SOP，记录 ai-factory 会话、窗口分工和安全规则。 |
| logs/ | P1 新增 | 项目日志目录。 |
| logs/2026-06-15.md | P1 新增 | 记录 P0/P1 检查、标准化工作和阻塞问题。 |
| logs/2026-06-16.md | P1 新增 | 记录命名规范、手册更新和后续步骤。 |
| logs/2026-06-17.md | P2 新增 | 记录标准 ai-factory 会话创建、窗口命名和旧会话保留策略。 |
| logs/2026-06-18.md | P2/P3/通道清理 | 记录旧 tmux 会话清理、P3 执行规范、公司通道隔离和退役过程。 |
| logs/2026-06-19.md | V3.4.1 回滚 | 记录从后续单独使用 Codex 的方向回到 V3.4.1 阶段，并修正主机架构表述。 |
| logs/2026-06-20.md | P4-A 决策与 A1-A4 方案 | 记录本地沙盒链路验证决策、边界、任务树、A1-A3 执行和 A4 手动启动方案。 |
| logs/2026-06-23.md | P4-A A4 实测 | 记录 A4 gateway 手动启动、loopback 监听、无后台服务、关闭后端口释放和预期 API key 报错。 |
| logs/2026-06-24.md | P4-A A6/A7 与 P4-B 方案 | 记录 A6 最小本地安全测试、P4-A 收尾评估和 P4-B dry-run 方案。 |
| prompts/ | 原有，保留 | 未来放提示词模板。 |
| prompts/.gitkeep | 原有，保留 | 保留空的 prompts/ 目录。 |
| scripts/ | 原有，保留 | 未来放环境检查、启动服务、调用 Codex 等可执行脚本。 |
| scripts/.gitkeep | 原有，保留 | 保留 scripts/ 目录占位。 |
| scripts/openclaw_codex_bridge_preview.py | P4-C 新增 | 本地桥接预览脚本；把 dry-run 任务包转换成未来 `codex exec` 命令预览，但不执行。 |
| scripts/openclaw_codex_dry_run.py | P4-B 新增 | OpenClaw 到 Codex 转交合约 dry-run 脚本；只生成任务包和风险判定，不执行 Codex。 |
| tools/ | P1 新增 | 未来放辅助工具或可复用小程序，例如手册生成、日志解析、仓库检查。 |
| tools/.gitkeep | P1 新增 | 保留空的 tools/ 目录。 |
| workflows/ | 原有，保留 | 未来放 OpenClaw 到 Codex 到 GitHub 到回传的工作流定义。 |
| workflows/.gitkeep | 原有，保留 | 保留空的 workflows/ 目录。 |

当前没有需要删除的目录。.DS_Store、临时输出、密钥和环境变量文件应继续由 .gitignore 阻止进入 GitHub。

### 正式手册命名

```text
个人AI工厂建设手册_V{主版本}.{次版本}_正式版.docx
示例：个人AI工厂建设手册_V3.4_正式版.docx
```

### 日志与文档命名

- 项目日志：logs/YYYY-MM-DD.md。
- 故障记录：优先写入当天日志；需要独立文件时使用 logs/YYYY-MM-DD_incident_简短英文说明.md。
- SOP 文档：放入 docs/，使用大写英文和下划线，例如 DEPLOYMENT_SOP.md。
- 面向 AI 的长期规则：优先写入 AGENTS.md。
- 面向人的正式说明：优先写入 README.md 或 Word 手册。
### tmux 命名

长期 session 固定为 ai-factory。推荐窗口名：control、codex、gateway、logs、dev、monitor。临时 session 使用小写英文短横线，例如 openclaw-test 或 docs-render。

### 脚本、工具与任务命名

脚本文件统一使用小写英文和下划线。命名动词优先使用 check_、run_、sync_、build_、deploy_、backup_、restore_、doctor_。

```text
scripts/check_environment.sh
scripts/run_codex_task.sh
tools/render_manual.py
```

### Git 分支与提交命名

分支名使用小写英文短横线；提交信息使用简短英文祈使句，便于 GitHub 历史检索。

```text
p1-github-standardization
p2-tmux-standardization
fix-github-ssh
docs-naming-rules

Standardize AI factory repository
Add naming rules to manual
Fix GitHub SSH setup notes
```

### OpenClaw 与 Codex 任务命名

OpenClaw 接收到工程任务后，应生成稳定任务名，格式建议为 YYYY-MM-DD_简短英文任务名。任务名用于日志、临时工作目录、回传摘要和后续检索，不得包含密钥、客户隐私、账号密码或长句。

```text
2026-06-16_add-naming-rules
2026-06-16_fix-github-ssh
```

## 第十七章：tmux 标准化

tmux 是远程长期执行的基础。它解决 SSH 断线后任务丢失的问题，也让 Codex、OpenClaw、日志窗口和服务窗口有固定位置。

当前唯一标准会话为 `ai-factory`，所有窗口起始路径统一为 `/Users/duckulacissy/Duci-s-AI-Factory`。旧 session `factory`、`codex`、`openclaw`、`monitor` 已在确认后清理。

| 窗口 | 标准命名 | 分工 |
| --- | --- | --- |
| 0 | control | 项目总控、Git 状态、临时命令、阶段检查。 |
| 1 | codex | Codex CLI 执行窗口，负责工程任务、文件修改、命令运行。 |
| 2 | gateway | 未来个人 OpenClaw gateway 或消息桥接窗口；当前保持 inactive，未经确认不启动任何 gateway，不运行公司 `cc-connect` / Feishu。 |
| 3 | logs | OpenClaw、Codex、Git 和系统服务日志观察窗口。 |
| 4 | dev | npm、Python、skill、脚本测试和临时开发任务。 |
| 5 | monitor | htop、磁盘、网络、服务状态和健康检查。 |

### 推荐命令

```text
tmux ls
tmux new -As ai-factory
tmux attach -t ai-factory
tmux rename-window control
```

### 完成标准

- 固定 session 名称为 ai-factory。
- 可通过 SSH 断线重连后恢复 session。
- Codex、OpenClaw gateway、logs、dev、monitor 不混用同一个窗口。
- 服务启动、停止、重启命令写入 SOP。
- 关键输出可追溯到日志文件。

## 第十八章：权限与安全边界

```text
安全原则
AI 工厂越自动化，越要限制默认权限。默认允许读取和建议；默认不允许删除、重置、泄露密钥、暴露服务或改变核心架构。
```

- API Key、SSH Key、Token、密码不得写入 GitHub。
- .env、*.key、*.pem、*.p12、secrets/ 必须进入 .gitignore。
- SSH Key 不复制到项目目录。
- NAS 中区分公开资料、私有资料、密钥资料和备份资料。
- Agent 默认不得删除文件、重置仓库、强制推送、修改系统级权限。
- 涉及端口暴露、公网访问、反向代理、远程登录权限时必须先确认。
- 涉及付费 API、长期运行服务、自动发送消息时必须先确认。
### 禁止暴露到公网

- SSH 22 端口。
- VNC / 屏幕共享 5900 端口。
- OpenClaw gateway。
- 本地 Web 服务调试端口。
以上入口统一走 Tailscale 私有网络。不要为了方便临时打开路由器端口，也不要用公网 IP 直连 Mac mini。公司 `cc-connect` / Feishu 已废除，不作为个人 AI 工厂入口。

## 第十九章：回滚与恢复机制

| 故障场景 | 优先处理 | 恢复记录 |
| --- | --- | --- |
| SSH 连接失败 | 检查 Tailscale 在线状态、IP、SSH 服务、用户名和密钥。 | 写入故障日志，记录最终原因。 |
| tmux session 丢失 | 确认是否服务重启；按 SOP 重建 ai-factory session。 | 记录丢失窗口和是否有未保存任务。 |
| Git 仓库异常 | 先 git status；禁止直接 reset；必要时新建备份分支。 | 记录异常文件、原因和恢复命令。 |
| Codex 执行失败 | 保留输出，缩小任务范围，重新读取 AGENTS.md。 | 记录失败原因、修复方法和下一步。 |
| OpenClaw 配置错误 | 停止服务，恢复最近可用配置，重新小范围测试。 | 记录配置文件、变更点和回滚版本。 |
| NAS 挂载失败 | 检查网络、凭据、挂载路径和权限。 | 记录路径、错误信息和恢复方式。 |

## 第二十章：故障排查库初版

故障排查库用于把常见问题变成可执行检查路径。遇到问题时先查本章，再临时求助或搜索。

| 问题 | 检查顺序 | 处理建议 |
| --- | --- | --- |
| Mac mini 连不上 | 1. Mac mini 是否开机；2. 是否登录 Tailscale；3. MacBook 是否同一 tailnet；4. SSH 服务是否开启。 | 不要用公网 IP；优先使用 Tailscale IP；必要时用 VNC 或本地屏幕救急。 |
| Codex 命令找不到 | 1. command -v codex；2. shell PATH；3. Codex 是否安装；4. 是否在正确用户下执行。 | 修复 PATH 或重新安装 Codex CLI；记录修复命令。 |
| tmux 滚动不方便 | 检查是否进入 copy-mode。 | 先使用 tmux 原生命令滚动；不要一开始强行开鼠标模式，避免影响复制。 |
| OpenClaw gateway 挂了 | openclaw gateway status --deep；openclaw doctor；openclaw logs --follow --local-time。 | 保留日志，确认配置文件和端口；必要时 openclaw gateway restart。 |
| Mac mini 重启后服务未恢复 | 检查 Tailscale、tmux、Codex CLI、OpenClaw gateway、GitHub 仓库状态。 | 按重启后检查清单逐项恢复，写入故障日志。 |
| Git 状态混乱 | git status；git diff；确认是否有用户未提交修改。 | 禁止直接 reset；必要时新建备份分支或先提交 WIP。 |

## 第二十一章：常用命令速查表

| 类别 | 命令 | 用途 |
| --- | --- | --- |
| Mac mini 远程 | ssh 用户名@Tailscale-IP | 从 MacBook 进入 Mac mini。 |
| tmux | tmux new -As ai-factory | 创建或进入固定会话。 |
| tmux | tmux ls | 查看当前会话。 |
| Codex | codex --version | 确认 Codex CLI 可用。 |
| Codex | codex exec --cd ~/dev/github/项目名 "任务内容" | 让 OpenClaw 或脚本触发 Codex 非交互执行。 |
| OpenClaw | openclaw gateway start | 启动 gateway。 |
| OpenClaw | openclaw gateway status --deep | 查看 gateway 深度状态。 |
| OpenClaw | openclaw logs --follow --local-time | 跟随查看本地时间日志。 |
| Git | git status | 任何修改前先看仓库状态。 |
| Git | git diff | 提交前查看实际改动。 |
| Tailscale | tailscale status | 确认私有网络连通。 |

## 第二十二章：环境清单

以下清单需要在下一轮现场体检时补齐。它不是装饰信息，而是未来迁移、恢复和自动化的基础。

| 项目 | 当前值 | 备注 |
| --- | --- | --- |
| Mac mini 主机名 | DuckulasydeMini.lan | hostname |
| Tailscale IP | 待补充 | 当前 shell 未发现 tailscale CLI，后续从 Tailscale App 或 CLI 补齐。 |
| GitHub 仓库地址 | git@github.com:duci0603/Duci-s-AI-Factory.git | origin fetch/push |
| 本地仓库路径 | /Users/duckulacissy/Duci-s-AI-Factory | Mac mini 上的实际路径 |
| Node.js 版本 | v26.3.0 | node -v |
| Git 版本 | 2.50.1 (Apple Git-155) | git --version |
| Codex CLI 版本 | 0.139.0 | codex --version |
| OpenClaw 路径 | /opt/homebrew/bin/openclaw | 2026-06-19 已安装 CLI，版本 2026.6.8；2026-06-23 已完成 A4 手动 gateway 启动验证，当前已停止，LaunchAgent 未安装。 |
| tmux session 名称 | ai-factory | 建议固定 |
| NAS 挂载路径 | 待补充 | 长期记忆库 |

## 第二十三章：项目日志制度

禁止依赖记忆推进项目。每个阶段和里程碑必须记录日志。

### 记录内容

- 日期
- 当前阶段
- 完成事项
- 问题
- 原因
- 解决方案
- 经验
- 下一步
### 项目日志 #001

完成事项：Tailscale 部署、SSH 远程控制、VNC 远程桌面。

经验：SSH 作为主控制通道。VNC 作为备用图形界面通道。当 SSH、5900 端口、Tailscale 正常时，优先检查 Screen Sharing 服务状态。

### 项目日志 #002

完成事项：GitHub 账号创建、SSH Key 生成、GitHub SSH 认证成功、Duci-s-AI-Factory 仓库创建、本地仓库同步、agents/docs/prompts/scripts/workflows 目录建立。

经验：Git 不会跟踪空目录。目录初始化时应创建 .gitkeep 文件。

下一步：完成 GitHub 标准化收尾，进入 tmux 标准化。

### 项目日志 #003

完成事项：基于 V3.2 手册和部署讨论，形成 V3.3 手册更新。新增部署阶段、验收关卡、OpenClaw+Codex 协作工作流、任务路由规则、AGENTS.md 基础版、安全边界、回滚恢复机制和环境清单。

下一步：进行 Mac mini 环境体检，并执行 GitHub 标准化收尾。

### 项目日志 #004

完成事项：结合《个人专属超级AI系统搭建教程》文章，形成 V3.4 手册更新。新增 Mac mini 常驻主机规范、OpenClaw/龙虾 gateway 定位、Codex 三种形态、主机级目录结构、tmux 窗口建议、常用命令速查表和故障排查库初版。

经验：OpenClaw/龙虾不应作为复杂工程主 Agent；更稳的分工是 OpenClaw 负责接活，Codex 负责干活，GitHub 负责记录，Mac mini 负责常驻。

下一步：执行 Mac mini 环境体检，补齐环境清单，并完成 GitHub 标准化收尾。

### 项目日志 #005

日期：2026-06-15。完成事项：创建 .gitignore、AGENTS.md，更新 README.md，同步 docs/AI_FACTORY_MANUAL.md 到 V3.4 仓库同步版，创建 logs/ 与 tools/ 标准目录。

问题：GitHub SSH 认证仍需修复；当前命令行未发现 tailscale CLI 和 openclaw CLI。下一步：修复 GitHub SSH 公钥认证，设置 Git 全局用户名和邮箱，完成一次规范提交并推送。

### 项目日志 #006

日期：2026-06-16。完成事项：新增项目命名规范，覆盖仓库、目录、文件、日志、tmux、脚本、分支、提交信息和 OpenClaw/Codex 任务名；同步更新 AGENTS.md 和手册正式版。

下一步：渲染并确认 Word 手册；随后解决 Git 写入权限、Git 身份和 GitHub SSH 认证，完成 P1 标准化提交。

### 项目日志 #007

日期：2026-06-17。完成事项：创建标准 tmux session ai-factory，建立 control、codex、gateway、logs、dev、monitor 六个窗口，并记录 TMUX_SOP。旧 session 暂时保留作为回滚。

下一步：确认新布局舒适后，清理旧空 session，并继续推进 AI 执行规范。

### 项目日志 #008

日期：2026-06-18。完成事项：清理旧空 tmux session；确认 ai-factory 为唯一标准会话；新增 docs/AI_EXECUTION_SOP.md；更新 AGENTS.md、README.md 和手册同步版；提交并推送 Add AI execution SOP。随后按用户确认废除公司侧 `cc-connect` / Feishu 通道，旧运行目录、会话、日志、LaunchAgent 和旧同步脚本不再作为个人 AI 工厂流程使用。

下一步：进入 P4 OpenClaw 试部署，先验证个人 gateway 能启动、能接收测试消息、能调用本地脚本，且不会自动执行高风险任务。

### 项目日志 #009

日期：2026-06-19。完成事项：根据 `个人AI工厂建设手册_V3.4.1_正式版.docx` 回滚仓库文档到 V3.4.1 阶段；修正主机架构表述，明确主机链路是 MacBook Air → Tailscale/SSH → Mac mini → GitHub → NAS，OpenClaw/龙虾属于未来个人 AI 工作流 gateway，不是主机链路中的独立主机。

边界：公司侧 `cc-connect` / Feishu 不恢复、不复用；未来 OpenClaw/龙虾试部署必须使用个人专用配置、个人凭证、个人日志和独立会话。

下一步：在用户确认后进入 P4，只做 OpenClaw/龙虾可用性和安装路径检查，不启动长期 gateway 服务。

### 项目日志 #010

日期：2026-06-19。完成事项：完成 OpenClaw 官方资料核对；安装 OpenClaw CLI；确认 gateway 未启动、LaunchAgent 未安装、channels 未配置、sessions 为 0。

下一步：确认 onboarding 策略后再执行，不直接启动 gateway。


### 项目日志 #011

日期：2026-06-20。完成事项：确认 P4-A 本地沙盒链路验证策略；明确本阶段验证流程能否安全走通，不使用真实项目测试，不接真实消息入口，不自动调用 Codex 修改文件。

边界：使用个人专用 `~/.openclaw`；gateway 只绑定 `127.0.0.1:18789`；暂不安装 daemon / LaunchAgent；暂不接 channels；不使用公司 `cc-connect`；不公网暴露；只使用个人 API/模型授权；手动启动，测试后可停止。

下一步：执行 A1 前置只读检查，只查路径、版本、端口、`~/.openclaw` 状态和 `cc-connect` 清理状态，不运行 `openclaw onboard`，不启动 gateway。


### 项目日志 #012

日期：2026-06-20。完成事项：完成 P4-A 的 A1 前置只读检查、A2 沙盒边界确认、A3 最小化本地 onboarding；整理 A4 手动启动 gateway 的执行方案和检测/停止命令。

A1 结果：OpenClaw CLI 位于 `/opt/homebrew/bin/openclaw`，版本 `OpenClaw 2026.6.8 (844f405)`；18789 端口未监听；`cc-connect` 命令不可执行；LaunchAgent / daemon 未安装；channels 未配置。

A2 决策：local、loopback、18789、tailscale off、token auth、不安装 daemon、不接 channels、不公网暴露、不复用公司配置、不自动调用 Codex 改文件。

A3 结果：生成 `~/.openclaw/openclaw.json`、`~/.openclaw/workspace`、`~/.openclaw/agents/main/sessions`；token 使用 `OPENCLAW_GATEWAY_TOKEN` 环境变量引用，配置文件不保存明文 token；未启动 gateway，未接 channels，未写模型 API key。

A4 方案：等待用户再次确认后，在 tmux gateway 窗口前台运行 `openclaw gateway run --bind loopback --port 18789 --auth token --tailscale off`；另开窗口用 `lsof` 和 `openclaw gateway status` 检测；测试后用 `Ctrl+C` 停止并确认端口关闭。

下一步：等待用户确认是否执行 A4 手动启动 gateway。

### 项目日志 #013

日期：2026-06-23。完成事项：完成 P4-A 的 A4 手动 gateway 启动验证和关闭验证。

A4 结果：OpenClaw gateway 在 `tmux` 的 `gateway` 窗口中以前台方式启动成功；监听地址仅为 `127.0.0.1:18789` 与 `[::1]:18789`；未公网暴露；LaunchAgent not loaded；service not installed；`launchctl list` 未发现 OpenClaw / cc-connect / claw 相关后台项。

关闭结果：使用 `Ctrl+C` 停止 gateway，日志显示 clean shutdown；停止后 `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出，确认端口关闭。

预期内问题：运行期间出现 `No API key found for provider "openai"`，原因是 A3 故意未写入模型 API key。该问题不影响 A4 gateway 启动验证，但意味着当前不能执行真实模型任务。

下一步：进入 A5 只读健康检查；不接真实消息入口，不发送外部消息，不运行真实工程任务。

### 项目日志 #014

日期：2026-06-24。完成事项：完成 P4-A 的 A6 最小本地安全测试和 A7 收尾记录。

A6 结果：OpenClaw gateway 在 `tmux` 的 `gateway` 窗口中以前台方式临时启动成功；监听地址仅为 `127.0.0.1:18789` 与 `[::1]:18789`；未出现公网监听；Tailscale exposure 保持 off；daemon / LaunchAgent 未安装。

状态检查：`openclaw gateway status`、`openclaw status`、`openclaw health`、`openclaw channels status`、`openclaw sessions list` 已执行。gateway 可达，但因当前命令路径没有 token/password 或 paired device token，health/status read-scope RPC 以认证/identity 安全失败结束；这符合 A6 最小安全测试边界。

边界保持：未配置模型 API key，未接 channels，未发送外部消息，未运行真实工程任务，未让 OpenClaw 调用 Codex 修改文件。

收尾结果：使用 `Ctrl+C` 停止 gateway，日志显示 clean shutdown；停止后 `lsof -nP -iTCP:18789 -sTCP:LISTEN` 无输出；`launchctl list` 未发现 OpenClaw / cc-connect / claw 后台项。

下一步：做 P4-A 收尾评估，并确认 P4-B 的目标、边界和授权策略；不要直接进入真实消息入口、模型 API key 或 daemon 部署。

### 项目日志 #015

日期：2026-06-24。完成事项：完成 P4-A 收尾评估，确认 P4-A 通过并可关闭；写入 P4-B OpenClaw 到 Codex 转交合约 dry-run 方案，并准备最小 dry-run 脚本。

P4-A 收尾评估：18789 端口无监听；`launchctl list` 未发现 OpenClaw / cc-connect / claw 后台项；`openclaw gateway status` 指向 local loopback 且 `ECONNREFUSED`，符合 gateway 已停止预期；Gateway service 和 Node service 均为 LaunchAgent not installed；channels 仍未配置；仅有本地 direct session `agent:main:main`。

P4-B 方案：先定义任务包字段、风险分级和拦截规则；只做本地 dry-run，不启动 gateway，不接 channels，不配置模型 API key，不安装 daemon，不发送消息，不调用 `codex exec`。

脚本准备：新增 `scripts/openclaw_codex_dry_run.py`，用于根据请求生成 dry-run JSON、风险判定和 Codex 任务包预览；脚本不执行 Codex，不写项目文件，不读取或保存密钥。

初步验证：只读总结请求返回 `L0 / dry_run_allowed`；文档更新请求返回 `L1 / approved_scope_only`；破坏性 `rm -rf logs` 请求返回 `L3 / blocked`；假 token-like 输入被脱敏为 `[REDACTED_SECRET]` 并返回 `L2 / needs_confirmation`。

下一步：判断当前 smoke verification 是否足够作为 P4-B 最小验收，或追加更多假任务；通过前不要进入真实消息入口、模型 API key、daemon 部署或自动 Codex 执行。

### 项目日志 #016

日期：2026-06-24。完成事项：完成 P4-C 本地脚本桥接预览；新增 `scripts/openclaw_codex_bridge_preview.py`，复用 P4-B dry-run 风险分类与脱敏逻辑，把允许预览的任务转换成未来 `codex exec` 命令草案。

边界保持：脚本只输出 JSON；不启动 OpenClaw gateway，不接 channels，不配置模型 API key，不安装 daemon / LaunchAgent，不发送消息，不调用真实 `codex exec`，不自动修改项目文件。

预演结果：L0 只读总结请求生成命令预览且 `execution_allowed_now=false`；L1 文档更新请求生成命令预览但仍要求真实执行前确认任务范围；L2 假 token-like + gateway 请求被脱敏并 hold；L3 删除日志请求被 hold。

结论：P4-C 最小桥接预览通过。当前仍没有真实执行链路，OpenClaw 不会调用 Codex。

下一步：做 P4-C 收尾评估，并准备 P5-A 入口选择策略；不要直接接入真实消息入口、模型 API key、daemon 或自动 Codex 执行。

### 项目日志 #017

日期：2026-06-24。完成事项：完成 P4-C 收尾评估，并写入 P5-A 个人消息入口选择策略。

P4-C 收尾评估：P4-C 最小桥接预览通过并可关闭。L0/L1 只生成未来 `codex exec` 命令草案，且始终 `execution_allowed_now=false`；L2/L3 继续 hold；当前仍没有真实 OpenClaw → Codex 执行链路。

P5-A 策略：对 Telegram、Slack、个人飞书、微信和本地 CLI 入口做候选对比。首选建议为 Telegram 个人 bot，采用 DM-only + allowlist；不启用群聊，不接团队 workspace，不复用公司 `cc-connect` / Feishu。

边界保持：本次只写策略与日志；不连接任何 channel，不写入 bot token 或模型 API key，不启动 gateway，不安装 daemon / LaunchAgent，不发送消息，不调用真实 `codex exec`。

下一步：由用户确认是否采用 Telegram 个人 bot 作为首个真实入口；确认后进入 P5-B 凭证与授权方案设计，仍先做配置草案与 dry-run。

### 项目日志 #018

日期：2026-06-24。完成事项：完成 P5-B Telegram 凭证与授权 dry-run 方案，并新增 `scripts/openclaw_telegram_auth_dry_run.py`。

依据：`openclaw channels add --help` 显示 Telegram 可作为 channel，且支持 `--token`、`--bot-token`、`--token-file`、`--use-env` 等凭证参数。P5-B 采用 dry-run 方式，不执行真实 `openclaw channels add`。

方案：首选 env-backed 凭证，未来环境变量名为 `OPENCLAW_TELEGRAM_BOT_TOKEN`；备选 token-file 只允许绝对路径且不得进入 Git；禁止 inline token。授权策略为 DM-only、allowlist only、groups disabled、unknown sender deny。

脚本验证：`scripts/openclaw_telegram_auth_dry_run.py --examples` 覆盖 env-backed + allowlist、缺少 allowlist、inline placeholder 三类场景；所有场景均 `connection_allowed_now=false`，不读取 token，不写 OpenClaw 配置，不发送消息。

边界保持：本次只写方案、日志和 dry-run 脚本；未连接 Telegram，未写入 bot token，未启动 gateway，未安装 daemon / LaunchAgent，未发送消息，未调用真实 `codex exec`。

下一步：用户审阅 P5-B 凭证来源与 allowlist 字段；确认后才进入 P5-C 最小 channel 配置草案，且 P5-C 仍需单独确认。

### 项目日志 #019

日期：2026-06-24。完成事项：完成 P5-C 最小 Telegram channel 配置草案，并新增 `scripts/openclaw_telegram_channel_config_draft.py`。

依据：只读确认 `openclaw channels status --help`、`openclaw channels list --help`、`openclaw channels remove --help` 和 `openclaw gateway status --help`；明确未来可用的 list/status/add/remove/probe/rollback 命令形态。

方案：P5-C 复用 P5-B 的 env-backed 凭证和 allowlist 草案，生成未来真实配置的 preflight、config、verify、probe 和 rollback 命令预览；所有预览均 `execution_allowed_now=false`。

脚本验证：`scripts/openclaw_telegram_channel_config_draft.py --examples` 覆盖 env-backed + allowlist、缺少 allowlist 两类场景；allowlist 完整时返回 `draft_ready`，缺少 allowlist 时 hold 且不生成配置序列。

边界保持：本次只写草案、日志和 dry-run 脚本；未连接 Telegram，未读取或写入 bot token，未执行 `openclaw channels add/remove/status --probe`，未启动 gateway，未安装 daemon / LaunchAgent，未发送消息。

下一步：用户审阅 P5-C 草案；如要进入真实配置，必须在 P5-D 中单独确认凭证输入方式、allowlist 值、执行窗口、验收命令和回滚策略。

### 项目日志 #020

日期：2026-06-24。完成事项：按用户要求更新手册 / 日志，并基于当前 `docs/AI_FACTORY_MANUAL.md` 导出一份可下载 Word 手册。

导出范围：Word 手册以当前 Markdown 同步版为内容来源，包含截至 P5-C 的 OpenClaw / Telegram channel 配置草案、P5-B 凭证授权 dry-run、P5-A 入口策略、P4-A 至 P4-C 收尾记录，以及项目日志 #001 至 #020。

边界保持：本次只做文档记录与 Word 导出；未连接 Telegram，未读取或写入 bot token，未执行 `openclaw channels add/remove/status --probe`，未启动 gateway，未安装 daemon / LaunchAgent，未发送消息。

下一步：用户审阅导出的 Word 手册和 P5-C 草案；如要进入真实 Telegram channel 配置，必须在 P5-D 中单独确认。

### 项目日志 #021

日期：2026-06-24。完成事项：按用户确认，写入 P5-D 真实 Telegram channel 配置审批清单。

审批清单：P5-D 明确真实配置前必须确认五件事：是否进入真实配置、凭证输入方式、allowlist 值、最小验收范围和回滚方式。默认建议为 env-backed 凭证、DM-only、allowlist only、只做本地 list/status 验收、不 probe、不发消息、soft rollback。

禁止动作：不得记录真实 token，不使用 inline token，不执行 `channels status --probe`，不发送 Telegram 测试消息，不启用群聊，不安装 daemon / LaunchAgent，不启动长期 gateway，不配置模型 API key，不执行 `channels remove --delete`，不复用公司 `cc-connect` / Feishu。

边界保持：本次只写审批清单；未连接 Telegram，未读取或写入 bot token，未执行 `openclaw channels add/remove/status --probe`，未启动 gateway，未安装 daemon / LaunchAgent，未发送消息。

下一步：用户逐项确认 P5-D 审批清单；只有用户明确说进入 P5-E 真实配置执行后，才可进入真实 Telegram channel 配置。

### 项目日志 #022

日期：2026-06-24。完成事项：根据用户新决策，入口路线从 Telegram 改为个人飞书。

决策：用户明确表示“不要选择 Telegram 作为 gateway 的入口，选择飞书”。因此 Telegram P5-B / P5-C / P5-D 保留为历史 dry-run、配置草案和审批清单记录，但不再作为当前执行路线；不进入 Telegram 真实配置。

本地依据：只读确认 `openclaw channels add --help` 和 `openclaw channels status --help` 的 channel 列表均包含 `feishu`。

边界保持：这里的“飞书”只允许是个人飞书 / 个人专用配置；不得复用公司 `cc-connect` / Feishu，不恢复旧公司运行目录、会话、日志、LaunchAgent 或同步脚本；未连接飞书，未读取或写入 app secret / token，未启动 gateway，未安装 daemon / LaunchAgent，未发送消息。

同步操作：正式中文 Word 手册已按当前 Markdown 重新生成，包含 P5-E 入口决策变更。

下一步：进入 P5-F 个人飞书入口资料核对与凭证授权 dry-run 方案；仍不直接配置真实飞书 channel。

### 项目日志 #023

日期：2026-06-24。完成事项：完成 P5-F 个人飞书入口资料核对与凭证授权 dry-run 方案，并新增 `scripts/openclaw_feishu_auth_dry_run.py`。

依据：只读核对 `openclaw --version`、`openclaw channels add --help`、`openclaw channels status --help` 和 OpenClaw 本地 Feishu 文档 `/opt/homebrew/lib/node_modules/openclaw/docs/channels/feishu.md`。确认本地 OpenClaw 版本为 `2026.6.8 (844f405)`，Feishu channel 支持默认 WebSocket 模式，关键配置字段包含 `appId`、`appSecret`、`dmPolicy`、`allowFrom`、`groupPolicy`、`groupAllowFrom` 和 `requireMention`。

方案：P5-F 首选 env SecretRef 凭证，不记录真实 app id / app secret。未来配置只引用 `OPENCLAW_FEISHU_APP_ID` 和 `OPENCLAW_FEISHU_APP_SECRET` 两个环境变量名；授权策略为个人 DM allowlist、groups disabled、unknown sender deny / pairing only、dynamic agent creation disabled、streaming disabled。

脚本验证：`scripts/openclaw_feishu_auth_dry_run.py --examples` 覆盖 env SecretRef + allowlist、缺少 allowlist、inline credential、personal-only 未确认、尝试启用 group allowlist 五类场景；allowlist 完整时返回 `draft_ready`，其他不满足边界的场景返回 `needs_allowlist` 或 `hold`。额外执行个人 open_id placeholder、personal-only 未确认、group allowlist 三类单独预演，结果符合预期。

边界保持：本次只写方案、日志和 dry-run 脚本；未连接飞书，未读取或写入 app id / app secret / verification token / encrypt key，未执行 `openclaw channels login/add/status --probe`，未写 `~/.openclaw` 配置，未启动 gateway，未安装 daemon / LaunchAgent，未发送消息，未调用真实 `codex exec`，未复用公司 `cc-connect` / Feishu。

验证备注：普通 `python3 -m py_compile scripts/openclaw_feishu_auth_dry_run.py` 因当前沙盒禁止写入 macOS Python 缓存目录 `~/Library/Caches/com.apple.python/...` 而失败；改用 `PYTHONPYCACHEPREFIX=/private/tmp/openclaw_feishu_pycache` 后编译通过，脚本也已通过 `python3 -B` 实际执行验证。

同步操作：正式中文 Word 手册已按当前 Markdown 重新生成，包含 P5-F 个人飞书凭证授权 dry-run 方案和项目日志 #023。

下一步：进入 P5-G 最小个人飞书 channel 配置草案；P5-G 仍只生成 preflight、配置、验收、probe 和回滚命令预览，不执行真实飞书配置。


## 第二十四章：未来章节规划

- 经验库
- 标准操作流程（SOP）
- Agent 设计
- OpenClaw 部署
- NAS 知识库
- 服务自启动与健康检查

## 第二十五章：最终目标

```text
微信 / Telegram / Slack / 定时任务
↓
OpenClaw / 龙虾 gateway
↓
codex exec / skill CLI / 脚本
↓
Codex 工程执行
↓
GitHub 记录
↓
结果回传
```

最终目标是构建真正属于自己的 AI 员工体系。它不是一次性部署一堆工具，而是逐步形成能接单、能执行、能记录、能恢复、能成长的长期系统。MacBook 是驾驶舱，Mac mini 是机房，Codex 是工程师，OpenClaw/龙虾是消息前台，Tailscale 是专线网络。
