# Partial Orders on Lattice Paths (Open Problem)

NE lattice paths from $(0, 0)$ to $(a, b)$ are paths starting at $(0,0)$ and ending at $(a,b)$ which consist of a sequence of single unit steps either north and east  that never pass below the diagonal (see example below). These turn out to have deep connections to a number of topics in algebra, geometry, and number theory. In \[1\], Schiffler defines two order relations on such paths called *matching ordering* ($\leq_M$) and the *Lagrange ordering* ($\leq_L$) that are motivated constructions in the algebraic theory of cluster algebras and number theory. Matching ordering assigns a number to each lattice path based on the number of perfect matchings of an associated snake graph, while the Lagrange ordering assigns a number to each lattice path equal to the Lagrange number of a continued fraction. These numbers each define the respective partial order. In many ways, these orders are still poorly understood. For instance, one open question asks whether one can find a simple way of determining whether two paths $w$ and $w'$ have the same relationship in both orders ($w \leq_L w'$ and $w \leq_M w'$) or different relationships in both orders ($w \leq_L w'$ and $w \geq_M w'$ or vice versa) \[2\]. These datasets are designed to enable a better understanding of the relationships between $w \leq_L w'$ and $w \leq_M w'$.

## Details and an example

We provide two different pairs of lattice paths below. The example on the left is a cover pair in Lagrange order. The example on the right is covering pair in matching order. 

ADD ME

## Dataset

This dataset contains pairs of lattice paths starting at $(0,0)$ and ending at $(n,n-1)$ that are only allowed to take steps either north or east and must stay below the line $y = \frac{n}{n-1}x$. They are thus encoded by a sequence of $1$'s (for steps east) and $0$'s (for steps north) of length $(n+1) + n = 2n+1$. Each pair of lattice paths is a covering pair in exactly one of the two partial orders, the Lagrange order or the matching order.

Each line in a file is the concatenation of two 0-1 sequences (one for each path) for a length $4n+2$ row of $0$'s and $1$'s. The two lattice paths are separated by ``;``. For example, on a $3 \times 2$ grid, the sequence:
``1,1,1,0,0;1,1,0,1,0``
corresponds to the two lattice paths in the figure above. The first is in red and second is in blue, with segments traversed by both paths colored red. 

Datasets can be found [here](https://drive.google.com/file/d/1Wm9mtZQjXXQ4rl0TU9KtJ1T4RQaGsJNz/view?usp=sharing). The file names are:

- ``lagrange_covers_train_10_9.txt``
- ``lagrange_covers_train_11_10.txt``
- ``lagrange_covers_train_12_11.txt``
- ``lagrange_covers_train_13_12.txt``
- ``lagrange_covers_test_10_9.txt``
- ``lagrange_covers_test_11_10.txt``
- ``lagrange_covers_test_12_11.txt``
- ``lagrange_covers_test_13_12.txt``
- ``matching_covers_train_10_9.txt``
- ``matching_covers_train_11_10.txt``
- ``matching_covers_train_12_11.txt``
- ``matching_covers_train_13_12.txt``
- ``matching_covers_test_10_9.txt``
- ``matching_covers_test_11_10.txt``
- ``matching_covers_test_12_11.txt``
- ``matching_covers_test_13_12.txt``

## Data Generation

Datasets were generated using SageMath. A SageMath notebook with the code to do this can be found in this repository.

## Task

**Math question:** As stated in [\[1\]](https://arxiv.org/abs/2302.02185), the problem is to "Study the posets $\mathcal{D}(a,b)$ and $\mathcal{D}$ with respect to $\leq_L$ and $\leq_M$." Where $\mathcal{D}(a,b)$ is the set of all NE lattice paths from $(0,0)$ to $(a,b)$ that never pass below the diagonal and $\mathcal{D} = \cup \mathcal{D}(a,b)$ where the union is taken over all integers $0 < a < b$ with $a,b$ relatively prime. 

**ML task:** Recall that $x$ covers $y$ in a partial order if $y < x$ and there is no $z$ such that $y < z < x$. Given a pair of lattice paths $(w,w')$, train a model that can predict whether $w'$ covers $w$ in either matching or Lagrange order (cases where $w'$ covers $w$ in both orders are few and have been excluded. 

Note that the ML task is far more specific that the math question. The idea is that a model that can effectively identify covers, has probably extracted useful features from lattice paths that carry interesting information about the partial orders $\leq_L$ and $\leq_M$.

## Small model performance

| Size | Logistic regression | MLP | Transformer | TODO | 
|----------|----------|-----------|------------|------------|
| $n= 10$ | $66.2\\%$ | $90.6\\% \pm 0.8\\%$ | $65.3\\% \pm 0.0\\%$| $0.0\\%$ |
| $n= 11$ | $66.3\\%$ | $95.8\\% \pm 0.3\\%$ | $69.4\\% \pm 6.0\\%$| $0.0\\%$ |
| $n= 12$ | $66.5\\%$ | $98.6\\% \pm 0.1\\%$ | $86.2\\% \pm 14.2\\%$| $0.0\\%$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

## References

\[1\] Schiffler, Ralf. "Perfect matching problems in cluster algebras and number theory." arXiv preprint arXiv:2302.02185 (2023).

\[2\] Apruzzese, P. J., and Kevin Cong. "On Two Orderings of Lattice Paths." arXiv preprint arXiv:2310.16963 (2023).
