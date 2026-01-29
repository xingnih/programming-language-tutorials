# Go DS Cheatsheet（LeetCode 常用）

## map / set
```go
m := map[int]int{}
m[1] = 2
v, ok := m[1]
_ = v; _ = ok

set := map[int]struct{}{}
set[3] = struct{}{}
_, ok = set[3]
```

## stack (slice)
```go
st := []int{}
st = append(st, 10)
x := st[len(st)-1]
st = st[:len(st)-1]
_ = x
```
