# Schubert polynomial structure constants (open problem)

Schubert polynomials \[1,2,3\] are a family of polynomials indexed by permutations of $S_n$. Developed to study the cohomology ring of the flag variety, they have deep connections to algebraic geometry, Lie theory, and representation theory. Despite their geometric origins, Schubert polynomials can be described combinatorially \[4,5\], making them a well-studied object in algebraic combinatorics. An important open problem in the study of Schubert polynomials is understanding their *structure constants*. 

When two Schubert polynomials are multiplied, their product can be written as a linear combination of Schubert polynomials
$\mathfrak{S}\_{\beta} \mathfrak{S}\_{\gamma} = \sum\_{\alpha} c^{\alpha}\_{\beta \gamma} \mathfrak{S}\_{\alpha}$.
The question is whether the $c^{\alpha}\_{\beta \gamma}$ (the *structure constants*) have a combinatorial interpretation. To give an example of what we mean by combinatorial interpretation, when Schur polynomials (which can be viewed as specific case of Schubert polynomials) are multiplied together, the coefficients in the resulting product are equal to the number of semistandard tableaux satisfying certain properties.

## Example

We multiply Schubert polynomials corresponding to permutations of $\{1,2,3\}$, $\beta = 2 1 3$ and $\gamma = 1 3 2$. Writing these in terms of indeterminants $x_1$, $x_2$, and $x_3$, we have $\mathfrak{S}\_{\beta} = x_1 + x_2$ and $\mathfrak{S}\_{\gamma} = x_1$. Multiplying these together we get
$\mathfrak{S}_{\beta}\mathfrak{S}\_{\gamma} = x_1^2 + x_1x_2$. As $\mathfrak{S}\_{2 3 1} = x\_1x\_2$ and $\mathfrak{S}\_{3 1 2} = x\_1^2$. Hence $\mathfrak{S}\_{\beta}\mathfrak{S}\_{\gamma} = \mathfrak{S}\_{2 3 1} + \mathfrak{S}\_{3 1 2}$. It follows that $c\_{\beta,\gamma}^{\alpha} = 1$ if $\alpha = 2 3 1$ or $\alpha = 3 1 2$ and otherwise $c\_{\beta,\gamma}^{\alpha} = 0$.

