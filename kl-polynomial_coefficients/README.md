# The coefficients of Kazhdan-Lusztig polynomials (open problem)

Kazhdan-Lusztig (KL) polynomials are polynomials in a variable $q$ and with integer coefficients that (for our purposes) are indexed by a pair of permutations \[1\]. We will write the KL polynomial associated with permutations $\sigma$ and $\nu$ as $P_{\sigma,\nu}(q)$. For example, the KL polynomial associated with permutations $\sigma = 1$ $4$ $3$ $2$ $7$ $6$ $5$ $10$ $9$ $8$ $11$ and $\nu = 4$ $6$ $7$ $8$ $9$ $10$ $1$ $11$ $2$ $3$ $5$ is

$P_{\sigma,\nu}(q) = 1 + 16q + 103q^2 + 337q^3 + 566q^4 + 529q^5 + 275q^6 + 66q^7 + 3q^8.$

KL polynomials have deep connections throughout several areas of mathematics. For example, KL polynomials are related to the dimensions of intersection homology in Schubert calculus, the study of the Hecke algebra, and representation theory of the symmetric group. They can be computed via a recursive formula [\[1\]](https://link.springer.com/article/10.1007/BF01390031), nevertheless, in many ways they remain mysterious. For instance, there is no known closed formula for the degree of $P_{\sigma,\nu}(q)$.

One family of questions revolve around the coefficients of $P_{\sigma,\nu}(q)$. For instance, it has been hypothesized that the coefficient on the term $q^{\ell(\sigma) - \ell(\nu)-1/2}$ (where $\ell(x)$ is a statistic called the length of the permutation), which is known as the $\mu$-coefficient, has a combinatorial interpretation but currently this is not known. Better understanding of this and other coefficients would be of significant interest to mathematicians from a range of fields.

**Dataset:** Each instance in this dataset consists of a pair of permutations of $n$, $x$ and $w$, along with the coefficients of the polynomial $P_{x,w}(q)$. We provide full datasets for $n = 5,6$. Each instance corresponds to a line in the train/test files. So if $x =$ $1$ $2$ $3$ $4$ $5$ $6$ and $w=4$ $5$ $6$ $1$ $2$ $3$ and $P_{v,w}(q) = 1 + 4q + 4q^2 + q^3$ then this is written as the line

``123456, 456123, 1, 4, 4, 1``

Note that coefficients are listed by increasing degree of the power of $q$ (e.g., the coefficient on $1$ comes first, then the coefficient on $q$, then the coefficient on $q^2$, etc.)

The files we provide are: 
- ``kl_polynomials_5_train.txt``
- ``kl_polynomials_5_test.txt``
- ``kl_polynomials_6_train.txt``
- ``kl_polynomials_6_test.txt``

The datasets can be loaded by: (1) unzipping the file found ADD ME in your chosen `directory`, (2) choosing a value for $n$ (5 or 6), and then (3) running the following commands (here we choose $n = 6$)

```
import numpy as np
import load_datasets 

folder = # provide the file path to the directory you chose here
X = load_datasets.get_dataset('schubert', n=5, folder = folder)
```

The basic statistics of the datasets are as follows

### Kazhdan-Lusztig Polynomials for Permutations of $5$ elements

We summarize the different values of each of the coefficients for all $P_{x,w}(q)$ when $x, w \in S_5$. 

**Constant Terms:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 8,500 | 3,020 | 11,520 |
| Test  | 2,119 | 761 | 2,880 |

**Coefficients on $q$:**

|  | 0 | 1 | 2 | Total number of instances | 
|----------|----------|----------|----------|----------|
| Train | 11,210 | 274 | 36 | 11,520 |
| Test  | 2,796 | 76 | 8 | 2,880 |

**Coefficient on $q^2$:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 11,518 | 2 | 11,520 |
| Test  | 2,878 | 2 | 2,880 |

### Kazhdan-Lusztig Polynomials for Permutations of $6$ elements

We summarize the different values of each of the coefficients for all $P_{x,w}(q)$ when $x, w \in S_6$. 

**Constant Terms:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 335,976 | 78,744 | 414,720 |
| Test  | 84,017 | 19,663 | 103,680 |

**Coefficients on $q$:**

|  | 0 | 1 | 2 | 3 | 4 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|
| Train | 396,951 | 13,646 | 3,524 | 542 | 57 | 414,720 |
| Test  | 99,297 | 3,374 | 878 | 110 | 21 | 103,680 |

**Coefficient on $q^2$:**

|  | 0 | 1 | 2 | 3 | 4 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|
| Train | 413,068 | 1,383 | 211 | 32 | 26 | 414,720 |
| Test  | 103,284 | 331 | 41 | 16 | 8 | 103,680 |

**Coefficient on $q^3$:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 414,708 | 12 | 414,720 |
| Test  | 103,674 | 6 | 103,680 |

## Task 

The ML task is to predict the coefficients of $P_{x,w}(q)$ given $x$ and $w$. We break this up into a separate task for each coefficient though one could choose to predict all simultaneously. Since there are generally very few different integers that arise as coefficients (at least in this small examples), we frame this problem as one of classification.

The broader problem is establish a better understanding of the coefficients of Kazhdan-Lusztig polynomials which known to carry rich geometric information and are assumed to hold a combinatorial interpretation as well (i.e., they count something). While the classification task as framed does not capture this more nuanced question, illuminating connections between $x$, $w$, and the coefficients of $P_{x,w}(q)$ has the potential to yield critical insights.

## Small model performance

### Prediction of the coefficient on $q^2$

TODO

| Size | Logistic regression | MLP | Transformer | Guessing 0 | 
|----------|----------|-----------|------------|------------|
| $n= 5$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 6$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |

## Data Generation

Datasets were generated using SageMath. A SageMath notebook with the code to do this can be found in this repository.

\[1\] Kazhdan, David, and George Lusztig. "Representations of Coxeter groups and Hecke algebras." Inventiones mathematicae 53.2 (1979): 165-184.

\[2\] Warrington, Gregory S. "Equivalence classes for the μ-coefficient of Kazhdan–Lusztig polynomials in Sn." Experimental Mathematics 20.4 (2011): 457-466.
