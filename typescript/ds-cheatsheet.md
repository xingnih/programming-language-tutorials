# TypeScript DS Cheatsheet（LeetCode 常用）

## Map / Set
```ts
const m = new Map<number, number>();
m.set(1, 2);
const v = m.get(1) ?? 0;

const set = new Set<number>();
set.add(3);
const ok = set.has(3);
```
