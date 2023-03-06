# Equações Diferenciais - Equação do Calor [Método Explícito]

Aula: Aula 20
Created: November 22, 2021 12:58 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ A equação do calor é utilizado em vários campos da ciência os quais envolvem a modelagem da dispersão de partículas (ou seu movimento) em um fluido (assim como na dispersão do calor).

$\hookrightarrow$ A equação do Calor é uma Equação Diferencial Parcial, na qual aplicaremos o método das diferenças finitas.

# Equação do Calor

$\hookrightarrow$ Considerando a barra como sendo mais longa que larga (i.e unidimencional) temos uma função $u(x,t)$ que representa a temperatura em um ponto $x$ no tempo $t$, em uma barra de comprimento $L$.

$$
\begin{cases}
\frac{\partial u}{\partial t} = \frac{\partial ^2 u}{\partial x^2} \\ 
0\le x \le L \\ 
0\le t \le T
\end{cases}
$$

- Contendo como valor inicial: $u(x, 0) = q(x), 0\le x\le L$.
- E Contendo os valores de contorno:

$$
\begin{cases}
u(0,t) = \gamma_1 \\
u(L,t) = \gamma_2
\end{cases} \Rightarrow 0 < t \le T
$$

# Solução Numérica

$\hookrightarrow$ Começamos por dividir $[0, L]$ em nossa malha de $(n+2)$ pontos:

$$
x_i = ih,  \ \ h = \frac{L}{n+1},  \ \ i = 0, ..., n+1
$$

$\hookrightarrow$ Dividimos $[0, T]$ em $(m+1)$ pontos:

$$
t_j = j\Delta t,  \ \ \Delta t = \frac{T}{m},\ \ \ j = 0,..., m
$$

$\hookrightarrow$ Agora teremos uma solução, descretizada:

$$
u_{ij} \approx u(x_1, t_j)
$$

- Com a condição inicial:

$$
u_{i0} = g(x_i),  \ \ i=0,1,...,n+1
$$

- Aproximando $u_{xx}$ com $t$ constante:

$$

\boxed{u_{xx}(x_i, t_j) \approx \frac{u_{i-1, j} - 2u_{ij} + u_{i+1, j}}{h^2}}
$$

- Aproximação da primeira derivada $u_t$ por diferença avançada:

$$
\boxed{u_t(x_1, t_1) \approx \frac{u_{i,j+1} - u_{ij}}{\Delta t}}
$$

- Agora iremos substituir na EDP original:

$$
\boxed{\frac{u_{i,j+1} - u_{ij}}{\Delta t} = \frac{u_{i-1, j} - 2u_{ij} + u_{i+1, j}}{h^2}}
$$

- Agrupamos e reorganizamos a equação acima, e utilizando $\alpha =  \frac{\Delta t}{h^2}$ para facilitar:

$$
\boxed{u_{i, j+1} = \alpha u_{i-1, j} + (1-2\alpha)u_{ij} + \alpha u_{i+1, j}}
$$

# Exemplo

## Método Explícito

- Tendo $L = 1, T=1, h=0.5, \Delta t = 0.5$
- Além disso temos $u(0,t) = 0, u(1,t) = 1$
- E como valores de contorno temos $u_{00} = u_{10} = u_{20} = 1$

- 1º Passo - Calculo do $n$ e m
    - Temos que:
    
    $$
    h = \frac{L}{n+1} \therefore n = 1
    $$
    
    - E temos que, para o $m:$
    
    $$
    \Delta t = \frac{T}{m} \therefore m = 2
    $$
    
- 2º Passo - Identificação dos pontos:
    
    $$
    \gamma_1 = 0 \\
    \gamma_2 = 1
    $$
    
    - Além disso temos:
    
    $$
    \alpha = \frac{\Delta t}{h^2} = 2
    $$
    
- 3º Passo - Resolução do sistema linear
    
    ![Screen Shot 2021-11-22 at 1.56.23 PM.png](Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Equac%CC%A7a%CC%83o%20do%20Calor%20%5BMe%CC%81t%208df5acdb84f7496e84652e7f36b5f199/Screen_Shot_2021-11-22_at_1.56.23_PM.png)
    
    - Relembrando que $q(x_n) = u(n, 0)$