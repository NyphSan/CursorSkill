# 记忆不断档（续温自检）

聊天记忆会丢；**以 ORG 落盘为准**。

## 你（老板）怎么做

1. **重要结论只认文件**：看板、ARCH/EXEC/REVIEW/PM、PROJECT.md —— 不说「你记得上次…」当唯一依据。  
2. **固定主控会话或固定开场**：新开 Agent 时第一句带  
   `project=SCL` + `续温`（或 `/cursor-admin` 续温）。  
3. **大决策当场落盘**：改口径/定界/确认下一刀时，要求主控写入对应 `records/`。  
4. **长任务分段确认**：每刀 PASS 后看一眼 `BOARD.md`，再回「确认」。  
5. **不要假设跨聊天记得**：换窗 = 断档，必须续温。

## 主控每轮接单前（强制）

在分解/派工之前读盘，并在看板或回复顶部给出 **续温结果**：

```text
## 续温
- Project：…
- BOARD：…（路径）
- 最新 ARCH / EXEC / REVIEW / PM：（有则路径+一句话；无则「无」）
- 闸门状态：锁定 / 可开 D?
- 断档风险：低 / 中（缺文件或与用户口述冲突）/ 高
```

必读（以当前 Project 为例 SCL）：

| 读 | 路径 |
|----|------|
| 项目 | `projects/SCL/PROJECT.md` |
| 看板 | `projects/SCL/records/main/BOARD.md` |
| 清单 | `projects/SCL/records/main/BACKLOG.md` |
| 各岗最新报告 | `records/lead-eng|exec|review|pm/` 按时间取最新 |

若用户口述与落盘冲突 → **以落盘为准**，或标断档并请用户裁决后写回文件。

## 禁止

- 仅靠「我觉得我们上次说了」开工改 GAME_ROOT  
- 把新结论只留在聊天、不更新 BOARD/报告  
