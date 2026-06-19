# 个人AI工厂建设手册 V3.4.1（仓库同步版）

本文件根据本地正式 Word 手册 `个人AI工厂建设手册_V3.4.1_正式版.docx` 回滚同步，用于 Codex、OpenClaw、Git 和日常执行。

| 文档定位 | 项目唯一真相来源（SSOT） |
| --- | --- |
| 基础设施主线 | MacBook Air → Tailscale/SSH → Mac mini → GitHub → NAS |
| AI 工作流主线 | 个人消息入口 → OpenClaw/龙虾 → Codex → Tool Chain → GitHub/NAS |
| 核心分工 | 人负责决策，AI负责执行 |
| 本版更新 | GitHub SSH修复、标准tmux会话、AI执行SOP、窗口分工、目录文件说明、P4前置状态 |
| 更新日期 | 2026-06-18 |

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
- 确认 OpenClaw CLI / gateway 安装方式
- 确认 gateway 接收消息后如何安全转交 Codex
- 补齐 NAS 长期记忆库路径与资料分类
### 后续路线

```text
已完成：P0 基础设施验收
已完成：P1 GitHub 标准化
已完成：P2 tmux 标准化
已完成：P3 AI 执行规范固化
↓
下一步：P4 OpenClaw 试部署
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
│   └── 2026-06-19.md
├── prompts/
│   └── .gitkeep
├── scripts/
│   └── .gitkeep
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
| prompts/ | 原有，保留 | 未来放提示词模板。 |
| prompts/.gitkeep | 原有，保留 | 保留空的 prompts/ 目录。 |
| scripts/ | 原有，保留 | 未来放环境检查、启动服务、调用 Codex 等可执行脚本。 |
| scripts/.gitkeep | 原有，保留 | 保留空的 scripts/ 目录。 |
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
| OpenClaw 路径 | 待补充 | 当前仍未确认 openclaw CLI 安装路径，P4 处理。 |
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
