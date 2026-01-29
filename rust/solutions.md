# Rust Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```rs
use std::collections::HashMap;
fn freq(nums: Vec<i32>) -> HashMap<i32,i32> {
  let mut m = HashMap::new();
  for x in nums {
    *m.entry(x).or_insert(0) += 1;
  }
  m
}
```
