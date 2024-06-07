# Partial Orders on Lattice Paths (Open Problem)

\[1\] defines two order relations on NE lattice paths from $(0, 0)$ to $(a, b)$ called the *matching ordering* ($\leq_M$) and the *Lagrange ordering* ($\leq_L$), and proposes studying these partially ordered sets. The matching ordering assigns a number to each lattice path based on the number of perfect matchings of an associated snake graph, while the Lagrange ordering assigns a number to each lattice path equal to the Lagrange number of a continued fraction. These numbers each define the respective partial order. An open question related to the matching and Lagrange orders is whether we can find a simple way of determining whether two paths $w$ and $w'$ have the same relationship in both orders ($w \leq_L w'$ and $w \leq_M w'$) or different relationships in both orders ($w \leq_L w'$ and $w \geq_M w'$ or vice versa) \[2\]. 

**Dataset:** Pairs of NE lattice paths $(w,w')$ on a grid of size $n \times n-1$ where $w'$ covers $w$ in either the matching or Lagrange order (but not both). We include $n = 10,11,12,13$.

**Task:** Train a model that can predict whether $(w,w')$ is a covering pair in Lagrange or matching order.

Datasets can be found [here](https://drive.google.com/file/d/1Wm9mtZQjXXQ4rl0TU9KtJ1T4RQaGsJNz/view?usp=sharing)

\[1\] Schiffler, Ralf. "Perfect matching problems in cluster algebras and number theory." arXiv preprint arXiv:2302.02185 (2023).

\[2\] Apruzzese, P. J., and Kevin Cong. "On Two Orderings of Lattice Paths." arXiv preprint arXiv:2310.16963 (2023).
