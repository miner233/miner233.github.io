---
comments: true
tittle: ST 表
tags:
  - OI
  - 数据结构
---
# ST 表

ST 表是基于倍增思想实现的稀疏表，用于快速查询区间的某个特性（最大值、最小值等），查询时间复杂度 `O(1)`，但不支持修改。

```cpp
// 洛谷 P1886
#include <bits/stdc++.h>
using namespace std;
signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> a(n+1, 0), lg(n+1, 0);
    for(int i=1; i<=n; i++) cin >> a[i];
    for(int i=2; i<=n; i++) lg[i]=lg[i>>1]+1;
    int max_log = lg[n];
    vector<vector<int>> st(max_log+1, vector<int>(n+1));   // ST 表
    for(int j=1; j<=n; j++) st[0][j]=a[j];
    for(int i=1; i<=max_log; i++){
        int len=1<<(i-1);
        for(int j=1; j+(1<<i)-1<=n; j++)
            st[i][j]=min(st[i-1][j], st[i-1][j+len]);
    }
    int s=lg[k];
    for(int j=1; j+k-1<=n; j++){
        int l=j, r=j+k-1;
        int ans=min(st[s][l], st[s][r-(1<<s)+1]);
        cout << ans << " ";
    }
    cout << endl;
    for(int i=1; i<=max_log; i++){
        int len=1<<(i-1);
        for(int j=1; j+(1<<i)-1<=n; j++)
            st[i][j]=max(st[i-1][j], st[i-1][j+len]);
    }
    for(int j=1; j+k-1<=n; j++){
        int l=j, r=j+k-1;
        int ans=max(st[s][l], st[s][r-(1<<s)+1]);
        cout << ans << " ";
    }
    return 0;
}
```