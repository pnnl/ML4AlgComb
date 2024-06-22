# The Robinson-Schensted-Knuth correspondence (classic result)

The Robinson-Schensted (RS) algorithm \[1,2\] gives a bijection between pairs of standard Young tableau of the same shape $\lambda \vdash n$ and permutations in $S_n$ of conjugacy class $\lambda$, providing a bijective proof of a fundamental identity from representation theory. Knuth extended the RS algorithm to a bijection known as the Robinson-Schensted-Knuth (RSK) correspondence, which maps matrices of non-negative integers to pairs of semistandard Young tableaux of the same shape. This correspondence is significant in algebraic combinatorics not only because of the connection it provides between the combinatorial structure of Young tableaux and the theory of symmetric functions, but also because of the many generalizations and variants it has inspired, which has led to substantial progress in the field.

The goal of this benchmark is to see whether a model can learn the RSK algorithm. That is, for a fixed $n$ the model is provided with a permutation $\pi \in S_n$ and required to predict pairs of standard Young tableaux. Although the algorithm is known, it would be significant for a model to learn this correspondence due to the the intricate combinatorial rules involved. Notably, the RSK correspondence can be used to find the length of the longest increasing subsequence, so a model that learns this algorithm implicitly must also learn to solve the increasing subsequence problem. Additionally, given the numerous generalizations of the RSK correspondence, a model that performs well on this benchmark could potentially be investigated for its ability to generalize to other related combinatorial settings. 

**Dataset:** This dataset consists of triples: two standard Young tableau of size $n$ and their corresponding permutation (via the RSK algorithm). We include datasets for $n = 8,9,10$. 

**Task:** Given pairs of standard Young tableau, predict the corresponding permutation.

The datasets can be downloaded [here](https://drive.google.com/file/d/1CfuxD_XgTefbEduxJnXgXoUOt-GY-smq/view?usp=sharing). 

\[1\] Robinson, G. de B. "On the representations of the symmetric group." American Journal of Mathematics (1938): 745-760.

\[2\] Schensted, Craige. "Longest increasing and decreasing subsequences." Canadian Journal of mathematics 13 (1961): 179-191.
