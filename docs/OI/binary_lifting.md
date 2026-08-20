---
tittle: 倍增
comments: true
tags:
  - OI
  - 数学
---

!!! note "查看更多相关内容"
	- [OI Wiki](https://oi-wiki.org/basic/binary-lifting/)

倍增思想的本质是**二进制拆分**，通过预先计算以 2 的幂次为步长/长度的信息，将原本线性复杂度的计算优化为对数级别：

- **原理**：

  任意整数都可以拆分为若干个 2 的幂次之和（如 $7=2^0+2^1+2^2$），因此仅需要预处理 $O(log_2n)$ 个区间就能覆盖任意目标范围

- **特性**：空间换时间

  通过预处理提前存储结果，查询时直接组合复用，避免重复计算

```cpp
// 迭代实现快速幂，倍增
int qpow(int a, int n, int p){
	int res=1;
	long long t=a;
	while(n){
		if(n&1) res=res*t%p;
		t=t*t%p;
		n>>=1;
	}
	return res;
}
```

