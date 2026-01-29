# TypeScript Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```ts
function freq(nums: number[]): Map<number, number> {
  const m = new Map<number, number>();
  for (const x of nums) m.set(x, (m.get(x) ?? 0) + 1);
  return m;
}
```
