# The mHeight function of a permutation (intermediary result)

The mHeight function is a statistic associated with a permutation that relates to all $3412$-patterns in the permutation. It plays a crucial role in the proof by Gaetz and Gao \[1\] which resolved a long-standing conjecture of Billey and Postnikov \[2\] about the coefficients on Kazhdan-Lusztig polynomials which carry important geometric information about certain spaces, Schubert varieties, that are of interest both to mathematicians and physicists. The task of predicting the mHeight function thus represents an interesting opportunity to understand whether a non-trivial intermediate step in an important proof can be learned by machine learning. 

Let $\sigma  = a_1 \ldots a_n \in S_n$ be a permutation containing at least one occurrence of a $3412$ pattern. Let $(a_i,a_j,a_k,a_\ell)$ be a $3412$ pattern so that $1 \leq i < j < k < \ell \leq n$ but $a_k < a_\ell < a_i < a_j$. The *height* of $(a_i,a_j,a_k,a_\ell)$ is $a_\ell - a_i$. The *mHeight* of $\sigma$ is then the minimum height over all $3412$ patterns in $\sigma$. 

**Dataset:** Permutations of size $n$ labeled by their mHeight. We provide datasets for $n = 10,11,12$.

**Task:** Predict the mHeight of a permutation. 

The datasets can be found [here](https://drive.google.com/file/d/1NteiP494xpQ4KzR9dVUaDhNtUPnumeuX/view?usp=sharing)

## Small model performance

| Size | Logistic regression | MLP | Transformer | TODO | 
|----------|----------|-----------|------------|------------|
| $n= 10$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 11$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 12$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |

\[1\] Gaetz, Christian, and Yibo Gao. "On the minimal power of $ q $ in a Kazhdan-Lusztig polynomial." arXiv preprint arXiv:2303.13695 (2023).

\[2\] Billey, Sara, and Alexander Postnikov. "Smoothness of Schubert varieties via patterns in root subsystems." Advances in Applied Mathematics 34.3 (2005): 447-466.
