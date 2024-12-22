# Weaving patterns (open problem)

Weaving patterns are $n \times n-1$-matrices with $\{0,1\}$-entries introduced by Felsner \[1\] to study the number of reduced decompositions of the permutation $\sigma = n \; n-1 \; \ldots 1$ up to commutation equivalence. The number of such objects also counts the number of parallel sorting networks, the number of rhombic tilings of regular polygons, and is connected to the study of the higher Bruhat orders. Weaving patterns can be enriched by replacing the $\{0,1\}$ entries to the matrix with $\{1,2,\dots,n\}$ entries that track the element being swapped. An $O(n^2)$ algorithm for determining if a given 0-1 matrix is a valid weaving pattern exists but gives no additional insight into the structure of weaving patterns and correspondingly the asymptotics of reduced decompositions.

The enumeration of reduced decompositions up to commutation equivalence has been studied by many including Knuth and Stanley. An exact formula is likely out of reach, so asymptotic upper and lower bounds are of great interest. ML models that can detect necessary or sufficient conditions for a matrix to be a valid weaving pattern have the potential to lead to substantial improvements in the upper bound.

## Dataset 

Weaving patterns of size $n \times n − 1$ are a special type of matrix containing entries in ${1, 2, . . . , n}$. They correspond to representations of the longest word permutation of $n$ elements (the permutation that sends $1 \mapsto n$, $2 \mapsto n − 1$, etc.). This task involves trying to identify weaving patterns among matrices that look like weaving patterns but are not.

Each $n \times n − 1$ matrix is stored on single line. For instance,
`(0, 1, 2, 3, 3, 2, 3, 4, 2, 3, 2, 1, 5, 4, 3, 2)`
where the matrix is represented in row-major format. An integer representing whether the matrix corresponds to a weaving pattern ‘0’ or not ‘1’ is listed after the matrix.

For a given $n$, the dataset consists of a mixture of enriched weaving patterns and non-weaving pattern (i.e., matrices with $\{1, 2, \ldots, n\}$-entries). We provide $n = 6, 7, 8$ [here](https://drive.google.com/file/d/1HsWuHpTkCOtpyTG2dFH49jzkKIZYwKG8/view?usp=sharing). The statistics are as follows:

### Weaving patterns of size $6$
|| # Weaving patterns | # Non-weaving patterns | 
|----------|----------|-----------|
| Train | 634 | 1116 |
| Test  | 275 | 476 |

### Weaving patterns of size $7$
|| # Weaving patterns | # Non-weaving patterns | 
|----------|----------|-----------|
| Train | 17,388 | 96,012 |
| Test  | 7,310 | 41,290 |

### Weaving patterns of size $8$
|| # Weaving patterns | # Non-weaving patterns | 
|----------|----------|-----------|
| Train | 17,388 | 96,012 |
| Test  | 7,310 | 41,290 |

## Task
Classify whether a matrix in the dataset is a weaving pattern or not. 

## Baselines

### Logistic Regression

| Size | Accuracy | 
|----------|----------|
| $n= 6$ | $70.4 \pm 0.00$ |
| $n= 7$  | $85.8 \pm 0.00$ |

### Transformer

| Size | Accuracy | 
|----------|----------|
| $n= 6$ | $88.7 \pm 0.01$ |
| $n= 7$  | $99.1 \pm 0.00$ |

\[1\] Felsner, Stefan. "On the number of arrangements of pseudolines." Proceedings of the twelfth annual Symposium on Computational Geometry. 1996.