## Dataset 
Each instance in this dataset is a triple of permutations $(\beta, \gamma, \alpha)$, labeled by its coefficient $c^{\alpha}\_{\beta \gamma}$ in the expansion of the product $\mathfrak{S}\_{\beta} \mathfrak{S}\_{\gamma}$. The datasets are organized so that $\beta$ and $\gamma$ are always drawn from the symmetric group on $n$ elements (we provide datasets for $n = 3$, $4$, and $5$), but $\alpha$ may belong to a strictly larger symmetric group. Not all possible triples of permutations are included since the vast majority of these would be zero. The dataset consists of an approximately equal number of zero and nonzero coefficients (but they are not balanced between quantities of non-zero coefficients). We provide datasets for $n = 4, 5, 6$ [here](https://drive.google.com/file/d/15bERRWWue-3gKSir3hVhfejNTeZJgsl9/view?usp=sharing). 

Each line in the file corresponds to a structure constant so that 
`([1,2,3,5,4],[1,2,3,5,4],[1,2,3,6,4,5];1)`
means that $c^{1 2 3 6 4 5}_{1 2 3 5 4,1 2 3 5 4} = 1$ or that in the expansion of the product $\mathfrak{S}\_{\alpha} \mathfrak{S}\_{\beta}$, $\mathfrak{S}\_{\gamma}$ has a coefficient of 1. To the point above, this instance is from $n = 5$ but note that the third permutation actually belongs to $S_6$. 

The datasets can be loaded by: (1) unzipping the file found [here](https://drive.google.com/file/d/15bERRWWue-3gKSir3hVhfejNTeZJgsl9/view?usp=sharing) in your chosen `directory`, (2) choosing a value for $n$ (18, 20, or 22), and then (3) running the following commands (here we choose $n = 5$)

```
import numpy as np
import load_datasets 

folder = # provide the file path to the directory you chose here
X = load_datasets.get_dataset('schubert', n=5, folder = folder)
```

The basic statistics of the datasets are as follows

### Permutations of size $4$

All structure constants in this case are either 0 or 1 (so the classification problem is binary). 

|  | 0 | 1 | Total number of instances | 
|----------|----------|----------|----------|
| Train | 851 | 833 | 1,684 |
| Test  | 201 | 220 | 421 |

### Permutations of size $5$

All structure constants in this case are either 0, 1, or 2. 

|  | 0 | 1 | 2 |  Total number of instances | 
|----------|----------|----------|----------|----------|
| Train | 42,831 | 42,619 | 170 | 85,620 |
| Test  | 10,681 | 10,680 | 44 | 21,405 |

### Permutations of size $6$

All structure constants in this case are either 0, 1, 2, 3, 4, or 5. 

|  | 0 | 1 | 2 | 3 | 4 | 5 |  Total number of instances | 
|----------|----------|----------|----------|----------|----------|----------|----------|
| Train | 4,202,040 | 4,093,033 | 109,217 | 2,262 | 9 | 9 | 8,406,564 |
| Test  | 1,052,062 | 1,021,898 | 27,110 | 568 | 3 | 0 | 2,101,641 |

## Task 

The immediate machine learning task is to predict the coefficient $c^{\alpha}\_{\beta \gamma}$ given the triple $(\alpha,\beta,\gamma)$. The broader mathematical question is finding a combinatorial interpretation of these structure constants. We hope that analyzing performant models will yield insights that will help reach this goal.

## Data generation

The Sage notebook within this directory gives the code used to generate these datasets. The process involves:

- For a chosen $n$, compute the products $\mathfrak{S}\_{\beta} \mathfrak{S}\_{\gamma}$ for $\beta,\gamma \in S_n$.
- For each of these pairs, extract and add to the dataset all non-zero structure constants $c^{\alpha_1}\_{\beta,\gamma}, \dots, c^{\alpha_k}\_{\beta,\gamma}$
- Furthermore, for each $c^{\alpha_i}\_{\beta,\gamma} \neq 0$, randomly permute $\alpha_i \mapsto \alpha_i'$ to find $c^{\alpha_i'}\_{\beta,\gamma} = 0$ and $c^{\alpha_i'}\_{\beta,\gamma}$ is not already in the dataset.

## Small model performance

| Size | Logistic regression | MLP | Transformer | Guessing majority class | 
|----------|----------|-----------|------------|------------|
| $n= 4$ | $64.4\\%$ | $89.5\\% \pm 2.6\\%$ | $96.7\\% \pm 3.5\\%$| $47.7\\%$ |
| $n= 5$ | $66.7\\%$ | $99.8\\% \pm 0.0\\%$ | $81.0\\% \pm 22.1\\%$| $49.9\\%$ |
| $n= 6$ | $65.5\\%$ | $99.8\\% \pm 0.0\\%$ | $85.0\\% \pm 10.9\\%$| $50.1\\%$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

## References

\[1\] Bernstein, IMGI N., Israel M. Gel'fand, and Sergei I. Gel'fand. "Schubert cells and cohomology of the spaces G/P." Russian Mathematical Surveys 28.3 (1973): 1.

\[2\] Demazure, Michel. "Désingularisation des variétés de Schubert généralisées." Annales scientifiques de l'École Normale Supérieure. Vol. 7. No. 1. 1974.

\[3\] Lascoux, Alain, and Marcel-Paul Schützenberger. "Structure de Hopf de l’anneau de cohomologie et de l’anneau de Grothendieck d’une variété de drapeaux." CR Acad. Sci. Paris Sér. I Math 295.11 (1982): 629-633.

\[4\] Billey, Sara C., William Jockusch, and Richard P. Stanley. "Some combinatorial properties of Schubert polynomials." Journal of Algebraic Combinatorics 2.4 (1993): 345-374.

\[5\] Bergeron, Nantel, and Sara Billey. "RC-graphs and Schubert polynomials." Experimental Mathematics 2.4 (1993): 257-269.
