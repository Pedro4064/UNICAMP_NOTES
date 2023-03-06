# Sistema Linear - Método Gauss-Jacobi

Aula: Aula 09
Created: September 27, 2021 5:22 PM
Prova: P1

- SUMÁRIO

# Introdução

$\hookrightarrow$ Esse método, diferentemente dos outros, é considerado um método iterativo.

$\hookrightarrow$ Com isso, iremos encontrar uma aproximação mais refinada a partir de um vetor inicial.

$\hookrightarrow$ É mais interessante irmos por um método iterativo ao invés de um método direto quando estamos trabalhando com um sistema linear esparso, isso é, nossa matriz muito grande que possui uma quantidade elevada de zeros.

# Algoritmo

## 1º Passo

$\hookrightarrow$ Para o algoritmo Gauss-Jacobi nós sempre iniciamos com o sistema original escrito em sua forma de sistema, e não de matriz:

$$
A_{n,n}x = b
$$

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + ...+ a_{1n}x_n &= b_1 \\ 
a_{21}x_1 + a_{22}x_2 + ...+ a_{2n}x_n &= b_2 \\ 
... \\
a_{n1}x_1 + a_{n2}x_2 + ...+ a_{nn}x_n &= b_n \\ 
\end{cases}
$$

## 2º Passo

$\hookrightarrow$ Agora podemos isolar $x_i$  na $i$-ésima linha, supondo que $a_{ii} \ne 0$.

$$
\begin{cases}
x_1^{(k+1)} &= \frac{1}{a_{11}}[b_1 - ( a_{12}x_2 + ...+ a_{1n}x_n)] \\ 
x_2^{(k+1)} &= \frac{1}{a_{22}}[b_2 - ( a_{21}x_1+ a_{23}x_3 + ...+ a_{2n}x_n)] \\ 
... \\ 
x_n^{(k+1)} &= \frac{1}{a_{nn}}[b_n - ( a_{n1}x_1+ a_{n2}x_2 + ...+ a_{n,n-1}x_{n-1})] \\ 
\end{cases}
$$

$\hookrightarrow$ Onde o $x$ isolado é da etapa $k+1$ e o que está do lado direito é o da iteração anterior.

## Critérios de Parada

- Critério Absoluto
    - Quando utilizamos um critério absoluto nós comparamos a **norma infinita** do vetor encontrado com a norma do vetor da iteração passada.
    - A norma infinita é o valor absoluto do maior número do vetor.
    
    $$
    ||x^{(k)} - x^{(k-1)}||_\infty = \max\{||x^{(k)} - x^{(k-1)}||\} \le \varepsilon
    $$
    
- Critério Relativo
    - Levamos em consideração a ordem de grandeza do que estamos comparando:
    
    $$
    \frac{||x^{(k)} - x^{(k-1)}||_\infty}{||x^{(k)}||_\infty} =  \frac{\max\{|x_1^{(k)} - x_1^{(k-1)}|, |x_2^{(k)} - x_2^{(k-1)}|, ...\}}{\max\{|x_1^k|,|x_2^k|, ... \}} \le \varepsilon
    $$
    

# Ponto Fixo Matricial

$\hookrightarrow$ Assim como nós falamos sobre o método de Newton para resolvermos problemas de zero de função por ponto fixo, o método de Gauss-Jacobi também é um algoritmo de ponto fixo, só que matricial.

$\hookrightarrow$ Onde temos por objetivo transformar um sistema de equações:

$$
Ax=b \iff x = G(x) = Cx +g
$$

 $\hookrightarrow$ Tal que:

$$
x^{(k+1)} = G(x^{(k)}) = Cx^{(k)} + g
$$

$\hookrightarrow$ De tal forma que em Gauss-Jacobi temos:

$$
C = \begin{bmatrix}0 & \frac{-a_{12}}{a_{11}} & \frac{-a_{13}}{a_{11}} & ...  & \frac{-a_{1n}}{a_{11}}\\
\frac{-a_{21}}{a_{22}}& 0 & \frac{-a_{23}}{a_{22}} & ...  & \frac{-a_{2n}}{a_{22}}\\
... \\ 
\frac{-a_{n1}}{a_{nn}} & \frac{-a_{n2}}{a_{nn}}& \frac{-a_{n3}}{a_{nn}} & ...  & 0\\

\end{bmatrix}
$$

$$
g = \begin{bmatrix}
b_1/a_{11} \\
b_2/a_{22} \\ 
.\\
.\\
.\\
b_n / a_{nn}

\end{bmatrix}
$$

## Convergência de Métodos Iterativos

$\hookrightarrow$ Seja $\lambda_i$ os autovalores de uma matriz $Z$ qualquer e $|\lambda_i|$ sua magnitude.

$\hookrightarrow$ Com isso, o Raio Espectral $\rho (Z) = \max\{|\lambda_i|\}$.

$\hookrightarrow$ A partir disso temos que:

> Para qualquer vetor inicial $x^{(0)}$, a sequência $\{x^{(k)}\}$ dada por $x^{(k)} = Cx^{(k-1)}+g$ converge para a solução única se e somente se $\rho(C)<1$.
> 

## Critério das Linhas de Convergência para Gauss-Jacobi

$\hookrightarrow$ Seja:

$$
\alpha_k = \frac{\sum^n_{j=1\\, j\ne k} |a_{kj}|}{|a_{kk}|}
$$

e 

$$
\alpha = \max_{ 1\le k \le n} \alpha_k
$$

$\hookrightarrow$ Temos então que, se $\alpha < 1$ temos que Gauss-Jacobi converge para qualquer chute inicial.

$\hookrightarrow$ Basicamente, para cada linha, somamos todos os elementos da linha menos o que está na diagonal e dividimos pelo que está na diagonal, fazendo isso para todas as linhas. O maior resultado precia ser menor que um para que Gauss-Jacobi converja.