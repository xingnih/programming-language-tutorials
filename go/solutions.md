# Go Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```go
func freq(nums []int) map[int]int {
  m := map[int]int{}
  for _, x := range nums { m[x]++ }
  return m
}
```
