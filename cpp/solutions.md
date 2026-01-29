# C++ Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```cpp
unordered_map<int,int> freq(const vector<int>& nums){
  unordered_map<int,int> m;
  for(int x: nums) m[x]++;
  return m;
}
```
