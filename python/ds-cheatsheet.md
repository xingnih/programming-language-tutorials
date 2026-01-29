# Python DS Cheatsheet（LeetCode 常用）

## dict / set
```py
m = {}
m[1] = 2
v = m.get(1, 0)

seen = set()
seen.add(3)
ok = 3 in seen
```

## stack / queue
```py
st = []
st.append(10)
x = st.pop()

from collections import deque
q = deque()
q.append(1)
y = q.popleft()
```

## sort
```py
nums.sort()
points.sort(key=lambda p: (p[0], p[1]))
```
