# JavaScript Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```js
function freq(nums) {
  const m = new Map();
  for (const x of nums) m.set(x, (m.get(x) ?? 0) + 1);
  return m;
}
```

## 2) 去重（保留順序）
```js
function dedup(nums) {
  const seen = new Set();
  const out = [];
  for (const x of nums) {
    if (seen.has(x)) continue;
    seen.add(x);
    out.push(x);
  }
  return out;
}
```

## 3) 反轉字串
```js
function rev(s) {
  return [...s].reverse().join('');
}
```
