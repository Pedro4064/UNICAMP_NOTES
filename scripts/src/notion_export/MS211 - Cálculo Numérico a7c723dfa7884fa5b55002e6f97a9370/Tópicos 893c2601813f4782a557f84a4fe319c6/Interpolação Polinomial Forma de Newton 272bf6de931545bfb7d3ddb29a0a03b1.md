# Interpolação Polinomial: Forma de Newton

Aula: Aula 25
Created: November 25, 2021 7:11 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Até o momento vimos dois diferentes tipos de formas de interpolação polinomial, sendo elas a forma de [Vardemond](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Vandermonde%2029c583f9b0464d33bcbb83933bd47da8.md) e a forma de [Lagrange](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Lagrange%20fcac697df44c450a821a7d1aa2e3ffc5.md).

$\hookrightarrow$ Iremos introduzir agora, entretanto, a forma de Newton, que tem como vantagem uma melhor construção do polinômio, principalmente para achar seu valor em um ponto $x$ específico (o que é extremamente vantajoso para nós em calculo numérico) devido à ser formado por um sistema triangular e funções bases mais simples.

# Método de Newton

## Funções-Base

$\hookrightarrow$ Para o método de Newton, teremos como função base:

$$
\begin{aligned}
N_0(x) &= 1  \\ 
N_1(x) &= (x_1 - x_0) \\ 
N_2(x) &= (x_2 - x_0)(x - x_1) \\ 
... \\ 
N_n(x) &= (x_n - x_0)(x_n - x_1) ... (x_n - x_{n-1}) \\
\end{aligned}
$$

$\hookrightarrow$ Que no geral temos:

$$
\boxed{N_n = \prod_{k = 0} ^{n-1}(x_n - x_k)}
$$

## Polinômio

$\hookrightarrow$ Com um polinômio geral:

$$
\boxed{p_n(x) = a_0 + a_1(x_1 - x_0) + a_2(x_2 - x_0)(x_2 - x_1) + ... + a_n(x_n - x_0)(x_n - x_1)...(x_n - x_{n-1})}
$$

## Representação Matricial

$$
Na = y
$$

$$
N = \begin{bmatrix}
1 \\ 
1 & (x_1 - x_0) \\ 
1 & (x_2 - x_0) & (x_2 - x_0)(x_2 - x_1) \\ 
... \\ 
1 & (x_n - x_0) & (x_n - x_0)(x_n - x_1) & ... & (x_n-x_0)...(x_n - x_{n-1})
\end{bmatrix}
$$

- Que é uma triangular inferior

$$
a = \begin{bmatrix}
a_0 \\ 
a_1 \\ 
a_2 \\ 
... \\ 
a_n
\end{bmatrix}
$$

## Encontrando $a$ - Diferenças Divididas

$\hookrightarrow$ Como sabemos, o que queremos é achar os valores em $a$.

$\hookrightarrow$ Para isso (e baseados nas expressões acima) temos fórmulas chamadas de diferença dividida.

$$
\begin{aligned}
a_0 &= f(x_0) = f[x_0] \\ 
a_1 &= \frac{f(x_1) - f(x_0)}{x_1 - x_0} = \frac{f[x_1] - f[x_0]}{x_1 - x_0} = f[x_0, x_1] \\
a_2 &= \frac{f[x_1, x_2] - f[x_0, x_1]}{x_2 - x_0} = f[x_0, x_1, x_2]
\end{aligned}
$$

$\hookrightarrow$  De modo geral temos que $a_n$ é de orden $n$ tal que:

$$
\begin{aligned}
ordem \ 0 &: f[x_k] = f(x_k) = y_k \\ 
ordem \ 1 &: f[x_{k-1}, x_k] = \frac{f[x_k] - f[x_{k-1}]}{x_k - x_{k-1}} \\ 
ordem \ 2 &: f[x_{k-2}, x_{k-1}, x_{k}] = \frac{f[x_{k-1}, x_k] - f[x_{k-2}, x_{k-1}]}{x_k - x_{k-2}} \\ 
ordem  \ n &: f[x_{k-n}, ..., x_k] = \frac{f[x_{k - n + 1}, ...,  x_k] - f[x_{k-n}, ..., x_{k-1}]}{x_k - x_{k-n}}
\end{aligned}
$$

### Tabelas de Diferenças

![Screen Shot 2021-11-25 at 7.56.24 PM.png](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Newton%20272bf6de931545bfb7d3ddb29a0a03b1/Screen_Shot_2021-11-25_at_7.56.24_PM.png)

## Polinomio

$\hookrightarrow$ E para o polinômio temos:

![Screen Shot 2021-11-25 at 8.00.43 PM.png](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Newton%20272bf6de931545bfb7d3ddb29a0a03b1/Screen_Shot_2021-11-25_at_8.00.43_PM.png)

## Polinomio por parêntesis Encaixados

![Screen Shot 2021-11-25 at 8.02.34 PM.png](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Newton%20272bf6de931545bfb7d3ddb29a0a03b1/Screen_Shot_2021-11-25_at_8.02.34_PM.png)

# Passo a Passo

- 1º Passo - Tabela de Diferenças
    - A primeira coisa que precisamos fazer é a tabela de diferenças:
        - Primeiro coluna → valores de $X$
        - Segunda coluna → Diferença Dividida de ordem 0
        - Terceira Coluna → Diferença Dividida de ordem 1
        - Quarta Coluna → Diferença Dividida de ordem 2
        - ...
    
    ![Screen Shot 2021-11-25 at 8.13.21 PM.png](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Newton%20272bf6de931545bfb7d3ddb29a0a03b1/Screen_Shot_2021-11-25_at_8.13.21_PM.png)
    
- 2º Passo - Identificar $a$ e substituir no polinômio
    - É de suma importância identificar cada $a_k$ que precisa e sua respectiva diferença dividida para que possamos substituir na forma [geral do polinômio](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Newton%20272bf6de931545bfb7d3ddb29a0a03b1.md):
    
    $$
    \boxed{p_n(x) = a_0 + a_1(x_1 - x_0) + a_2(x_2 - x_0)(x_2 - x_1) + ... + a_n(x_n - x_0)(x_n - x_1)...(x_n - x_{n-1})}
    $$