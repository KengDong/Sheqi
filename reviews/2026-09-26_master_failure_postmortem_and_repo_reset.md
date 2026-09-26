---
status: COMPLETE / AWAITING AUTHOR REVIEW
date: 2026-09-26
branch: reboot-v4-fanqie-root-audit
scope: full-history / process / market / benchmark / prose / reader / git
dispatch_effect: NONE
---

# SHEQI MASTER FAILURE POSTMORTEM
## 从最早版本到 REBOOT-V4：所有主要踩坑、重复犯错与真正保留下来的资产

# 0. Executive Verdict

The project has repeatedly failed for one meta-reason:

> **we kept optimizing proxies for reader desire, then treating proxy PASS as proof that readers would want the book.**

The proxy changed over time:
- worldbuilding completeness;
- hook architecture;
- benchmark parity;
- long-run architecture;
- AI reader scores;
- story reservoir size;
- character collision;
- scale;
- commercial engine;
- shelf click;
- AI production stability;
- current-hot structure.

But the final authority question stayed under-tested:

> **Would a real target reader voluntarily keep reading this exact book, on this exact platform, from an unknown author?**

The project therefore accumulated a large amount of correct diagnostics around repeatedly wrong or unproven creative bets.

# 1. Five Root Diseases

## ROOT 1｜Surrogate Objective Substitution

The project repeatedly replaced:
> “readers want this”

with easier-to-measure proxies:
- “the structure is complete”;
- “the engine repeats”;
- “the world scales”;
- “the AI can maintain state”;
- “the package gets a click”;
- “the reader understands the design”.

This is the deepest recurring failure.

## ROOT 2｜Evidence Hierarchy Inversion

Lower evidence repeatedly overruled higher evidence:
- selfcheck over taste;
- architecture over prose;
- forced AI completion over natural abandonment;
- theoretical long-run proof over author boredom;
- shelf curiosity over repeated fantasy desire.

Historical proof:
> multiple STRONG PASS cycles were later overturned by the author's voluntary stop / dislike.

## ROOT 3｜Generation by Checklist

A diagnostic rule was discovered,
then quietly promoted into a generation instruction.

Sequence:
> problem found -> new rule -> writer satisfies rule -> prose becomes more engineered -> new problem found -> add another rule.

This produced:
> technically compliant fiction with declining naturalness and desire.

## ROOT 4｜Upstream Market Abstraction

Market study increasingly asked:
> “what designs survive / serialize / compound?”

instead of:
> “what do current readers repeatedly want to fantasize about?”

That bias selected:
- repair;
- operations;
- property;
- logistics;
- shop;
- infrastructure;
because those are easy to structure and track.

A02 exposed the extreme:
> a stable engine with weak primary reader desire.

## ROOT 5｜AI Used Beyond Its Reliable Taste Role

AI was useful for:
- research;
- continuity;
- variant generation;
- hard-error QA;
- state tracking.

But it was repeatedly allowed to act as:
- preference ranker;
- “fresh reader” taste oracle;
- commercial selector;
- final PASS generator.

The author then had to discover obvious taste failures manually.

# 2. Full Failure Ledger

## A. Market / Topic Selection Failures

### F01｜Wrong first market question
Old question:
> what book designs increase breakout probability?

Missing first question:
> what fantasies / emotional experiences are current readers actually buying?

Effect:
> structure-first market synthesis.

### F02｜Genre label confused with reader desire
“末日 / 职业 / 店铺 / 组织 / 领主” was sometimes treated as demand.

But these may only be:
> DELIVERY VEHICLES.

The actual fantasy may be:
- survival;
- power;
- ownership;
- status;
- attachment;
- mystery;
- autonomy.

### F03｜Profession fallacy
Jobs were over-selected because they create stable scenes.

Examples of dangerous primary directions:
- utilities;
- property;
- insurance;
- maintenance;
- logistics;
- factory;
- generic shop.

These can be texture,
but without direct hit proof they should not be treated as primary demand.

### F04｜AI-production convenience became a hidden positive selection function
Fields such as:
- fixed engine;
- state compressibility;
- low hallucination radius;
- bounded research;
- long runway

were useful production constraints,
but together they biased the pool toward operational fiction.

Correct role:
> veto / feasibility warning only.

### F05｜Cross-platform averaging
Qidian and Fanqie were often mixed into one “commercial market”.

This hides:
- different acquisition;
- different patience;
- different distribution;
- different reading economics.

