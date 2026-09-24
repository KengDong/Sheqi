---
status: completed
date: 2026-09-24
role: editor_in_chief
decision: D-0093C
scope: Batch A author-read prose naturalness audit
canon_effect: none
prose_patch_status: deferred-until-author-read-complete
---

# D-0093C｜Batch A Micro-Prose Naturalness / Friction Audit

Trigger:
> Author reports that all seven arcs are broadly coherent, but many contain small local phrases / names / transitions that feel unnatural or not fully smooth.

This audit does NOT rewrite prose while the author is still reading.
It records confirmed defects and project-wide editing rules for the next polish pass.

# 1. Confirmed Hard Continuity Error｜A《无身份资产》

The same warehouse/site is inconsistently referred to as:
- 七码仓
- 八码仓
- 六码仓

Examples occur inside the same continuous outage incident.

This is a genuine text consistency defect, not reader unfamiliarity.

Required later patch:
> freeze one warehouse name/number and normalize every reference.

Related jargon:
> “箱变” is technically valid shorthand for 箱式变电站, but its first occurrence assumes industry knowledge.

Better first-use principle:
> first occurrence uses a reader-legible full phrase, later dialogue may shorten it naturally.

Example:
> “昨晚暴雨把片区一座箱式变电站泡了。”
Later:
> “箱变进水。”

# 2. Confirmed Reader-Friction Cluster｜B《养一条会跟我走的灵脉》

Author specifically flags:
- 渠棚
- 菜畦
- 三岔集
- 分口
- 泄口闸石

Problem is not that any single word is invalid.
The issue is:
> several semi-literary / pseudo-historical nouns accumulate in a short span without enough concrete everyday anchoring.

This produces a “constructed fantasy terminology” texture.

Guideline:
> prefer objects / place names a reader can picture immediately; reserve specialized historical/waterworks terms for moments where the object itself matters.

Potential direction:
- 渠棚 -> 旧水棚 / 旧歇脚棚 / 南渠棚（after natural introduction）
- 菜畦 -> 菜地 / 两垄菜地
- 三岔集 -> if retained, establish it first as “三岔口那片集市/镇子”, then use short name
- 分口 -> 分水口 / 岔口 depending physical meaning
- 泄口闸石 -> first show the stone/gate physically, then name it if needed

Do not mechanically modernize everything; the target is visual immediacy.

# 3. Character Anchor Failure｜“阿满”

In Ch1 the child is introduced only as:
> 陶婶的小孙子 / 孩子

At the start of Ch2, the prose suddenly uses:
> “阿满刚才还不敢动……”

The reader has not yet been explicitly told:
> the child = 阿满.

Full name “陶满” is only revealed much later during permit registration.

This validates the author's “阿满突然出来我不知道是谁” reaction.

Required later patch:
> anchor nickname on first relevant introduction, e.g. 陶婶叫孩子“阿满”, or narration “她的小孙子阿满”.

This is a general project rule:
> no nickname / surname / role-name switch without a first-use anchor.

# 4. Semantic Half-Beat｜“从前不算现在”

Context:
> 陶婶：“至少从前，这地方不是青鹤门的。”
> 陆照川：“从前不算现在。”

The intended meaning is inferable:
> historical use does not prove current ownership / legal status.

But the line is one semantic beat short.
Because the scene is already juggling:
- old public-use history;
- current land ownership;
- Qinghemen boundary;
- tomorrow's contract-office check;

“从前不算现在” reads like a slogan rather than a precise human response.

Better principle:
> when a line carries legal/spatial inference, let the character name the missing noun.

Possible natural direction:
> “从前不是，不代表现在也不是。”
or
> “以前谁都能住，不代表现在还算公棚。明天问清楚。”

Do not necessarily use these exact lines; preserve character voice.

# 5. Why C《劫痕道途》 Feels Smoother

Author reports a large smoothness gap between B and C.

Observed reasons:

