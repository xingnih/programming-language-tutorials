# Java DS Cheatsheet（LeetCode 常用）

## HashMap / HashSet
```java
import java.util.*;
Map<Integer, Integer> m = new HashMap<>();
m.put(1, 2);
int v = m.getOrDefault(1, 0);

Set<Integer> set = new HashSet<>();
set.add(3);
boolean ok = set.contains(3);
```

## Stack / Queue（用 ArrayDeque）
```java
Deque<Integer> st = new ArrayDeque<>();
st.push(10);
int x = st.pop();

Deque<Integer> q = new ArrayDeque<>();
q.addLast(1);
int y = q.removeFirst();
```
