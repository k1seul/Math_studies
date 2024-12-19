# Linear Algebra assignment for [Abstract Linear Algebra for Machine Learning(Quantum Formalism)](https://quantumformalism.com/abstract-linear-algebra-for-ml)
Lecture given by [Rakvi S. Ph.D](https://raakvi.wixsite.com/rakvi)
## Algebra, Topology, Differential Calculus and Optimization for computer Science and Machine Learning [Textbook Link](https://www.cis.upenn.edu/~jean/math-deep.pdf)
2000 page math book. 😇
Solving Problem sets form the book.

## Lecture Overview

Mathematical Foundations:

* In-Depth Linear Algebra: Dive deep into vector spaces, eigenvalues, eigenvectors, transformations, and more.
Rigorous Proof Writing: Develop your ability to construct and understand mathematical proofs, enhancing your analytical skills.
* Interactive Learning: Participate in live lectures, receive personalized feedback on homework assignments, and engage in live tutorials to reinforce your understanding.
Applications in Machine Learning:

* Algorithm Exploration: Learn how advanced linear algebra concepts are applied in machine learning algorithms like PCA, SVD, and neural networks.
Real-World Use Cases: Analyze case studies and participate in projects that demonstrate the practical applications of linear algebra in ML.
* Guest Speakers and Tutorials: Gain insights from industry experts and guest speakers who will share their experiences and best practices in the field.

# Weekly Subjects and Homeworks

- **Topics**: Groups, Rings, and Fields  
- **Learning Objectives**:  
  - Understand the basic definitions and properties of groups, rings, and fields.  
  - Explore examples and counterexamples to solidify understanding.  
  - Learn about group homomorphisms and ring homomorphisms.  

- **Progress**:  
  - Studied the definitions of groups, rings, and fields from the textbook.  
  - Understood the ring axioms and explored examples such as integers modulo \(n\).  
  - Reviewed field properties, focusing on finite fields and their applications.
 
- **Summary** (generated with gpt) 
# Groups, Rings, and Fields

## Group
A **group** is a set \( G \) equipped with a binary operation \( \cdot \) that satisfies the following properties:
1. **Closure**: For all \( a, b \in G \), \( a \cdot b \in G \).
   \[
   \forall a, b \in G, \, a \cdot b \in G
   \]
2. **Associativity**: For all \( a, b, c \in G \),
   \[
   (a \cdot b) \cdot c = a \cdot (b \cdot c)
   \]
3. **Identity Element**: There exists an element \( e \in G \) such that for all \( a \in G \),
   \[
   a \cdot e = e \cdot a = a
   \]
4. **Inverse Element**: For every \( a \in G \), there exists an element \( b \in G \) such that
   \[
   a \cdot b = b \cdot a = e
   \]
where \( e \) is the identity element.

If the group operation is commutative, i.e.,
\[
a \cdot b = b \cdot a \quad \forall a, b \in G,
\]
the group is called an **abelian group**.

---

## Ring
A **ring** is a set \( R \) equipped with two binary operations, usually called addition \( + \) and multiplication \( \cdot \), such that:
1. \( (R, +) \) is an abelian group (with additive identity \( 0 \)).
   \[
   \forall a, b, c \in R, \, (a + b) + c = a + (b + c), \quad a + 0 = a, \quad \text{and} \quad a + (-a) = 0
   \]
2. \( (R, \cdot) \) is a semigroup (i.e., associative).
   \[
   \forall a, b, c \in R, \, (a \cdot b) \cdot c = a \cdot (b \cdot c)
   \]
3. **Distributive Laws**: For all \( a, b, c \in R \),
   \[
   a \cdot (b + c) = a \cdot b + a \cdot c, \quad \text{and} \quad (a + b) \cdot c = a \cdot c + b \cdot c
   \]

If \( R \) also satisfies:
- \( \cdot \) is commutative,
- \( R \) has a multiplicative identity \( 1 \neq 0 \),

then \( R \) is called a **commutative ring with identity**.

---

## Field
A **field** is a commutative ring \( F \) with identity \( 1 \neq 0 \), such that every nonzero element \( a \in F \) has a multiplicative inverse \( a^{-1} \in F \), satisfying
\[
a \cdot a^{-1} = 1
\]

In other words, a field satisfies the following:
1. \( (F, +) \) is an abelian group:
   \[
   \forall a, b, c \in F, \, (a + b) + c = a + (b + c), \quad a + 0 = a, \quad \text{and} \quad a + (-a) = 0
   \]
2. \( (F \setminus \{0\}, \cdot) \) is an abelian group:
   \[
   \forall a, b \in F \setminus \{0\}, \, a \cdot b = b \cdot a, \quad \text{and} \quad a \cdot a^{-1} = 1
   \]
3. Multiplication distributes over addition:
   \[
   \forall a, b, c \in F, \, a \cdot (b + c) = a \cdot b + a \cdot c
   \]

Examples of fields include \( \mathbb{Q} \) (rational numbers), \( \mathbb{R} \) (real numbers), and \( \mathbb{C} \) (complex numbers).



