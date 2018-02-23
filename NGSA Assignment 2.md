# NGSA: Assignment 1

## I. Graph Theory and Graph Properties
### Question 1
#### ($a$) $$k = A \cdot \overrightarrow{1}$$
#### ($b$) $$m = \frac{1}{2}\sum_{i,j}{A_{i,j}} $$
#### ~~(c )~~ $$N_{i,j} = \sum{(\overrightarrow{A_i} + \overrightarrow{A_i}  == 2)}$$
____
### Question 2
Total edges = $c_1 \times n_1 = c_2 \times n_2$
$\implies c_2 = \frac{n_1}{n_2} \cdot c_1$
___
### Question 3
#### ($a$)$$\Delta(G) = \frac{1}{6} \times trace(A^3)$$ 
#### ($b$)$$\Delta(G) = \frac{1}{6} \sum_{i=1}^{n}\lambda_i^3$$
#### ($c$)$$\Delta_i = \frac{\sum_j \lambda_j^3 u_{i,j}^2}{2}$$
where $\lambda$ is the eigenvalue of A and $u_{i,j}$ is the i-th entry of the j-th eigenvector
______
## II. Graph Models
### Question 4
#### ($a$)  $$total\ edges = n\times c = p \times (n^2 -n)$$
$$p = \frac{c}{n-1}$$
$t \leftarrow C_n^3$ is all the possible set of 3 nodes
$X_1 \dotsc X_n is \ a \ set\ where \ X_j = 1$ iff j-th set can form a triange
$$\mathbb{E} \sum_{j=1}^{t}X_j = \sum_{j=1}^{t}\mathbb{E}X_j = tp^3 = \frac{n(n-1)(n-2)}{6}\cdot \frac{c^3}{(n-1)^3} $$
$$= \frac{c^3}{6}\cdot \frac{n^2-2n}{n^2-2n+1} \xrightarrow[] {n\ is\ large} \frac{1}{6}c^3$$

#### ($b$) Similar to ($a$): $\mathbb{E}X_j = 3\times p^2$ for a triplet. 
$$\mathbb{E} \sum_{j=1}^{t}X_j = \sum_{j=1}^{t}\mathbb{E}X_j = 3t p^2$$
$$= \frac{c^2}{2}\cdot \frac{n(n-2)}{n-1} \xrightarrow[] {n\ is\ large} \frac{1}{2}nc^2 $$

#### ($c$) $$C \xrightarrow[] {n\ is\ large}  \frac{\frac{1}{2}c^3}{\frac{1}{2} nc^2} = \frac{c}{n}$$

## III. Centrality Criteria
### Question 5
#### ($a$)$$x_i = 1+ \sum_j \alpha^{d_{i,j}}$$
#### ($b$)
	for i in range(n):
		for j in range(n):
			x_i = 1+sum(alpha ^ d(i,j))
the complexity is O($n^2$)
### Question 6
Set the sum of the distance of all the nodes in $n_A$ to A is a; The sum of the distance of all the nodes in $n_B$ to B is b. Thus:
$$C_A = \frac{n}{a+b+n_B}$$
$$C_B = \frac{n}{a+b+n_A}$$
## IV. Analyzing a Real Network
### Question 7
#### ($a$)
#### ($b$)
#### ($c$)
#### ($d$)

### Question 8
#### ($a$)
#### ($b$)
#### ($c$)
### Question 9
#### ($a$)
#### ($b$)
### Question 10
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEyNzA1NjY4MF19
-->