# C# Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```csharp
Dictionary<int,int> Freq(int[] nums) {
  var m = new Dictionary<int,int>();
  foreach (var x in nums) m[x] = m.GetValueOrDefault(x, 0) + 1;
  return m;
}
```
