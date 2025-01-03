# The mHeight function of a permutation (intermediary result)

Truly challenging open problems in mathematics often require the development of new mathematical constructions (or even entire new areas of mathematics). This dataset represents a modest example of this. The mHeight function is a statistic associated with a permutation that relates to all $3412$-patterns in the permutation. It was developed and plays a crucial role in the proof by Gaetz and Gao \[1\] which resolved a long-standing conjecture of Billey and Postnikov \[2\] about the coefficients on Kazhdan-Lusztig polynomials (see our [Kazhdan-Lusztig polynomial dataset](https://github.com/pnnl/ML4AlgComb/tree/master/kl-polynomial_coefficients)) which carry important geometric information about certain spaces, Schubert varieties, that are of interest both to mathematicians and physicists. The task of predicting the mHeight function represents an interesting opportunity to understand whether a non-trivial intermediate step in an important proof can be learned by machine learning. 

Let $\sigma  = a_1 \ldots a_n \in S_n$ be a permutation containing at least one occurrence of a $3412$ pattern. Let $(a_i,a_j,a_k,a_\ell)$ be a $3412$ pattern so that $1 \leq i < j < k < \ell \leq n$ but $a_k < a_\ell < a_i < a_j$. The *height* of $(a_i,a_j,a_k,a_\ell)$ is $a_\ell - a_i$. The *mHeight* of $\sigma$ is then the minimum height over all $3412$ patterns in $\sigma$. 

## An Example



## Dataset 

Permutations of size $n$ labeled by their mHeight. We provide datasets for $n = 10,11,12$.

**Task:** Predict the mHeight of a permutation. 

The datasets can be found [here](https://drive.google.com/file/d/1NteiP494xpQ4KzR9dVUaDhNtUPnumeuX/view?usp=sharing)

### Permutations of size $9$

For $n = 9$, mHeight takes values 0, 1, 2, 3, 4, 5. 

| mHeight value  | 0 | 1 | 2 | 3 | 4 | 5 |  Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|----------|
| Train | 49,166 | 3,107 | 500 | 80 | 10 | 1 | |
| Test  | 12,243 | 813 | 142 | 16 | 2 | |

### Permutations of size $10$

For $n = 10$, mHeight takes values 0, 1, 2, 3, 4, 5, 6. 

| mHeight value  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|----------|
| Train | 352,428 | 17,934 | 3,140 | 524 | 75 | 10 | 1 | |
| Test  | 88,124 |  4,521 | 742 | 118 | 21 | 2 | 0 | |

Train data statistics
0: 352428
1: 17934
2: 3140
3: 524
4: 75
6: 1
5: 10

Test data statistics
0: 88124
2: 742
1: 4521
3: 118
4: 21
5: 2

## Small model performance

| Size | Logistic regression | MLP | Transformer | TODO | 
|----------|----------|-----------|------------|------------|
| $n= 9$ | $70.8\\%$ | $92.1\\% \pm 0.3\\%$ | $82.8\\% \pm 1.1\\%$| $0.0$ |
| $n= 10$ | $94.2\\%$ | $99.9\\% \pm 0.0\\%$ | $99.9\\% \pm 0.0\\%$| $0.0$ |

\[1\] Gaetz, Christian, and Yibo Gao. "On the minimal power of $ q $ in a Kazhdan-Lusztig polynomial." arXiv preprint arXiv:2303.13695 (2023).

\[2\] Billey, Sara, and Alexander Postnikov. "Smoothness of Schubert varieties via patterns in root subsystems." Advances in Applied Mathematics 34.3 (2005): 447-466.
