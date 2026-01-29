# C++ DS Cheatsheet（LeetCode 常用）

## unordered_map / unordered_set
```cpp
unordered_map<int,int> m;
m[1] = 2;
int v = m.count(1) ? m[1] : 0;

unordered_set<int> set;
set.insert(3);
bool ok = set.count(3);
```

## stack / queue
```cpp
vector<int> st;
st.push_back(10);
int x = st.back(); st.pop_back();

deque<int> q;
q.push_back(1);
int y = q.front(); q.pop_front();
```
