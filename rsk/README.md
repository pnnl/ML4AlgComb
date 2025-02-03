# The Robinson-Schensted-Knuth correspondence (classic result)

The Robinson-Schensted (RS) algorithm \[1,2\] gives a bijection between pairs of standard Young tableau of the same shape $\lambda \vdash n$ and permutations in $S_n$ of conjugacy class $\lambda$, providing a bijective proof of a fundamental identity from representation theory. Knuth extended the RS algorithm to a bijection known as the Robinson-Schensted-Knuth (RSK) correspondence, which maps matrices of non-negative integers to pairs of semistandard Young tableaux of the same shape. This correspondence is significant in algebraic combinatorics not only because of the connection it provides between the combinatorial structure of Young tableaux and the theory of symmetric functions, but also because of the many generalizations and variants it has inspired, which has led to substantial progress in the field.

The goal of this benchmark is to see whether a model can learn the RSK algorithm. That is, for a fixed $n$ the model is provided with a permutation $\pi \in S_n$ and required to predict pairs of standard Young tableaux. Although the algorithm is known, it would be significant for a model to learn this correspondence due to the the intricate combinatorial rules involved. Notably, the RSK correspondence can be used to find the length of the longest increasing subsequence, so a model that learns this algorithm implicitly must also learn to solve the increasing subsequence problem. Additionally, given the numerous generalizations of the RSK correspondence, a model that performs well on this benchmark could potentially be investigated for its ability to generalize to other related combinatorial settings. 

**Dataset:** This dataset consists of triples: two standard Young tableau of size $n$ and their corresponding permutation (via the RSK algorithm). We include datasets for $n = 8,9,10$. 

Unlike some of the other datasets where permutations are written in one-line notation, in this dataset we write them in terms of their inversion set. For a permutation $\sigma$ on $n$ elements, the inversion set gives all pairs of numbers $1 \leq i < j \leq n$ such that $\sigma(j) < \sigma(i)$. There are $\binom{n}{2}$ possible inversions for $\sigma$. We represent the inversion set as a binary code where $1$ means that $\sigma$ inverts $(i, j)$ and $0$ means that it does not. Note that an inversion set completely characterizes a permutation.

We list permutations in lexicographical order so that the full list of inversions of $\{1, 2, 3\}$ is $(1,2)$, $(1,3)$, $(2,3)$.
The permutation $213$, inverts $(1, 2)$ but not $(1, 3)$ or $(2, 3)$, so we would write it as ``1, 0, 0``.

The datasets can be downloaded [here](https://drive.google.com/file/d/1CfuxD_XgTefbEduxJnXgXoUOt-GY-smq/view?usp=sharing). 

## Data generation

## Task

**Math question (solved):** The RSK algorithm is important because it establishes a bijection between permutations of $n$ and a pair of standard Young tableaux. It is central to the field of algebraic combinatorics.

**ML task:** Given a pair of standard Young tableaux, predict the corresponding permutation. As noted above, output permutations are represented as a $\{0,1\}$-vector corresponding to their inversion set.

The RSK algorithm is non-trivial. It would be a powerful proof-of-concept in the application of ML for math if a machine learning algorithm could re-discover it.

## Small model performance

| Size | Logistic regression | MLP | Transformer | Guessing target mean | 
|----------|----------|-----------|------------|------------|
| $n= 8$ | $0.21$ | $0.43 \pm 0.05$ | $1.51 \pm 0.02$| $0.21$ |
| $n= 9$ | $0.21$ | $0.96 \pm 0.07$ | $3.85 \pm 0.09$| $0.21$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

## References

\[1\] Robinson, G. de B. "On the representations of the symmetric group." American Journal of Mathematics (1938): 745-760.

\[2\] Schensted, Craige. "Longest increasing and decreasing subsequences." Canadian Journal of mathematics 13 (1961): 179-191.
