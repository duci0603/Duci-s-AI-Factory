# 个人AI工厂建设手册 V3.5（仓库同步版）

本文件是 GitHub 仓库中的机器可读同步版。正式 Word 手册由本地 Codex 输出目录保存为 `个人AI工厂建设手册_V3.5_正式版.docx`。

本文件用于 Codex、Git、tmux 和日常执行。重大版本应与 Word 正式版保持一致。

## 第一章：文档管理原则

本手册是项目唯一真相来源（SSOT）。

不再创建平行规划书。所有架构、决策、经验、故障、日志统一记录于本手册、仓库同步版或项目日志。项目推进不得依赖聊天记录或模型记忆。

## 第二章：项目目标

打造长期在线、可持续成长、可远程管理、可自主执行的个人 AI 工厂。

核心原则：人负责决策，AI 负责执行。

V3.5 核心分工：

```text
用户负责决策
Codex 负责执行
GitHub 负责记录
Mac mini 负责常驻
NAS 负责长期沉淀
```

当前正式路线不再包含公司侧 `cc-connect` / Feishu 通道，也不部署 OpenClaw gateway。个人 AI 工厂现阶段只使用 Codex App、Codex CLI、tmux `ai-factory`、GitHub，后续再接 NAS。

## 第三章：总体架构

```text
MacBook Air（驾驶舱）
↓
Tailscale
↓
SSH（主控制通道）
↓
Mac mini（AI 工厂）
↓
GitHub（项目仓库与版本记录）
↓
NAS（长期记忆库与资料沉淀）
```

主机级架构：

- MacBook Air：驾驶舱、遥控器、日常操作入口
- Mac mini：机房、AI 常驻主机、Codex 专用执行环境
- Codex：工程执行层，负责读项目、改文件、跑命令、生成 skill、维护代码
- Tailscale：专线网络，不暴露 SSH、VNC、未来消息入口和本地调试端口到公网
- GitHub：版本记录与成果沉淀
- NAS：长期资料、知识库、备份和大文件沉淀

## 第四章：项目治理规则

1. 本手册是唯一真相来源（SSOT）。
2. 不依赖聊天记录推进项目。
3. 不依赖模型记忆判断项目状态。
4. 所有重要决策必须写入手册。
5. 每完成一个阶段必须更新状态。
6. 每完成一个里程碑必须记录日志。
7. 涉及核心架构、权限、安全、密钥、远程服务暴露的变更必须先获得用户确认。
8. AI 可以建议修改路线，但必须说明变更内容、原因、收益、风险和迁移成本。

## 第五章：技术路线锁定机制

基础设施路线：

```text
MacBook Air → Tailscale → SSH → Mac mini → GitHub → NAS
```

Agent 路线：

```text
Codex App / Codex CLI → Tool Chain
```

未经批准不得修改核心架构、引入替代 Agent 框架、引入替代执行引擎或改变项目主线。

## 第六章：项目当前状态

已完成：

- Node.js
- Git
- Codex CLI
- SSH 远程控制
- VNC 远程桌面
- GitHub 仓库
- 本地项目骨架
- GitHub SSH 认证
- P1 GitHub 标准化
- P2 tmux 标准化
- P3 AI 执行规范固化
- 标准 tmux 会话：`ai-factory`
- 公司侧 `cc-connect` / Feishu 通道已废除；旧运行目录、会话、日志和同步脚本已按用户确认删除
- Codex 已作为个人 AI 工厂执行层保留，入口为 Codex App、Codex CLI、tmux 和 GitHub

待修复或待补齐：

- 当前命令行未发现 `tailscale` CLI
- NAS 长期记忆库路径与资料分类待补齐
- 如未来确实需要消息入口，需新建个人专用 gateway，不复用公司通道，且必须重新审批

## 第七章：部署阶段与验收关卡

