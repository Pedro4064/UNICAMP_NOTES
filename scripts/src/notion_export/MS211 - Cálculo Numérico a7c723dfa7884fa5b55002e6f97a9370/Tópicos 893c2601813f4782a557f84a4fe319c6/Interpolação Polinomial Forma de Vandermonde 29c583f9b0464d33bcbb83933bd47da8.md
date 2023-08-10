# Interpolação Polinomial: Forma de Vandermonde

Aula: Aula 24
Created: November 25, 2021 9:27 AM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ A interpolação é muito utilizada, principalmente quando precisamos achar um valor que está entre entradas de uma tabela.

# Problema

$\hookrightarrow$ Dado uma tabela contendo $x_1, ..., x_n$ (distintos chamados de nós) e $y_1, ..., y_n$ podemos dizer que:

$$
\varphi (x) \ interpola \iff  \varphi (x_k) = y_k
$$

# Interpolação Polinomial

$\hookrightarrow$ Dado uma tabela contendo $x_1, ..., x_n$ (distintos chamados de nós) e $y_1, ..., y_n$ temos que nossa interpolação polinomial necessitará de um polinômio de ordem $\le n$.

$\hookrightarrow$ Levando isso em consideração teremos como objetivo encontrar tal polinômio:

$$
p_n(x) = a_0 + a_1 x + ...+a_n x^n
$$

$\hookrightarrow$ E queremos obter $a_0, ..., a_n$ tais que:

$$
p_n(x_k) = a_0 + a_1x_k + ... + a_n x_k^n = y_k,  \ \ \ k = 0, 1, ..., n
$$

$\hookrightarrow$ Basicamente temos todos os pontos $y_k$ e $x_k$ da tabela, logo teremos um sistema linear com $n+ 1$ incógnitas e $n+1$ equações para encontrar os $a$:

$$
V a = y
$$

$$
V = \underbrace{\begin{bmatrix}
1 & x_0 & x_0^2 &... & x_0^n \\
1 & x_1 & x_1^2 &... & x_1^n \\ 
...\\
1 & x_n & x_n^2 &... & x_n^n \\
\end{bmatrix}}_{Matriz \ de \ Vandermonde}
$$

$$
a = \begin{bmatrix}
a_0 \\ a_1 \\ . \\ .\\ .\\ a_n
\end{bmatrix} \ \ y = \begin{bmatrix}
y_0 \\ y_1 \\ . \\ .\\ .\\ y_n
\end{bmatrix}
$$

<aside>
<img src="Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Vandermonde%2029c583f9b0464d33bcbb83933bd47da8/yuru_camp.png" alt="Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Vandermonde%2029c583f9b0464d33bcbb83933bd47da8/yuru_camp.png" width="40px" /> Onde a Matriz de Vandermonde tem a propriedade de:
$det(V) \ne 0 \therefore$  $a$ tem solução única. Isso significa que existem um polinômio único que soluciona, logo independente do método vai ser o mesmo.

</aside>