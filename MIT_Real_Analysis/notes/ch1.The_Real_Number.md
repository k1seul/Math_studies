
# The Real Number
(based on [Understanding Analysis](https://link.springer.com/book/10.1007/978-1-4939-2712-8), by Stephen Abbott)
## 1) The Axiom of Completeness 

* Brief Definition of real number

The $\mathbb{R}$ is a set containing the rationals $\mathbb{Q}$ such that it is a *ordered field* that has additive and multiplicative inverses. 

#### Definition 1.1.1 *Field* 
A set $F$ is a *field* if there exist two operations addition and multiplication that satisfies the following conditions 
1. (commutativity) $x+y = y+x$ and $xy = yx$ for all $x, y \in F$
2. (associativity) $(x+y)+z = x +(y+z)$ and $(xy)z = x(yz)$ for all $x, y, z \in F$
3. (identities exist) There exist two special elements $0$ and $1$ with $0 \neq 1$ such that 
$x + 0 = x$ and $x1 =x$ for all $x \in F$
4. (inverse exist) Given $x \in F$, there exists an element $-x \in F$ such that $x + (-x) =0$.
If $x \neq 0$, there exists an element $x^{-1}$ such that $xx^{-1} =1$
5. (distributive property) $x(y+z) = xy + yz$ for all $x, y, z \in F$

#### Definition 1.1.2 *Ordering*
1. For arbitrary $x, y \in F$, at least one of the statements $x \leq y$ or $y \leq x$ is true.
2. If $x \leq y$ and $y \leq x$, then $x = y$
3. If $x \leq y$ and $y \leq z$, then $x \leq z$
4. If $y \leq z$, then $x + y \leq x + z$
5. If $x \geq 0$ and $y \geq 0$, then $xy \geq 0$

### Axiom 1.1.3 Axiom of Completeness
*Every nonempty set of real numbers that is bounded above has a least upper bound*

#### Definition 1.1.4 *Bounded Above*
A set $A \subseteq \mathbb{R}$ is *bounded above* if there exists a number $b \in \mathbb{R}$ s.t. $a \leq b \ \forall a \in A$ and $b$ is called a *upper bound*.

#### Definition 1.1.5 *Least Upper Bound*
A real number $s \in \mathbb{R}$ is called *least upper bound* for a set $A \subseteq \mathbb{R}$ if it satisfies
1. $s$ is a upper bound of $A$
2. if $b$ is a upper bound of $A$, then $b \geq s$


#### Definitions 1.1.6 Supremum and Infimum

###! Supremum (Sup)
The **supremum** of a set $A \subseteq \mathbb{R}$ is defined as the least upper bound of that set. It is denoted as $\sup A$ and has the following properties:

1. **Upper Bound**: $\sup A$ is an upper bound of $A$, meaning:
   $$
   a \leq \sup A \quad \forall a \in A
   $$

2. **Least Upper Bound**: If $b$ is any upper bound of $A$, then:
   $$
   \sup A \leq b
   $$

In other words, $\sup A$ is the smallest number that is greater than or equal to every element in the set $A$.

### Infimum (Inf)
The **infimum** of a set $A \subseteq \mathbb{R}$ is defined as the greatest lower bound of that set. It is denoted as $\inf A$ and has the following properties:

1. **Lower Bound**: $\inf A$ is a lower bound of $A$, meaning:
   $$
   \inf A \leq a \quad \forall a \in A
   $$

2. **Greatest Lower Bound**: If $c$ is any lower bound of $A$, then:
   $$
   c \leq \inf A
   $$

In simpler terms, $\inf A$ is the largest number that is less than or equal to every element in the set $A$.

#### Example 1.1.6
By the axiom of completeness, there is a real number $c \in \mathbb{R}$, which is the least upper bound 
of $S = \{ r \in \mathbb{Q}: r^2 < 2 \}$ 
We can define $\sqrt{2} = \sup S$

#### Lemma 1.1.7 
Assume $s \in \mathbb{R}$ is an upper bound of a set $A \subseteq \mathbb{R}$. Then, $s = \sup A$ if and only if, for every choice of $\epsilon >0$, there exists an element $a \in A$ satisfying $s - \epsilon < a$
**Proof**:
* Forward case:
If $s$ is a least upper bound, $\forall \epsilon > 0$, $s - \epsilon$ is no longer a upper bound. (simple proof by contradiction)
$$\therefore \exists a \in A \text{ s.t. } s-\epsilon < a$$
* Backward case 
If $s < \sup A$
$$\exists \epsilon = \frac{\sup A - s}{2} > 0 \text{ s.t.}$$
$$\exists a \in A \ \ s < s + \epsilon < a < \sup A$$
$s$ is not a upper bound. contradiction.

if $s > \sup A$
$$\exists \epsilon = \frac{s - \sup A}{2} > 0 \text{ s.t.}$$
$$\sup A < s - \epsilon <  s$$
$s$ is not least upper bound. contradiction.

$\therefore$ By the ordering principle of real number $s = \sup A$ $\Box$


## 2) Consequences of Completeness

### Theorem 1.2.1 Nested Interval Property
For each $n \in \mathbb{N}$, given closed inverval $I_n = [a_n, b_n] = \{x \in \mathbb{R} : a_n \leq x \leq b\}$ Also assume, each $I_n$ contains $I_{n+1}$ then, 
$$I_1 \supseteq I_2 \supseteq I_3 \dots$$
$$\bigcap_{n=1}^{\infty} I_n \neq \emptyset$$

**Proof**
Let 
$$A = \{a_n : n \in \mathbb{N}\}$$
by setting 
$$x = \sup A$$
$$x \in I_n, \ \ \forall n \in \mathbb{N}$$
Thus,
$$x \in \bigcap_{n=1}^{\infty} I_n$$
$$\therefore \bigcap_{n=1}^{\infty} I_n \neq \emptyset$$


#### Theorem 1.2.2 Archimedean Property
i. Given any number $x \in \mathbb{R}, \ \ \exists n \in \mathbb{N} \text{ s.t. } n > x$
ii. Given any real number $y>0, \ \ \exists n \in \mathbb{N} \text{ s.t. } 1/n < y$

**Proof**:
Proof by contradiction
Let $\mathbb{N}$ bounded above, then by **AOC**
$$\exists a \in \mathbb{R} \text{ s.t. } a = \sup A$$
$$\exists n \in \mathbb{N}, a - 1 < n \text{ by lemma 1.1.7}$$
$$a < n + 1 \in \mathbb{N}$$
Contradiction $\Box$
ii is just a case when $x = 1/y$

#### Theorem 1.2.3 Density of $\mathbb{Q}$ in $\mathbb{R}$
for every two real number $a,b \ \ (a <b)$ there exists rational $r$ s.t. $a < r <b$

**Proof**
By Archimedean Property
$$\exists n \in \mathbb{N} \text{ s.t. } \frac{1}{n} < b -a$$
pick $m \in \mathbb{Z}$ s.t. 
$$m - 1 \leq na \leq m$$
$$m \leq na + 1 < n(b - \frac{1}{n}) + 1 =nb$$
$$na < m, m < nb$$
$$\therefore a < \frac{m}{n} < b$$

#### Theorem 1.2.4 
Suppose $x,y \in \mathbb{R}$ and $x < y$. Prove there exists $i \in \mathbb{R} \setminus \mathbb{Q}$ such that $x < i < y$.

**Proof**
Proof by Contradiction:
Let
$$x, y \in \mathbb{R} \text{ and } x < y, \text{ there is no irrational between } x, y \tag{a}$$

$$x - \sqrt{2} \in \mathbb{R}, \quad y - \sqrt{2} \in \mathbb{R}$$
$$\text{Since } \exists r \in \mathbb{Q} \text{ such that } x - \sqrt{2} < r < y - \sqrt{2}$$
$$x < r + \sqrt{2} < y$$
$$\text{And by (a), } r + \sqrt{2} \in \mathbb{Q}$$
$$\text{Thus, } \sqrt{2} \in \mathbb{Q}$$
Contradiction.

$\therefore$  If $x,y \in \mathbb{R}$ and $x < y$, then there exists $i \in \mathbb{R} \setminus \mathbb{Q}$ such that $x < i < y$.


---
> Written with [StackEdit](https://stackedit.io/).