| 阶段 | 目标 | 完成标准 |
|---|---|---|
| P0 | 基础设施验收 | SSH、Tailscale、VNC、GitHub SSH、Codex CLI 可用；记录主机名、IP、路径和版本。 |
| P1 | GitHub 标准化 | README、.gitignore、.gitkeep、docs、logs、AGENTS.md 基础版存在；完成一次规范提交。 |
| P2 | tmux 标准化 | 固定 session 名称、窗口命名、重连方式、日志窗口和执行窗口。 |
| P3 | AI 执行规范固化 | AGENTS.md 明确安全边界、执行流程、日志规则、禁止动作和审批规则。 |
| P4 | 公司通道废除与 Codex-only 固化 | 公司侧 `cc-connect` / Feishu 运行目录、会话、日志和旧同步脚本删除；文档确认个人 AI 工厂只使用 Codex App、Codex CLI、tmux、GitHub。 |
| P5 | NAS 知识库接入 | 资料分类、路径规范、备份策略和检索方式明确。 |
| P6 | 日常运维 SOP | 形成启动、停止、升级、故障排查、日志归档和恢复流程。 |

## 第八章：Codex-only 分工

用户负责决策、确认风险和批准关键动作。Codex 负责干活。GitHub 负责记录。Mac mini 负责常驻。NAS 负责长期沉淀。

Codex 是当前唯一正式工程执行层，负责进入仓库、读规则、改文件、跑命令、检查结果并记录日志。

当前已确认：公司侧 `cc-connect` / Feishu 通道已废除，不再作为个人 AI 工厂主流程的一部分。旧运行目录、会话、日志和同步脚本已按用户确认删除。Codex 本体不依赖 `cc-connect`，它通过 Codex App、Codex CLI、tmux `ai-factory` 和 GitHub 继续作为个人 AI 工厂执行层。

## 第九章：Codex-only 工作流

```text
你
↓
Codex App / Codex CLI
↓
tmux ai-factory
↓
Codex 工程执行
↓
GitHub 记录
↓
NAS 长期记忆（后续）
↓
你确认 / 追问 / 批准下一步
```

最小可行调用方式：

```bash
codex exec --cd ~/dev/github/Duci-s-AI-Factory "请检查项目状态，补齐 AGENTS.md，并更新项目日志"
```

当前仓库实际路径仍是：

```text
/Users/duckulacissy/Duci-s-AI-Factory
```

后续可再迁移或软链接到 `~/dev/github/`。

## 第十章：Codex 三种形态

| 形态 | 适合任务 | 建议使用场景 |
|---|---|---|
| Codex App | 完整项目开发、浏览器验证、图形界面、Computer Use、复杂多文件任务。 | 远程桌面进入 Mac mini 后使用。 |
| Codex CLI | SSH、脚本、自动化、改文件、跑命令、日志检查、`codex exec` 非交互任务。 | 个人 AI 工厂的命令行执行方式。 |
| Codex IDE 插件 | 在 VS Code / Cursor 内直接协作编辑代码。 | 人在 MacBook 上近距离开发和审阅代码。 |

## 第十一章：Mac mini 常驻主机规范

- Mac mini 尽量固定放置，保持供电稳定。
- 关闭自动睡眠，避免 Codex、tmux 长任务中断。
- Tailscale 保持登录同一账号，并确认 MacBook、iPhone、Mac mini 在同一个 tailnet 内。
- SSH 作为主控制通道，VNC/屏幕共享作为图形备用通道。
- 所有长期任务必须运行在 tmux 内，避免 SSH 断线导致任务丢失。
- 日志观察、Codex CLI、开发命令应拆分到不同 tmux 窗口。`gateway` 窗口仅保留为未来个人消息入口的预留空位，当前不得运行公司通道。

## 第十二章：仓库标准化

当前目标：P4 公司通道废除与 Codex-only 固化。

标准目录：

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

主机级建议目录：

```text
~/dev/github/          # 正式 GitHub 项目目录
~/dev/lab/             # 临时实验目录
~/.codex/              # Codex 配置、skills、用户级规则
~/.ai-factory/         # 未来个人 AI 工厂本机配置预留目录，创建前需确认
```

## 第十三章：命名规范

命名规范的目标是降低未来自动化和多人/多 Agent 协作成本。名称应当稳定、可读、可搜索，并能被脚本安全处理。

### 项目与仓库命名

