# C# DS Cheatsheet（LeetCode 常用）

## Dictionary / HashSet
```csharp
var dict = new Dictionary<int,int>();
dict[1] = 2;
var v = dict.GetValueOrDefault(1, 0);

var set = new HashSet<int>();
set.Add(3);
var ok = set.Contains(3);
```

## Stack / Queue
```csharp
var st = new Stack<int>();
st.Push(10);
var x = st.Pop();

var q = new Queue<int>();
q.Enqueue(1);
var y = q.Dequeue();
```