Current author intent:
> Fanqie first launch.

Therefore platform-native proof must come first.

### F06｜Veteran success used too easily as newcomer proof
A veteran hit proves:
> market ceiling.

It does not prove:
> unknown-author entry accessibility.

Need separate:
- veteran control;
- newcomer / low-author-credit breakout.

### F07｜Hot market ≠ good entry market
Previously under-tested:
- competition density;
- packaging sameness;
- trend lifecycle;
- saturation;
- newcomer substitution pressure.

### F08｜No hard failure-corpus requirement early enough
Studying only hits encourages cargo cult.

Need:
> hit vs ordinary / weak same-pool matched controls.

### F09｜Click curiosity confused with repeated fantasy demand
Shelf tests can prove:
> “I might click once.”

They cannot prove:
> “I want 100 chapters of this core pleasure.”

A02 is a direct example.

### F10｜Monetization and distribution entered too late
The project objective is not only:
> good book.

It is:
> breakout + continued reading + sustained income.

For Fanqie,
entry must eventually account for:
- recommendation validation;
- early read-through;
- stable updates;
- long free-reading engagement;
- platform quality governance.

---

## B. Benchmark Failures

### F11｜AI ideation first, benchmark later
The AI often created the solution first,
then searched hits to justify it.

Result:
> benchmark as decoration.

Correct:
> benchmark before major creative mutation.

### F12｜Commonality treated as causality
If all hits have:
- fast premise;
- clear reward;
- recurring cast;

that may be hygiene,
not breakout cause.

Need:
- negative controls;
- ablation;
- Difference Audit.

### F13｜Benchmark scope too structural
The project studied:
- Hook;
- Ch1-3;
- Ch1-10;
- architecture;

more than:
- space legibility;
- object introduction;
- dialogue;
- camera order;
- sentence flow;
- information priority;
- real prose feel.

This caused:
> macro-correct, prose-abnormal fiction.

### F14｜Fantasy-stripped commercial mirroring
Lane B mirrored:
- cadence;
- reward timing;
- organization progression;
- compounding

while removing the benchmark's actual fantasy:
- monsters;
- power;
- special identity;
- forbidden access;
- danger.

This created:
> structural clones without the commercial appetite.

### F15｜Generic “Commercial Mirror” checklist
A02 Mirror Card had no named direct opening benchmark.

It reduced to:
> problem -> diagnosis -> decision -> result -> social state.

That is not true benchmarking.
It is checklist generation.

### F16｜Incomplete competitor evidence sometimes treated too strongly
Catalogue / synopsis / limited-text evidence cannot justify:
> prose-technique equivalence.

Direct prose calibration must use actual accessible text.

### F17｜Benchmark feature shopping
Combining:
> popular A's threat + popular B's relationship + popular C's reversal

produces average commercial soup.

The transferable unit should be:
> reader-level causal function.

---

## C. Concept / Story Design Failures

### F18｜Mechanism-first concept design
Rule / profession / system / operation often became the book's center.

Reader should first receive:
> desire, danger, person, fantasy.

Mechanism is delivery.

### F19｜Rule-first Field design
A Field became:
> a laboratory proving one returned rule.

Characters became test subjects.

Correct:
> Field must first be a complete desirable horror / survival / suspense story.

### F20｜Scale inflation substituted for dramatic intensity
When the author said:
> small / not wild / not enough,

the process added:
- bigger world;
- city overlap;
- void;
- more systems;
- farther chapter horizons.

Bigger nouns did not create stronger scenes.

### F21｜Architecture before desire
Large resources went into:
- Ch100;
- Ch300;
- Ch700;
- macro systems;
- canopy;
- ledgers

before short prose had proven desire.

### F22｜Reservoir proved supply, not demand
30–50 situations can prove:
> the engine produces scenes.

It cannot prove:
> readers want those scenes.

A02 survived because this distinction was blurred.

### F23｜Character Collision proved constructability, not magnetism
A designed cast can have:
- independent wants;
- offscreen agency;
- horizontal links

and still feel dead in prose.

### F24｜Minimal Horizon proved coherence, not attraction
Near -> Mid -> Far can scale naturally
while the reader still does not want Near.

### F25｜Sunk-cost candidate protection
Promising concepts became:
> books the process tried to rescue.

Rule-Reality was the clearest example.

This distorted kill decisions.

### F26｜False-negative fear became survival bias
Avoiding premature cuts is useful.

