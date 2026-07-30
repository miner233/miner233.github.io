---
tags:
  - 图论
  - OI
---
## 定义

*生成树* 是指连通无向图的生成子图。

*最小生成树（MST）*是指无向连通图的边权最小生成树。

## kruskal 算法
利用边权求最小生成树。

`e[i]` 存第 `i` 条边的起点、终点和边权，`fa[x]` 存 `x` 点的父结点。

实现思路：

1. 初始化并查集，把 `n` 个点放在 `n` 个独立的集合内。
2. 将所有的边按边权从小到大排序（贪心思想）。
3. 按顺序枚举每一条边，如果这条边连接的两个点不在同一集合，就把这条边加入最小生成树，并**合并**这两个集合；如果这条边连接的两个点在同一集合，就跳过
4. 重复执行步骤 3，直到选取了 `n-1` 条边为止。

```cpp
sturct edge{
	int u, v, w;
	bool operatorr<(cosnt edge &t)const{return w<t.w;}
}e[N];
int fa[N], ans, cnt;
int find(int x){
	if(fa[x]==x) return x;
	return fa[x]=find(fa[x]);
}
bool kruskal(){
    sort(e, e+m);
    for(int i=1; i<=n; i++) fa[i]=i;
    for(int i=0; i<m; i++){
        int x=find(e[i].u);
        int y=find(e[i].v);
        if(x!=y){
            fa[x]=y;
            ans+=e[i].w;
            cnt++;
        }
    }
    return cnt==n-1;
}
```