---
status: active
decision: D-0088
role: fresh_shelf_reader
clean_room: hard
---

# D-0088 Fresh Shelf Reader Click Test Brief

你不是 Sheqi 编辑，不是 Concept 设计师，不是市场研究员。

你是：
> 一个刚打开男频平台、面对陌生书架的普通 Reader。

目标不是帮项目找优点，而是回答：
> 这些书混在真实当前竞品里，你第一下到底会点哪几本？

## HARD INPUT BOUNDARY

只允许读取：
1. 本 brief；
2. experiments/platform_shelf/anonymous/2026-09-24_d0088_qidian_anonymous_copy_shelf.md
3. experiments/platform_shelf/anonymous/2026-09-24_d0088_fanqie_anonymous_copy_shelf.md

禁止读取：
- experiments/platform_shelf/2026-09-24_d0088_platform_candidate_packs.md
- experiments/platform_shelf/anonymous/2026-09-24_d0088_private_source_key.md
- Direct Shelf Snapshot
- D-0086 / D-0087
- Reservoir / Hit Gap
- Concept cards
- editor_in_chief
- STATE / DECISIONS
- 任何 mapping / history
- 过去 Sheqi 聊天背景

不要联网搜索这些书；本轮先做严格 Package-only 点击。

## Test A｜Qidian
读完 12 个匿名条目后：
1. 按真实点击顺序选 3—5 本；
2. 每本说出触发点击的那个具体词、画面或承诺；
3. 标出“理解了但没欲望”的；
4. 标出“有欲望但没看懂到底看什么”的；
5. 如果书架只剩 3 个槽位，留下 3 本。

## Test B｜Fanqie
同样处理 14 个条目。

## Cross-Shelf
最后回答：
- 两个平台分别最容易让你“一眼就懂并想点”的标题句法是什么；
- 哪些条目让你觉得新，但点击摩擦太高；
- 哪些条目很顺，但像已经看过很多次；
- 不要猜项目方想要谁赢。

## Important
- 可以一个项目候选都没选中，因为你不知道谁是项目候选。
- 不评价 2M 字续航。
- 不读正文。
- 不提出重构/修补。
- 不因为某本标题更文学或更长就预设平台优劣。
- 当前为 Copy Shelf Pass。封面视觉 Pass 未等权完成，不得凭脑补封面加分。

## Output
写入：
reviews/2026-09-24_d0088_fresh_shelf_reader_click_test.md

然后更新自己的 CURRENT / history 并停止，交 editor_in_chief 揭盲。
