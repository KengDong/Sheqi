---
status: approved-visual-bible-skeleton
version: 1.0
approved_at: 2026-09-21
authority: author-approved-process
canon_effect: none
outline_effect: none
source_proposal: reviews/2026-09-21_visual_bible_skeleton_proposal_for_audit.md
source_audit: reviews/2026-09-21_visual_bible_skeleton_final_audit.md
---

# VISUAL BIBLE｜视觉连续性骨架 V1

## 0. 总原则

> **先有已批准文字事实，再让视觉资产服从它；AI随机图无权反向修改故事。**

文字与视觉权威：

> manuscript > Canon > approved Outline > approved chapter cards > approved visual assets > visual exploration

视觉资产状态：

1. **Approved Reference Asset**
2. **Candidate Asset**
3. **V0 Exploration**

若图与文字冲突：
> **图改。**

若视觉制作暴露文字本身存在真实矛盾：
1. 登记冲突；
2. 引用冲突来源；
3. 停止升级视觉资产；
4. 由作者决定是否走文字层 Proposal。

视觉层不得自行 Retcon。

---

# 1. 每条视觉事实必须带4个字段

- **state**
  - TEXT-LOCKED
  - VISUAL-FIELD
  - OPEN
- **source_ref**
  - 具体来源文件
- **scope**
  - scene-only
  - location-local
  - volume-local
  - character-global
  - world-global
- **version**

这四项用于防止：

> 一个具体事故场景布局，被误升级成全国统一世界规则。

---

# 2. 模块

- `QA_HARD_GATES.md`：正式图硬门
- `REFERENCE_REGISTRY.md`：所有reference登记
- `SCENE_MATRIX.md`：场景 / 空间事实
- `CHARACTER_MATRIX.md`：角色视觉字段
- `TIMELINE_VISUAL_STATE.md`：同一角色 / 场景随剧情变化
- `VISUAL_TASK_TEMPLATE.md`：单次视觉任务模板
- `STYLE_BOARD.md`：全局视觉方向字段

---

# 3. 当前生产顺序

第一阶段：

1. 固定中转台 NORMAL / A' 双状态；
2. 驿货行材质 / 器物 / 工作动线；
3. 合租屋功能平面；
4. 全局风格板；
5. 再进入陆野 V0 人物方向；
6. 再做乔九 / 石小庚人物方向。

当前仍不生成：
- 陆野最终公开母脸；
- 合租旧友正式人脸；
- 曹闻川正式母脸；
- 余世 / 弃相 / 漏舍终极视觉；
- 第一件正式余器定稿；
- 卷末复合余灾最终形态。

---

# 4. 插图策略

> **正文低密度功能图 + 内部高质量空间图 + 宣传图重点投入。**

允许：
- 第一卷正文0张图；
- 内部QA图很多；
- 宣传阶段重点做高质量场景 / 群像。

不做：
- 每章一图；
- 每5—10章机械配图；
- 角色一出场就插立绘；
- 为了“有图”而图解已经能读懂的场景。

正文必须满足：
> 没图也能完全理解。

---

# 5. 角色连续性

未来角色流程：

> 文字视觉卡 -> V0 6—10个差异化方向 -> 作者筛2—3个 -> turnaround -> 表情 / 全身 -> approved master -> reference bundle -> 后续生成 / 编辑 -> QA

禁止依赖：
- seed；
- 角色名；
- 同一prompt；
- 模型跨会话“记忆”。

跨会话必须重新提供：
> approved reference assets。

---

# 6. 当前视觉风格候选

当前主候选：
> **克制的半写实国风插画。**

尚未冻结具体色号与正式商业美术法典。

原则：
- 正常人间环境先成立；
- 修仙设施是生活系统的一部分；
- 穷但不脏；
- 舍务正规、可维护，不像邪教；
- 修仙能力不靠满屏发光；
- 角色差异优先来自轮廓、穿法、工具、动作习惯。

---

# 7. 版本升级

Skeleton V1只冻结：
- 视觉工作流；
- 权威；
- QA；
- reference制度；
- 当前空间字段。

任何具体图要进入 Approved，必须单独审核。

平台公开前：
> 再核对当时AI图 / 版权 / 平台规则。
