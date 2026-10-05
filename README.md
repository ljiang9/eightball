# eightball · 魔法神谕球

终端里的 Magic 8-Ball：问一句，摇一摇，得到一个随机回答。纯标准库，本地运行。

## 用法

```bash
python3 -m eightball "我今天运气好吗？"
python3 -m eightball "Should I deploy on Friday?" --shake
python3 -m eightball "能成吗？" --category positive   # 只抽肯定类
python3 -m eightball "行不行？" --seed 42              # 固定结果（演示用）
```

## 回答库

共 20 条，自写的中英混合回答，分三类：

| 类别 | 数量 | 说明 |
|---|---|---|
| positive（肯定） | 7 | "毫无疑问，当然可以。" / "Absolutely yes." … |
| neutral（中立） | 6 | "现在还看不清楚，稍后再问。" / "Ask again after coffee." … |
| negative（否定） | 7 | "不太妙，建议换个思路。" / "Don't count on it." … |

默认从全部 20 条里均匀随机抽取（`secrets.SystemRandom`）。

## 诚实说明

- 这是**随机数发生器**，不是建议系统：回答与你的问题没有任何因果关系。
- 连续问同一问题直到抽到想要的答案，是人类，不是魔法。
- `--seed` 只用于演示和测试可复现。

## 已知局限

- 回答库是写死的 20 条，看多了会重复；想加自己的直接改 `POSITIVE`/`NEUTRAL`/`NEGATIVE` 列表。
- `--shake` 只是终端小动画，没有物理摇晃加成（也没有减成）。

## License

MIT，Copyright (c) 2026 ljiang9。