## a. New nouns are attached to immediate physical action
Examples:
- 劫钉 -> immediately cracks / discharges;
- 净痕院 -> immediately tied to a concrete treatment choice;
- 承劫渠 -> immediately used in an exam / crisis.

The noun arrives with:
> object + consequence + person who cares.

## b. Relationship dialogue has clear local intention
阮青禾 does not speak mainly to explain theme.
She wants:
- him to get treated;
- him to stop deciding her choices;
- him to leave records.

Therefore even thematic lines feel like conflict rather than narration.

## c. Character identity is anchored before shorthand matters
阮青禾 enters carrying a medical kit and treating him before the text asks the reader to remember her role.

# 6. Why E《把一条副本规则带回现实》 Feels Smoother

Author reports direct immersion and modern prose fluency.

Observed reasons:

- familiar contemporary objects dominate the surface language:
  地铁口 / 手机 / 妈 / 妹妹 / 出租车 / 北货场;
- only one extraordinary rule is introduced;
- the rule is phrased in ordinary Chinese:
  “天黑后不能说真名”;
- the first consequence occurs immediately during a normal phone call;
- exposition is mostly delayed until the reader has already experienced the effect.

General lesson:
> familiar surface vocabulary lets the Premium carry the novelty burden.

# 7. Shared Project-Level Micro-Prose Risks

The seven Opening Arcs show varying degrees of the following:

### A. Concept-first naming
The writer invents a compact technical/fantasy noun before asking:
> would a normal person in this scene actually call it that?

### B. Semantic compression
A line is logically inferable but omits the noun / relation needed for effortless reading.

### C. Alias drift
child -> nickname;
warehouse/site -> changing number;
job title -> role shorthand;
without explicit anchoring.

### D. Engineered thematic closure
Several reader reports independently noticed:
> key scene turns are unusually clean, with theme statements landing exactly where the architecture needs them.

This is not automatically bad.
But if combined with dense terminology, it creates an “AI designed the beat” feeling.

### E. Explicit architecture sentences
Patterns such as:
- “他忽然明白了一件事”
- “这不是……而是……”
- “第一次真正……”
are useful occasionally, but should not be default bridge devices.

Pattern-count audit did not show a single catastrophic phrase repeated across all books, so the problem is not one literal tic.
It is:
> prose often explains the causal meaning one beat more neatly than natural viewpoint consciousness would.

# 8. New Editing Rule｜Reader-Friction Pass

Before any surviving candidate expands into sustained long-form prose, run a dedicated pass that asks sentence by sentence:

1. Is this noun how a person would naturally call the object here?
2. Does the reader know who this nickname refers to?
3. Did a location/object change names accidentally?
4. Does the dialogue omit a noun the speaker would naturally include?
5. Is a sentence explaining a theme that the scene already made obvious?
6. Can a specialized term be replaced by a visible object on first use?
7. Is the prose asking the reader to memorize more than one new invented term in the same paragraph?
8. Would this line still sound natural read aloud?

# 9. Name Collision

Batch A E protagonist:
> 程野

Batch B B7 protagonist:
> 程野

These are separate candidate novels, so not a reader-facing conflict if only one survives, but they create R&D confusion and future contamination risk.

Given current author response:
> E《把一条副本规则带回现实》 = 92 / strongest personal pull.

Recommendation:
> reserve “程野” for E for now.
If B7 survives its absolute reader + author read, rename B7 protagonist before deeper development.

Do not rename during D-0095 blind evaluation.

# 10. Patch Timing

Do NOT patch the anonymous Batch A files while author first read is in progress.

Reason:
> preserve the exact text that generated the human behavioral evidence.

After author read is formally closed:
- create clean patched source versions;
- preserve original experimental evidence files unchanged;
- patch only candidates that continue.

# Verdict

Author's “小地方不自然” observation is CONFIRMED.

It is not primarily a macro-story failure.

It is a project-wide:
> **micro-prose / naming / anchoring / semantic-friction problem**

with B showing a stronger concentration than C/E.

This should become a formal pre-P7 polish gate for all survivors.
