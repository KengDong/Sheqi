#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lightweight prose lint for Sheqi formal drafts.

Usage:
    python tools/prose_lint.py path/to/chapter.md

This is a warning tool, not a prose judge.
It catches mechanical patterns that should be fixed before author review.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SHORT_DIALOGUE_MAX = 4
SHORT_PARA_MAX = 8
WINDOW_CHARS = 300

WATCH = [
    "下一秒", "下一瞬", "就在这一刻", "很轻", "很快", "很慢",
    "瞬间", "猛地", "突兀", "准确落在", "愣了一下", "沉默了一下",
    "眼神一变", "心里一动", "脑海里第一个念头", "嘴角",
]

def clean_len(s: str) -> int:
    s = re.sub(r"[\s\u3000]+", "", s)
    s = re.sub(r"[“”‘’「」『』，。！？、；：—…,.!?;:\-【】\[\]()（）]", "", s)
    return len(s)

def is_dialogue(s: str) -> bool:
    s = s.strip()
    return s.startswith(("“", "「", "『")) and s.endswith(("”", "」", "』"))

def is_ui_or_heading(s: str) -> bool:
    s = s.strip()
    return s.startswith("#") or (s.startswith("【") and s.endswith("】"))

def paragraphs(text: str):
    out = []
    start = 0
    for block in re.split(r"\n\s*\n", text):
        stripped = block.strip()
        if stripped:
            idx = text.find(block, start)
            line = text.count("\n", 0, idx) + 1
            out.append((line, stripped))
            start = idx + len(block)
    return out

def warn(msg: str):
    print("WARN:", msg)

def lint(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    ps = paragraphs(text)
    warnings = 0

    # 1) Standalone short paragraphs / dialogue shorthand
    for line, p in ps:
        if is_ui_or_heading(p):
            continue
        n = clean_len(p)
        if n <= 2 and not is_dialogue(p):
            warn(f"L{line}: narrative paragraph is only {n} chars: {p!r}")
            warnings += 1
        if is_dialogue(p) and n <= SHORT_DIALOGUE_MAX:
            warn(f"L{line}: very short standalone dialogue ({n} chars): {p!r}")
            warnings += 1
        elif n <= SHORT_PARA_MAX and not is_dialogue(p):
            warn(f"L{line}: short standalone paragraph ({n} chars): {p!r}")
            warnings += 1

    # 2) Three consecutive short prose/dialogue units
    for i in range(len(ps) - 2):
        chunk = ps[i:i+3]
        if all(not is_ui_or_heading(p) and clean_len(p) < 8 for _, p in chunk):
            warn("L{}-{}: 3 consecutive short units: {}".format(
                chunk[0][0], chunk[-1][0], " | ".join(p for _, p in chunk)
            ))
            warnings += 1

    # 3) Short-line density in ~300-char windows
    plain = [(line, p, clean_len(p)) for line, p in ps if not is_ui_or_heading(p)]
    for i in range(len(plain)):
        total = 0
        shorts = []
        j = i
        while j < len(plain) and total < WINDOW_CHARS:
            line, p, n = plain[j]
            total += n
            if n < 8:
                shorts.append((line, p))
            j += 1
        if total >= 180 and len(shorts) > 2:
            warn(f"L{plain[i][0]}+: >2 short standalone units in ~{total} chars: " +
                 " | ".join(f"L{ln}:{p}" for ln, p in shorts))
            warnings += 1
            break

    # 4) Watchlist repetition
    for phrase in WATCH:
        count = text.count(phrase)
        if count >= 2:
            warn(f"phrase repeated {count}x: {phrase}")
            warnings += 1

    # 5) Contrast-pattern repetition
    contrast = len(re.findall(r"不是[^。！？\n]{0,20}[，,。；;]?\s*(?:而是|是)", text))
    if contrast >= 2:
        warn(f"'不是…是/而是…' contrast pattern appears {contrast}x")
        warnings += 1

    # 6) Subject-verb monotony approximation
    names = ["程野", "周航", "邵教练", "季长庚"]
    for name in names:
        starts = len(re.findall(rf"(?:^|\n\s*\n){re.escape(name)}[^\n。！？]{{0,8}}", text))
        if starts >= 8:
            warn(f"many paragraphs begin with {name} ({starts}x); vary syntax")
            warnings += 1

    print(f"\n{path}: {warnings} warning(s)")
    return 1 if warnings else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tools/prose_lint.py chapter.md")
        raise SystemExit(2)
    raise SystemExit(lint(Path(sys.argv[1])))
