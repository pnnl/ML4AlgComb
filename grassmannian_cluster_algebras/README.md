# Grassmannian Cluster Algebras and Semistandard Young Tableau (Open Problem)

The Grassmann manifold $\text{Gr}(k,n)$ is the set of full-rank $k \times n$ matrices up to equivalence of elementary row operations (equivalently the space whose points are $k$-dimensional subspaces in $\mathbb{R}^n$). Grassmannians are of fundamental geometric importance and are a central tool in a model of quantum field theory known as supersymmetric Yang-Mills theory. 

Among the many algebraic-combinatorial properties of Grassmannians is an algebraic structure on its coordinate ring making it into an algebraic object called a cluster algebra. A recent result of [Chang, Duan, Fraser, and Li \[1\]](https://arxiv.org/abs/1907.13575) parameterize cluster variables of the Grassmannian coordinate ring in terms of equivalence classes of semistandard Young tableaux (SSYT). Not every SSYT indexes a cluster variable and a natural question to ask is whether there is a naive combinatorial rule that specifies whether a particular SSYT indexes a cluster variable. One necessary condition is that the tableaux is of rectangular shape. 

The idea to apply machine learning to this problem was first posed by [\[2\]](https://arxiv.org/abs/2212.09771). We follow their set up and use the positive examples that they computed (i.e., SSYT that index a cluster variable). However, we choose a different method of sampling tableau that do not index cluster variables that we found makes the problem harder (and therefore forces the model to learn more robust features).

## Details and an example

In the cluster algebra associated with Grassmann manifold $\text{Gr}(k,n)$, each cluster variable is indexed by a rectangular SSYT with $k$ rows with entries drawn from $\\{1,\dots,n\\}$ (because this is a SSYT, the entries need to weakly increase as one moves left to right in the rows and strictly increase as one moves down each column). The *rank* of these rectangular SSYT (and the rank of the associated cluster algebras) is given by their number of columns. Following [\[2\]](https://arxiv.org/abs/2212.09771), in this dataset we focus on $\text{Gr}(3,12)$ and hence look at rectangular SSYT with 3 rows filled with entries drawn from $\\{1,\dots,12\\}$. We further restrict to rank 4 SSYT. This leaves us with a collection of $3 \times 4$ arrays whose entries increase weakly across rows and strictly down columns. 

To give two examples, the SSYT below corresponds to a cluster variable

<img src="ssyt_valid.png" alt="drawing" width="200"/>
 
but this one does not

<img src="ssyt_invalid.png" alt="drawing" width="200"/>

Note that both are genuine SSYT of shape $3 \times 4$ with entries from $\\{1, \dots, 12\\}$.

## Dataset

The dataset consists of a collection of rectangular SSYT each with a label indicating whether it indexes a cluster variable or not. Those that do not index a cluster variable are labeled with a `0` and those that do are labeled with a `1`. Tableaux have shape $3 \times 4$, and are filled with values drawn from $\{1,2,\dots,12\}$. 

The data can be found here [here](https://drive.google.com/file/d/1Dd4PAOgm7bAtXSGmQW81OE-O_7dS7qU_/view?usp=sharing). The files are named: 
- ``3_4_12_invalid_train.txt``
- ``3_4_12_invalid_test.txt``
- ``3_4_12_valid_test.txt``
- ``3_4_12_valid_train.txt``

In the files we use braces $[$ and $]$ to demarcate rows of the dataset, so that

``[[2, 3, 4, 7], [3, 5, 6, 8], [4, 9, 11, 12]]``

corresponds to the tableau pictured in the Figure below

<img src="fig-grassmannian-tableau-example.png" alt="drawing" width="200"/>

The datasets can be loaded by: (1) unzipping the file found [here](https://drive.google.com/file/d/1Dd4PAOgm7bAtXSGmQW81OE-O_7dS7qU_/view?usp=sharing) in your chosen `directory` and then running the following commands 

```
import numpy as np
import load_datasets 

folder = # provide the file path to the directory you chose here
X = load_datasets.get_dataset('grassmannian_cluster_algebras', n=6, folder = folder)
```

Dataset statistics are as follows

|  | SSYT indexes a cluster variable | SSYT does not index a cluster variable | Total number of instances | 
|----------|----------|----------|----------|
| Train | 74,329 | 74,329 | 148,658 |
| Test  | 18,582 | 18,582 | 37,164 |

## Data generation

The positive examples sampled for this dataset were generated using code from the paper [\[2\]](https://arxiv.org/abs/2212.09771). This code can be found at [https://github.com/edhirst/GrassmanniansML](https://github.com/edhirst/GrassmanniansML). We generated our own negative examples because we found that the model learned some spurious correlations as a result of the sampling strategy used in [\[2\]](https://arxiv.org/abs/2212.09771). To sample random rectangular SSYT, we took advantage of the [`random_element()`](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/tableau.html#sage.combinat.tableau.SemistandardTableaux_shape.random_element) method in the `Tableaux` class in Sage.

## Task

**Math question:** Find a concise characterization of those SSYT that index cluster variables.

**ML task:** Train a model that can predict whether a SSYT indexes a cluster variable or not. 

## Small model performance

| Architecture  | Accuracy | 
|----------|----------|
| Logistic regression | 65.7% | 
| MLP | 99.3% $\pm$ 0.1% | 
| Transformer | 99.5% $\pm$ 0.1% | 
| Guessing '0' or '1' | 50% |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training. 

## References

\[1\] Chang, Wen, et al. "Quantum affine algebras and Grassmannians." Mathematische Zeitschrift 296.3 (2020): 1539-1583.

\[2\] Cheung, Man-Wai, et al. "Clustering cluster algebras with clusters." arXiv preprint arXiv:2212.09771 (2022).

![image](https://github.com/user-attachments/assets/384d06f0-9052-45a3-a9c8-d81f084fdad2)
