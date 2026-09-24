---
status: pass-with-explicit-cover-gate
decision: D-0088
role: platform_shelf_forge
final_click_verdict: not-performed
---

# D-0088 Platform Shelf Forge Selfcheck

## Scope
- [x] 只做当前起点直接/邻近书架。
- [x] 只做当前番茄直接/邻近书架。
- [x] 没有重做整个男频市场。
- [x] 同时处理 ST1—ST5。
- [x] ST5 没有因为 D-0087 HUMAN-LAYER GAP 降低 packaging 待遇。
- [x] 未选 Primary。
- [x] 未写章节正文。
- [x] 未修改 Concept。

## External Evidence
- [x] Fanqie 使用当前官方作品页 / keyword 详情页。
- [x] Qidian 使用当前官方域书单页 + 官方荣誉页；已明确用户书单不是官方榜单。
- [x] 未虚构 CTR、推荐位、实时排名、在读。
- [x] 对公开抓取不稳定的封面没有脑补。
- [x] 当前证据截止 2026-09-24 11:20 UTC+8。

## Platform Native Packaging
- [x] 每个自然平台至多给 2 个标题。
- [x] 每个自然平台都有 one-line category promise。
- [x] 每个自然平台都有 tags。
- [x] 每个自然平台简介首屏约 120—180 汉字。
- [x] 每个自然平台都有 First-Screen Promise。
- [x] 每个自然平台都有封面方向文字说明。
- [x] 不把旧书名当不可改。
- [x] ST1 番茄、ST4 起点被允许标记 PLATFORM MISMATCH，没有硬适配。

## Concept-Fidelity Check
- ST1：没有改成“受伤自动升级”；保留真实成本、治愈悖论、旧痕构筑。
- ST2：没有改成灵宠；保留活灵脉=移动修炼地/资产/家园。
- ST3：没有改成远程城市管理游戏；保留公共设施、权限、现场责任。
- ST4：没有改成普通囤货基地车；标题/简介都把“建筑核心→移动城”放在最前。
- ST5：没有改成“万人给我挂机经验”；保留“真实修炼验证→有效优化永久回流”。

## Anonymous Test Integrity
- [x] Qidian strip 将 4 个自然平台候选与 8 个真实当前/直接竞品混排。
- [x] Fanqie strip 将 4 个自然平台候选与 10 个真实当前/直接竞品混排。
- [x] Anonymous strip 不出现 ST 编号、Reservoir、Hit Gap、内部 verdict。
- [x] Reader 被明确允许一个项目候选都不选。
- [x] Source key 与 Reader input 分离。

## Cover Gate
正式 brief 要求 cover visual，但同时禁止虚构当前竞品数据；当前公共抓取不能稳定取得所有实时封面。

因此本 Forge 选择：
- 不造假；
- 先交付等权的 title/tags/first-lines Anonymous Copy Shelf；
- 把真实封面 source 与候选 cover direction 放在 PRIVATE source key；
- 视觉 Pass 只有在真实封面与候选视觉卡都能等尺寸呈现时才允许执行。

Forge output：PASS WITH COVER-AWARE SECOND-PASS GATE。

下一步必须由全新 fresh_shelf_reader clean-room 窗口执行匿名点击；本窗口不得自己做最终点击裁决。
