# Cursor 网络稳定化（优化后）

- **Date：** 2026-08-07  
- **脚本：** `scripts/optimize-cursor-network.ps1`

## 已自动锁定的稳定栈

| 项 | 值 |
|----|-----|
| v2rayN / xray | 保活 |
| 路由 | **Global** |
| 入站 | SOCKS `10808` + **HTTP `10809`** |
| 系统代理 | `127.0.0.1:10809`（HTTP，勿指 SOCKS） |
| 用户环境变量 | `HTTP_PROXY` / `HTTPS_PROXY` → `http://127.0.0.1:10809` |
| Cursor settings | `http.proxy` + `disableHttp2=true` |

一键：

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\optimize-cursor-network.ps1
```

验收：

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\cursor-gpt-netcheck.ps1
```

## 稳定门禁

| 检查 | 必须 |
|------|------|
| `api2.cursor.sh` | OK |
| **`agentn.global.api5.cursor.sh`** | **OK**（Task 子代理 / GPT Agent） |
| `api.openai.com` | OK（经代理） |

**当前卡点（脚本无法代换节点）：** `agentn` 仍 **HTTP/0.9** → 当前 **节点质量**不够。  
本地代理栈已优化；**换到能通 agentn 的节点**后，再跑 optimize / netcheck 直到绿。

## 老板必做（才能「稳定使用」）

1. v2rayN **换节点**（延迟低、能开 GPT 的那类）  
2. 保持 **系统代理开** + 路由 **全局**  
3. 跑 `optimize-cursor-network.ps1` 直到 exit 0  
4. **重启 Cursor**  
5. 再开 Task / GPT  

可选：管理员开 **TUN**（托盘确认出现虚拟网卡，不只是配置勾选）。

## 与工作流停顿关系

子代理 TLS aborted ≈ `agentn` 不通或不稳。  
`api2` 通不能代表 Task 稳定。
