# 网络维护手册（交给 network-ops）

- **岗位：** 网络员工 / network-ops（归属主控）  
- **参考原文：** 老板桌面 `配置通用网络环境指令.docx` → 仓内副本 `docs/ops/REF-通用网络环境指令.md`  
- **目标：** 长期维护 **AI Agent 通用网络环境**，使主控 Task / Cloud worker / CLI 工具可稳定运行  
- **版本对齐：** CursorTeam ≥1.1.8  

---

## 1. 你是谁、做什么

| 做 | 不做 |
|----|------|
| 代理保活、通路验收、任务前门禁、掉线排障、落盘报告 | 改游戏业务 / ARCH / 擅自改订阅密钥 |
| 用户级代理变量、WinIE、（有管理员时）WinHTTP | 关防火墙 / 关 SSL / winsock reset / 改系统路由（无老板授权） |
| 升级主控：节点必须老板 GUI 换 | 假装「api2 通 = Task 可派」 |

**成功定义：** `task-env-preflight.ps1` → **绿**（agentn OK）。软绿仅临时，须继续追到绿。

---

## 2. 架构定版（本机实测）

```text
v2rayN + xray
  HTTP  127.0.0.1:10809   ← 系统代理 / 环境变量 / git / Cursor / WinHTTP
  SOCKS 127.0.0.1:10808   ← ALL_PROXY=socks5://…
路由：优先 Global
无稳定 AI 系统 TUN 时：不要假装 TUN 优先；用 HTTP/SOCKS 第二优先（见参考文档第五阶段）
```

| 端点 | 含义 |
|------|------|
| `api2.cursor.sh` | 控制面；通 ≠ Task 稳 |
| `agentn.global.api5.cursor.sh` | **Task/Agent 硬门禁**；HTTP/0.9 = 换节点 |
| `api.openai.com` | 401/403 算网络可达 |

---

## 3. 日常维护（唯一入口）

```powershell
# 巡检 + 自动修复用户级配置 + 验收（推荐）
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\network-ops-maintain.ps1

# 仅优化栈
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\optimize-cursor-network.ps1

# 仅任务前门禁
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\task-env-preflight.ps1

# 老板确认 UI GPT 可用时的临时软绿（须继续追绿）
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\task-env-preflight.ps1 -BossConfirmGpt
```

### 节奏

| 时机 | 动作 |
|------|------|
| 每日开工 / 主控派 Task 前 | `network-ops-maintain.ps1` 或至少 `task-env-preflight.ps1` |
| 掉线 / TLS aborted / GPT 不可用 | maintain → 若 agentn 红：升级老板换节点 → 再 maintain |
| Cursor / agent CLI 升级后 | 检查 worker；`better-sqlite3` ABI 错则 rebuild 或重装 CLI |
| 管理员主控会话可用时 | 同步 WinHTTP → `127.0.0.1:10809` |

---

## 4. 执行原则（摘自参考文档，写死）

1. **检测 → 分析 → 备份 → 修改 → 测试 → 保留或回滚**  
2. 不假设固定端口；以本机监听与连通为准（当前实测 10808/10809）  
3. 已满足要求则不继续改  
4. 一次只改一个层级  
5. **禁止**（无明确授权）：关 SSL 校验、关防火墙、装未知证书、改系统路由、删代理/VPN、network/winsock reset  

### 方案优先级

1. 稳定 TUN（本机若无 AI TUN → 跳过）  
2. **稳定 HTTP/SOCKS（当前定版）**  
3. 补环境变量覆盖 CLI  
4. 单工具补丁（git/npm/pip）  

---

## 5. 门禁与主控协作

| 预检 | 主控 |
|------|------|
| 绿 | 可派后台 Task |
| 软绿（BossConfirmGpt） | 可派但监控 TLS；网络岗继续追绿 |
| 黄（agentn 红） | 禁 Task；网络岗排障 |
| 红（代理挂） | 先 ensure-v2ray / optimize |

落盘：`docs/network/PREFLIGHT-*.md` · `NETOPT-*.md` · `NETCHECK-*.md` · `MAINTAIN-*.md`

---

## 6. 老板必须动手的唯一项

**换 v2rayN 节点**，直到：

```text
curl --proxy http://127.0.0.1:10809 https://agentn.global.api5.cursor.sh/
```

不再出现 HTTP/0.9，且 netcheck **agentn OK**。

网络岗不能代选节点密钥；只能提示「当前节点不通 agentn」。

---

## 7. Worker（My Machines）附带职责

- 组织仓 worker：`scripts/start-org-worker.ps1` → name `cursorteam-pc`  
- 若报 `better-sqlite3` NODE_MODULE_VERSION 不匹配：在对应 `cursor-agent\versions\…\node_modules\better-sqlite3` 下对 **bundled node** rebuild，或干净重装 agent CLI（先退出占用进程）  
- worker 须常驻；掉线先 maintain 网络再启 worker  

---

## 8. 回滚速查

| 层 | 回滚 |
|----|------|
| WinHTTP | `netsh winhttp reset proxy` |
| 用户环境变量 | 见 `docs/network/backup-*/env-user-before.json` |
| git proxy | `git config --global --unset http.proxy`（及 https） |
| 系统代理 | 设置 → 代理 → 关，或恢复 backup 中 ie-proxy.json |

---

## 9. 验收清单（维护完成须能勾）

- [ ] v2rayN + xray 在跑；10809/10808 监听  
- [ ] WinIE / User env / git → HTTP 10809；ALL_PROXY=socks5://10808  
- [ ] WinHTTP 已同步（需管理员时由主控提权会话执行）  
- [ ] api2 OK；**agentn OK（硬目标）**  
- [ ] GitHub / npm registry HTTPS PASS  
- [ ] 最新 `MAINTAIN-*.md` 或 PREFLIGHT 绿  
- [ ] （可选）`cursorteam-pc` worker Running  

最终对外口径：`AGENT_NETWORK_CONFIGURATION_COMPLETE` 后仍由本岗 **持续维护**，不是一次性工程。
