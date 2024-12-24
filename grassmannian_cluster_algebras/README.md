# Grassmannian Cluster Algebras and Semistandard Young Tableau (open problem)

The Grassmann manifold $\text{Gr}(k,n)$ is the set of full-rank $k \times n$ matrices up to equivalence of elementary row operations (equivalently the space whose points are $k$-dimensional subspaces in $\mathbb{R}^n$). Grassmannians are of fundamental geometric importance and are a central tool in a model of quantum field theory known as supersymmetric Yang-Mills theory. 

Among the many algebraic-combinatorial properties of Grassmannians is an algebraic structure on its coordinate ring making it into an algebraic object called a cluster algebra. A recent result of [Chang, Duan, Fraser, and Li \[1\]](https://arxiv.org/abs/1907.13575) parameterize cluster variables of the Grassmannian coordinate ring in terms of equivalence classes of semistandard Young tableaux (SSTY). Not every SSTY indexes a cluster variable and a natural question to ask is whether there is a naive combinatorial rule that specifies whether a particular SSTY indexes a cluster variable. One necessary condition is that the tableaux is of rectangular shape. 

The idea to apply machine learning to this problem was first posed by [\[2\]](https://arxiv.org/abs/2212.09771). We follow their set up and use the positive examples that they computed (i.e., SSTY that index a cluster variable). However, we choose a different method of sampling tableau that do not index cluster variables that we found makes the problem harder (and therefore forces the model to learn more robust features).

## Details and an example

In the cluster algebra associated with Grassmann manifold $\text{Gr}(k,n)$, each cluster variable variable is indexed by a rectangular SSYT with $k$ rows with entries drawn from $\{1,\dots,n\}$ (because this is a SSYT, the entries need to weakly increase as one moves left to right in the rows and strictly increase as one moves down each column). The *rank* of these rectangular SSTY (and the rank of the associated cluster algebras) is given by their number of columns. Following [\[2\]](https://arxiv.org/abs/2212.09771), in this dataset we focus on $\text{Gr}(3,12)$ and hence look at rectangular SSTY with 4 rows filled with entries drawn from $\{1,\dots,12\}$. We further restrict to rank 4 SSYT. This leaves us with a collection of $3 \times 4$ arrays whose entries increase weakly across rows and strictly down columns. 

To give two examples 



## Dataset 

The dataset consists of a collection of rectangular SSYT each with a label indicating whether they index a cluster variable or not. Those that do not index a cluster variable are labeled with a `0` and those that do are labeled with a `1`. The dataset we provide consists of tableau of shape $3 \times 4$, filled with values from $1,2,\dots,12$. The files we provide are: 
- ``3_4_12_invalid_train.txt``
- ``3_4_12_invalid_test.txt``

These contain tableau that do not correspond to cluster variables, 'invalid examples'. Files containing the valid examples can be obtained at [https://github.com/edhirst/GrassmanniansML](https://github.com/edhirst/GrassmanniansML). We will provide code at [https://github.com/pnnl/ML4AlgComb](https://github.com/pnnl/ML4AlgComb) to generate the full splits from the data obtained at these two sources.

We use braces $[$ and $]$ to demarcate rows of the dataset, so that

``[[2, 3, 4, 7], [3, 5, 6, 8], [4, 9, 11, 12]]``

corresponds to the tableau pictured in the Figure below

<img src="fig-grassmannian-tableau-example.png" alt="drawing" width="200"/>

## Task

Predict whether a Young tableaux indexes a cluster variable.

The datasets can be found [here](https://drive.google.com/file/d/1Dd4PAOgm7bAtXSGmQW81OE-O_7dS7qU_/view?usp=sharing)

## Data generation

## Small model performance

| Architecture  | Accuracy | 
|----------|----------|
| Logistic regression |  | 
| MLP |  | 
| Transformer |  | 

\[1\] Chang, Wen, et al. "Quantum affine algebras and Grassmannians." Mathematische Zeitschrift 296.3 (2020): 1539-1583.

\[2\] Cheung, Man-Wai, et al. "Clustering cluster algebras with clusters." arXiv preprint arXiv:2212.09771 (2022).

