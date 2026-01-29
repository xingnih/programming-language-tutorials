# Swift Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```swift
func freq(_ nums: [Int]) -> [Int:Int] {
  var m: [Int:Int] = [:]
  for x in nums { m[x, default: 0] += 1 }
  return m
}
```
