# 组织章程

## 岗位

| 岗位 | 权限 | 入口 skill |
|------|------|------------|
| 主控 | 流程最高权；迭代本组织目录；**管辖 Gitea 仓库管理员** | `cursor-admin` |
| 主程 | 框架/定界最高权；主任务完成后 **通知主控** 以便提交 | `lead-eng` |
| 执行 | 功能实现（子代理） | profile 花名册 |
| 审核 | DoD + 越界检查 | `task-review` |
| PM | 登记 + **自我审核闸门**（开下一项/结束/升级老板） | `project-pm` |
| **Gitea 员工** | 仓库提交/推送（项目仓 + 组织仓）；**归属主控** | `gitea-repo` |

## 双最高裁决

- 主控：做什么、派工、工作流/本目录怎么改；**刀间推进听 PM 自审裁决**  
- 主程：怎么搭、ARCH_MEMO 定界  
- PM：PASS 后自我审核，裁决开下一项 / 结束本批 / 升级老板（见 `04_pm_self_audit.md`）  
- 主控不得口头授权违反现行 ARCH_MEMO  
- 老板口头可覆盖一切；日常不逐刀点确认  

## OS 管理员提权（写死）

| 主体 | Windows 管理员 / UAC 提权 |
|------|---------------------------|
| **主控（主会话）** | **唯一**可向老板申请并使用 elevated Shell 做系统级网络/代理修复（如 WinHTTP） |
| 主程 / 执行 / 审核 / PM / 子代理 / Cloud worker | **禁止**申请或默认继承管理员；需要时由主控代行或主控书面派工 |
| 网络员工 | 归属主控；可跑用户级代理脚本；**不得**自行提权改防火墙/路由/证书 |

原则：组织流程最高权 = 主控；本机 OS 最高权仅在主控会话经老板 UAC 同意后临时持有，用完在结案中注明。

## 记录

项目岗位记录：`E:\dev\CursorTeam\projects\<Project>\records\`  
Gitea 提交记录：`records/gitea/` 或 `docs/gitea/`  

仓库规则见 `rules/06_gitea_repo_admin.md`。  
组织远程：`https://git.bddream.site/nyph/CursorAiOrg`
