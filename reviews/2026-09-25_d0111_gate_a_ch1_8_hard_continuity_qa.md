---
status: completed
date: 2026-09-25
decision: D-0111
gate: A
scope: current authoritative Ch1-8 hard continuity / logic only
verdict: PASS_AFTER_MICROFIX
---

# D-0111 Gate A｜Current Ch1—8 Hard Continuity / Logic QA

# Boundary

This QA deliberately did NOT judge:
- Fang Cen attractiveness / charm;
- Cheng Xiaoman cuteness / sibling pull;
- Tang Ji magnetism;
- Cheng Ye charisma;
- prose style;
- commercial shock / breakout quality.

Only hard mechanics and continuity were checked.

# Final Verdict

> **PASS_AFTER_MICROFIX**

No remaining blocking contradiction was found in the current Ch1—8 source after the fixes below.

Authoritative sources checked:
- `experiments/opening_arcs/r4_把一条副本规则带回现实/opening_arc.md`
- `experiments/rule_reality/d0106_fengmenlou_field2_prototype.md`
- `architecture/2026-09-25_r1_true_name_identity_binding_lock.md`

Continuous package regenerated:
- `experiments/rule_reality/2026-09-25_opening_field2_continuous_v2.md`

# Hard Issues Found + Fixed

## A1｜Same-name experiment control speaker was ambiguous

Problem:
> the first person saying “陈浩” was not explicitly established as unfamiliar with both same-name targets.

Why blocking:
> if he already knew one Chen Hao, the bare-name NO-trigger result would not prove the rule.

Fix:
> explicitly use an externally borrowed young officer and confirm before the test that he has never met either Chen Hao.

Result:
- bare “陈浩” -> no trigger;
- photo A + “陈浩” -> target A;
- new listener can re-trigger A after hearing successful trigger;
- photo B + same spoken characters -> target B.

This now matches the mechanic lock exactly.

## A2｜Photo-first livestream explanation contradicted listener propagation

Problem:
> prose said Wei Pingzhou showed Xiaoman's photo first “to bind identity for all viewers.”

But lock says:
> a valid spoken trigger itself teaches listeners which specific person the name referred to.

Fix:
> clarify that Wei Pingzhou already had a valid Xiaoman binding;
> the photo is not required for first trigger;
> the photo makes the exposure socially stronger by tying direction to face / school / identity and enabling offline recognition.

## A3｜Unintended nighttime Wei Pingzhou triggers

Problem:
> once Fang / Cheng Ye already had Wei Pingzhou's confirmed identity binding, speaking “魏平舟” casually at night would itself trigger R1.

Several dialogue lines were therefore accidentally firing the rule before the intended public counter-use.

Fix:
- “报魏平舟” -> “报他的实名”;
- “知道魏平舟在哪” -> “知道他在哪”;
- quoted full-name discussion -> “这个名字 / 他的实名”;
- Cheng Ye's pre-counter line “魏平舟” -> “你的真名，我知道了.”

Result:
> only the deliberate public “魏平舟” remains as the actual nighttime counter-trigger.

## A4｜Ch4 countdown did not reach Ch5 19:47 entry

Problem:
> Ch4 morning countdown used ~10:58,
> while Ch5 still had ~00:05:58 at 19:41 and zero at 19:47.

That arithmetic could not be continuous with the dawn/breakfast scene.

Fix:
- `10:58:41` -> `12:39:41`;
- prose mirror -> `十二点三十九分三十三秒`;
- `10:57:56` -> `12:38:56`.

Now:
> morning countdown -> 19:47 zero is continuous,
> while the separate R1 sunset/night cycle remains independent.

## A5｜Voice-medium wording accidentally implied prerecorded playback

Problem:
> “群里语音也一样” can naturally read as a prerecorded voice message.

Current mechanic lock confirms:
- live phone/radio/livestream/live voice;
- prerecorded playback is NOT yet canonized.

