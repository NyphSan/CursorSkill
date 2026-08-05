# 配置表分析与校验框架

> 来源：game-config-analyzer skill
> 用途：自动筛查游戏配置表，分类战斗公式表与产出消耗表，并做产出消耗模拟

## 配置表分类规则

### 战斗公式表特征词
表名/Sheet名含以下关键词 → 识别为战斗公式表

| 关键词 | 典型表名 |
|---|---|
| 武器/Weapon | WeaponDamage / 武器表 |
| 技能/Skill | Skill / 技能表 |
| 敌人/Enemy/Mob | EnemyStats / 敌人属性 |
| 角色/Character/Hero | CharacterGrowth / 角色成长 |
| 暴击/Crit | CritFormula / 暴击表 |
| 防御/Defense/Armor | Defense / 防御公式 |
| 伤害/Damage | DamageFormula |
| 攻击/Attack | AttackTable |
| 血量/HP/HitPoint | HPTable |
| 关卡/Stage/Wave | StageConfig / 关卡表 |

### 产出消耗表特征词
表名/Sheet名含以下关键词 → 识别为产出消耗表

| 关键词 | 典型表名 |
|---|---|
| 掉落/Drop/Loot | DropTable / 掉落表 |
| 金币/Gold/Coin | GoldIncome / 金币表 |
| 经验/Exp/XP | ExpTable / 经验表 |
| 商店/Shop/Store | Shop / 商店表 |
| 升级/Upgrade/Level | UpgradeCost / 升级消耗 |
| 强化/Enhance/Strength | Enhance / 强化表 |
| 抽卡/Gacha/Recruit | Gacha / 抽卡表 |
| 任务/Quest/Task/Daily | QuestReward / 任务表 |
| 体力/Stamina/Energy | Stamina / 体力表 |
| 货币/Currency | CurrencyFlow |

## 产出消耗模拟逻辑

### 核心指标
```
净资源速率 = 单位时间产出 - 单位时间消耗
累计资源 = ∫(净资源速率)dt
```

### 模拟维度
1. **前期（1-10级）**：新手期资源是否充足，能否平滑过渡
2. **中期（11-30级）**：核心玩法循环，产出消耗是否平衡
3. **后期（31级+）**：终局内容，是否存在通货膨胀

### 问题诊断规则

| 问题 | 诊断条件 | 严重程度 |
|---|---|---|
| 资源枯竭 | 净资源速率<0持续超过5分钟游戏时间 | 🔴 严重 |
| 通货膨胀 | 累计资源>消耗需求×3 | 🟡 中等 |
| 卡点过强 | 升级消耗/单位时间产出>30分钟 | 🟠 较高 |
| 产出单一 | 某资源100%来自单一渠道 | 🟡 中等 |

## 割草/幸存者类特有检查

- **割草效率**：DPS vs 敌人密度，是否割得动
- **生存能力**：HP vs 敌人DPS，是否站得住
- **成长曲线**：每10级战力增幅是否在50%~80%区间
- **付费深度**：免费玩家能否通关主线