But excessive caution kept too many candidates alive because:
> “maybe the next gate measures its real strength.”

This increased cost and delayed hard taste decisions.

### F27｜Too many dimensions changed at once
Some iterations changed:
- world;
- scale;
- character;
- voice;
- hook;
- mystery

simultaneously.

That destroys causal learning.

Version discipline must change:
> one major hypothesis per comparison whenever possible.

---

## D. Protagonist / Character Failures

### F28｜Character adjectives instead of behavior
Old protagonist designs:
- smart;
- calm;
- responsible;
- cautious.

Result:
> senior project manager.

Character magnetism came only when expressed as:
- enemy mode;
- ally mode;
- wound;
- contradiction;
- repeated behavior under pressure.

### F29｜Competence fantasy written as ordinary common sense
Examples:
- record;
- call police;
- preserve evidence;
- make backups.

Correct in life,
weak as book-specific fantasy.

Competence must be:
> impossible to transplant unchanged into another novel.

### F30｜Protagonist becomes premise interface
Even in hot worlds,
the protagonist can become:
> the person who operates the mechanic correctly.

Need separate:
- world fantasy;
- protagonist fantasy.

### F31｜Relationships used as functions
Characters sometimes entered to provide:
- medical view;
- authority conflict;
- exposition;
- emotional settlement.

A functional cast is not automatically a lovable cast.

### F32｜Unknown-author cold-start personality tax underweighted
An unknown author lacks brand patience.

Opening needs faster proof through at least one:
- distinctive protagonist personality;
- relationship chemistry;
- personality intensity;
- immediately pleasurable fantasy.

“well written and correct” is not enough.

---

## E. Prose / Reader-Legibility Failures

### F33｜Author-language / design-language leaked into prose
Examples:
- engineering nouns;
- compact labels;
- system-like abstractions.

Reader saw:
> a design document rendered as fiction.

### F34｜Referential opacity
Words looked familiar but readers had no visual model:
- object;
- position;
- relation;
- function.

### F35｜Spatial model not established
The author had:
> diagrams / visual bibles.

The reader had:
> left / right / outer / inner words with no scene model.

### F36｜API dialogue
Characters spoke like:
> system interfaces exchanging state.

Dialogue served design correctness rather than human intention.

### F37｜Over-compression
Fear of exposition caused:
> core premise under-explained,
while secondary mechanical details were over-specified.

### F38｜Terminology introduced before reader need
New words accumulated faster than useful mental models.

### F39｜Alias / naming drift
Examples:
- nickname before anchor;
- warehouse/site numbers changing;
- role names switching.

Small friction compounded into:
> AI / draft feeling.

### F40｜Engineered thematic closure
Sentences and scene turns landed too neatly:
> “这不是……而是……”
> “他忽然明白……”
> “第一次真正……”

Repeated use made prose feel architected.

### F41｜Theme statements replaced lived implication
The text explained what the event meant
instead of allowing behavior and consequence to imply it.

### F42｜Naturalness QA happened too late
The author repeatedly discovered:
- awkward noun;
- unclear scene;
- unnatural line;
- generic AI phrasing

after large structural work was already done.

---

## F. Reader / Testing Failures

### F43｜Forced-completion AI Reader inflation
Reader instruction:
> read all 6/10 chapters and then judge.

Real behavior:
> stop whenever bored.

Forced completion produced false STRONG PASS.

### F44｜AI Reader entered evaluation mode
AI often rewarded:
- understanding;
- completeness;
- design intent.

Consumption asks:
> do I want another page?

### F45｜AI ranking used as selection authority
Synthetic preferences were treated too much like market taste.

Current author instruction:
> AI should not provide final candidate ranking.

### F46｜Selfcheck inflation
Writer / architect selfchecks proved:
> task compliance.

They were too often read emotionally as:
> quality proof.

### F47｜Author became the training loop
The author repeatedly had to discover:
- boring;
- small;
- mechanical;
- generic;
- wrong topic;
- bad prose.

This is a process failure.

The system should filter obvious failures before author exposure.

### F48｜Real-human evidence too late / too little
AI clean readers are useful diagnostics,
not final market proof.

Before launch:
> several real target readers with voluntary stop behavior are needed if practical.

### F49｜P0 was still too late
Even REBOOT-V3 placed:
- Reservoir;
- Character Benchmark;
- Collision;
- Horizon

