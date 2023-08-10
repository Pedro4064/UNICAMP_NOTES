# Ajuste de Curvas por Mínimos Quadrados: Caso Linear

Aula: Aula 22
Created: November 24, 2021 9:23 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Quando estamos ajustando curvas pelo método de mínimos quadrados a maior tendência é de o fazermos utilizando funções lineares como alvo.

$\hookrightarrow$ Isso é devido principalmente ao fato de que somos capazes de aproximar as nossas modelagens para comportamento linear, mesmo que originalmente não sejam (por isso uma aproximação).

# Problema

$\hookrightarrow$ Assim como dito anteriormente, temos pares de valores $(x_i, y_i)$ tabelados e uma função $\varphi(x)$, que no nosso caso específico de aproximação por reta temos que $\varphi(x) = \alpha_1 x + \alpha_2$ o que implica que $g_1(x)  = x$ e $g_2(x) = 1$.

## Produtos Escalares

$\hookrightarrow$ Como vimos anteriormente, somos capazes de representar o sistema linear para acharmos $\alpha_1$ e $\alpha_2$ como uma multiplicação matricial:

$$
A\alpha = b
$$

$\hookrightarrow$ Onde:

$$
A \rightarrow a_{ij} = \langle g_i, g_j\rangle
$$

$\hookrightarrow$ Que no nosso caso específico seria:

$$
\begin{aligned}
a_{11} &= \lang g_1, g_1 \rang = \sum ^n _{i = 1} x_i^2 \\ 
a_{12} &= a_{21} =  \lang g_1, g_2 \rang = \sum ^n _{i = 1} x_i \\ 
a_{22} &= \lang g_2, g_2 \rang = \sum ^n _{i = 1} 1 = n
\end{aligned}
$$

$\hookrightarrow$ E para a matrix $b$ temos:

$$
\begin{aligned}
b_1 &= \lang y, g_1 \rang = \sum^n _{i = 1} x_i y_i \\ 
b_2 &= \lang y, g_2 \rang = \sum^n _{i = 1} y_i
\end{aligned}
$$

## Equações Normais

$\hookrightarrow$ Utilizando as equações acima temos que:

$$
\boxed{\alpha_1 = \frac{b_1 a_{22} - a_{12} b_2}{a_{11}a_{22} - a_{12}^2}}
$$

$$
\boxed{\alpha_2 = \frac{b_2 a_{11} - b_1 a_{21}}{a_{22}a_{11} - a_{12} a_{21}}}
$$