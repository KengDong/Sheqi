# B01｜三个 GPT 窗口并行研究：启动卡
date: 2026-10-09
repo: https://github.com/KengDong/Sheqi
base: reboot-v6-verified-scene-lab

## 为什么分三个
作者强调“多搜索点不好吗？”且要求“脑洞大开和高效的”。
Git不会自动唤起GPT。作者需要打开3个独立对话，三个窗口都要有 GitHub 插件权限和网页搜索能力。每人一个branch和handoff，不能共写base。

## 窗口1｜番茄男频实读
Branch: `b01-fanqie-scene-scout`
Role: `b01_fanqie_scout`
Startup:
> 继续 Sheqi。使用 GitHub 插件访问 KengDong/Sheqi。当前分支 b01-fanqie-scene-scout，身份 b01_fanqie_scout。先读 AGENTS.md 和 handoffs/b01_fanqie_scout/CURRENT.md，按 CURRENT 指定的 brief 直接进行真实网页搜索、核实具体高脑洞情节，分批提交成果并创建到 reboot-v6-verified-scene-lab 的 PR。只在自己的分支和目录工作。不要只写计划，也不要创作小说。

## 窗口2｜起点等跨平台脑洞
Branch: `b01-crossplatform-idea-scout`
Role: `b01_crossplatform_scout`
Startup:
> 继续 Sheqi。使用 GitHub 插件访问 KengDong/Sheqi。当前分支 b01-crossplatform-idea-scout，身份 b01_crossplatform_scout。先读 AGENTS.md 和 handoffs/b01_crossplatform_scout/CURRENT.md，按 CURRENT 指定的 brief 直接搜索各平台真实高脑洞设定、名场面和可持续玩法，核查出处，分批提交成果并创建到 reboot-v6-verified-scene-lab 的 PR。只在自己的分支和目录工作。不要只写计划，也不要创作小说。

## 窗口3｜真实读者热议名场面
Branch: `b01-reader-reaction-scout`
Role: `b01_reader_reaction_scout`
Startup:
> 继续 Sheqi。使用 GitHub 插件访问 KengDong/Sheqi。当前分支 b01-reader-reaction-scout，身份 b01_reader_reaction_scout。先读 AGENTS.md 和 handoffs/b01_reader_reaction_scout/CURRENT.md，按 CURRENT 指定的 brief 搜索真实读者讨论中主动提及的离谱名场面、爆笑桥段和神反转，追溯章节原文核验，分批提交成果并创建到 reboot-v6-verified-scene-lab 的 PR。只在自己的分支和目录工作。不要只写计划，也不要创作小说。

## 窗口4｜汇总总编（等3个分支有成果后才运行）
Branch: `reboot-v6-verified-scene-lab`
Role: `verified_scene_scout` (CURATOR / CONSOLIDATOR)
Startup:
> 继续 Sheqi，总编汇总身份 verified_scene_scout。访问 KengDong/Sheqi 的 reboot-v6-verified-scene-lab 分支，先读 AGENTS.md、meta/ACTIVE_WORKSTREAMS.md 和 handoffs/verified_scene_scout/CURRENT.md，再检查 b01-fanqie-scene-scout、b01-crossplatform-idea-scout、b01-reader-reaction-scout 的实际研究成果/PR。核查来源与重复、合并有效成果、整理完整素材索引和分批作者选择板。不要替作者选最终小说，不写正文，也不要把未核验的转述写成已读正文。

## 具体执行注意
- 3个研究窗口可以同时开。无须一个窗口完成后才开下一个。
- 新窗口可能需要手动在工具中启用/授权 GitHub；Git 内容不会自动进入新聊天上下文，必须先读取指定 CURRENT。
- 每人只能写自己的分支和独立目录，否则 Git 相互覆盖。
- 如果 GPT 说“已搜索几十条”但未写出来源与 Git 提交，不视为完成。
- 完成后要提交 Git、开 PR（**不要自行 merge**）。由汇总总编检查后合并。
- 当前不启动 B02/写小说。作者先挑选具体场面/玩法。
