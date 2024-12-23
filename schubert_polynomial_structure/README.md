# Schubert polynomial structure constants (open problem)

Schubert polynomials \[1,2,3\] are a family of polynomials indexed by permutations of $S_n$. Developed to study the cohomology ring of the flag variety, they have deep connections to algebraic geometry, Lie theory, and representation theory. Despite their geometric origins, Schubert polynomials can be described combinatorially \[4,5\], making them a well-studied object in algebraic combinatorics. An important open problem in the study of Schubert polynomials is understanding their *structure constants*. 

When two Schubert polynomials are multiplied, their product is a linear combination of Schubert polynomials
$\mathfrak{S}\_{\beta} \mathfrak{S}\_{\gamma} = \sum\_{\alpha} c^{\alpha}\_{\beta \gamma} \mathfrak{S}\_{\alpha}$
The question is whether the $c^{\alpha}\_{\beta \gamma}$ (the *structure constants*) have a combinatorial interpretation. To give an example of what we mean by combinatorial description, in the case of Schur polynomials (which can be viewed as specific case of Schubert polynomials), the coefficients in the product are equal to the number of semistandard tableaux satisfying certain properties.

**Dataset:** Each instance in this dataset is a triple of permutations $(\beta, \gamma, \alpha)$, labeled by its coefficient $c^{\alpha}\_{\beta \gamma}$ in the expansion of the product $\mathfrak{S}\_{\beta} \mathfrak{S}\_{\gamma}.$ Not all possible triples of permutations are included; the dataset consists of an approximately equal number of zero and nonzero coefficients. We provide datasets for $n = 4, 5, 6$.

**Task:** The task is to predict the coefficient $c^{\alpha}\_{\beta \gamma}$.

Datasets can be found [here](https://drive.google.com/file/d/15bERRWWue-3gKSir3hVhfejNTeZJgsl9/view?usp=sharing).

## Baselines

### MLP

| Model Type | Accuracy | # of Layers |
|----------|----------|----------|
| $n = 3$ | $82.4 %± 0.00%$ | $2$ |
| $n = 4$ | $93.3 %± 0.00%$ | $4$ |
| $n = 5$ | $99.8 %± 0.00%$ | $2$ |

### Logistic Regression

| Size | Accuracy | 
|----------|----------|
| $n= 3$ | $76.5 \pm 0.00%$ |
| $n= 4$  | $64.4 \pm 0.00$ |
| $n= 5$  | $66.7 \pm 0.00%$ | 

### Transformer

| Size | Accuracy | 
|----------|----------|
| $n= 3$ | $72.9 \pm 0.03%$ |
| $n= 4$  | $97.7 \pm 0.00%$ |
| $n= 5$  | $97.3 \pm 0.00%$ | 

\[1\] Bernstein, IMGI N., Israel M. Gel'fand, and Sergei I. Gel'fand. "Schubert cells and cohomology of the spaces G/P." Russian Mathematical Surveys 28.3 (1973): 1.

\[2\] Demazure, Michel. "Désingularisation des variétés de Schubert généralisées." Annales scientifiques de l'École Normale Supérieure. Vol. 7. No. 1. 1974.

\[3\] Lascoux, Alain, and Marcel-Paul Schützenberger. "Structure de Hopf de l’anneau de cohomologie et de l’anneau de Grothendieck d’une variété de drapeaux." CR Acad. Sci. Paris Sér. I Math 295.11 (1982): 629-633.

\[4\] Billey, Sara C., William Jockusch, and Richard P. Stanley. "Some combinatorial properties of Schubert polynomials." Journal of Algebraic Combinatorics 2.4 (1993): 345-374.

\[5\] Bergeron, Nantel, and Sara Billey. "RC-graphs and Schubert polynomials." Experimental Mathematics 2.4 (1993): 257-269.
