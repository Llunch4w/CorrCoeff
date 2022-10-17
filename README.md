# Correlation Cofficient
> 统计学三大相关系数 **Pearson(皮尔逊)** , **Spearman(斯皮尔曼)** , **Kendall(肯德尔)** 计算方式

# Pearson系数
## 特征
- 用于量度两个变量 $X$ 和 $Y$ 之间的线性相关
- 取值范围为：$[-1, 1]$ , 1是总线性正相关，0是非线性相关性，-1是负线性相关。
- Person相关系数的一个关键数学特性在于它在两个变量的位置和尺度的单独变化下是不变的。也就是说，我们可以将 $X$ 变换为 $a+bX$ , 并将 $Y$ 变换为 $c+dY$ ，而不改变相关系数。

## 公式
$$
\rho_{X,Y} = \frac{conv(X, Y)}{\sigma_X \sigma_Y}
= \frac{E(X-\mu_X)E(Y-\mu_Y)}{\sigma_X \sigma_Y}
=\frac{E(XY)-E(X)E(Y)}{\sqrt{E(X^2)-E^2(X)}\sqrt{E(Y^2)-E^2(Y)}}
$$

## Code
```python
sigma = lambda n: len(n) * sum(map(lambda i: i**2, n)) - (sum(n) ** 2)
E_XY = len(x) * sum(map(lambda a: a[0] * a[1], zip(x, y)))
EX_EY = sum(x) * sum(y)
```

## 应用条件
- 适用于线性相关的情形
- 样本中的极端值对Pearson积差相关系数的影响极大
- 要求相应的变量呈双变量正态分布。双变量正态分布并非简单要求变量 $x$ 和 $y$ 各自服从正态分布，而是要求服从一个联合的双变量正态分布。


# Spearman秩相关系数
## 特征
- 秩，可以理解为一种顺序或者排序，秩相关系数就是根据原始数据的排序位置进行求解。
- 该方法对原始变量的分布不做要求，属于非参数统计方法。
- 取值范围为：$[-1, 1]$ ，当两个变量完全单调相关时，Spearman相关系数为 +1 或 -1。

## 公式
> 原始数据被转换为等级数据后，使用公式进行计算。

$$
\rho = \frac{\sum_i(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_i(x_i-\bar{x})^2\sum_i(y_i-\bar{y})^2}}
=1-\frac{6\sum d_i^2}{n(n^2-1)}, d_i = rank_X - rank_Y 
$$

## Code
```python
to_index = lambda n: map(lambda val: sorted(n).index(val)+1, n)
d = sum(map(lambda x, y: (x - y)**2, to_index(x), to_index(y)))
n = len(x)
res = 1.0 - 6.0 * d / float(n*(n**2 - 1.0))
```


# Kendall秩相关系数
## 特征
- 用于反映分类变量相关性的指标，适用于两个变量均为有序分类的情况。比如有多个分类等级取值的变量就是有序分类变量。
- 取值范围在 $[-1, 1]$ 之间，1表示两个随机变量拥有一致的等级相关性，-1表示随机变量拥有完全相反的等级相关性，0代表两个随机变量相互独立。

## 公式
> Kendall系数基于协同的思想。对于 $X$, $Y$ 的两对观察值 $X_i, Y_i$ 和 $X_j, Y_j$ ， 如果 $X_i < Y_i$ 且 $X_j < Y_j$ ， 则称这两对观察值是和谐的，否则就是不和谐的。

$$
\tau = \frac{(number\ of\ concordant\ pairs) - (number\ of\ discordant\ pairs)}{\frac{1}{2}n(n-1)}
$$

# 运行方式
```bash
sh script/run.sh
```