---
comments: true
tags:
  - 数据结构
  - OI
---

!!! note "查看更多相关内容"
    - [OI Wiki](https://oi-wiki.org/ds/dsu/)

## 定义

并查集（Disjoint Set Union，DSU）是一种用于管理**元素所属集合**的数据结构，实现为一片**森林**。

支持查找（Find，查找元素所属集合）和合并（Unite，将两个元素所在的集合合并为一个集合）。

对于非整数，可以使用哈希表将元素映射到整数。

并查集通常用数组实现。

对于并查集数组 `dsu[]`，`dsu[i]` 表示元素 `i` 所在集合的根（存储下标），若该元素就是其所在集合的根，则存储它自己的下标。

## 操作

并查集支持以下三种操作：`make_set` 建集、`find` 查找和 `union` 合并。

### `make_set` 建集

初始每个元素都有一个独立的集合，这个集合只有其一个元素，且根就是其本身。

实现思路：创建一个 `root[]` 数组，表示一个并查集，将每个元素的根都指向它本身。

```cpp
void make_set(){   // 建集
    root.assign(n, 0);
    for(int i=0; i<n; i++) root[i]=i;
}
```

### `union` 合并

将两个元素所在的集合合并（前提是这两个元素不在一个集合内）。

实现思路：`union(x, y)`，将 x 所属集合合并到 y 所属集合内，y 做新的根。

**优化——按秩合并（启发式合并）** ：把小集合的根指向大集合的根。

=== "朴素版"
    ```cpp
    bool union(int x, int y){   // 将 x 所属集合合并到 y 所属集合内，y 做新的根
        int rootx=find(x), rooty=find(y);
        if(rootx==rooty) return false;
        root[find(x)]=find(y)
        root[rootx] = rooty;
        return true;
    }
    ```
    也可以这么写：
    ```
    void union(int x, int y){
	    root[find(x)]=find(y)
    }
    ```

=== "按秩合并优化"
    ```cpp
    // 按秩合并
    vector<int> siz(n, 1);
    void union(int x, int y){
        int rootx=find(x), rooty=find(y);
        if(x==y) return;
        if(siz[x]>siz[y]) swap(x, y);
        root[x]=y;
        siz[y]+=siz[x];
    ```


### `find` 查找

查找元素所属集合。

通常用于判断两个元素是否在同一集合内。

**优化——路径压缩**：在返回的路上，顺带修改各结点的父结点为根。

=== "递归实现"
    ```cpp
    // 递归实现（朴素版）
    int find(int x){
        if(fa[x]==x) return x;
        return find(fa[x]);
    }
    ```

=== "递归实现（路径压缩版）"
    ```cpp
    // 递归实现
    int find(int x){
        if(fa[x]==x) return x;
        return a[x]=find(fa[x]);   // 路径压缩
    }
    ```

=== "递推实现"
    ```cpp
    int find(int x){
        int i=x;
        while(i!=root[i]) i=root[i];
        return i;
    }
    ```

## 实现
以下是一个封装好的 DSU 模板。
```cpp
class dsu{
    private:
        int n, m;   // 总结点个数，当前连通块数量
        vector<int> fa, siz;
        dsu(int a, int b){
            n=a; m=b;
            fa.assign(n+5, -1);
            siz.assign(n+5, 1);
            for(int i=1; i<=n; i++) fa[i]=i;
        }
        bool dsu_find(int x){
            return (fa[x]==x?x:fa[x]=dsu_find(fa[x]));
        }
        bool dsu_link(int a, int b){   // 将 a 所在的集合合并到 b 所在的集合
            int fa1=dsu_find(a), fa2=dsu_find(b);
            if(fa1==fa2) return false;
            if(fa1>fa2) swap(fa1, fa2);
            siz[fa2]+=siz[fa1];
            fa[fa1]=fa[fa2];
            m--;
            return true;
        }
    public:
        int size(){   // 获取连通块个数
            return m;
        }
        bool find(int x){
            return dsu_find(x);
        }
        bool link(int a, int b){
            return dsu_link(a, b);
        }
};
```