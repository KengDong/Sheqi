---
status: active-authority
version: 1.0
created_at: 2026-09-23
decision: D-0080
---

# REPOSITORY OPERATING MODEL V1
## Sheqi / Hit-Fiction R&D Git重构规则

# 0. Goal

Git不是“所有想法都同权”的知识仓库。

它必须同时做到：
1. 当前authority一眼可见；
2. 历史失败不丢；
3. 实验彼此隔离；
4. 只有被真实证据验证的资产才升级；
5. Writer不会被几十份诊断文档淹没。

# 1. Entry Point

任何新执行窗口第一步只读：

> `meta/CURRENT_AUTHORITY.md`

除非CURRENT_AUTHORITY明确要求，
不要从：
- old STATE；
- history；
-旧DECISIONS；
-旧Canon；
-旧Outline；
自行推断项目方向。

# 2. Directory Roles

## meta/
只放：
- 当前最高原则；
- authority导航；
- 决策；
- 流程标准；
- promotion rules；
- active workstreams。

不能放：
- 大量候选创意正文；
- 实验草稿；
- writer自由尝试。

## research/
只放：
- 外部证据；
- benchmark机制研究；
-正式设计研究；
- active briefs。

Research不能自动成为Authority。

## experiments/
默认所有新想法先在这里。

新主目录：
> `experiments/first_principles_forge/`

推荐：
- `A_native/`
- `B_function_clones/`
- `C_wild/`
- `reservoirs/`
- `prototypes/`
- `anonymous_reader_packages/`

实验资产默认：
> **non-authority**

直到Promotion Gate通过。

## reviews/
放：
- Total Editor verdict；
- Reader evidence；
- Postmortem；
- Promotion / Kill decision。

Review可以影响authority，
但只有DECISIONS明确升级才生效。

## handoffs/
只负责：
> 某个执行角色“现在干什么”。

CURRENT不承担长期知识库职责。

每个CURRENT应尽量短：
- role；
- status；
- authority入口；
- current task；
- outputs；
- hard stop；
- handoff_to。

## history/
只做不可变审计快照。

历史PASS：
> 只代表当时证据下的结论。

不得因为文件名里有PASS，
自动继承为当前authority。

# 3. Authority Promotion Ladder

所有新书 / 新版本统一：

### E0｜Idea
一句话Concept。
位置：
> experiments

### E1｜Desire-Pass Concept
通过Total Editor Desire Cut。
仍是experiment。

### E2｜Reservoir-Pass
30—50个真想看的Situation能持续生成。
仍不建Canon。

### E3｜Character-Collision Pass
人物自己能制造故事。

### E4｜Minimal Horizon Pass
Near / Mid / Far成立。

### E5｜P1/P3 Prose Pass
正文开始证明。

### E6｜P7 Voluntary Reader Pass
第一关键行为Gate。

### E7｜P10 Voluntary Reader Pass
才允许申请：
> **Book Candidate Promotion**

### E8｜Promoted Book Candidate
此时才允许建立：
- book bible；
- longform branch；
- authority outline；
- formal continuity ledger。

### E9｜Primary
需要：
- sustained prose evidence；
- reader evidence；
- Total Editor；
- author approval。

# 4. Branch Policy

## Before E7
不为每个Concept开Git branch。

原因：
> branch会制造假authority和同步成本。

统一main下实验目录隔离。

## After E7
若候选需要长期独立发展，
才允许建立正式branch，例如：
- `book/candidate-x`
- `book/c01-reborn`
- `book/c12-reborn`

branch目的：
> 长篇资产隔离。

不是创意头脑风暴。

# 5. Version Naming

实验不再使用：
> final / final2 / final_final。

统一：
- concept_v1
- reservoir_v1
- p1_v1
- p3_v1
- p7_v1

每次新版本必须注明：
- previous evidence；
- one hypothesis changed；
- what must improve；
- kill condition。

禁止一版同时改十个维度，
否则无法知道为什么变好/变坏。

# 6. Writer Boundary

Writer不得自动读取整个repo。

Writer输入由当前brief显式列出。

默认最多：
- 1页Book Desire Thesis；
- core rules；
- character desires；
- irreversible ledger；
- relevant reservoir；
- current horizon；
- voice guide。

禁止把：
- benchmark report；
- all reviews；
- all checklists；
- Total Editor答案；
直接塞给Writer。

# 7. Reader Boundary

Fresh Reader必须硬隔离：
- 不读Concept说明；
- 不读Benchmark；
- 不读Writer selfcheck；
- 不读Total Editor；
- 不知道版本来源；
- 不知道计划让其读到哪里。

匿名包只有：
> 小说文本。

Reader停止后才访谈。

# 8. Diagnostics Library

以下全部归为：
> **Diagnostic Library**

- `meta/HEAD_TIER_READER_DESIRE_STANDARD.md`
- `meta/BENCHMARK_CAUSALITY_STANDARD.md`
- Longform Canopy
- Long Horizon
- Five Curves
- Scene Ecology
- Macro Promise
- Semantic Rolling-3

用途：
> Reader证据出现问题后诊断。

不是：
> Writer开工前全部逐项满足。

# 9. Legacy Preservation

D-0001—D-0079：
> 全部保留。

旧C01/C12正文：
> 全部保留。

旧PASS：
> 全部保留。

原因：
> 失败历史本身是高价值训练数据。

但新窗口若未被CURRENT_AUTHORITY指向，
不得把旧PASS当当前命令。

# 10. One Rule

> **main保存“我们现在相信什么”和“我们试过什么”；只有真实阅读证据能把实验升级成权威。**
