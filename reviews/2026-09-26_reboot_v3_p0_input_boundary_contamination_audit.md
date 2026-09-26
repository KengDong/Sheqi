---
status: COMPLETE
date: 2026-09-26
decision: REBOOT-V3
stage: P0 First Screen
issue: INPUT_BOUNDARY_CONTAMINATION
---

# P0 Input Boundary Contamination Audit

## 0. Verdict

The original Native-vs-Mirror writer protocol is:
> **INVALID FOR CAUSAL A/B INFERENCE**

Root cause:
> Native Card and Mirror Function Card were stored in the SAME Git file.

A GitHub file read can return the entire file.
Therefore a writer instructed to "read only the Native section" may still receive the Mirror section in model context before Native is written.

Section-level reading instructions are NOT a reliable information barrier.

## 1. Affected candidates

### A02
Status:
> CLEANLY ABORTED BEFORE PROSE.

The writer detected the contamination before writing Native, Mirror, or committing prose.

Therefore:
> no prose contamination occurred.

### A01
Existing Native + Mirror prose:
> ARCHIVE ONLY / INVALID FOR FORMAL N-vs-M CAUSAL COMPARISON.

Reason:
> source card physically contained Mirror guidance at Native-read time.

The prose may still be useful as ordinary draft evidence later, but not as proof that Native was blind to Mirror.

### A04
Same:
> ARCHIVE ONLY / INVALID FOR FORMAL N-vs-M CAUSAL COMPARISON.

### B10
Same:
> ARCHIVE ONLY / INVALID FOR FORMAL N-vs-M CAUSAL COMPARISON.

## 2. Affected downstream evidence

The anonymous A01/A04 pair packages created from contaminated outputs are:
> INVALID FOR FORMAL PAIRWISE TEST.

Any clean-reader result using those packages must be discarded.

At the time of audit:
> both pair readers were still READY and had not submitted reports.

They must be cancelled before execution.

## 3. Corrective design

P0 experiment V2 uses:
> **PHYSICAL FILE ISOLATION + SEPARATE WRITER WINDOWS**

For each candidate:

### Base Card
Contains:
- title;
- package promise;
- protagonist;
- recurring people;
- Near contract;
- candidate-specific hard constraints.

Contains ZERO Mirror functions.

### Native Writer
May read only:
- Native shared brief;
- candidate Base Card.

Outputs Native only.
Stops.

### Mirror Writer
May read only:
- Mirror shared brief;
- same Base Card;
- candidate Mirror Function Card.

Outputs Mirror only.
Stops.

Mirror writer does NOT read Native prose.

This produces a cleaner comparison:
> same concept/base information, one condition receives extra proven commercial-function guidance.

## 4. New hard rule

> **If two experimental conditions require information asymmetry, their privileged instructions must live in physically separate files and must be executed in separate clean windows.**

Same-file section boundaries are prohibited.

## 5. Evidence consequence

Do NOT use the existing A01/A04/B10 paired outputs to conclude:
- Mirror wins;
- Native wins;
- commercial mirroring helps;
- commercial mirroring hurts.

Those questions remain unanswered until P0 V2 reruns.

## 6. One sentence

> **这次不是Writer失败，而是实验设计失败；正确修法是把信息边界做成物理边界，而不是靠“请只读上半段”。**