before first real prose.

That allowed design confidence to accumulate before taste proof.

---

## G. Experimental Design Failures

### F50｜Same-file information asymmetry was not real isolation
Native and Mirror instructions lived in one physical file.

A file read could expose both.

Result:
> invalid causal A/B evidence.

Correct:
> separate files + separate clean windows.

### F51｜Mirror writer condition over-constrained
Even after physical isolation,
Base Card forced nearly the same:
- scene;
- problem;
- payoff;
- conflict.

The experiment measured small wording/cadence differences,
not genuinely different execution strategies.

### F52｜Condition labels were stronger than actual manipulation
“Commercial Mirror” sounded like:
> direct hit-derived execution.

In reality it sometimes meant:
> generic commercial advice.

Experiment names must describe actual treatment.

### F53｜Reader order / contamination controls were not designed from the start
Counterbalancing and private mapping were added later.

Experimental hygiene should be part of initial design,
not a repair.

---

## H. Git / Project Management Failures

### F54｜Authority drift
At multiple points:
- CURRENT_AUTHORITY;
- STATE;
- ACTIVE_WORKSTREAMS;
- CURRENT handoffs

disagreed.

Git was “the memory” but the memory had multiple conflicting present tenses.

### F55｜Historical NEXT leaked into current execution
Old files retained:
> NEXT / READY / PASS

and could be mistaken for live instructions.

### F56｜PASS language outlived evidence
A historical PASS represented:
> evidence at that time.

It was too easy for later windows to inherit it as current truth.

### F57｜Main became both control plane and experiment sink
A huge amount of:
- experiments;
- authority;
- postmortems;
- handoffs

accumulated on one branch.

Even with directory discipline,
the control surface became cognitively noisy.

### F58｜Too many parallel windows
Large candidate pools + many clean-room roles created:
- coordination cost;
- author management cost;
- stale states;
- higher contamination risk.

### F59｜Task dispatch sometimes outran root review
A new failure led quickly to:
> a new scout / new brief / new gate.

This created patch-on-patch process growth before deciding whether the entire stage should be reopened.

### F60｜WIP discipline existed but was not always enough
Even WIP<=2 creative workers can still create process sprawl if:
- readers;
- scouts;
- editors;
- side lanes

all multiply simultaneously.

### F61｜Writer context sometimes included too much design
The more rules a Writer sees,
the more likely prose becomes:
> execution of requirements.

Writer input needs to be minimal and causal,
not comprehensive.

---

# 3. Repeated Error Loops

## LOOP A｜Author says “not good”
Process response:
> add a rule.

Then:
> writer obeys rule.

Then:
> prose gets more designed.

Then author says:
> still not good, but in a new way.

This loop happened repeatedly.

## LOOP B｜Book feels small
Process response:
> increase world / engine / horizon.

Correct response should have been:
> identify what immediate desire / dramatic intensity is missing.

## LOOP C｜Character feels bland
Process response:
> add character adjectives / backstory.

Correct:
> test behavior + relationship chemistry in prose.

## LOOP D｜Prose feels unclear
Process response:
> remove explanation.

Then:
> over-compression / black-box nouns.

Correct:
> prioritize information, not simply reduce it.

## LOOP E｜Commercial uncertainty
Process response:
> add more benchmark structure.

Correct:
> identify the actual reader fantasy and direct market pool.

## LOOP F｜A candidate survives many gates
Process inference:
> probably strong.

But if those gates test different proxies,
survival may only mean:
> the book is robustly well-designed, not desired.

---

# 4. What Is Actually Trustworthy

## KEEP AS HIGH-VALUE PROCESS ASSETS

### A. Behavioral evidence hierarchy
Real voluntary stop / continue:
> highest.

### B. Author taste as final internal ranking
AI does not choose the final concept.

### C. Physical clean-room isolation
Information asymmetry requires:
> separate files + separate windows.

### D. Benchmark causality standard
Keep:
- negative controls;
- ablation;
- Difference Audit;
- function vs skin.

### E. Human prose / reader-language lessons
Keep:
- scene model first;
- familiar surface language;
- first-use anchoring;
- information priority;
- no API dialogue.

### F. Story Reservoir
Keep only AFTER desire proof.

Use it to ask:
> can this desirable thing continue?

Not:
> does this deserve to exist?

### G. Character Collision
Keep only AFTER prose desire proof.

### H. Old-state compounding
Strong long-run diagnostic,
not a cold-start selection criterion.

