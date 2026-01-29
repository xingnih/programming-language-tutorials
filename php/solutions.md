# PHP Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```php
function freq($nums) {
  $m = [];
  foreach ($nums as $x) $m[$x] = ($m[$x] ?? 0) + 1;
  return $m;
}
```
