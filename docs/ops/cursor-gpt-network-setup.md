# Cursor · GPT 可用网络环境（本机诊断结论）

- **Date：** 2026-08-06（更新：掉线复盘）  
- **主机：** Windows · v2rayN + xray · 系统代理 `127.0.0.1:10808`（**SOCKS**）  
- **现象：** 模型可选 GPT，但 Agent 不稳 / 主控突然不可用  

## 掉线复盘（2026-08-06 23:17）

| 现场 | 含义 |
|------|------|
| `ProxyEnable=0` 或 `10808` **无 Listen** | **v2rayN/xray 已退出** |
| 直连 `api2` 偶发仍通 | 部分 Cursor 基础 API 可不经代理 → 误以为「还能用」 |
| 直连 `agentn` / `openai` 失败 | Agent/GPT 必挂 → **主控/Agent 突然没法用** |

**根因（本次）：代理进程没了，不是 Cursor 账号坏了。**  
一键拉起：`scripts/ensure-v2ray.ps1`

## 诊断结论（代理起来之后仍常见）

| 端点 | 经 SOCKS `10808` | 含义 |
|------|------------------|------|
| `api2.cursor.sh` | **200 OK** | 普通 API 通路正常 |
| `api.openai.com` | **401**（无 Key 属正常） | OpenAI 经当前节点可达 |
| `agentn.global.api5.cursor.sh` | **FAIL（HTTP/0.9）** | **当前节点仍不通 Agent 层** → GPT 仍不稳 |

官方：Agent 走 `api5` / `agentn.*.api5.cursor.sh`。  
文档：https://cursor.com/docs/enterprise/network-configuration.md

---

## 日常保证「不突然挂」

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\ensure-v2ray.ps1
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\ensure-v2ray.ps1 -RunNetcheck
```

建议：开机后先跑 `ensure-v2ray.ps1`；托盘确认 v2rayN 未退出；换节点直到 netcheck 里 **agentn=OK**。

---

## 目标环境

```text
v2rayN 常驻 → 节点通 agentn → 优先 TUN → Cursor HTTP/1.1
→ 验收：GPT-5.6 能回，无 Reconnecting 死循环
```

### 换节点验收

```powershell
curl.exe -sS -o NUL -w "http=%{http_code} time=%{time_total}`n" `
  --proxy "socks5h://127.0.0.1:10808" --connect-timeout 12 --max-time 20 `
  "https://agentn.global.api5.cursor.sh/"
```

- **合格：** `200` / `401` / `404`  
- **不合格：** `HTTP/0.9`、`timeout`、`000`

### Cursor

1. Network → **HTTP/1.1**  
2. Models：**关** Override OpenAI Base URL  
3. 已设：`cursor.general.disableHttp2`、`http.proxySupport`  
4. **不要**对 SOCKS `10808` 填 `http://127.0.0.1:10808`

---

## 脚本

| 脚本 | 作用 |
|------|------|
| `scripts/ensure-v2ray.ps1` | 拉起 v2rayN、确认 10808、开系统代理 |
| `scripts/cursor-gpt-netcheck.ps1` | 测 api2 / openai / **agentn** |

## 主控可遥控：路由「全局」

老板确认「开全局就能用 GPT-5.6」。本机 v2rayN 库中有三套路由：

| Remarks | 含义 |
|---------|------|
| V4-绕过大陆(Whitelist) | 默认曾激活；部分 Cursor Agent 流量易直连失败 |
| **V4-全局(Global)** | 兜底全走 `proxy` |
| V4-黑名单(Blacklist) | 黑名单代理 |

```powershell
# 切到全局并重启 v2rayN + 开系统代理
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\v2rayn-set-routing.ps1 -Mode Global -Netcheck

# 切回绕过大陆
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\v2rayn-set-routing.ps1 -Mode Whitelist
```

**能力边界：** 主控可改 DB/`RoutingIndexId` 并重启客户端；**不能**替你点选托盘菜单，也**不能**保证当前节点一定通 `agentn`（节点质量另测）。

## 当前状态

- 路由：**已切到 Global**（2026-08-06）  
- v2rayN/xray 在跑，系统代理开，`api2`/`openai` OK  
- curl 测 **agentn 仍可能 FAIL** → 请在 Cursor 内直接试 GPT-5.6；若仍不行再换节点 / 开 TUN  
