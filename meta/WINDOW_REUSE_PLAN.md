---
status: active
version: 1.1
created_at: 2026-09-22
authority: process
canon_effect: none
outline_effect: none
---

# WINDOW REUSE PLAN｜World Background Reframe阶段窗口复用方案

## 原则
优先复用已存在聊天窗口；只有clean-room独立性或外部研究独立性真正需要时才新开。

## 1. 旧“结构盲读 / Reader-Language”窗口
- reuse_as: `benchmark_deepread`
- status: ACTIVE
- brief: `research/briefs/2026-09-22_no_money_cultivation_deepread_brief.md`
- source: Library `/Sheqi/Research Sources/Benchmark Full Texts/没钱修什么仙_用户研究版.txt`
- reason:
  - 已读过项目设计，永久失去正式blind资格；
  - 但非常适合做结构、信息密度、Reader-Language、正文自然度拆解；
  - 因此转职研究，不浪费。
- forbidden:
  - 不得承担最终clean-room blind read。

## 2. 中段+衔接窗口
- reuse_as: `world_reframe`
- status: QUEUED
- brief: `research/briefs/2026-09-22_sheqi_world_reframe_brief.md`
- starts_after:
  - benchmark_deepread report
  - market_scout report
- reason:
  - 最熟当前Canon / Story Engine / 第一卷结构；
  - 适合判断新世界底盘改动级别、可复用资产与长期发动机。
- forbidden:
  - 不参与第一轮外部市场扫描，避免沉没成本偏见污染样本池。

## 3. 开头 / 主作者窗口
- reuse_as: `world_prototype`
- status: QUEUED
- brief: `research/briefs/2026-09-22_world_background_prototype_duel_brief.md`
- starts_after: world_reframe Top3
- reason:
  - 已通过Event-First prose calibration；
  - 由同一Writer写Top3 + Traditional Control，可减少“不同作者水平”造成的比较噪声。
- safeguards:
  - 四个原型同篇幅/同核心人物/同写作约束；
  - Writer不得排名；
  - Traditional Control不得故意写差。

## 4. 视觉窗口
- reuse_as: visual-world-texture stress tester
- status: PAUSED UNTIL TOP3
- future_task:
  - 对Top3候选分别回答第一屏可视物、普通生活空间、衣食住行、职业设施、舍弃痕迹如何肉眼可见；
  - 只做“世界是否能被看见”的压力测试，不先做漂亮设定图。
- reason:
  - 新背景是否真正新鲜，必须能在街道/房间/工作台/学校/医院/广告等普通空间中被看见。

## 5. 新窗口A｜Market Scout
- must_be_new: YES
- status: ACTIVE
- brief: `research/briefs/2026-09-22_crossgenre_background_market_scan_brief.md`
- reason:
  - 需要尽可能少受Sheqi旧设计污染；
  - 负责外部2024—2026跨题材热门样本扫描。

## 6. 新窗口B｜Clean-room Blind Reader
- must_be_new: YES, BUT LATER
- status: NOT YET OPEN
- starts_after: Top3 + Traditional Control prototypes complete
- reason:
  - 旧结构盲读窗口已污染；
  - 最终必须有真正没看过设计理由的陌生读者。
- first_pass_reads_only:
  - 4个匿名prototype文本；
  - blind brief。

## 总窗口成本
- 现在新增：**1个**（Market Scout）。
- 后续新增：**1个**（Clean-room Blind Reader）。
- 其余任务全部复用现有窗口。


---

# 7. 原“开头 / 主作者”窗口｜RETIRED

- status: **RETIRED / CONTEXT LIMIT REACHED**
- completed:
  - Book-Level Prototype Duel
  - Finalist B/D Ch2—Ch3 Stress Test
- user_note:
  > 原窗口已到对话上限。
- hard_rule:
  > **以后不再复用该窗口。**

# 8. 新窗口C｜Book Writer V2

- must_be_new: **YES**
- status: QUEUED
- current: `handoffs/book_writer_v2/CURRENT.md`
- starts_after:
  - Returning Reader Continuation Test
  - Fresh 3-Chapter Shelf Test
  - Total Editor synthesis
- purpose:
  > 承担后续所有正文 / Book Bible / 续章写作任务。
- handoff_rule:
  > 只按Git CURRENT与正式brief接棒，不依赖旧Writer聊天记忆。


---

# D-0080｜FIRST-PRINCIPLES STORY FORGE WINDOW PLAN

旧窗口复用计划自本节起降级为历史参考；当前执行以D-0080为准。

## 总编窗口
- role: editor_in_chief
- status: ACTIVE / JUDGE ONLY
- current: `handoffs/editor_in_chief/CURRENT.md`
- hard:
  > 不在本窗口代写Lane A/B/C创意，避免“出题者=选手=裁判”。

## 新窗口D｜Lane A Native Rebuild
- must_be_new: YES
- clean_room_level: targeted isolation
- current: `handoffs/story_forge_native/CURRENT.md`
- purpose:
  > 只从C01/C12最小种子重新长出6个发动机版本。
- forbidden:
  > 旧正文 / 旧Early20 / 其它Lane。

## 新窗口E｜Lane B Function Clone
- must_be_new: YES
- clean_room_level: causal-function isolation
- current: `handoffs/story_forge_function_clone/CURRENT.md`
- purpose:
  > 只拿抽象Reader函数，产出≥15个原创Concept。
- forbidden:
  > C01/C12 / 具体热门正文 / 其它Lane。

## 新窗口F｜Lane C Wild Concept
- must_be_new: YES
- clean_room_level: HARD
- current: `handoffs/story_forge_wild/CURRENT.md`
- purpose:
  > 完全无项目背景产出≥10个Wild Concepts。
- forbidden:
  > 除CURRENT指向边界文件外的整个Sheqi项目。

## Execution Order
三Lane可并行。
完成后均停止，不互读。

总编只有在三份输出全部DONE后才执行：
> **Phase-1 Desire Cut｜PULL / MAYBE / DROP**

不允许在某Lane先完成后就提前“优化”它，避免先发优势。