| 类型 | 规则 | 示例 |
|---|---|---|
| 中文项目名 | 用于正式说明、人类阅读和手册标题。 | 个人 AI 工厂 |
| GitHub 仓库名 | 使用英文、短横线连接，保持与远程仓库一致。 | `Duci-s-AI-Factory` |
| 本地正式项目目录 | 建议长期放入 `~/dev/github/`，目录名与仓库名一致。 | `~/dev/github/Duci-s-AI-Factory` |
| 临时实验目录 | 放入 `~/dev/lab/`，不得作为长期真相来源。 | `~/dev/lab/gateway-test` |

当前实际仓库路径仍是：

```text
/Users/duckulacissy/Duci-s-AI-Factory
```

后续可迁移或软链接到：

```text
~/dev/github/Duci-s-AI-Factory
```

### 仓库目录命名

仓库内目录统一使用小写英文复数，避免中文目录、空格和特殊符号。

```text
agents/
docs/
logs/
prompts/
scripts/
tools/
workflows/
```

空目录统一用 `.gitkeep` 保留。临时实验、缓存、输出文件不得随意放入正式目录，应放入 `.gitignore` 覆盖的 `work/` 或 `outputs/`。

### 核心文件命名

| 文件 | 作用 | 规则 |
|---|---|---|
| `README.md` | GitHub 首页和人工说明。 | 保持简洁，说明目标、架构、目录和当前阶段。 |
| `AGENTS.md` | AI 执行规则。 | 给 Codex 读取，写清权限、安全、日志和流程。 |
| `.gitignore` | Git 忽略规则。 | 必须覆盖密钥、环境变量、缓存、临时输出。 |
| `docs/AI_FACTORY_MANUAL.md` | 手册仓库同步版。 | 与 Word 正式版在里程碑时保持一致。 |
| `logs/YYYY-MM-DD.md` | 项目日志。 | 用日期命名，记录当天状态、问题、经验和下一步。 |

### 当前仓库结构说明

以下结构是 P1 标准化后应保留并推送到 GitHub 的完整结构：

