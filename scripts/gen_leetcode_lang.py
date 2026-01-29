#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LANGS = {
  # folder: (title, extensions note)
  "python": "Python",
  "javascript": "JavaScript",
  "typescript": "TypeScript",
  "java": "Java",
  "cpp": "C++",
  "c": "C",
  "csharp": "C#",
  "go": "Go",
  "kotlin": "Kotlin",
  "swift": "Swift",
  "rust": "Rust",
  "php": "PHP",
  "ruby": "Ruby",
  "scala": "Scala",
}

COMMON_INTRO = """目標：讓你用這個語言在 LeetCode 上『寫得出來、交得上去』。
不講演算法，只講：語法、常用容器、題目函式模板、常見操作。
"""

TEMPLATES = {
  "python": {
    "template": """class Solution:\n    def twoSum(self, nums: list[int], target: int) -> list[int]:\n        return []\n""",
    "basics": """## if / for / function\n```py\nx = 3\nif x > 0:\n    pass\nfor i, v in enumerate(nums):\n    pass\n\ndef add(a: int, b: int) -> int:\n    return a + b\n```\n\n## list / string 常用\n```py\nlen(nums)\nnums.append(5)\nnums[1:4]\n"a,b".split(",")\n"".join(["a","b"])\n```\n\n## debug\n```py\nprint(nums)\n```\n""",
    "ds": """## dict / set\n```py\nm = {}\nm[1] = 2\nv = m.get(1, 0)\n\nseen = set()\nseen.add(3)\nok = 3 in seen\n```\n\n## stack / queue\n```py\nst = []\nst.append(10)\nx = st.pop()\n\nfrom collections import deque\nq = deque()\nq.append(1)\ny = q.popleft()\n```\n\n## sort\n```py\nnums.sort()\npoints.sort(key=lambda p: (p[0], p[1]))\n```\n""",
    "solutions": """## 1) 計次\n```py\nfrom collections import Counter\n\ndef freq(nums: list[int]) -> dict[int,int]:\n    return dict(Counter(nums))\n```\n\n## 2) 去重（保留順序）\n```py\ndef dedup(nums: list[int]) -> list[int]:\n    seen = set()\n    out = []\n    for x in nums:\n        if x in seen: continue\n        seen.add(x)\n        out.append(x)\n    return out\n```\n\n## 3) 反轉字串\n```py\ndef rev(s: str) -> str:\n    return s[::-1]\n```\n""",
  },

  "javascript": {
    "template": """/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number[]}\n */\nvar twoSum = function(nums, target) {\n  return [];\n};\n""",
    "basics": """## if / for / function\n```js\nlet x = 3;\nif (x > 0) {}\nfor (let i = 0; i < nums.length; i++) {\n  const v = nums[i];\n}\nfor (const v of nums) {}\n```\n\n## array / string 常用\n```js\nnums.push(5);\nnums.slice(1, 4);\n"a,b".split(",");\n["a","b"].join("");\n```\n""",
    "ds": """## Map / Set\n```js\nconst m = new Map();\nm.set(1, 2);\nconst v = m.get(1) ?? 0;\n\nconst set = new Set();\nset.add(3);\nconst ok = set.has(3);\n```\n\n## stack / queue\n```js\nconst st = [];\nst.push(10);\nconst x = st.pop();\n\n// queue（小資料 OK）\nconst q = [];\nq.push(1);\nconst y = q.shift();\n```\n\n## sort\n```js\nnums.sort((a,b)=>a-b);\npoints.sort((p,q)=> (p[0]-q[0]) || (p[1]-q[1]));\n```\n""",
    "solutions": """## 1) 計次\n```js\nfunction freq(nums) {\n  const m = new Map();\n  for (const x of nums) m.set(x, (m.get(x) ?? 0) + 1);\n  return m;\n}\n```\n\n## 2) 去重（保留順序）\n```js\nfunction dedup(nums) {\n  const seen = new Set();\n  const out = [];\n  for (const x of nums) {\n    if (seen.has(x)) continue;\n    seen.add(x);\n    out.push(x);\n  }\n  return out;\n}\n```\n\n## 3) 反轉字串\n```js\nfunction rev(s) {\n  return [...s].reverse().join('');\n}\n```\n""",
  },

  "typescript": {
    "template": """function twoSum(nums: number[], target: number): number[] {\n  return [];\n}\n""",
    "basics": """## if / for / function\n```ts\nlet x = 3;\nif (x > 0) {}\nfor (let i = 0; i < nums.length; i++) {\n  const v = nums[i];\n}\nfor (const v of nums) {}\n```\n""",
    "ds": """## Map / Set\n```ts\nconst m = new Map<number, number>();\nm.set(1, 2);\nconst v = m.get(1) ?? 0;\n\nconst set = new Set<number>();\nset.add(3);\nconst ok = set.has(3);\n```\n""",
    "solutions": """## 1) 計次\n```ts\nfunction freq(nums: number[]): Map<number, number> {\n  const m = new Map<number, number>();\n  for (const x of nums) m.set(x, (m.get(x) ?? 0) + 1);\n  return m;\n}\n```\n""",
  },

  "java": {
    "template": """class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        return new int[]{};\n    }\n}\n""",
    "basics": """## if / for\n```java\nint x = 3;\nif (x > 0) {}\nfor (int i = 0; i < nums.length; i++) {\n  int v = nums[i];\n}\nfor (int v : nums) {}\n```\n\n## String\n```java\nString s = \"a,b\";\nString[] parts = s.split(\",\");\nint n = s.length();\n```\n""",
    "ds": """## HashMap / HashSet\n```java\nimport java.util.*;\nMap<Integer, Integer> m = new HashMap<>();\nm.put(1, 2);\nint v = m.getOrDefault(1, 0);\n\nSet<Integer> set = new HashSet<>();\nset.add(3);\nboolean ok = set.contains(3);\n```\n\n## Stack / Queue（用 ArrayDeque）\n```java\nDeque<Integer> st = new ArrayDeque<>();\nst.push(10);\nint x = st.pop();\n\nDeque<Integer> q = new ArrayDeque<>();\nq.addLast(1);\nint y = q.removeFirst();\n```\n""",
    "solutions": """## 1) 計次\n```java\nimport java.util.*;\nMap<Integer,Integer> freq(int[] nums) {\n  Map<Integer,Integer> m = new HashMap<>();\n  for (int x: nums) m.put(x, m.getOrDefault(x, 0) + 1);\n  return m;\n}\n```\n""",
  },

  "cpp": {
    "template": """#include <bits/stdc++.h>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        return {};\n    }\n};\n""",
    "basics": """## if / for\n```cpp\nint x = 3;\nif (x > 0) {}\nfor (int i = 0; i < (int)nums.size(); i++) {\n  int v = nums[i];\n}\nfor (int v : nums) {}\n```\n""",
    "ds": """## unordered_map / unordered_set\n```cpp\nunordered_map<int,int> m;\nm[1] = 2;\nint v = m.count(1) ? m[1] : 0;\n\nunordered_set<int> set;\nset.insert(3);\nbool ok = set.count(3);\n```\n\n## stack / queue\n```cpp\nvector<int> st;\nst.push_back(10);\nint x = st.back(); st.pop_back();\n\ndeque<int> q;\nq.push_back(1);\nint y = q.front(); q.pop_front();\n```\n""",
    "solutions": """## 1) 計次\n```cpp\nunordered_map<int,int> freq(const vector<int>& nums){\n  unordered_map<int,int> m;\n  for(int x: nums) m[x]++;\n  return m;\n}\n```\n""",
  },

  "c": {
    "template": """/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* twoSum(int* nums, int numsSize, int target, int* returnSize){\n    *returnSize = 0;\n    return NULL;\n}\n""",
    "basics": """## if / for\n```c\nint x = 3;\nif (x > 0) { }\nfor (int i = 0; i < n; i++) { }\n```\n\n## string\n```c\n#include <string.h>\nint n = (int)strlen(s);\n```\n""",
    "ds": """C 沒有內建 HashMap/Set/Queue。\n\n- LeetCode 常見：自己寫 hash table（struct + open addressing）\n- 或用排序後再處理\n\n這份速成先專注在語法與陣列/字串操作。\n""",
    "solutions": """## 3) 反轉字串（就地）\n```c\n#include <string.h>\nvoid reverse(char* s) {\n  int n = (int)strlen(s);\n  for (int i=0, j=n-1; i<j; i++, j--) {\n    char t = s[i];\n    s[i] = s[j];\n    s[j] = t;\n  }\n}\n```\n""",
  },

  "csharp": {
    "template": """public class Solution {\n    public int[] TwoSum(int[] nums, int target) {\n        return new int[]{};\n    }\n}\n""",
    "basics": """## if / for\n```csharp\nif (x > 0) {}\nfor (int i=0; i<nums.Length; i++) {\n  int v = nums[i];\n}\nforeach (var v in nums) {}\n```\n""",
    "ds": """## Dictionary / HashSet\n```csharp\nvar dict = new Dictionary<int,int>();\ndict[1] = 2;\nvar v = dict.GetValueOrDefault(1, 0);\n\nvar set = new HashSet<int>();\nset.Add(3);\nvar ok = set.Contains(3);\n```\n\n## Stack / Queue\n```csharp\nvar st = new Stack<int>();\nst.Push(10);\nvar x = st.Pop();\n\nvar q = new Queue<int>();\nq.Enqueue(1);\nvar y = q.Dequeue();\n```\n""",
    "solutions": """## 1) 計次\n```csharp\nDictionary<int,int> Freq(int[] nums) {\n  var m = new Dictionary<int,int>();\n  foreach (var x in nums) m[x] = m.GetValueOrDefault(x, 0) + 1;\n  return m;\n}\n```\n""",
  },

  "go": {
    "template": """func twoSum(nums []int, target int) []int {\n    return nil\n}\n""",
    "basics": """## if / for / func\n```go\nif x > 0 { }\nfor i := 0; i < len(nums); i++ {\n    v := nums[i]\n    _ = v\n}\nfor _, v := range nums {\n    _ = v\n}\nfunc add(a, b int) int { return a + b }\n```\n""",
    "ds": """## map / set\n```go\nm := map[int]int{}\nm[1] = 2\nv, ok := m[1]\n_ = v; _ = ok\n\nset := map[int]struct{}{}\nset[3] = struct{}{}\n_, ok = set[3]\n```\n\n## stack (slice)\n```go\nst := []int{}\nst = append(st, 10)\nx := st[len(st)-1]\nst = st[:len(st)-1]\n_ = x\n```\n""",
    "solutions": """## 1) 計次\n```go\nfunc freq(nums []int) map[int]int {\n  m := map[int]int{}\n  for _, x := range nums { m[x]++ }\n  return m\n}\n```\n""",
  },

  "kotlin": {
    "template": """class Solution {\n    fun twoSum(nums: IntArray, target: Int): IntArray {\n        return intArrayOf()\n    }\n}\n""",
    "basics": """## if / for / fun\n```kt\nif (x > 0) { }\nfor (i in nums.indices) {\n  val v = nums[i]\n}\nfor (v in nums) { }\nfun add(a: Int, b: Int): Int = a + b\n```\n""",
    "ds": """## HashMap / HashSet\n```kt\nval m = HashMap<Int, Int>()\nm[1] = 2\nval v = m[1] ?: 0\n\nval set = HashSet<Int>()\nset.add(3)\nval ok = set.contains(3)\n```\n""",
    "solutions": """## 1) 計次\n```kt\nfun freq(nums: IntArray): HashMap<Int, Int> {\n  val m = HashMap<Int, Int>()\n  for (x in nums) m[x] = (m[x] ?: 0) + 1\n  return m\n}\n```\n""",
  },

  "swift": {
    "template": """class Solution {\n    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {\n        return []\n    }\n}\n""",
    "basics": """## if / for\n```swift\nif x > 0 { }\nfor i in 0..<nums.count {\n  let v = nums[i]\n}\nfor v in nums { }\n```\n\n## String（刷題常轉 Array）\n```swift\nlet chars = Array(s)\n```\n""",
    "ds": """## Dictionary / Set\n```swift\nvar m: [Int:Int] = [:]\nm[1] = 2\nlet v = m[1] ?? 0\n\nvar set = Set<Int>()\nset.insert(3)\nlet ok = set.contains(3)\n```\n""",
    "solutions": """## 1) 計次\n```swift\nfunc freq(_ nums: [Int]) -> [Int:Int] {\n  var m: [Int:Int] = [:]\n  for x in nums { m[x, default: 0] += 1 }\n  return m\n}\n```\n""",
  },

  "rust": {
    "template": """impl Solution {\n    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {\n        vec![]\n    }\n}\n""",
    "basics": """## if / for / fn\n```rs\nlet x: i32 = 3;\nif x > 0 { }\nfor &v in nums.iter() {\n    let _ = v;\n}\nfn add(a: i32, b: i32) -> i32 { a + b }\n```\n""",
    "ds": """## HashMap / HashSet\n```rs\nuse std::collections::{HashMap, HashSet};\nlet mut m: HashMap<i32, i32> = HashMap::new();\nm.insert(1, 2);\nlet v = *m.get(&1).unwrap_or(&0);\n\nlet mut set: HashSet<i32> = HashSet::new();\nset.insert(3);\nlet ok = set.contains(&3);\n```\n""",
    "solutions": """## 1) 計次\n```rs\nuse std::collections::HashMap;\nfn freq(nums: Vec<i32>) -> HashMap<i32,i32> {\n  let mut m = HashMap::new();\n  for x in nums {\n    *m.entry(x).or_insert(0) += 1;\n  }\n  m\n}\n```\n""",
  },

  "php": {
    "template": """class Solution {\n    /**\n     * @param Integer[] $nums\n     * @param Integer $target\n     * @return Integer[]\n     */\n    function twoSum($nums, $target) {\n        return [];\n    }\n}\n""",
    "basics": """## if / for / foreach\n```php\nif ($x > 0) { }\nfor ($i=0; $i<count($nums); $i++) {\n  $v = $nums[$i];\n}\nforeach ($nums as $v) { }\n```\n""",
    "ds": """## associative array 當 map\n```php\n$m = [];\n$m[1] = 2;\n$v = $m[1] ?? 0;\n```\n""",
    "solutions": """## 1) 計次\n```php\nfunction freq($nums) {\n  $m = [];\n  foreach ($nums as $x) $m[$x] = ($m[$x] ?? 0) + 1;\n  return $m;\n}\n```\n""",
  },

  "ruby": {
    "template": """# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer[]}\ndef two_sum(nums, target)\n  []\nend\n""",
    "basics": """## each / each_with_index / def\n```rb\nnums.each_with_index do |v, i|\nend\n\ndef add(a, b)\n  a + b\nend\n```\n""",
    "ds": """## Hash / Set\n```rb\nm = Hash.new(0)\nm[1] += 1\n\nrequire 'set'\nset = Set.new\nset.add(3)\n```\n""",
    "solutions": """## 1) 計次\n```rb\ndef freq(nums)\n  m = Hash.new(0)\n  nums.each { |x| m[x] += 1 }\n  m\nend\n```\n""",
  },

  "scala": {
    "template": """object Solution {\n  def twoSum(nums: Array[Int], target: Int): Array[Int] = {\n    Array()\n  }\n}\n""",
    "basics": """## if / for\n```scala\nval x = 3\nif (x > 0) { }\nfor (i <- nums.indices) {\n  val v = nums(i)\n}\n```\n""",
    "ds": """## mutable HashMap / HashSet\n```scala\nimport scala.collection.mutable\nval m = mutable.HashMap[Int, Int]()\nm.update(1, 2)\nval v = m.getOrElse(1, 0)\n\nval set = mutable.HashSet[Int]()\nset.add(3)\nval ok = set.contains(3)\n```\n""",
    "solutions": """## 1) 計次\n```scala\nimport scala.collection.mutable\n\ndef freq(nums: Array[Int]): mutable.HashMap[Int, Int] = {\n  val m = mutable.HashMap[Int, Int]()\n  nums.foreach(x => m.update(x, m.getOrElse(x, 0) + 1))\n  m\n}\n```\n""",
  },
}


