# Benchmarks in Algebraic Combinatorics
## A Collection of Algebraic Combinatorics Benchmark Datasets for Scientific Discovery in Mathematics and the Evaluation of Reasoning in Machine Learning

The challenge of sifting through large datasets with the goal of identifying structure and patterns is a common activity in research level mathematics. As an obvious example, entire careers have been spent looking for patterns in the set of prime numbers. Since modern machine learning is increasingly capable of pulling subtle patterns out of highly structured, complicated datasets at scale, there is hope that data-driven approaches may be able to accelerate the pace of research in mathematics.

From the other direction, mathematics offers a useful arena in which to study machine learning itself. Mathematics, unlike many other tasks that machine learning is applied to, tends to have solutions which are formally understood and can be rigorously checked. While there are now a number of benchmarks aimed at evaluating the performance of machine learning models in mathematics, they all tend to be oriented toward large language models and mostly fail to capture the sophistication of research level mathematics. But as any mathematician can attest, mathematics is not purely tied to language. Thus, there is value in making available "raw" mathematics datasets which represent real problems in mathematics.

Motivated by this we introduce **Benchmarks in Algebraic Combinatorics (ACBench)**, a collection of datasets drawn from the mathematical domain of algebraic combinatorics, an area of mathematics which studies discrete structures arising from the field of abstract algebra, including representation theory, algebraic geometry, etc.

We have included two types of datasets in these benchmarks:
- **Datasets that capture open problems:** Using machine learning to drive scientific discovery has been a fundamental goal within the AI-community since its inception. One challenge, particularly in mathematics, is that the data supporting such discovery is itself often complicated, requiring a domain expert to collect/generate, preprocess, and explain. To lower the barrier of entry to the machine learning community, we include datasets centered around open problems in algebraic combinatorics. We hope that use of these by the AI-community will translate into progress in mathematics. 
- **Datasets that capture classical or foundational subjects and algorithms in algebraic combinatorics:** On the other hand, there are cases where it is valuable to be able to evaluate ML approaches to mathematics where a solution is known. It might be interesting to understand whether a particular ML algorithm rediscovers a known result and if not, whether there are other approaches that have been missed until now by the mathematical community. 

For both types of datasets we (will eventually) include the code for generating the dataset, the official train/test splits, background information which explains the dataset and problems associated with it, and some baseline performances of models trained and evaluated on splits.

**Contributors:**
- Herman Chau (University of Washington)
- Helen Jenne (Pacific Northwest National Laboratory)
- Davis Brown (Pacific Northwest National Laboratory)
- Sara Billey (University of Washington)
- Jackson Warley (Pacific Northwest National Laboratory)
- Jesse He (UCSB)

**Maintainer:** Henry Kvinge (Pacific Northwest National Laboratory, University of Washington)

### Datasets
- [**Grassmannian cluster algebras:**](https://github.com/pnnl/ML4AlgComb/tree/master/grassmannian_cluster_algebras) Identify when a rectangular semistandard Young tableau corresponds to a cluster variable in a cluster algebra associated with the Grassmannian manifold.
- [**Kazhdan-Lusztig polynomial coefficients:**](https://github.com/pnnl/ML4AlgComb/tree/master/kl-polynomial_coefficients) Kazhdan-Lusztig polynomials, which are parametrized by two permutations, are known to carry extensive combinatorial information yet in many ways remain mysterious. The goal of this task is to predict the coefficients on these polynomials from the indexing permutation alone.
- [**Lattice path posets:**](https://github.com/pnnl/ML4AlgComb/tree/master/lattice_path_posets) The set of lattice paths from $(0,0)$ to $(n,n-1)$ which only take steps east and north and never cross the diagonal $y = \frac{n}{n-1}x$ capture the combinatorics of a range of important phenomena in mathematics. One way to study the set of such paths is to impose a partial order on them. The task for this dataset involves predicting which of two poset structures a
- [**The mHeight function:**](https://github.com/pnnl/ML4AlgComb/tree/master/mheight_function)
- [**Mutation equivalence of quivers:**](https://github.com/pnnl/ML4AlgComb/tree/master/quiver_mutation_equivalence)
- [**The Robinson-Schensted-Knuth Correspondence:**](https://github.com/pnnl/ML4AlgComb/tree/master/rsk)
- [**Schubert polynomial structure constants:**](https://github.com/pnnl/ML4AlgComb/tree/master/schubert_polynomial_structure)
- [**Symmetric group characters:**](https://github.com/pnnl/ML4AlgComb/tree/master/symmetric_group_character)
- [**Weaving patterns:**](https://github.com/pnnl/ML4AlgComb/tree/master/weaving_patterns)

**Would you like to contribute a dataset?:** Please contact us acbenchdataset@gmail.com.

Disclaimer:
This material was prepared as an account of work sponsored by an agency of the United States Government.  Neither the United States Government nor the United States Department of Energy, nor the Contractor, nor any or their employees, nor any jurisdiction or organization that has cooperated in the development of these materials, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product, software, or process disclosed, or represents that its use would not infringe privately owned rights.
Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.
PACIFIC NORTHWEST NATIONAL LABORATORY
operated by
BATTELLE
for the
UNITED STATES DEPARTMENT OF ENERGY
under Contract DE-AC05-76RL01830
