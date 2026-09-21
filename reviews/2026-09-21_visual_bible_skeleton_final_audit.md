---
status: final-audit-complete-pending-author
document_type: visual-bible-skeleton-final-audit
project: 修仙先舍一件人间事
created_at: 2026-09-21
source: reviews/2026-09-21_visual_bible_skeleton_proposal_for_audit.md
authority: review-only
canon_effect: none
outline_effect: none
visual_effect: none-until-approved
recommendation: approve-with-2-structure-revisions
---

# Visual Bible Skeleton Proposal｜总编终审

## 0. 总裁决

**通过。**

这版已经真正解决了最核心的问题：

> 未来AI插图不再“每次重新抽一个世界”，而是基于批准reference继续生成 / 编辑。

尤其正确的有：

- 文字权威高于视觉；
- Approved / Candidate / V0 分层；
- hard-gate优先于美术软评分；
- 不依赖seed；
- reference bundle；
- 先空间后人物脸；
- 固定中转台 NORMAL / A' 双状态；
- 合租屋按时间状态维护；
- V0 不构成事实；
- 图不能反向Retcon章卡；
- 余世 / 弃相 / 漏舍不提前视觉定稿。

正式落地前只需要2项结构修订。

---

# 1. 每个视觉字段必须带“来源 + 作用域”

Proposal 已经用：

- [TEXT-LOCKED]
- [VISUAL-FIELD]
- [OPEN]

区分状态，这是对的。

但正式 Visual Bible 还需要再加两个字段：

> **source_ref**
>
> **scope**

原因：

同样一个 [TEXT-LOCKED] 可能只锁：

> 第2—3章这个固定中转台事故场景。

却不代表：

> 全国所有中转台都如此。

例如：
- 凹入式舍台服务位；
- O外环位置；
- 南侧安全线；
- 西北救援通道；

都是当前批准章卡里的具体场景事实。

它们不应在未来被视觉系统误读成：
> 通用舍台建筑规范。

## 正式字段建议

每条视觉事实至少记录：

- state: TEXT-LOCKED / VISUAL-FIELD / OPEN
- source_ref: 来源文件
- scope:
  - scene-only
  - location-local
  - volume-local
  - character-global
  - world-global
- version

这会显著降低视觉资产“偷偷升级成Canon”的风险。

---

# 2. Skeleton 本身也应该模块化，不要变成一个1700行总文件

这份 Proposal 作为设计稿没有问题。

但正式落地如果所有内容都放进一个 Visual Bible 文件，未来每次画图都读1700行，同样会产生提示负担和误用。

## 建议正式目录至少拆成

### 核心
- `visual/bible/README.md`
  - 权威层级
  - 资产状态
  - 总原则

### QA
- `visual/bible/QA_HARD_GATES.md`

### Registry
- `visual/bible/REFERENCE_REGISTRY.md`

### 场景
- `visual/bible/SCENE_MATRIX.md`

### 角色
- `visual/bible/CHARACTER_MATRIX.md`

### 时间状态
- `visual/bible/TIMELINE_VISUAL_STATE.md`

### 任务模板
- `visual/bible/VISUAL_TASK_TEMPLATE.md`

Proposal里的长解释可以保留在 review / research，不需要每次生产都加载。

---

# 3. 固定中转台字段｜PASS

我专门对照了已冻结前三章章卡。

以下被标记为 TEXT-LOCKED 的关键几何：

- F 正常沿东西方向进入固定导向位；
- 南侧安全线 / 撤离区；
- 西北专业救援通道；
- 凹入式舍台服务位；
- O外环、S核心；
- R位于F右端独立加固格；
- B为既有辅助制动 / 牵引结构；
- W为左侧合法工作位；

都能在已批准 `outline/chapter_cards/volume1_ch001_003.md` 找到来源。

没有发现视觉层自行编造几何。

通过。

---

# 4. Hard Gates｜PASS

建议正式采用。

特别支持：

> 一致性不是“总分90就过”，而是关键身份 / 时间 / 空间 / 剧透有任一硬错误就退回。

这比总分制可靠。

---

# 5. 人物V0顺序｜PASS

继续保持：

> 先固定中转台
> -> 驿货行材质 / 器物
> -> 合租屋
> -> 全局风格板
> -> 再做陆野6—10个差异化V0方向。

现在不要锁最终脸。

---

# 6. 插图密度｜PASS

继续冻结：

> **正文可以0张；内部图可以很多；宣传图重点投入。**

不机械按章数配图。

---

# 7. 作者拍板项

建议批准：

1. Skeleton总体结构；
2. 增加 source_ref + scope；
3. 正式落地时模块化目录；
4. hard-gate QA；
5. reference / version制度；
6. 第一阶段先空间、后人物脸。

通过后可以正式创建 `visual/bible/` 结构。

但仍然：

> **不需要现在生成正式公开插图。**