Fix:
> “群聊实时通话也一样。”

No prerecorded-audio edge case is now accidentally canonized.

## A6｜Field #2 repeatedly re-triggered Tang Ji / leaked Cheng Ye's full name

Problem:
- Tang Ji intentionally self-names once for rescue positioning;
- later dialogue casually reuses “唐霁,” which under R1 would repeatedly trigger her location;
- Tang Ji later calls “程野” despite Cheng only introducing himself as “小程,” creating an information-source leak and an unintended R1 trigger.

Fix:
- after the one intentional self-name trigger, spoken coordination uses “唐医生”;
- Tang Ji explicitly says to avoid repeating her true name;
- “程野” -> “小程.”

Result:
> R1 matters once in Field #2, but does not silently keep firing in ordinary coordination.

# Verified R1 Mechanic Chain

## First trigger
PASS:
> speaker must have a specific-person referent.

## Same-name behavior
PASS:
> bare same-name string does not scan namesakes.

## Listener propagation
PASS:
> successful trigger teaches listeners the stable specific-person referent.

## Re-trigger
PASS:
> a listener with propagated referent can later speak the name for the same target.

## Self-name
PASS:
> Tang Ji self-name is the one deliberate Field #2 use.

## Media
PASS:
> phone / live police channel / livestream / live group call language remains inside confirmed media.

## Written names
PASS:
> written name/photo may establish identity binding but does not by itself create the location trigger.

# Ch4 -> Ch5 Bridge

PASS.

Ch4 establishes:
- visible-only next-entry countdown;
- `青禾里一期·二号楼`;
- planned 40 floors;
- current construction at 9 floors;
- Cheng Ye plans a daylight check.

Ch5 establishes:
- 17:12 daylight site verification;
- same address;
- same nine-floor construction state;
- ordinary prep bag;
- 19:41 return to site;
- ~5:58 remaining;
- zero at 19:47;
- transformation only after zero;
- completed 40-floor future tower.

No teleport / missing bridge remains.

# Field #2 Door-Rule Continuity

PASS against Card A's three prototype clauses:

1. fully closed door cannot be opened from outside;
2. recognized inside person can explicitly invite an outsider through;
3. after the last recognized inside person leaves, prior outsider permission does not make outsiders become recognized inside people.

On-page consistency checked:
- 302;
- 303 wedge-before-full-close;
- 803 invitation;
- 804 failed outsider-only opening;
- 6F / 7F fallback retaining original residents;
- later relay-room usage.

No emergency fourth clause was found.

# Chapter-to-Chapter Continuity

PASS:
- Ch1 -> Ch2 continues the same freight-yard/night chase;
- Ch2 -> Ch3 cleanly moves to next daylight;
- Ch3 -> Ch4 continues the same live Wei Pingzhou escalation;
- Ch4 -> Ch5 now has explicit countdown/address/site bridge;
- Ch5 -> Ch6 continues upward evacuation;
- Ch6 -> Ch7 continues same smoke/door relay;
- Ch7 -> Ch8 directly pays off the “sacrifice two households” setup.

# Commits

Opening hard fixes:
- `fdad7c971c7cc58ddd279d6121c4c082ff6b13b1`
- `450e082f42202dcc6220d8a44efc752b80fb4053`

Field hard fixes:
- `5ee1dd2c64b391878346f495a97845707d89947d`

Continuous package sync:
- `4b8fbd6c5db8eedf17def1a348a8c785c50b7e6b`

# Gate Result

> **D-0111 GATE A PASS.**

Unlock:
> `handoffs/reality_character_magnet_lab_writer/CURRENT.md`

Next:
> D-0111 Gate B controlled Fang Cen A/B/C + Xiaoman A/B/C micro-prototypes.

Main full Ch1—8 reader remains BLOCKED until:
> character lab -> preference evidence -> integration -> fresh hard QA -> regenerated anonymous package.
