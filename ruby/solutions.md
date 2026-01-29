# Ruby Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```rb
def freq(nums)
  m = Hash.new(0)
  nums.each { |x| m[x] += 1 }
  m
end
```
