# Finding a Concise Description of Weaving Pattern Matrices (Open Problem)

Weaving patterns are $n \times n-1$-matrices with $\{0,1\}$-entries introduced by Felsner \[1\] to study the number of reduced decompositions of the permutation $\sigma = n \; n-1 \; \ldots 1$ up to commutation equivalence. The number of such objects also counts the number of parallel sorting networks, the number of rhombic tilings of regular polygons, and is connected to the study of the higher Bruhat orders. Weaving patterns can be enriched by replacing the $\{0,1\}$ entries to the matrix with $\{1,2,\dots,n\}$ entries that track the element being swapped. An $O(n^2)$ algorithm for determining if a given 0-1 matrix is a valid weaving pattern exists but gives no additional insight into the structure of weaving patterns and correspondingly the asymptotics of reduced decompositions.

The enumeration of reduced decompositions up to commutation equivalence has been studied by many including Knuth and Stanley. An exact formula is likely out of reach, so asymptotic upper and lower bounds are of great interest. ML models that can detect necessary or sufficient conditions for a matrix to be a valid weaving pattern have the potential to lead to substantial improvements in the upper bound.

## Dataset 
Each $n \times n − 1$ matrix is stored on single line. For instance, the matrix

| Row 1, Cell 1 | Row 1, Cell 2 | Row 1, Cell 3 |
| Row 2, Cell 1 | Row 2, Cell 2 | Row 2, Cell 3 |

`2,1,2,3,4,3,4,5,4,5,2,3,4,5,4,5,4,3,2,3,4,5,4,3,2`

where the matrix is represented in row-major format. An integer representing whether the matrix corresponds to a weaving pattern ‘0’ or not ‘1’ is listed after the matrix.

The datasets can be loaded by: (1) unzipping the file found [here](https://drive.google.com/file/d/1HsWuHpTkCOtpyTG2dFH49jzkKIZYwKG8/view?usp=sharing) in your chosen `directory`, (2) choosing a value for $n$ (6, 7), and then (3) running the following commands (here we choose $n = 7$)

```
import numpy as np
import load_datasets 

folder = # provide the file path to the directory you chose here
X = load_datasets.get_dataset('weaving', n=7, folder = folder)
```

The task is formulated as binary classification. Class statistics are as follows:

### Weaving patterns of size $6$
|| # Weaving patterns | # Non-weaving patterns | Total instances |
|----------|----------|-----------|-----------|
| Train | 634 | 1,116 | 1,750 |
| Test  | 275 | 476 | 751 |

### Weaving patterns of size $7$
|| # Weaving patterns | # Non-weaving patterns | Total instances |
|----------|----------|-----------|-----------|
| Train | 17,388 | 96,012 | 113,400 |
| Test  | 7,310 | 41,290 | 48,600 |

## Data generation

A Java file that generates all weaving patterns for a given value of $n$ can be found above. To sample negatives ($\{1,2,\dots,n\}$-entry matrices that are not weaving patterns) we simply took true weaving patterns and randomly permuted two of the entries in a random row. We checked that the result matrix was not a weaving pattern by comparing it to all true weaving patterns that we had already found. 

## Task

**Math question:** Find a concise characterization of those $\{1,2,\dots,n\}$-valued $n \times n-1$ matrices that correspond to weaving patterns.

**ML task:** Train a model that can predict whether a $\{1,2,\dots,n\}$-valued $n \times n-1$ matrices corresponds to a weaving pattern or not. 

## Small model performance

| Size | Logistic regression | MLP | Transformer | Guessing majority class | 
|----------|----------|-----------|------------|------------|
| $n= 6$ | $70.4$ | $86.1 \pm 0.2$ | $85.9 \pm 2.3$| $63.4$ |
| $n= 7$ | $85.8$ | $99.3 \pm 0.2$ | $99.9 \pm 0.0$| $85.0$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

## References

\[1\] Felsner, Stefan. "On the number of arrangements of pseudolines." Proceedings of the twelfth annual Symposium on Computational Geometry. 1996.
