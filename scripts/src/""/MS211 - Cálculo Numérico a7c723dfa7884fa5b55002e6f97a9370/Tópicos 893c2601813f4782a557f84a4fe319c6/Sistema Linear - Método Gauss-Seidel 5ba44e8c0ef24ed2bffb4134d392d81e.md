# Sistema Linear - Método Gauss-Seidel

Aula: Aula 10
Created: September 28, 2021 8:20 AM
Prova: P1

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ Assim como o método Gauss-Jacobi, esse novo método também é interativo para descobrir os valores de um sistema linear.

$\hookrightarrow$ Ele é muito parecido com o Gauss-Jacobi, mas há diferenças, então tome cuidado.

# Algoritmo

## 1º Passo - Montar o sistema

$\hookrightarrow$ Nessa parte escrevemos o sistema em sua forma normal de equações, e não matricial.

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + ...+ a_{1n}x_n &= b_1 \\ 
a_{21}x_1 + a_{22}x_2 + ...+ a_{2n}x_n &= b_2 \\ 
... \\
a_{n1}x_1 + a_{n2}x_2 + ...+ a_{nn}x_n &= b_n \\ 
\end{cases}
$$

## 2º Passo - Isolar

$\hookrightarrow$ Assim como em Gauss-Jacobi, iremos isolar o $x_i$ na $i$-ésima linha:

$$
\begin{cases}
x_1 &= \frac{1}{a_{11}}[b_1 - ( a_{12}x_2 + ...+ a_{1n}x_n)] \\ 
x_2 &= \frac{1}{a_{22}}[b_2 - ( a_{21}x_1+ a_{23}x_3 + ...+ a_{2n}x_n)] \\ 
... \\ 
x_n &= \frac{1}{a_{nn}}[b_n - ( a_{n1}x_1+ a_{n2}x_2 + ...+ a_{n,n-1}x_{n-1})] \\ 
\end{cases}
$$

## 3º Passo - Interação

$$
\begin{cases}
x_1^{(k+1)} &= \frac{1}{a_{11}}[b_1 - ( a_{12}x_2^{(k)} + ...+ a_{1n}x_n^{(k)})] \\ 
x_2^{(k+1)} &= \frac{1}{a_{22}}[b_2 - ( a_{21}x_1^{(k+1)}+ a_{23}x_3^{(k)} + ...+ a_{2n}x_n^{(k)})] \\ 
... \\ 
x_n^{(k+1)} &= \frac{1}{a_{nn}}[b_n - ( a_{n1}x_1+ a_{n2}x_2 + ...+ a_{n,n-1}x_{n-1})] \\ 
\end{cases}
$$

$\hookrightarrow$ Basicamente o lado esquerdo será o da nova iteração, e a grande diferença do método de Gauss-Seidel para a Gauss-Jacobi é que nós substituímos os $x$ do lado direito que já foram calculados em $k+1$. Em suma, reaproveitamos todos os $x$ no cálculo de $x_n^{(k+1)}$  

$\hookrightarrow$ Isso resulta no método de Gauss-Seidel irá convergir mais rapidamente.

<aside>
<img src="Sistema%20Linear%20-%20Me%CC%81todo%20Gauss-Seidel%205ba44e8c0ef24ed2bffb4134d392d81e/Evangelion.gif" alt="Sistema%20Linear%20-%20Me%CC%81todo%20Gauss-Seidel%205ba44e8c0ef24ed2bffb4134d392d81e/Evangelion.gif" width="40px" /> OBS: Lembre de substituir os $x$s subsequentes!!!!

</aside>

## Critério de Parada

$\hookrightarrow$ Assim como em [Gauss-Jacobi](Sistema%20Linear%20-%20Me%CC%81todo%20Gauss-Jacobi%202abc3873f7164c2d94371d1e64ed78a0.md), usamos a norma infinita para calcularmos o critério de parada, seja absoluto ou relativo.

# Critério de Sassenfeld de Convergência

$\hookrightarrow$ Seja $\beta_1 = (|a_{12}| + |a_{13}| + ... + |a_{1n}|) / |a_{11}|$

$\hookrightarrow$  Seja $\beta_2 = (|a_{21}| \beta_1 + |a_{23}| + ... + |a_{2n}|) / |a_{22}|$

$\hookrightarrow$  Seja $\beta_3 = (|a_{31}| \beta_1+|a_{32}| \beta_2 + |a_{34}| + ... + |a_{2n}|) / |a_{33}|$

<aside>
🧠 $\beta_j = (|a_{j1}| \beta_1 + |a_{j2}|\beta_2 + ... + |a_{j(j-1)}|\beta_{j-1} + |a_{j(j+1)}|\beta_{j+1} + |a_{jn}|)/ |a_{jj}|$

</aside>

$\hookrightarrow$ Basicamente somamos todos os elementos da linha menos o elemento da diagonal, e dividimos pelo elemento da diagonal. A grande diferença desse critério para o de Gauss_Jacobi é que precisamos multiplicar o $\beta_j$ nos elementos $a_{ij}$ que já foram calculados anteriormente. 

$\hookrightarrow$ Assim, pegamos o maior dos $\beta$ calculados. Se $\max\{\beta_j \} < 1$ temos que converge.

# Forma Matricial

$\hookrightarrow$ Tendo uma matriz $D$ sendo a matriz diagonal da matriz $A$:

![Screen Shot 2021-09-28 at 9.01.53 AM.png](Sistema%20Linear%20-%20Me%CC%81todo%20Gauss-Seidel%205ba44e8c0ef24ed2bffb4134d392d81e/Screen_Shot_2021-09-28_at_9.01.53_AM.png)

$\hookrightarrow$ Sendo a matriz $L$ a parte contendo triangular inferior da matriz $A$:

![Screen Shot 2021-09-28 at 9.02.37 AM.png](Sistema%20Linear%20-%20Me%CC%81todo%20Gauss-Seidel%205ba44e8c0ef24ed2bffb4134d392d81e/Screen_Shot_2021-09-28_at_9.02.37_AM.png)

$\hookrightarrow$ Sendo a matriz $U$ a parte contendo a triangular superior de $A$:

![Screen Shot 2021-09-28 at 9.03.08 AM.png](Sistema%20Linear%20-%20Me%CC%81todo%20Gauss-Seidel%205ba44e8c0ef24ed2bffb4134d392d81e/Screen_Shot_2021-09-28_at_9.03.08_AM.png)

$\hookrightarrow$ Temos que:

$$
A =  L+D+U
$$

$\hookrightarrow$ Relembrando que todo método iterativo remete a um ponto fixo matricial temos que:

$$
x^{(k+1)} = Cx^{(k)} + g
$$

- Em Gauss-Jacobi
    
    $$
    Ax = b \iff (L + D + U)x = b \\ 
    \iff Dx = -(L+U)x + b \\ 
    \iff x = \underbrace{-D^{-1}(L+U)}_{C}x + \underbrace{D^{-1}b}_{g}
    $$
    
- Em Gauss-Seidel
    
    $$
    Ax = b  \iff (L+D+U)x = b \\ 
    \iff (L+D)x = -Ux + b \\ 
    \iff x = \underbrace{-(L+D)^{-1}Ux}_{C} + \underbrace{(L+D)^{-1}b}_g
    $$
    

# Pontos Positivos e Negativos

## Métodos Diretos

- Solução Exata
- Número finito de passos

- Sistemas Esparsos
- Reduzir a Esparsidade
- Muitos Sensíveis a Erro de arredondamento

## Métodos Iterativos

### Gaus-Seidel

- Convergência Rápida

### Gauss-Jacobi

- Paralelização Mais Fácil