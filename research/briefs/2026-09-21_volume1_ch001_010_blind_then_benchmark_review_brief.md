---
status: ready
document_type: two-pass-blind-benchmark-review-brief
project: 修仙先舍一件人间事
created_at: 2026-09-21
authority: process
canon_effect: none
outline_effect: none
---

# 前10章｜两阶段盲读 + Benchmark校准任务书

## 重要结论

本轮不是“一个GPT读完以后凭感觉判好坏”。

必须分成两个阶段：

> **Phase A：严格盲读，记录真实读者反应。**
>
> **Phase B：Phase A冻结以后，再允许读Benchmark Rubric，做结构校准。**

两个阶段的目的不同。

Phase B 不得回头篡改 Phase A。

---

# Phase A｜严格盲读

## 身份
> 第一次接触《修仙先舍一件人间事》的普通男频读者 / 追读测试员。

## 唯一允许读取

1. `reviews/2026-09-21_volume1_ch001_010_structure_blind_packet.md`
2. `research/briefs/2026-09-21_volume1_ch001_010_structure_blind_read_brief.md`

除此之外一律禁止。

禁止：
- AGENTS
- Canon
- STATE
- DECISIONS
- Outline
- 原始章卡
- research reports
- benchmark rubric
- 作者设计理由
- 其它 review

## 必须先完成并写入

> `reviews/2026-09-21_volume1_ch001_010_structure_blind_read_report.md`

写完以后明确写：

> **PHASE A LOCKED**

Phase A一旦锁定，后面不得修改。

---

# Phase B｜Benchmark校准

只有 Phase A 已经写入并锁定以后，才允许继续。

## 现在新增允许读取

1. Phase A自己的盲读报告
2. `research/reports/2026-09-21_structure_benchmark_rubric.md`

不要读取：
- 作者设计理由；
- Story Engine；
- Canon；
- 原始章卡；
- STATE；
- DECISIONS；
- 其它审稿意见。

## 身份

> **男频结构Benchmark评审员**

你现在不是模拟“普通读者”，而是回答：

> Phase A的真实反应放到高表现男频作品常见的功能机制里，哪些是实质结构风险，哪些只是“摘要还无法判断”？

## 必须遵守

- 只比功能，不比具体桥段；
- 不模仿名作；
- 不评价真实文笔，因为当前没有正文；
- 不给总分；
- 不用“某名作这么写，所以我们也要这么写”；
- 不新增剧情解决方案。

## 输出

> `reviews/2026-09-21_volume1_ch001_010_structure_benchmark_review.md`

必须包含：
1. 12项Benchmark分别：STRONG / OK / WEAK / NOT-EVALUABLE-YET；
2. 对Phase A的三个最大追读风险逐一判断：
   - 真实结构问题；
   - 摘要层问题；
   - 必须等正文验证；
3. 最多3个现在值得修的结构问题；
4. 最多5个必须留到正文再判断的问题；
5. 最多3个最值得保护的结构资产。

---

# Phase C｜不要自己做最终裁决

完成 A / B 后停止。

不要：
- 自己改章卡；
- 自己写PATCH；
- 自己宣布“通过，可以开正文”。

最终裁决交给总编窗口。

原因：

> 盲读者记录体验；
> Benchmark评审校准尺度；
> 总编负责判断是否改结构。

三个角色不要混成一个。
