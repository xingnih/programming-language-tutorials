# Rust DS Cheatsheet（LeetCode 常用）

## HashMap / HashSet
```rs
use std::collections::{HashMap, HashSet};
let mut m: HashMap<i32, i32> = HashMap::new();
m.insert(1, 2);
let v = *m.get(&1).unwrap_or(&0);

let mut set: HashSet<i32> = HashSet::new();
set.insert(3);
let ok = set.contains(&3);
```
