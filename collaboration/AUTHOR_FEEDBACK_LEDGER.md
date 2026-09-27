# Sheqi｜AUTHOR FEEDBACK LEDGER
status: SHARED LEARNING LOG
stable_path: yes

Purpose:
> preserve author taste and corrections as reusable project memory, not one-off chat patches.

# Routing categories
Each meaningful feedback item should be classified as one of:

STYLE_CORE
> reusable prose rule across chapters.

STYLE_FAILURE
> recurring bad pattern to avoid.

CHARACTER_CORE
> stable personality / behavior truth.

CHARACTER_STATE
> only true because of current knowledge / relationship / chapter state.

WORLD_RULE
> setting / mechanism logic.

STORY_DIRECTION
> plot structure / reader fantasy / arc decision.

LOCAL_EDIT
> only fixes one sentence/scene; do not overgeneralize.

# Current captured feedback

## 2026-09-27｜Fragmented AI prose
Author feedback:
> AI likes single-character / tiny lines; it looks strange.
> “少贫。查。刚才。” are still the same problem even after removing single-character lines.

Classification:
> STYLE_CORE + STYLE_FAILURE

Derived rule:
> fast prose != fragmented prose.
> Paragraph breaks must follow semantic beats.
> Drafting-short dialogue must be integrated unless brevity itself carries emotion.

Applied:
- style/CURRENT_PROSE_STANDARD.md
- style/COMMON_PROSE_FAILURES.md
- tools/prose_lint.py

## 2026-09-27｜Author should not be low-level QA
Author feedback:
> cannot manually catch this every chapter; wastes time.

Classification:
> WORKFLOW / STYLE_CORE

Derived rule:
> formal prose must pass semantic-beat, dialogue, action, AI-pattern, read-aloud and lint checks before author review.

Applied:
- handoffs/shared/FORMAL_PROSE_WRITER_PROTOCOL.md
- style/CURRENT_PROSE_STANDARD.md

## 2026-09-27｜Cheng Ye humor must appear in interaction
Author feedback:
> internal narration alone did not sufficiently show light/humorous personality.

Classification:
> CHARACTER_CORE

Derived rule:
> personality should appear in reciprocal dialogue and decisions, but not through joke density.

Applied:
- characters/CHENG_YE_CHARACTER_BIBLE.md

## 2026-09-27｜Cheng Ye target personality
Author preference:
> functional inspiration from Lu Yang-type energy in 《谁让他修仙的！》.

Classification:
> CHARACTER_CORE

Derived behavior, not imitation:
- optimistic baseline;
- quick associative thinking;
- reads rules creatively;
- slightly crooked but internally reasonable conclusions;
- willing to test weird route himself;
- danger -> humor drops, attention sharpens.

Hard:
> no copied jokes / wording / scenes / author style.

Applied:
- characters/CHENG_YE_CHARACTER_BIBLE.md

## 2026-09-27｜Modern / ancient name separation
Author feedback:
> modern and ancient names should visually classify world/era.

Classification:
> STYLE_CORE / WORLD PRESENTATION

Derived rule:
> modern line uses contemporary realistic names;
> source-era important actors use older naming texture without ornamental cliché.

Applied:
- experiments/reboot_v4/characters/2026-09-27_x19_modern_ancient_naming_convention_v1.md
- style/CURRENT_PROSE_STANDARD.md

## 2026-09-27｜Action continuity
Author feedback:
> “这一脚” then sudden palm hit felt disconnected.

Classification:
> STYLE_FAILURE

Derived rule:
> movement must preserve momentum/body position and connect footwork to hit outcome.

Applied:
- style/CURRENT_PROSE_STANDARD.md
- style/COMMON_PROSE_FAILURES.md

## 2026-09-27｜Abstract AI explanation
Author feedback:
> phrases like “把退路全吃掉” sound AI-ish.

Classification:
> STYLE_FAILURE

Derived rule:
> replace design/summary abstractions with human speech + observable consequence.

Applied:
- style/COMMON_PROSE_FAILURES.md

# Update protocol
When new feedback arrives:
1. record the actual feedback in concise paraphrase;
2. classify it;
3. derive the smallest reusable rule;
4. update the relevant stable file;
5. record paths/commit if meaningful.

Do NOT:
- turn every local wording preference into a global law;
- overwrite old feedback without reason;
- let ledger become a chapter diary.

# Desired effect
Future windows should inherit:
> not only what was chosen,
> but what the author repeatedly dislikes and why.


## 2026-09-27｜热门笔法多章取样后，作者确认“这次进步了很多”
Author feedback:
> 认可“完整语义单元 / 高密度段落 / 人物行为制造幽默 / 世界信息附着现实利益”这轮学习方向，
> 要求把方法和学习结论正式更新进 Git，再交给新窗口继续打磨。

Classification:
> STYLE_CORE + WORKFLOW

Derived rules:
- 快来自“少而密”的叙事单位，不来自碎句；
- 一个重要段落/对话回合尽量承担两个以上功能；
- 程野的轻松感优先通过“歪但自洽的判断 -> 真去做 -> 外界反馈”体现；
- 世界观信息优先附着钱、训练、学校、平台、资格等现实利益；
- Benchmark 结论只有在作者确认有效后才进入稳定写作标准。

Applied:
- research/benchmarks/2026-09-27_prose_craft_multichapter_benchmark_v1.md
- style/CURRENT_PROSE_STANDARD.md
- style/COMMON_PROSE_FAILURES.md

## 2026-09-27｜武技术语“第三转/第四转”不够直观
Author feedback:
> “第三转第四转有点看不懂，应该是第三式招之类的才对。”

Classification:
> STYLE_CORE + WORLD PRESENTATION

Derived rule:
> reader-facing martial/technique structure uses immediately legible units:
> 第X式 / 第X式接第Y式。
> 精确身体动作再用换向、内扣、回撤等词说明。
> 不把作者内部动作节点术语直接扔给Reader。

Applied:
- style/CURRENT_PROSE_STANDARD.md
- style/COMMON_PROSE_FAILURES.md
- next Ch1 baseline terminology pass.
