# Grassmannian Cluster Algebras and SSYTs (open problem)

The Grassmann manifold Gr $(k,n)$ is the set of full-rank $k \times n$ matrices up to equivalence of elementary row operations (equivalently the space whose points are $k$-dimensional subspaces in $\mathbb{R}^n$). Grassmannians are of fundamental geometric importance and are a central tool in a model of quantum field theory known as supersymmetric Yang-Mills theory. 

Among the many algebraic-combinatorial properties of Grassmannians is an algebraic structure on its coordinate ring making it a cluster algebra. A recent result of Chang, Duan, Fraser, and Li \[1\] parameterize cluster variables of the Grassmannian coordinate ring in terms of equivalence classes of semistandard Young tableaux. Not every semistandard Young tableaux indexes a cluster variable and a natural question to ask is which are valid cluster variable indices. A necessary condition is that the tableaux is of rectangular shape. We follow the set-up set up of \[2\] who first applied machine learning to this problem, though we choose a different method of sampling tableau that do not index cluster variables.

**Dataset:** A collection of rectangular semistandard Young tableau each with a label indicating whether they index a cluster variable or not.

**Task:** Predict whether a Young tableaux indexes a cluster variable.

The datasets can be found at: 

\[1\] Chang, Wen, et al. "Quantum affine algebras and Grassmannians." Mathematische Zeitschrift 296.3 (2020): 1539-1583.
\[2\] Cheung, Man-Wai, et al. "Clustering cluster algebras with clusters." arXiv preprint arXiv:2212.09771 (2022).

