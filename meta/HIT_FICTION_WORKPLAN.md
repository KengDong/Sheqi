---
status: active
version: 1.2
created_at: 2026-09-22
authority: process
canon_effect: none
outline_effect: none
authorized_by: meta/DECISIONS.md D-0053
---

# HIT FICTION WORKPLAN｜作品级头部候选重选执行计划

## 0. 最高目标

> **不是把《舍弃》做好。**
>
> **是做出一部能与当前头部热门网文正面对读、一样好看、一样上瘾、一样有新鲜感、让人一读不可收拾的小说。**

《舍弃》仅作为现有强候选参与竞争。

---

# Phase A｜两条独立并行研究线

## A1｜Reader Obsession Market Scan

### 窗口
> **复用现有 Market Scout 窗口**

### 身份
> market_scout / Reader Desire Analyst

### 任务
> 研究读者真正沉迷的生活、欲望、竞争、关系和幻想。

不是研究：
- 世界接口数量；
- 设定复杂度；
- Sheqi如何适配。

### 输出
`research/reports/2026-09-22_reader_obsession_market_scan.md`

### 完成后
- CURRENT -> PAUSED / DONE
- history
- 交 editor_in_chief

---

## A2｜Independent Hit Concept Foundry

### 窗口
> **新开独立GPT窗口**

### 身份
> hit_concept_scout / Independent Book Concept Architect

### 隔离要求
第一轮不得读取：
- Sheqi Canon；
- Approved Outline；
- 当前Ch1；
- C1R / C2 / C8R；
- Reader Obsession最新报告。

只允许读取：
- Commercial First Principles；
- 《没钱修什么仙》Deep Read。

### 任务
至少提出：
> **12个整本小说级Concept**

其中必须有：
- >=4个完全不含舍弃；
- >=3个只保留“不可逆代价/人格损失”精神；
- >=3个可复用部分Sheqi资产；
- 其余自由。

内部淘汰：
> **Top 5 Book Concepts**

### 输出
`research/design/2026-09-22_hit_concept_foundry.md`

### 完成后
- CURRENT -> PAUSED / DONE
- history
- 交 editor_in_chief

---

# Phase B｜Book-Level Total Editor Synthesis

### 窗口
> **当前总评审窗口执行，不新开**

### 前置
A1 + A2均DONE。

### Stage B1｜热门头部Benchmark Gate
先把：
- Hit Concept Foundry Top 5；
- Reader Obsession报告产生的新增挑战者（若有）；
- Sheqi-family C1R / C2 / C8R / Traditional Control；

**分别独立对标真实热门头部作品。**

热门作品才是标尺，《舍弃》不是标尺。

直接问：
> **这个候选如果今天和《没钱修什么仙》及其他成熟热门作品一起摆在读者面前，够不够吸引、够不够想追？**

明显掉档：
> **直接淘汰，不进入Prototype。**

### Stage B2｜Prototype Candidate Selection
只从通过Popular Benchmark Gate的候选中选择Top 4。

### 任务
不是打理论总分，也不是先比较“谁比Sheqi强”。

必须重点看：
- 我是否本能想点；
- 我想不想活在/围观这种人生；
- 第一页会发生什么；
- 第一章兑现什么；
- 前10章有没有连续欲望升级；
- 章节菜单本身是否想点；
- 主角是否容易燃烧；
- 钱/身份/关系/秘密是否自然；
- 是否有“热门书未来感”；
- 100万字后是否仍然有新的欲望层级。

### 最终
先形成：
> **Popular Benchmark Pass List**

然后只留：
> **Top 4 Prototype Candidates**

Sheqi-family可以0个入选，不设保底名额。

### 输出
总评审Synthesis + 新Prototype brief。

---

# Phase B｜状态更新
- Reader Obsession：DONE
- Hit Concept Foundry：DONE
- Popular Fiction Benchmark Gate：DONE
- Total Editor Prototype Pool：APPROVED
  - A/C10《死人也要履约》
  - B/C01《明天已经卖掉》
  - C/C08《职业遗产》
  - D/C12《替有钱人渡劫》
- C03：HOLD
- C02：FAIL
- Sheqi-family：本轮不占Prototype席

# Phase C｜统一Writer真实冷开场对撞

### 窗口
> **复用现有 开头 / 主作者 GPT**

### 原因
四个候选必须由同一Writer写，避免作者水平差异污染实验。

### 控制要求
- 相近篇幅；
- 同等认真程度；
- 不告诉Writer“哪个是总评审偏爱”；
- 不故意给旧Sheqi保留优势；
- 每篇必须从第一屏进入真正事件；
- 不允许世界说明书。

### 输出
4个匿名Prototype。

Writer：
> **不得排名。**

---

# Phase D｜真正Clean-room Reader Test

### 窗口
> **新开一个完全干净的GPT窗口**

不能复用：
- 旧结构盲读；
- 旧blind_reader；
- market_scout；
- world_reframe；
- 总评审；
- opening_writer。

### 第一轮只给
- 4篇匿名Prototype；
- 极短盲读任务。

不能给：
- 概念设计文档；
- 成本；
- 哪篇是Sheqi；
- 哪篇作者投入最多；
- 哪篇总评审看好。

### 只回答
1. 哪篇第一屏最想继续；
2. 哪篇最有“这书有意思”的感觉；
3. 哪篇主角最想跟；
4. 哪篇世界最自然，不像设计稿；
5. 哪篇读完最想立刻点下一章；
6. 哪篇最像真正能追很久的热门书；
7. 哪篇即使不知道设定说明，也已经好看。

---

# Phase E｜Authority Decision

总评审合流：
- Popular Benchmark Gate；
- Prototype实际读感；
- clean-room结果；
- D-0051 / D-0052 / D-0053 / D-0054。

然后才向作者提交：
> **1—2个真正胜出的整书方向。**

如果胜出者不是Sheqi：
> 提交 Full Reboot Proposal。

如果Sheqi-family胜出：
> 提交 P2 / P1 重构Proposal。

作者只做：
> 最终方向选择。

不做基础QA。

---

# 当前窗口状态

## 现在立即工作
1. Opening Writer / world_prototype｜ACTIVE：四篇匿名冷开场

## 现在暂停
- market_scout
- hit_concept_scout
- benchmark_deepread
- world_reframe
- mid_continuity
- visual
- old blind_reader

## 下一步新开
- **Fresh Book Prototype Blind Reader**
- 必须等四篇Prototype DONE后再新开。
- 必须是从未参与本项目的新窗口。

现在不要新开：
- Prose Editor
- Visual Reframe

---

# 当前用户需要操作

现在只需要：
1. 回到现有“开头 / 主作者”窗口；
2. 发送“继续 Sheqi，按 Git CURRENT 执行”。

四篇Prototype完成后回总评审。
届时再新开真正clean-room blind reader。
