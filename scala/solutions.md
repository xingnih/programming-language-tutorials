# Scala Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 1) 計次
```scala
import scala.collection.mutable

def freq(nums: Array[Int]): mutable.HashMap[Int, Int] = {
  val m = mutable.HashMap[Int, Int]()
  nums.foreach(x => m.update(x, m.getOrElse(x, 0) + 1))
  m
}
```
