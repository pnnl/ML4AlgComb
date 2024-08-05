# Mutation equivalence of quivers (open problem)

Quivers and quiver mutations are central to the combinatorial study of cluster algebras, algebraic structures with connections to Poisson Geometry, string theory, and Teichmuller theory. Quivers are directed graphs, and a quiver mutation is a local transformation of the graph involving certain vertices and arrows that produces a new quiver. A fundamental open problem in this area is to find an algorithm that determines whether two quivers are mutation equivalent. Currently, no such algorithm exists for quivers on more than three vertices.  

Recent work has explored whether deep learning models can learn to correctly predict if two quivers are mutation equivalent \[1\]. Our dataset aims to facilitate continuation of this work. In \[1\] and in our dataset, quivers are represented using adjacency matrices. 

**Dataset:** Adjacency matrices for seven quivers, each with $11$ vertices, labeled by mutation equivalence class.

**Task:** Classify which mutation equivalence class an adjacency matrix corresponds to.

Datasets can be found [here](https://drive.google.com/file/d/1UmRLOhNq2mX6s4NQPIgciuGG9HfvrKWC/view?usp=sharing)

## Baselines

### MLP

| Model Type | Accuracy | # of Layers |
|----------|----------|----------|
| MLP | $88.7 \pm 0.00\%$ | 5 |


\[1\] Bao, Jiakang, et al. "Machine learning algebraic geometry for physics." arXiv preprint arXiv:2204.10334 (2022).
