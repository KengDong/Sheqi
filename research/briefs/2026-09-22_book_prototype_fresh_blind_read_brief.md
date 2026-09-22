---
status: active
version: 1.1
created_at: 2026-09-22
authority: evaluation
canon_effect: none
outline_effect: none
depends_on: book-level-prototype-duel-done
---

# Fresh Book Prototype Blind Read｜真正陌生读者测试

## EXECUTION REQUIREMENT
> **必须新开一个完全干净的GPT窗口。**

不得复用：
- 旧blind_reader；
- benchmark_deepread；
- market_scout；
- hit_concept_scout；
- world_reframe；
- editor_in_chief；
- opening_writer。

## 第一轮唯一输入
只允许读取：
- A正文
- B正文
- C正文
- D正文

不读取：
- Concept Foundry；
- Benchmark Gate；
- Writer Selfcheck；
- 总评审结论；
- A/B/C/D真实映射；
- Sheqi任何旧资产。

## 任务
把自己当成一个没有耐心预支的普通商业网文读者。

不要先拆结构。
先真实阅读。

### 第一层｜Absolute Read Test
**先分别判断每一篇本身值不值得追，不准先做四篇内部排名。**

对A / B / C / D逐篇回答：
- 如果它单独出现在小说平台，我读完这段后会不会主动点第二章？
- 哪个瞬间开始真正想看？
- 哪个瞬间开始掉兴趣？
- 我现在在乎的是“这个人 / 这段生活”，还是主要在乎“这个点子”？
- 如果接下来三章没有更大的Concept奇观，我还愿不愿意跟？
- 它现在像：
  > 真正可追的小说
  还是
  > 写得不错的高概念样章？

允许：
> **四篇全部FAIL。**

也允许：
> 只有一篇真正想追。

绝不能因为任务里有四篇，就默认必须选赢家。

### 第二层｜Relative Read Test
完成逐篇绝对判断后，再回答：

1. 哪篇最自然地让你继续往下读？
2. 哪篇第一屏最抓？
3. 哪篇主角最像一个你愿意继续跟的人？
4. 哪篇读完后最想立刻点第二章？
5. 哪篇的世界最有新鲜感，但又不像作者在展示设定？
6. 哪篇最容易想象自己追50—100章？
7. 哪篇读到后面最容易疲劳？为什么？
8. 如果只看真实读欲，你会留下哪些？**数量不限，可以0—4篇。**

## 关键要求
- 不做纯数值评分；
- 不因为题材偏好一句话决定；
- 不强行选冠军；
- 不强行保留两篇；
- 用真实阅读过程解释“哪里开始想看 / 哪里开始掉兴趣”；
- 区分：
  > 我喜欢这个点子
  与
  > 我想继续看这本小说。
- 必须明确写：
  > **这些样本里是否真的已经出现“值得继续押整本书”的作品。**
- 若没有：
  > **直接说没有。**


## 输出
> `reviews/2026-09-22_book_prototype_fresh_blind_read.md`

完成CURRENT + history后停止，交总评审。
