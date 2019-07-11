# Introduction to Algorithms

《Introduction to Algorithms》(第三版), [美] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivert, Clifford Stein著, 殷建平, 徐云, 王刚, 刘晓光, 苏明, 邹恒明, 王宏志 译, 机械工业出版社, 2013年

[TOC]

------

## 2

### 2.1 插入排序

``` pseudocode
for j = 2 to A.length
    key = A[j]
    // Insert A[j] into the sorted sequence A[i..j-1]
    i = j-1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key
```



### 2.2 循环不变式

#### Floyd–Hoare logic

$$
\frac
{\{C \land I\} \; \mathrm {body} \; \{ I \}}
{\{ I \} \; \mathbf {while} \; (C) \; \mathrm {body} \; \{ \lnot C \land I \}}
$$

## 3

### 3.1 渐进符号 **$o, \; \omega , \; O \; ,  \Theta , \; \Omega$**

$$
O(g(n)) = \{ f(n): \exists c,n_0 > 0 \;
s.t. \forall n \ge n_0, 0 \le f(n) \le cg(n) \}
$$

$$
\Theta (g(n)) = \{ f(n): \exists c_1,c_2,n_0 > 0 \;
s.t. \forall n \ge n_0, c_1 g(n) \le f(n) \le c_2 g(n) \}
$$

$$
\Omega (g(n)) = \{ f(n): \exists c,n_0 > 0 \;
s.t. \forall n \ge n_0,  cg(n) \le f(n) \}
$$

### 3.2 函数增长

#### \* 3.2.1 自然对数

$$
e^x = \sum_{i=0}^ \infty \frac {x^i}{i!}, \;
\ln (1+x) = \sum_{i=0}^ \infty (-1)^{i-1} \frac {x^i}{i}, \;
\frac {x}{1+x} \le \ln (1+x) \le x
$$

#### 3.2.2 常见结论

$$
\lg ^b n = o(n^a)(a \gt 1, b>0); \;
n^a = o(n^b)(a \gt 1, b>0)
$$

#### \* 3.2.3 Stirling 近似

$$
n! = \sqrt {2 \pi n} (\frac n e)^n(1+ \Theta (\frac 1 n))
$$

$$
\therefore \lg(n!)
= \lg (\sqrt {2 \pi n}(1+ \Theta (\frac 1 n)) +  n (\lg n - \lg e)
= \Theta (n \lg n)
$$

#### 3.2.4 Fibonacci

$$
\phi = \frac {1 + \sqrt 5} 2, \;
\hat \phi = \frac {1 - \sqrt 5} 2 , \;
F_i = \frac {\phi ^ i - \hat \phi ^ i}{\sqrt 5}
$$

$$
\because F_i \in \mathbb Z, \;
\frac {|\hat \phi ^ i|}{\sqrt 5} \lt \frac 1 2
$$

$$
\therefore F_i = \bigg \lfloor \frac {\phi ^i}{\sqrt 5} + \frac 1 2 \bigg \rfloor = \Theta (a^n)
$$

#### 3.2.5 习题

$$
\lg ^* x = \min \{ i \ge 0: \lg ^{(i)} n \le 1\}
$$

*e.g.*
$$
\lg ^* 1 = 0, \;
\lg ^* 2 = 1, \;
\lg ^* 4 = 2, \;
\lg ^* 16 = 3, \;
\lg ^* 65536 = 4, \;
\lg ^* 2^{65536} = 5, \;
\ldots
$$

##### 3-2-4

$$
\forall k \in \mathbb Z^+, \exists \big \lceil \lg n \big \rceil ! = \omega (n^k)
$$

$$
\big \lceil \lg \lg n \big \rceil ! = O (n)
$$

##### 3-2-5

$$
\Theta \big (\lg (\lg ^ * n) \big ) \subset \omega \big (\lg ^ * (\lg n) \big )
$$

$$
\forall k \in \mathbb N, 2^{2^{(k)}} \lt n \le 2^{2^{(k + 1)}}, \;
f(n) = \lg ^ * (\lg n) - \lg (\lg ^ * n) = k - \lg (k + 1)
$$

##### 3-3

$$
O \binom{1}{n^{\frac {1}{\lg n}}} \supset \\
O(\lg \lg^*n) \supset O \binom{\lg^*\lg n}{\lg^*n} \supset O(2^{\lg^*n}) \supset \\
O(\ln \ln n) \supset O(\sqrt{\lg n}) \supset O(\lg n)
\supset O(\lg^2 n) \supset O(2^\sqrt{2 \lg n}) \supset \\
O \binom{n^ \frac 1 2}{{{\sqrt 2}^{\lg n}}} \supset O \binom{n}{{2^{\lg n}}} \supset 
O \binom{n \lg n}{\lg n!} \supset O \binom{n^2}{4^{\lg n}} \supset O (n^3) \supset \\
\underline{O((\lg n)!) \supset \binom{{\lg n}^{\lg n}}{n^{\lg \lg n}}} \supset \\
O \big ((\frac {3}{2})^n \big ) \supset O(2^n) \supset O(n2^n) \supset O(e^n) \supset \\
O(n!) \supset O \big ((n+1)! \big ) \supset O(2^{2^n}) \supset O(2^{2^{n+1}})
$$





