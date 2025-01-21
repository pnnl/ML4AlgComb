# The coefficients of Kazhdan-Lusztig polynomials (open problem)

Kazhdan-Lusztig (KL) polynomials are polynomials in a variable $q$ and with integer coefficients that (for our purposes) are indexed by a pair of permutations \[1\]. We will write the KL polynomial associated with permutations $\sigma$ and $\nu$ as $P_{\sigma,\nu}(q)$. For example, the KL polynomial associated with permutations $\sigma = 1$ $4$ $3$ $2$ $7$ $6$ $5$ $10$ $9$ $8$ $11$ and $\nu = 4$ $6$ $7$ $8$ $9$ $10$ $1$ $11$ $2$ $3$ $5$ is

$P_{\sigma,\nu}(q) = 1 + 16q + 103q^2 + 337q^3 + 566q^4 + 529q^5 + 275q^6 + 66q^7 + 3q^8.$

KL polynomials have deep connections throughout several areas of mathematics. For example, KL polynomials are related to the dimensions of intersection homology in Schubert calculus, the study of the Hecke algebra, and representation theory of the symmetric group. They can be computed via a recursive formula [\[1\]](https://link.springer.com/article/10.1007/BF01390031), nevertheless, in many ways they remain mysterious. For instance, there is no known closed formula for the degree of $P_{\sigma,\nu}(q)$.

One family of questions revolve around the coefficients of $P_{\sigma,\nu}(q)$. For instance, it has been hypothesized that the coefficient on the term $q^{\ell(\sigma) - \ell(\nu)-1/2}$ (where $\ell(x)$ is a statistic of permutation  $x$ called the *length* of the permutation), which is known as the $\mu$-coefficient, has a combinatorial interpretation but currently this is not known. Better understanding of this and other coefficients would be of significant interest to mathematicians from a range of fields.

**Dataset:** Each instance in this dataset consists of a pair of permutations of $n$, $x$ and $w$, along with the coefficients of the polynomial $P_{x,w}(q)$. We provide full datasets for $n = 5,6,7$. Each instance corresponds to a line in the train/test files. So if $x =$ $1$ $2$ $3$ $4$ $5$ $6$ and $w=4$ $5$ $6$ $1$ $2$ $3$ and $P_{v,w}(q) = 1 + 4q + 4q^2 + q^3$ then this is written as the line

``123456, 456123, 1, 4, 4, 1``

Note that coefficients are listed by increasing degree of the power of $q$ (e.g., the coefficient on $1$ comes first, then the coefficient on $q$, then the coefficient on $q^2$, etc.)

The files we provide are: 
- ``kl_polynomials_5_train.txt``
- ``kl_polynomials_5_test.txt``
- ``kl_polynomials_6_train.txt``
- ``kl_polynomials_6_test.txt``
- ``kl_polynomials_7_train.txt``
- ``kl_polynomials_7_test.txt``

The datasets can be loaded by: (1) unzipping the file found [here](https://drive.google.com/file/d/1A9swYSBVM4Y5KAFC52AzVRMVshVz4yyR/view?usp=sharing) in your chosen `directory`, (2) choosing a value for $n$ (5, 6, or 7), and then (3) running the following commands (here we choose $n = 6$)

```
import numpy as np
import load_datasets 

folder = # provide the file path to the directory you chose here
X = load_datasets.get_dataset('schubert', n=6, folder = folder)
```

The basic statistics of the datasets are as follows

### Kazhdan-Lusztig Polynomials for Permutations of $5$ elements

We summarize the limited number of different values coefficients on $P_{x,w}(q)$ take when $x, w \in S_5$. 

**Constant Terms:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 8,496 | 3,024 | 11,520 |
| Test  | 2,123 | 757 | 2,880 |

**Coefficients on $q$:**

|  | 0 | 1 | 2 | Total number of instances | 
|----------|----------|----------|----------|----------|
| Train | 11,219 | 267 | 34 | 11,520 |
| Test  | 2,793 | 77 | 10 | 2,880 |

**Coefficient on $q^2$:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 11,514 | 6 | 11,520 |
| Test  | 2,876 | 4 | 2,880 |

### Kazhdan-Lusztig Polynomials for Permutations of $6$ elements

We summarize the limited number of different values coefficients on $P_{x,w}(q)$ take when $x, w \in S_6$.

**Constant Terms:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 336,071 | 78,649 | 414,720 |
| Test  | 83,922 | 19,758 | 103,680 |

**Coefficients on $q$:**

|  | 0 | 1 | 2 | 3 | 4 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|
| Train | 397,386 | 13,253 | 3,483 | 535 | 63 | 414,720 |
| Test  | 99,354 | 3,311 | 883 | 117 | 15 | 103,680 |

**Coefficient on $q^2$:**

|  | 0 | 1 | 2 | 3 | 4 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|
| Train | 412,707 | 1,705 | 242 | 40 | 26 | 414,720 |
| Test  | 103,177 | 441 | 46 | 8 | 8 | 103,680 |

**Coefficient on $q^3$:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 414,688 | 32 | 414,720 |
| Test  | 103,670 | 10 | 103,680 |

### Kazhdan-Lusztig Polynomials for Permutations of $7$ elements

We summarize the limited number of different values coefficients on $P_{x,w}(q)$ take when $x, w \in S_7$. 

**Constant Terms:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 17,479,910 | 2,841,370 | 20,321,280 |
| Test  | 4,370,771 | 709,549 | 5,080,320 |

**Coefficients on $q$:**

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Train | 19,291,150 | 660,600 | 266,591 | 80,173 | 18,834 | 3,221 | 711 | 20,321,280 |
| Test  | 4,822,214 | 165,768 | 66,593 | 19,963 | 4,762 | 819 | 201 | 5,080,320 |

**Coefficient on $q^2$:**

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Train | 20,072,738 | 170,412 | 46,226 | 16,227 | 7,621 | 4,023 | 1,287 | 1,153 | 785 | 350 | 152 | 139 | 121 | 42 | 4 | 20,321,280 |
| Test  | 5,017,962 | 42,748 | 11,568 | 4,021 | 1,905 | 1,065 | 349 | 287 | 183 | 86 | 40 | 37 | 47 | 22 | 5,080,320 |

**Coefficient on $q^3$:**

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 15 | Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Train | 20,291,535 | 22,094 | 4,779 | 1,660 | 590 | 195 | 206 | 115 | 34 | 26 | 24 | 18 | 4 | 20,321,280 |
| Test  | 507,2831 | 5,498 | 1,213 | 442 | 146 | 61 | 50 | 37 | 14 | 6 | 8 | 14 | 5,080,320 |

**Coefficient on $q^4$:**

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 17,479,910 | 2,841,370 | 20,321,280 |
| Test  | 4,370,771 | 709,549 | 5,080,320 |


## Data Generation

Datasets were generated using C code from Greg Warrington's [website](https://gswarrin.w3.uvm.edu/research/klc/klc.html) and adapting it for all pairs of permutations for $n = 5, 6, 7$.

## Task 

**Math question:** Establish a better understanding of the coefficients of Kazhdan-Lusztig polynomials which are known to carry rich geometric information and are assumed to hold a combinatorial interpretation (i.e., they count something).

**ML task:** The ML task is to predict the coefficients of $P_{x,w}(q)$ given $x$ and $w$. We break this up into a separate task for each coefficient though one could choose to predict all simultaneously. Since there are generally very few different integers that arise as coefficients (at least in these small examples), we frame this problem as one of classification. 

While the classification task as framed does not capture the broader math question exactly, illuminating connections between $x$, $w$, and the coefficients of $P_{x,w}(q)$ has the potential to yield critical insights.

## Small model performance

Since there are many possible tasks here, we did not run exhaustive hyperparameter searches, instead opting for the larger network sizes for our 

### Kazhdan-Lusztig Polynomials for Permutations of $5$ elements

| Coefficient | Logistic regression | MLP | Transformer | Guessing 0 | 
|----------|----------|-----------|------------|------------|
| $1$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $q$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $q^2$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |


### Kazhdan-Lusztig Polynomials for Permutations of $6$ elements

| Coefficient | Logistic regression | MLP | Transformer | Guessing 0 | 
|----------|----------|-----------|------------|------------|
| $1$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $q$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $q^2$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $q^3$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

## References

\[1\] Kazhdan, David, and George Lusztig. "Representations of Coxeter groups and Hecke algebras." Inventiones mathematicae 53.2 (1979): 165-184.

\[2\] Warrington, Gregory S. "Equivalence classes for the μ-coefficient of Kazhdan–Lusztig polynomials in Sn." Experimental Mathematics 20.4 (2011): 457-466.
