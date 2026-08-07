# 组织上云 · Cloud Agent + My Machines（本地落盘）

- **版本：** CursorTeam ≥1.1.5  
- **目标：** 组织默认走 **Cloud Agent**；对 `ORG_ROOT` / `GAME_ROOT` 的改文件与终端落在 **本机 worker**（My Machines）  
- **不是：** 纯云端 VM 改远程克隆却碰不到你电脑；也不是仅桌面「This Computer」本地 Agent  

---

## 定版架构

```text
入口（cursor.com/agents · Slack · GitHub…）
        │
        ▼
   Cloud Agent 编排（决策 / 对话在云端）
        │  tool call
        ▼
   My Machines worker（本机常驻）
        │
        ├── 改文件 / 终端 / stdio MCP → 本机磁盘与网络
        └── git remote → 组织仓云端 / 项目仓（见 rules/06）
```

| 模式 | 何时用 |
|------|--------|
| **Cloud + My Machines**（定版） | 组织刀、要改 `E:\dev\CursorTeam` 或本机 GAME_ROOT |
| **纯 Cloud VM** | 仅公网 GitHub/GitLab 仓、不需本机插件/UE/内网 |
| **桌面 Local Agent** | 你正坐在 Cursor IDE 里日常改代码（主控会话） |

---

## 本机 Worker（Windows）

### 一次性

```powershell
# 安装 CLI
irm 'https://cursor.com/install?win32=true' | iex
agent --version
agent login
agent status
```

凭证须为 **个人** 登录 / User API Key（**不能**用 Team Admin / Org / Service Account Key 启 My Machines）。

### 常驻（按仓各起一个）

```powershell
# 组织仓（CursorTeam）
cd E:\dev\CursorTeam
agent worker start --name "cursorteam-pc" --worker-dir E:\dev\CursorTeam

# 游戏仓（另开终端；remote 须已是目标 Git）
cd E:\Project\Game\S_\SCL
agent worker start --name "scl-pc" --worker-dir E:\Project\Game\S_\SCL
```

- **进程必须保持运行**（掉线 = 云端任务无法落本地）  
- **一 worker 绑启动目录的 git remote**；勿在错误目录启动  
- 代理环境：本机 v2ray / `ensure-v2ray.ps1`；放行 `api2.cursor.sh`、`api2direct.cursor.sh`  

保活建议：独立 PowerShell 窗口，或登录脚本调用 `scripts/start-org-worker.ps1`。

### 验收

1. 打开 https://cursor.com/agents  
2. 环境下拉出现 `cursorteam-pc`  
3. 发测试：「在 ORG_ROOT 写一行到 `docs/ops/_cloud_ping.md`」→ 本机应出现文件  

---

## 入口怎么指定本机

| 入口 | 示例 |
|------|------|
| Web Agents | 环境选 `cursorteam-pc` |
| Slack | `@Cursor worker=cursorteam-pc repo=nyph/CursorAiOrg 更新 BOARD` |
| 别名 | `machine=` 等同 `worker=` |

`worker=` 必须与 `--name` 一致，且任务目标 repo = worker 注册 repo。

---

## 与组织岗位的关系

| 岗位 | Cloud + My Machines |
|------|---------------------|
| 主控 | 可在云端派工；落盘仍写 `projects/*/records/`（本机路径） |
| 主程 / 执行 / 审核 | 子代理可在云端；改 GAME_ROOT 须 worker=`scl-pc` |
| Gitea | push 用本机凭据；远程权威见 `rules/06`（组织仓已云：`git.bddream.site`） |
| 网络员工 | worker 依赖本机代理；先 `ensure-v2ray` 再启 worker |

主控桌面会话（你当前这种）仍是 **Local Agent**，与 Cloud 并行不冲突。

---

## 限制（写死）

1. **Git 宿主：** 官方 Cloud 优先 GitHub/GitLab/Azure/Bitbucket；**Gitea（bddream）** 可能无法作为纯 Cloud VM 的一等源。组织仓已在 `https://git.bddream.site/nyph/CursorAiOrg` → **推荐 My Machines 落本地再 push Gitea**，不要假设纯云 VM 能直接 clone Gitea。  
2. Move to Cloud **不带**未提交本地改动。  
3. 多仓 = 多 worker，或纯云 Multi-repo Environment（仅支持官方托管时）。  
4. HTTP MCP 走 Cursor 后端；内网 MCP 用 **stdio**（跑在本机 worker）。  

---

## 文档

- https://cursor.com/docs/cloud-agent/my-machines.md  
- https://cursor.com/docs/cloud-agent.md  
- https://cursor.com/docs/cli/installation.md  
- https://cursor.com/agents  

脚本：`scripts/start-org-worker.ps1` · `scripts/ensure-v2ray.ps1`
