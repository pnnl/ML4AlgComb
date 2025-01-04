# Partial Orders on Lattice Paths (Open Problem)

NE lattice paths from $(0, 0)$ to $(a, b)$ are paths starting at $(0,0)$ and ending at $(a,b)$ which consist of a sequence of single unit steps either north and east (see example below). These turn out to have deep connections to a number of topics in algebra, geometry, and number theory. In \[1\], Schiffler defines two order relations on such paths called *matching ordering* ($\leq_M$) and the *Lagrange ordering* ($\leq_L$) that are motivated constructions in the algebraic theory of cluster algebras and number theory. Matching ordering assigns a number to each lattice path based on the number of perfect matchings of an associated snake graph, while the Lagrange ordering assigns a number to each lattice path equal to the Lagrange number of a continued fraction. These numbers each define the respective partial order. In many ways, these orders are still poorly understood. For instance, one open question asks whether one can find a simple way of determining whether two paths $w$ and $w'$ have the same relationship in both orders ($w \leq_L w'$ and $w \leq_M w'$) or different relationships in both orders ($w \leq_L w'$ and $w \geq_M w'$ or vice versa) \[2\]. These datasets are designed to try to help solve this problem.

**Dataset:** Pairs of NE lattice paths $(w,w')$ on a grid of size $n \times n-1$ where $w'$ covers $w$ in either the matching or Lagrange order (but not both). We include $n = 10,11,12,13$.

**Task:** Train a model that can predict whether $(w,w')$ is a covering pair in Lagrange or matching order.

Datasets can be found [here](https://drive.google.com/file/d/1Wm9mtZQjXXQ4rl0TU9KtJ1T4RQaGsJNz/view?usp=sharing)

## Data Generation

Datasets were generated using SageMath. A SageMath notebook with the code to do this can be found in this repository.

## Small model performance

| Size | Logistic regression | MLP | Transformer | TODO | 
|----------|----------|-----------|------------|------------|
| $n= 10$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 11$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 12$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 13$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

## References

\[1\] Schiffler, Ralf. "Perfect matching problems in cluster algebras and number theory." arXiv preprint arXiv:2302.02185 (2023).

\[2\] Apruzzese, P. J., and Kevin Cong. "On Two Orderings of Lattice Paths." arXiv preprint arXiv:2310.16963 (2023).
