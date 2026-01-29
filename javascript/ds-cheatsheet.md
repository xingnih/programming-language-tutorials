# JavaScript DS Cheatsheet（LeetCode 常用）

## Map / Set
```js
const m = new Map();
m.set(1, 2);
const v = m.get(1) ?? 0;

const set = new Set();
set.add(3);
const ok = set.has(3);
```

## stack / queue
```js
const st = [];
st.push(10);
const x = st.pop();

// queue（小資料 OK）
const q = [];
q.push(1);
const y = q.shift();
```

## sort
```js
nums.sort((a,b)=>a-b);
points.sort((p,q)=> (p[0]-q[0]) || (p[1]-q[1]));
```
