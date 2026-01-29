# Java Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```java
import java.util.*;
Map<Integer,Integer> freq(int[] nums) {
  Map<Integer,Integer> m = new HashMap<>();
  for (int x: nums) m.put(x, m.getOrDefault(x, 0) + 1);
  return m;
}
```