### I. Short prototype ladder
Micro-prose -> P0 -> P1 -> P3
is directionally correct,
but author / real-human evidence must dominate.

### J. Platform-specific strategy
Current author intent:
> Fanqie first.

This should be treated as an early market constraint.

---

# 5. What Loses Authority

The following are historical evidence only unless explicitly reactivated later:

- every old candidate PASS;
- every old ACTIVE / RESERVE label;
- Rule-Reality priority;
- C01/C12 candidate status;
- D0098 architecture priority;
- REBOOT-V3 candidate pool;
- A01/A02/A04/B10 progression;
- old AI shelf rankings;
- old AI reader rankings;
- old Market Dossier synthesis;
- old cross-platform selection board;
- old Fanqie scout READY state.

Raw factual research may be reused only after freshness verification.

---

# 6. New Non-Negotiable Principles

## P1｜Platform before concept
Current intended platform:
> Fanqie.

Do not average with Qidian at selection time.

## P2｜Reader pool before structure
First prove:
> a current Fanqie reader pool exists and an unknown author can enter it.

## P3｜Reader fantasy before delivery vehicle
Every concept must state:
- primary fantasy;
- secondary fantasy;
- protagonist fantasy.

## P4｜Validated mother chassis
No invented market demand by default.

Innovation belongs in:
> Premium.

## P5｜Author ranks, AI filters
AI may:
- eliminate unsupported;
- explain;
- QA.

AI may not:
> crown the winner.

## P6｜Desire before scalability
A scene / micro-prose must first be desirable.

Only then:
> Reservoir / Character / Horizon.

## P7｜Direct comps + matched failures
For any selected pool:
- hit;
- newcomer hit;
- weak/ordinary control.

## P8｜No rescue privilege
Any concept can die at any time.

Past investment is not evidence.

## P9｜Minimal Writer context
Writer sees:
> only what is required to write the current experiment.

## P10｜One hypothesis per comparison
Avoid giant multi-axis rewrites when learning causality matters.

---

# 7. Recommended Restart Point

This audit recommends the next *possible* restart point as:

> **Fanqie-specific market-entry mapping for unknown male authors**

But:
> this is a recommendation, NOT a dispatched task.

The market study should eventually answer:
- exact reader pools;
- current reading-rank proof;
- current new-book proof;
- newcomer examples;
- competition density;
- trend stage;
- matched failures;
- title/blurb commoditization;
- early binge / follow logic;
- compliance / quality-governance risk.

Only after that should the AUTHOR choose:
> WANT / MAYBE / NO.

No concept should exist before that human choice.

---

# 8. Recommended Future Sequence｜Not Yet Dispatched

1. Fanqie exact market-entry map.
2. AUTHOR chooses 1–3 reader pools.
3. Direct hit + matched-failure deep read.
4. Generate only 2–4 concepts per selected pool.
5. AUTHOR ranks concepts.
6. Three must-see scenes.
7. 300–600 char micro-prose.
8. AUTHOR voluntary continue / stop.
9. 800–1500 P0.
10. Add real target-reader voluntary evidence if practical.
11. Only survivors receive Reservoir / Character / Horizon.
12. P1 / P3 / Opening.
13. Fanqie launch-readiness simulation.
14. Long-run architecture only after sustained prose proof.

---

# 9. Git Reset Recommendation

## Control plane
Keep only these as “current”:
- BRANCH_PURPOSE;
- CURRENT_AUTHORITY;
- STATE;
- ACTIVE_WORKSTREAMS;
- editor CURRENT;
- master audit.

Everything else:
> library / historical evidence.

## Branching
This branch:
> process rebuild only.

Do NOT merge into main until:
- author accepts audit;
- new authority set is small and coherent.

Future creative candidate branches:
> only after a candidate earns sustained prose evidence.

## Handoffs
During audit:
> zero READY workers.

After audit:
> one worker at a time until control plane is proven stable.

---

# 10. Final Diagnosis

The project did not fail because:
> AI cannot write fiction at all.

It failed because:
> AI is extremely good at satisfying explicit structures,
and the process repeatedly mistook that ability for evidence of reader desire.

Therefore the new operating system must deliberately protect against:
> **well-designed garbage.**

# One Sentence

> **从现在开始，不再问“这个方案还能补什么才更完整”，先问“一个番茄陌生读者凭什么现在就想看，而且连续想看”。**
