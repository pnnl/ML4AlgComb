# Mutation equivalence of quivers (open problem)

Quivers and quiver mutations are central to the combinatorial study of cluster algebras, algebraic structures with connections to Poisson Geometry, string theory, and Teichmuller theory. Quivers are directed graphs, and a quiver mutation is a local transformation of the graph involving certain vertices and arrows that produces a new quiver. A fundamental open problem in this area is to find an algorithm that determines whether two quivers are mutation equivalent. Currently, no such algorithm exists for quivers on more than three vertices.  

Recent work has explored whether deep learning models can learn to correctly predict if two quivers are mutation equivalent \[1\]. Our dataset aims to facilitate continuation of this work. In \[1\] and in our dataset, quivers are represented using adjacency matrices. 

**Dataset:** Adjacency matrices for seven quivers, each with $11$ vertices, labeled by mutation equivalence class.

[comment]: <> (
All quivers of types A, D, A ̃, and D ̃ on 7, 8, 9, and 10 nodes.
• All quivers of type E ̃. (Type E ̃ is only defined for 7, 8, and 9 nodes, corresponding to
extended versions of E6, E7, and E8, respectively. All quivers of type E ̃ are mutation-finite.)
• All quivers of type E for n = 6, 7, 8. (The Dynkin diagram E9 is the same as the extended diagram E ̃8.) Type E is only mutation-finite for n = 6, 7, 8. and coincides with E ̃8 for n = 9.
• Quivers of type E10 up to a mutation depth of 8, with respect to Sage’s standard orientation for E10 (Fig. 9). (While type E is mutation finite for n ≤ 9, E10 is mutation-infinite).
The test set consists of quivers on 11 nodes. We use the full mutation classes of A11, A ̃10, D11 and D ̃10, and again generate quivers up to a mutation depth of 8 for E11. The number of quivers of each size from each class can be found in Table 1 in Appendix B.2. Note that type E ̃ is absent from the test set, because E ̃ is not defined for 11 nodes.)

Datasets can be found [here](https://drive.google.com/file/d/1UmRLOhNq2mX6s4NQPIgciuGG9HfvrKWC/view?usp=sharing)

## Data generation

## Task

**Math question:** Find simple rules to determine whether or not a quiver belongs to a specific mutation equivalence class (out of several mutation classes of Lie type).

**ML task:** Train a model that can predict whether a SSYT indexes a cluster variable or not. 

## Small model performance

| Size | Logistic regression | MLP | Transformer | Guessing 0 | 
|----------|----------|-----------|------------|------------|
| $n= 5$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |
| $n= 6$ | $0.0$ | $0.0 \pm 0.0$ | $0.0 \pm 0.0$| $0.0$ |

The $\pm$ signs indicate 95% confidence intervals from random weight initialization and training.

\[1\] Bao, Jiakang, et al. "Machine learning algebraic geometry for physics." arXiv preprint arXiv:2204.10334 (2022).
