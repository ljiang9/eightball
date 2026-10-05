"""eightball - 终端里的魔法神谕球。纯标准库，本地运行。

随机给出肯定/中立/否定三类回答之一。仅供娱乐，不是人生建议。
"""

import argparse
import random
import secrets
import sys

POSITIVE = [
    "毫无疑问，当然可以。",
    "前景一片光明，放手去做。",
    "是的，时机正好。",
    "Absolutely yes.",
    "The stars say yes.",
    "好运站在你这边。",
    "大胆去做，不会错。",
]

NEUTRAL = [
    "现在还看不清楚，稍后再问。",
    "答案藏在风里，再想想。",
    "Maybe. 再观察一下。",
    "Ask again after coffee.",
    "时机未到，别着急。",
    "这事可大可小，看你怎么做。",
]

NEGATIVE = [
    "不太妙，建议换个思路。",
    "现在不是好时机。",
    "恐怕不行，先缓一缓。",
    "Don't count on it.",
    "Outlook not so good.",
    "再等等，急不得。",
    "别问了，你心里已经有答案了。",
]

CATEGORIES = {"positive": POSITIVE, "neutral": NEUTRAL, "negative": NEGATIVE}
# 全部 20 条：肯定 7 / 中立 6 / 否定 7
ALL = POSITIVE + NEUTRAL + NEGATIVE

SHAKE_FRAMES = [
    r"   _____   ",
    r"  /     \  ",
    r" |   ?   | ",
    r"  \_____/  ",
]


def pick(category=None, rng=None):
    rng = rng or secrets.SystemRandom()
    pool = CATEGORIES[category] if category else ALL
    return rng.choice(pool)


def shake_animation():
    import time
    frames = ["   . o O   ", "  o O .    ", "   O . o   "]
    for f in frames:
        sys.stdout.write("\r" + f)
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\r          \r")


def main(argv=None):
    p = argparse.ArgumentParser(prog="eightball", description="终端魔法神谕球：问一句，摇一摇，得一个随机的回答。仅供娱乐。")
    p.add_argument("question", nargs="?", help="你的问题（必填）")
    p.add_argument("--category", choices=["positive", "neutral", "negative"],
                   help="只从某一类回答里抽")
    p.add_argument("--seed", type=int, default=None, help="固定随机种子（演示/测试用）")
    p.add_argument("--shake", action="store_true", help="摇一摇动画")
    args = p.parse_args(argv)

    if not args.question or not args.question.strip():
        print("error: 请先问一个问题，例如：eightball \"我今天运气好吗？\"", file=sys.stderr)
        return 2

    rng = random.Random(args.seed) if args.seed is not None else None
    if args.shake:
        shake_animation()
    print(pick(args.category, rng))
    return 0


if __name__ == "__main__":
    sys.exit(main())
