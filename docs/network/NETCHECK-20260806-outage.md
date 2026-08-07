# NETCHECK · 掉线排查

- **时间：** 2026-08-06 ~23:17–23:22  
- **岗位：** 网络员工 / 主控代行  

## 现象

处理网络时主控/Agent **突然不可用**。

## 现场

| 项 | 值 |
|----|-----|
| 系统代理 | 曾为关闭 / 10808 无 Listen |
| v2rayN / xray | **未运行**（后已 `Start-Process` 拉起） |
| 直连 api2 | 通 |
| 直连 agentn / openai | 不通 |

## 根因

**v2rayN/xray 进程退出** → 本地 SOCKS 消失 → Agent/GPT 链路断。  
api2 偶发直连仍通，造成「Cursor 还能动一半」的假象。

## 处置

1. 已重新启动 `v2rayN.exe`，xray 监听 `10808`，系统代理开启  
2. 新增 `scripts/ensure-v2ray.ps1` 保活  
3. 复测：api2/openai **OK**；**agentn 仍 HTTP/0.9**（节点问题，须换节点）

## 老板下一步

1. v2rayN **换节点**直到 `cursor-gpt-netcheck.ps1` 中 agentn=OK  
2. 建议开 **TUN**  
3. Cursor Network = HTTP/1.1；重启 Cursor 后再测 GPT-5.6  
