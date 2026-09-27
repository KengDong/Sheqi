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
