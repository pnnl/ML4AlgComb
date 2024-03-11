# Grassmannian Cluster Algebra

### Problem Importance

Hernandez and Leclerc [1] applied the theory of cluster algebras to the problem of prime modules in quantum affine algebras $U_q(\hat{\mathfrak{g}})$. They constructed a certain cluster algebra such that prime modules are given by cluster variables which are generated through mutation. A major conjecture of theirs is that the cluster variables obtained this way are in correspondence with real prime modules. One direction is proven by Qin [2], namely that all cluster variables are real prime modules. The other direction, showing that all real prime modules arise as cluster variables, is wide open.

In this problem, we are concerned with the case where $\mathfrak{g} = \mathfrak{sl}_n$, the special linear Lie algebra consisting of $n \times n$ matrices that have trace 0. In this case, Hernandez and Leclerc constructed an isomorphism between their cluster algebras and certain quotients of the Grassmannian cluster algebras $\mathbb{C}[\text{Gr}(k,n)]$. Chang, Duan, Fraser, and Li [3] put a monoid structure on equivalence classes of rectangular semistandard Young tableaux (SSYT) and through a series of equivalences show that real prime modules of $U_q(\hat{\mathfrak{g}})$ are parameterized by rectangular SSYT. Thus, understanding the subset of rectangular SSYTs that parameterize these real prime modules will help in understanding Hernandez and Leclerc's conjecture.

### Mathematical Background
One of the central objects of study is $\mathbb{C}[\text{Gr}(k,n)]$, the homogeneous coordinate ring with respect to the Pl\"ucker embedding of the Grassmannian $\text{Gr}(k,n)$. The easiest way to think about this is in terms of matrices. Roughly speaking, $\text{Gr}(k,n)$ is the set of full-rank $k \times n$ matrices up to equivalence of elementary row operations. The Pl\"ucker embedding sends each element $M \in \text{Gr}(k,n)$ to a tuple of $\binom{n}{k}$ real numbers $\Delta_{i_1, \ldots, i_k}$, one for each $k \times k$ minor $M_{i_1, \ldots, i_k}$ of $M$. The entries of a general $k \times n$ can be thought of as variables $x_{i,j}$ where $1 \le i \le k$ and $1 \le j \le n$. The homogeneous coordinate ring $\mathbb{C}[\text{Gr}(k,n)]$ is the ring $\mathbb{C}[x_{i,j}] / I$ where $I$ is the ideal of Pl\"ucker relations. The Pl\"ucker relations are some equations that relate the $\Delta_{i_1, \ldots, i_k}$. For example, if $n = 4$ and $k = 2$, you can show that necessarily $\Delta_{1,2}\Delta_{3,4} - \Delta_{1,3}\Delta_{2,4} + \Delta_{1,4}\Delta_{2,3} = 0$. Expanding out each $\Delta$ in terms of $x$'s yields the polynomial that generates the ideal $I$ in this case. 

It has been shown that $\mathbb{C}[\text{Gr}(k,n)]$ is in fact a cluster algebra of geometric type. In general, $\mathbb{C}[\text{Gr}(k,n)]$ has infinitely many cluster variables. There is a specific quotient $\mathbb{C}[\text{Gr}(k,n, \sim)]$ obtained by setting certain frozen variables to 1 which we will consider. It has been shown that cluster variables in $\mathbb{C}[\text{Gr}(k,n,\sim)]$ correspond with $\text{SSYT}(k,n,\sim)$, the rectangular SSYT with $k$ rows and entries in $[n]$, up to a quotient. Each equivalence class in $[T] \in \text{SSYT}(k,n,\sim)$ has a unique representative $\text{small}(T)$ which is a tableau with *small gaps*. That is, each column of $\text{small}(T)$ is of the form $[i, i+k] \setminus \{r\}$ for some $r \in [i+1, i+k-1]$. The primary questions we are interested in answering is:

**Problems:**
- *Characterize the tableaux $T$ where $[T]$ indexes a cluster variable in $\mathbb{C}[\text{Gr}(k,n)]$.*
- *Identify conditions for when two tableaux $T_1, T_2$ are compatible (i.e. appear in the same cluster seed).*

### Baseline Model
Coming soon...

### Additional References
- [Clustering Cluster Algebras with Clusters](https://arxiv.org/pdf/2212.09771.pdf) by Cheung, Dechant, He, Heyes, Hirst, and Li: Prior ML work on this problem. Their GitHub is at [https://github.com/edhirst/GrassmanniansML](here).

### References
- [1] David Hernandez and Bernard Leclerc. “Cluster algebras and quantum affine algebras”. In: Duke Math. J. 154.2 (2010), pp. 265–341. issn: 0012-7094,1547-7398.
- [2] Fan Qin. “Triangular bases in quantum cluster algebras and monoidal categorification conjectures”. In: Duke Math. J. 166.12 (2017), pp. 2337–2442. issn: 0012-7094,1547-7398.
- [3] Wen Chang, Bing Duan, Chris Fraser, and Jian-Rong Li. “Quantum affine algebras and Grassmannians”. In: Math. Z. 296.3-4 (2020), pp. 1539–1583. issn: 0025-5874,1432-1823.