```text
Duci-s-AI-Factory/
├── .gitignore
├── AGENTS.md
├── README.md
├── agents/
│   └── .gitkeep
├── docs/
│   ├── .gitkeep
│   └── AI_FACTORY_MANUAL.md
├── logs/
│   ├── 2026-06-15.md
│   └── 2026-06-16.md
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
|---|---|---|
| `.gitignore` | P1 新增 | 防止 `.DS_Store`、`.env`、密钥、缓存和临时输出进入 GitHub。 |
| `AGENTS.md` | P1 新增 | AI 执行规则文件，供 Codex 进入仓库时读取。 |
| `README.md` | 原有，P1 更新 | GitHub 首页说明，面向人类阅读。 |
| `agents/` | 原有，保留 | 未来放 Agent 定义、角色配置和任务模板。 |
| `agents/.gitkeep` | 原有，保留 | 保留空的 `agents/` 目录。 |
| `docs/` | 原有，保留 | 项目文档目录。 |
| `docs/.gitkeep` | 原有，暂时保留 | 保留空目录的占位文件；已有真实文件后可在后续清理。 |
| `docs/AI_FACTORY_MANUAL.md` | P1 新增 | 手册 Markdown 同步版，供 GitHub 和 Codex 读取。 |
| `logs/` | P1 新增 | 项目日志目录。 |
| `logs/2026-06-15.md` | P1 新增 | 记录 2026-06-15 的 P0/P1 检查、标准化工作和阻塞问题。 |
| `logs/2026-06-16.md` | P1 新增 | 记录 2026-06-16 的命名规范、手册更新和后续步骤。 |
| `prompts/` | 原有，保留 | 未来放提示词模板。 |
| `prompts/.gitkeep` | 原有，保留 | 保留空的 `prompts/` 目录。 |
| `scripts/` | 原有，保留 | 未来放可执行脚本，例如环境检查、启动服务、调用 Codex。 |
| `scripts/.gitkeep` | 原有，保留 | 保留空的 `scripts/` 目录。 |
| `tools/` | P1 新增 | 未来放辅助工具或可复用小程序，例如手册生成、日志解析、仓库检查。 |
| `tools/.gitkeep` | P1 新增 | 保留空的 `tools/` 目录。 |
| `workflows/` | 原有，保留 | 未来放 Codex → GitHub → NAS 等工作流定义。 |
| `workflows/.gitkeep` | 原有，保留 | 保留空的 `workflows/` 目录。 |

当前没有需要删除的目录。`.DS_Store`、临时输出、密钥和环境变量文件应继续由 `.gitignore` 阻止进入 GitHub。

正式 Word 手册命名规则：

```text
个人AI工厂建设手册_V{主版本}.{次版本}_正式版.docx
```

示例：

```text
个人AI工厂建设手册_V3.5_正式版.docx
```

### 日志与文档命名

- 项目日志：`logs/YYYY-MM-DD.md`
- 故障记录：优先写入当天日志；需要独立文件时使用 `logs/YYYY-MM-DD_incident_简短英文说明.md`
- SOP 文档：放入 `docs/`，使用大写英文和下划线，例如 `DEPLOYMENT_SOP.md`
- 面向 AI 的长期规则：优先写入 `AGENTS.md`
- 面向人的正式说明：优先写入 `README.md` 或 Word 手册

### tmux 命名

长期 session 固定为：

```text
ai-factory
```

推荐窗口名：

```text
control
codex
gateway
logs
dev
monitor
```

临时 session 可使用小写英文短横线，例如：

```text
gateway-test
docs-render
```

### 脚本、工具与任务命名

脚本文件统一使用小写英文和下划线：

```text
scripts/check_environment.sh
scripts/run_codex_task.sh
tools/render_manual.py
```

命名动词优先使用 `check_`、`run_`、`sync_`、`build_`、`deploy_`、`backup_`、`restore_`、`doctor_`。脚本名应说明动作和对象，不使用 `test1.py`、`new.py`、`final_final.py` 这类临时名。

### Git 分支与提交命名

分支名使用小写英文短横线：

```text
main
p1-github-standardization
p2-tmux-standardization
fix-github-ssh
docs-naming-rules
```

提交信息使用简短英文祈使句，便于 GitHub 历史检索：

```text
Standardize AI factory repository
Add naming rules to manual
Fix GitHub SSH setup notes
```

### Codex 任务命名

Codex 执行工程任务时，应生成稳定任务名，格式建议：

```text
YYYY-MM-DD_简短英文任务名
```

示例：

```text
2026-06-16_add-naming-rules
2026-06-16_fix-github-ssh
```

任务名用于日志、临时工作目录、回传摘要和后续检索。任务名不得包含密钥、客户隐私、账号密码或长句。

## 第十四章：tmux 标准化

当前标准会话：

- `ai-factory`

P2 只读体检结论：

- 当前 4 个旧 session 均只有 1 个窗口。
- 窗口名均为默认 `zsh`。
- pane 当前命令均为 `zsh`。
- 当前路径均为 `/Users/duckulacissy`。
- 未发现正在运行的长期服务或命令。
- 旧 session 已在确认后清理。

P2 标准布局已完成：

- `ai-factory` session 已存在。
- 标准窗口已创建：`control`、`codex`、`gateway`、`logs`、`dev`、`monitor`。
- 所有标准窗口当前路径均为 `/Users/duckulacissy/Duci-s-AI-Factory`。
- 旧 session `factory`、`codex`、`openclaw`、`monitor` 已清理。

长期窗口分工：

| 窗口 | 命名 | 分工 |
|---|---|---|
| 0 | control | 项目总控、Git 状态、临时命令、阶段检查。 |
| 1 | codex | Codex CLI 执行窗口，负责工程任务、文件修改、命令运行。 |
| 2 | gateway | 预留但停用的消息入口窗口；当前不得运行公司 `cc-connect` 或其他 gateway。 |
| 3 | logs | Codex、Git、系统服务日志观察窗口。 |
| 4 | dev | npm、python、skill、脚本测试和临时开发任务。 |
| 5 | monitor | htop、磁盘、网络、服务状态和健康检查。 |

常用命令：

```bash
tmux ls
tmux new -s ai-factory
tmux new -As ai-factory
tmux attach -t ai-factory
tmux kill-session -t ai-factory
```

详细 SOP 见：

```text
docs/TMUX_SOP.md
```

## 第十五章：权限与安全边界

- API Key、SSH Key、Token、密码不得写入 GitHub。
- `.env`、`*.key`、`*.pem`、`*.p12`、`secrets/` 必须进入 `.gitignore`。
- SSH Key 不复制到项目目录。
- NAS 中区分公开资料、私有资料、密钥资料和备份资料。
- Agent 默认不得删除文件、重置仓库、强制推送、修改系统级权限。
- 涉及端口暴露、公网访问、反向代理、远程登录权限时必须先确认。
- 涉及付费 API、长期运行服务、自动发送消息时必须先确认。

禁止暴露到公网：

- SSH 22 端口
- VNC / 屏幕共享 5900 端口
- 公司侧 `cc-connect` / Feishu 通道
- 未经审批的未来消息 gateway
- 本地 Web 服务调试端口

以上入口统一走 Tailscale 私有网络。

## 第十六章：AI 执行规范固化

P3 目标是让 Codex 的执行边界可重复、可审批、可记录。

详细 SOP 见：

```text
docs/AI_EXECUTION_SOP.md
```

### 固定启动检查

每次工程任务开始前必须：

1. 读取 `README.md`。
2. 读取 `AGENTS.md`。
3. 读取 `docs/AI_FACTORY_MANUAL.md`。
4. 读取最近的 `logs/YYYY-MM-DD.md`。
5. 执行 `git status --short`。
6. 判断是否存在用户未提交修改。
7. 确认当前阶段、任务、风险和下一步。

### 审批等级

| 等级 | 含义 | 示例 |
|---|---|---|
| L0 | 只读检查，无需额外确认。 | 查看文件、Git 状态、tmux 状态、工具版本。 |
| L1 | 低风险项目编辑，用户确认方向后可执行。 | 更新文档、日志、SOP、非密钥项目文件、提交并推送。 |
| L2 | 必须明确确认。 | 删除文件、kill session、安装依赖、改 SSH/Tailscale/VNC、防火墙、处理密钥、启动长期服务。 |
| L3 | 除非用户明确指定，否则禁止。 | `git reset --hard`、force push、暴露公网端口、提交密钥、替换核心架构。 |

### Codex 任务包

Codex 接收工程任务时应明确：

```text
task_id: YYYY-MM-DD_short-task-name
repo: /Users/duckulacissy/Duci-s-AI-Factory
phase: P4
request: 用户请求
risk_level: L0 | L1 | L2 | L3
approval_status: approved | needs_confirmation
expected_output: summary, changed_files, verification, next_step
```

### Codex 回传格式

Codex 应回传：

```text
status: completed | blocked | needs_confirmation
changed_files:
verification:
risks:
next_step:
```

## 第十七章：故障排查库初版

| 问题 | 检查顺序 | 处理建议 |
|---|---|---|
| Mac mini 连不上 | Mac mini 是否开机；是否登录 Tailscale；MacBook 是否同一 tailnet；SSH 服务是否开启。 | 不要用公网 IP；优先使用 Tailscale IP；必要时用 VNC 或本地屏幕救急。 |
| Codex 命令找不到 | `command -v codex`；shell PATH；Codex 是否安装；是否在正确用户下执行。 | 修复 PATH 或重新安装 Codex CLI；记录修复命令。 |
| tmux 滚动不方便 | 检查是否进入 copy-mode。 | 先使用 tmux 原生命令滚动；不要一开始强行开鼠标模式，避免影响复制。 |
| 误触公司通道或旧 gateway | 检查是否出现 `cc-connect`、Feishu、旧 LaunchAgent 或未经审批的消息服务。 | 停止使用该入口；确认不读取旧密钥；回到 Codex App / Codex CLI / tmux 主流程。 |
| Git 状态混乱 | `git status`；`git diff`；确认是否有用户未提交修改。 | 禁止直接 reset；必要时新建备份分支或先提交 WIP。 |

## 第十八章：常用命令速查表

| 类别 | 命令 | 用途 |
|---|---|---|
| Mac mini 远程 | `ssh 用户名@Tailscale-IP` | 从 MacBook 进入 Mac mini。 |
| tmux | `tmux new -As ai-factory` | 创建或进入固定会话。 |
| tmux | `tmux ls` | 查看当前会话。 |
| Codex | `codex --version` | 确认 Codex CLI 可用。 |
| Codex | `codex exec --cd ~/dev/github/项目名 "任务内容"` | 通过 CLI 触发 Codex 非交互执行。 |
| Git | `git status` | 任何修改前先看仓库状态。 |
| Git | `git diff` | 提交前查看实际改动。 |
| Tailscale | `tailscale status` | 确认私有网络连通。 |

## 第十九章：项目日志制度

记录内容：

- 日期
- 当前阶段
- 完成事项
- 问题
- 原因
- 解决方案
- 经验
- 下一步

禁止依赖记忆推进项目。

## 项目日志 #001

完成事项：

- Tailscale 部署
- SSH 远程控制
- VNC 远程桌面

经验：

- SSH 作为主控制通道。
- VNC 作为备用图形界面通道。
- 当 SSH、5900 端口、Tailscale 正常时，优先检查 Screen Sharing 服务状态。

## 项目日志 #002

完成事项：

- GitHub 账号创建
- SSH Key 生成
- GitHub SSH 认证成功
- Duci-s-AI-Factory 仓库创建
- 本地仓库同步
- agents/docs/prompts/scripts/workflows 目录建立

经验：

- Git 不会跟踪空目录。
- 目录初始化时应创建 `.gitkeep` 文件。

下一步：

- 完成 GitHub 标准化收尾，进入 tmux 标准化。

## 项目日志 #003

完成事项：

- 基于 V3.2 手册和部署讨论，形成 V3.3 手册更新。
- 新增部署阶段、验收关卡、OpenClaw+Codex 协作工作流、任务路由规则、AGENTS.md 基础版、安全边界、回滚恢复机制和环境清单。

下一步：

- 进行 Mac mini 环境体检，并执行 GitHub 标准化收尾。

## 项目日志 #004

完成事项：

- 结合《个人专属超级AI系统搭建教程》文章，形成 V3.4 手册更新。
- 新增 Mac mini 常驻主机规范、OpenClaw/龙虾 gateway 定位、Codex 三种形态、主机级目录结构、tmux 窗口建议、常用命令速查表和故障排查库初版。

经验：

- OpenClaw/龙虾不应作为复杂工程主 Agent。
- 更稳的分工是 OpenClaw 负责接活，Codex 负责干活，GitHub 负责记录，Mac mini 负责常驻。

下一步：

- 执行 Mac mini 环境体检，补齐环境清单，并完成 GitHub 标准化收尾。

## 项目日志 #005

日期：2026-06-15

当前阶段：P1 GitHub 标准化。

完成事项：

- 创建 `.gitignore`。
- 创建 `AGENTS.md`。
- 更新 `README.md`。
- 同步 `docs/AI_FACTORY_MANUAL.md` 到 V3.4 仓库同步版。
- 创建 `logs/` 与 `tools/` 标准目录。
- 新增项目命名规范，覆盖仓库、目录、文件、日志、tmux、脚本、分支、提交信息和 OpenClaw/Codex 任务名。

问题：

- GitHub SSH 认证仍需修复：`Permission denied (publickey)`。
- 当前命令行未发现 `tailscale` CLI 和 `openclaw` CLI。

下一步：

- 修复 GitHub SSH 公钥认证。
- 设置 Git 全局用户名和邮箱。
- 完成一次规范提交并推送。

## 项目日志 #006

日期：2026-06-18

当前阶段：P4 公司通道废除与 Codex-only 固化。

完成事项：

- 将仓库同步手册升级为 V3.5。
- 明确个人 AI 工厂当前只使用 Codex App、Codex CLI、tmux `ai-factory`、GitHub，后续再接 NAS。
- 废除公司侧 `cc-connect` / Feishu 通道，不再作为个人 AI 工厂入口。
- 按用户确认删除旧公司通道运行目录、会话、日志、LaunchAgent 和旧同步脚本。
- 将 `gateway` tmux 窗口标记为预留但停用。
- 将 OpenClaw gateway 试部署从当前阶段计划中移除；未来如确实需要消息入口，必须新建个人专用通道并重新审批。

经验：

- 公司/工作消息通道和个人 AI 工厂必须隔离，不能共用凭证、会话、日志或默认入口。
- Codex 本体不依赖 `cc-connect`，可以作为个人 AI 工厂独立执行层继续运行。

下一步：

- 推进 P5 NAS 知识库接入。
- 另行确认是否需要卸载全局 `cc-connect` 命令本体。