def write_lang(folder: str, name: str):
  p = ROOT / folder
  p.mkdir(parents=True, exist_ok=True)

  tmpl = TEMPLATES.get(folder, {})
  template = tmpl.get("template", "")
  map_snip = tmpl.get("map", "")

  (p / "README.md").write_text(
    f"# {name} for LeetCode — 語言速成（不講演算法）\n\n"
    + COMMON_INTRO
    + "\n## 檔案\n- `basics.md`\n- `ds-cheatsheet.md`\n- `practice.md`\n\n"
    + "## LeetCode 函式模板（常見）\n\n```\n" + template + "```\n",
    encoding="utf-8",
  )

  # basics
  basics = tmpl.get("basics", "")
  (p / "basics.md").write_text(
    f"# {name} Basics（LeetCode 必用）\n\n"
    + "這份只收：你刷題會一直用到的語法（不講演算法）。\n\n"
    + (basics or "(TODO: add snippets)\n"),
    encoding="utf-8",
  )

  # ds cheatsheet
  ds = tmpl.get("ds", "")
  (p / "ds-cheatsheet.md").write_text(
    f"# {name} DS Cheatsheet（LeetCode 常用）\n\n"
    + (ds or ("## HashMap / Dictionary\n\n```\n" + (map_snip or "// TODO") + "```\n")),
    encoding="utf-8",
  )

  # practice
  (p / "practice.md").write_text(
    f"# {name} Practice（練寫法）\n\n"
    "請用這份語言把下面幾個小題寫出來（不用管最優解）：\n\n"
    "1. 計次：輸入整數陣列，回傳 `value -> count` 的 map\n"
    "2. 去重：回傳去重後的陣列（保留出現順序）\n"
    "3. 反轉字串\n"
    "4. 排序 2D（如果語言方便）\n",
    encoding="utf-8",
  )

  # solutions (reference)
  sol = tmpl.get("solutions", "")
  (p / "solutions.md").write_text(
    f"# {name} Solutions（參考解 / 思路）\n\n"
    "下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。\n\n"
    + (sol or "(TODO: add solutions)\n"),
    encoding="utf-8",
  )


def main():
  for folder, name in LANGS.items():
    write_lang(folder, name)


if __name__ == "__main__":
  main()
