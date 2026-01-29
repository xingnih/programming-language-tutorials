# Python Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```py
from collections import Counter

def freq(nums: list[int]) -> dict[int,int]:
    return dict(Counter(nums))
```

## 2) 去重（保留順序）
```py
def dedup(nums: list[int]) -> list[int]:
    seen = set()
    out = []
    for x in nums:
        if x in seen: continue
        seen.add(x)
        out.append(x)
    return out
```

## 3) 反轉字串
```py
def rev(s: str) -> str:
    return s[::-1]
```
