# C Solutions（參考解 / 思路）

下面是 `practice.md` 的參考寫法（偏清楚、可直接貼上）。

## 3) 反轉字串（就地）
```c
#include <string.h>
void reverse(char* s) {
  int n = (int)strlen(s);
  for (int i=0, j=n-1; i<j; i++, j--) {
    char t = s[i];
    s[i] = s[j];
    s[j] = t;
  }
}
```
