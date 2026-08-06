# Org Retro · SCL F0–F5 框架迁移批

- **Date：** 2026-08-06  
- **Outcome：** success（F0–F5 全 PASS；PM 结束本批）

## What happened

SCL 框架改造批 F0→F5 经子代理流水线闭环：SCLCore 壳 → 首批 Core 叶 → ATBS→SCLTactical → 业务 README 收口 → 组织 profile 花名册。游戏仓 `72afca0e`；组织仓 F5 `c053309`。

## What worked

- ARCH 每刀锁范围；F3 保留 UATBS* 过渡降爆破面  
- PM 自审闸门连续开下一项（F3→F4→F5）不等老板  
- 子代理可见派工 + records 链（ARCH/EXEC/REVIEW/DONE/PM/gitea）可续温  
- F4 薄收口验证「无双份 Core」即可 PASS，不强行搬清单 B  

## What hurt

1. 大插件迁移 push 需 `http.postBuffer`（F3 Content 重命名）— 应在 gitea skill 预写 env 指引，勿改全局 git config  
2. 子代理完成通知与主控状态偶发滞后，需以落盘 records 为准  
3. `COMMIT-F5-ORG.md` 记录文件未纳入组织 commit（债）  
4. F5 无独立 ARCH，靠 ARCH-F0 DoD — 可接受但 EXEC 须自证更细  

## Org patches（候选 · 未本批实施）

- [ ] `gitea-repo` skill：大仓 push 用 `GIT_HTTP_POST_BUFFER` 环境变量说明  
- [ ] `templates/GIT_COMMIT.md`：区分项目仓 vs 组织仓 commit 记录路径  
- [ ] PM 模板：批末显式引用 `BATCH_CLOSEOUT.md`  

## Won't change

- F4c 清单 B 须独立 ARCH-F4c，不抢 F0–F5 批末  
- Presenter→ViewState / 3C 留业务  

## 排队（下一批）

F4c · D3 可达圆 · UATBS* 更名 · 脏文件单独提交
