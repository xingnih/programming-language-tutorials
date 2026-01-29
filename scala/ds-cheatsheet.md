# Scala DS Cheatsheet（LeetCode 常用）

## mutable HashMap / HashSet
```scala
import scala.collection.mutable
val m = mutable.HashMap[Int, Int]()
m.update(1, 2)
val v = m.getOrElse(1, 0)

val set = mutable.HashSet[Int]()
set.add(3)
val ok = set.contains(3)
```
