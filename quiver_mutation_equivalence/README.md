# Mutation equivalence of quivers (open problem)

Quivers and quiver mutations are central to the combinatorial study of cluster algebras, algebraic structures with connections to Poisson Geometry, string theory, and Teichmuller theory. Quivers are directed graphs, and a quiver mutation is a local transformation of the graph involving certain vertices and arrows that produces a new quiver. A fundamental open problem in this area is to find an algorithm that determines whether two quivers are mutation equivalent. Currently, no such algorithm exists for quivers on more than three vertices.  

Recent work has explored whether deep learning models can learn to correctly predict if two quivers are mutation equivalent \[1\]. Our dataset aims to facilitate continuation of this work. In \[1\] and in our dataset, quivers are represented using adjacency matrices. 

**Dataset:** The dataset consists of djacency matrices for 6 different equivalence classes of quivers (types $A$, $D$, $\tilde{A}$, $E$, $\tilde{E}$. In more detail, the training set consists of
- All quivers of types $A$, $D$, $\tilde{A}$, and $\tilde{D}$ on 7, 8, 9, and 10 nodes.
- All quivers of type $\tilde{E}$. (Type $\tilde{E}$ is only defined for 7, 8, and 9 nodes, corresponding to extended versions of $E\_6$, $E\_7$, and $E\_8$, respectively). All quivers of type $\tilde{E}$ are mutation-finite.)
- All quivers of type $E$ for $n = 6, 7, 8$. (The Dynkin diagram $E\_9$ is the same as the extended diagram $\tilde{E}\_8$.) Type $E$ is only mutation-finite for $n = 6, 7, 8$ and coincides with $\tilde{E}$ for $n = 9$.
- Quivers of type $E\_{10}$ up to a mutation depth of 8, with respect to Sage’s standard orientation for $E\_{10}$ (Fig. 9). (While type $E$ is mutation finite for $n \leq 9$, $E_{10}$ is mutation-infinite).
The test set consists of quivers on 11 nodes. We use the full mutation classes of $A\_{11}$, $\tilde{A\_{10}}$, $D\_{11}$ and $\tilde{D}\_{10}$, and again generate quivers up to a mutation depth of 8 for $E\_{11}$.

Datasets can be found [here](https://drive.google.com/file/d/1UmRLOhNq2mX6s4NQPIgciuGG9HfvrKWC/view?usp=sharing)

Dataset statistics are as follows:

| | $A_{11}$ | $B_{11}$ | $BD_{11}$ | $BE_{11}$ | $D_{11}$ | $DE_{11}$ | $E_{11}$ | Total |
|---|---|--|---|---|---|----|----|---|
| Training | 11,940 | 27,410 | 23,651 | 22,615 | 25,653 | 23,528 | 28,998 | 163,795 |
| Test | 2,984 | 6,852 | 5,912 | 5,653 | 6,413 | 5,881 | 7,249 | 40,944 |


## Data generation

## Task

**Math question:** Find simple rules to determine whether or not a quiver belongs to a specific mutation equivalence class (out of classes $A$, $D$, $\tilde{A}$, $\tilde{D}$, $E$, and $\tilde{E}$).

**ML task:** Train a model that can predict a quiver's mutation equivalence class out of the 6 options above.

See the work [\[2\]](https://arxiv.org/abs/2411.07467) for an example of how a model trained on this dataset can be used to re-discover known theorems.

## Small model performance

|  | Accuracy | 
|----------|----------|
| Logistic regression | $40.3\%$ |
| MLP | $86.5\% \pm 1.9\%$ | 
| Transformer | $92.9\% \pm 0.5\%$ |
| Guessing largest class | $17.7\%$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

\[1\] Bao, Jiakang, et al. "Machine learning algebraic geometry for physics." arXiv preprint arXiv:2204.10334 (2022).

\[2\] He, Jesse, et al. "Machines and Mathematical Mutations: Using GNNs to Characterize Quiver Mutation Classes." arXiv preprint arXiv:2411.07467 (2024).
