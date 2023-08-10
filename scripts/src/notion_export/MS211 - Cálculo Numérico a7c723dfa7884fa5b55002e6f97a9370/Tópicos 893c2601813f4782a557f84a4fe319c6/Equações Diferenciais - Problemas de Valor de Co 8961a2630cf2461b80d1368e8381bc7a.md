# Equações Diferenciais - Problemas de Valor de Contorno

Aula: Aula 19
Created: November 17, 2021 10:16 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução - P.V.C

$\hookrightarrow$ Em problemas de valor de contorno, ao contrário de como é em problemas de valor inicial, nos é conhecido vários pontos, ao invés de somente um.

$\hookrightarrow$ Além disso, problemas de valor de contorno tendem a ser modelagens de problemas espaciais, quanto problemas de valor inicial tendiam a ser problemas envolvendo tempo.

$$
\begin{cases}
y'' = f(x, y, y') \\
a_1 y(a) + b_1 y'(a) = y_1 \\ 
a_2 y(b) + b_2 y'(b) = y_2
\end{cases}
$$

$\hookrightarrow$ Onde $a_1$ e $b_1$ nem $a_2$  e $b_2$ podem ser nulos simultaneamente.

# P.V.C Linear

$\hookrightarrow$ No estude de problemas de valor de contorno temos um sub-conjunto de equações diferenciais, as chamadas lineares, como a demonstrada abaixo:

$$
\begin{cases}
y'' = A(x) y'(x) + B(x)y(x) + C(x)\\
a_1 y(a) + b_1 y'(a) = y_1 \\ 
a_2 y(b) + b_2 y'(b) = y_2
\end{cases}
$$

$\hookrightarrow$ Supondo que $x \in [a, b]$

# Método das Diferenças Finitas

$\hookrightarrow$ No método de diferenças finitas, nós dividimos  o intervalo $[a,b]$ em $n$ subintervalos de tamanho $h$:

$$
x_k = a+kh, \ \ \ \  k = 0,1,..., n
$$

$\hookrightarrow$ Onde $x_0 = a, x_n = b$ → chamados de de pontos de contorno (ou boundary points).

$\hookrightarrow$ $h = \frac{b - a}{2}$

$\hookrightarrow$ Além disso, os pontos $x_k$ são chamados os nós da chamada malha.

## Aproximação de $y'$

$\hookrightarrow$ Nós temos mais de uma forma de aproximar o valor da derivada de $y$, sendo elas:

- Diferença Avançada
    
    $$
    y'(x_k) \approx \frac{ y(x_k + h) - y(x_k)}{h} = \frac{y_{k+1}- y_k}{h}
    $$
    

- Diferença Atrasada
    
    $$
    y'(x_k) \approx \frac{ y(x_k) - y(x_k - h)}{h} = \frac{y_{k}- y_{k-1}}{h}
    $$
    

- Diferença Centrada
    
    $$
    y'(x_k) \approx \frac{ y(x_k + h) - y(x_k - h)}{2h} = \frac{y_{k+2}- y_{k-1}}{2h}
    $$
    

### Errors De Aproximação

$\hookrightarrow$ Dizemos que os erros dependem do step que temos, ou seja, do nosso $h$.

$\hookrightarrow$ Tendo isso em consideração somos capazes de analisar a ordem $O(h^p)$ do erro das aproximações $E(h)$ tal que:

$$
E(h) \le c \ | h^p|
$$

- ERRO na Diferença Avançada
    
     
    
    $$
    |E(h)| \le \frac{M}{2} |h|
    $$
    
    - Onde $M$ é o maior valor alcançado pela segunda derivada.
    - Com isso temos que o erro é de ordem linear $O(h)$
- ERRO na Diferença Atrasada
    - De forma análoga ao método avançado temos que a diferença atrasada também é linear.
    
- ERRO na Diferença Centrada
    
    $$
    |E(h)| \le \frac{M}{6} |h^2|
    $$
    
    - Tem ordem $O(h^2)$,  que resulta em uma fórmula mais precisa.

## Aproximação de $y''$

$\hookrightarrow$ Para aproximarmos numericamente o valor da segunda derivada temos:

$$
y''(x_k) \approx \frac{y(x_k + h) - 2y(x_k) + y(x_k - h)}{h^2}
$$

$\hookrightarrow$ Que se traduz, para o algoritmo como sendo:

$$
\boxed{y''(x_k) \approx \frac{y_{k+1} - 2y_k + y_{k-1}}{h^2}}
$$

## Passo a Passo

$$
\begin{cases}
y''(x) + 2y'(x) + y(x) = x \\ 
y(0) = 0 \\ 
y(1) = -1
\end{cases}
$$

$\hookrightarrow$ Com $h = 0.25$

- 1º Passo: Identificação de Pontos de Interesse
    - O primeiro passo é a identificação dos pontos de contorno:
    
    $$
    x_0 = 0, x_n = -1
    $$
    
- 2º Passo:  Calculo da quantidade de nós
    
    $$
    n = \frac{1}{h} = 4
    $$
    
- 3º Passo: Discretização da EDO
    - Nesse passo iremos re-escrever nossa EDO na sua forma discreta, isso é, substituindo as derivadas $y''$  e $y'$ pelas suas respectivas aproximações.
    
    $$
    \begin{aligned}
    y''(x_k) &\approx  \frac{y_{k+1} - 2y_k + y_{k-1}}{h^2} \\ 
    y'(x_k) &\approx \frac{y_{k+1} - y_{k-1}}{2h}
    \end{aligned} \\ \Downarrow  \\ 
    
    \frac{y_{k+1} - 2y_k + y_{k-1}}{h^2} + \frac{y_{k+1} - y_{k-1}}{2h} + y_k = x_k
    $$
    
- 4º Passo: Substituir $h$ e $x_k$
    - Agora iremos substituir os valores de $h = 0.25$ e $x_k = k \cdot h = 0.25k$ que aparecem na forma discreta da EDO para que possamos botar tudo em função de $y_{k+1}, y_k, y_{k-1}$ e $k$:
    
    $$
    0.75 y_{k-1} - 1.9375 y_k + 1.25 y_{k+1} = 0.015625k
    $$
    
- 5º Passo: Substituir por $k$
    - Para criarmos um sistema, iremos substituir os valores acima para $k=1, ..., k = n-1$
- 6º Passo: Resolver o sistema
    - Por eliminação de Gauss, por exemplo.
    

### Resolução → Método Matricial

- Para solucionarmos ESSA EDO EM ESPECíFICO, precisamos:
    1. Discretizar a EDO
    2. Resolver o seguinte sistema Tridiagonal:

→ Considerando:

$$
\begin{aligned}
d_k &= (h^2 - 2), \ \   1 \le k\le (n-1)\\
c_k &= (1 + h),  \ \ 1 \le k \le (n-2) \\ 
a_k &= (1 - h), \ \ 2 \le k \le (n-1)
\end{aligned}
$$

$$
\begin{bmatrix}
d_1 & c_1 \\
a_2 & d_2 & c_2 \\ 
&a_3 &d_3 &c_3 \\ 
&&.&.&. \\ 
&&&.&.&. \\ 
&&&&.&.&. \\
&&&&&a_{n-2} &d_{n-2} & c_{n-2} \\
&&&&&&a_{n-1} &d_{n-1} & c_{n-1} \\
\end{bmatrix} 
\begin{bmatrix}
y_1 \\ 
y_2 \\
y_3 \\ 
.\\
.\\
.\\
y_{n-2} \\ 
y_{n-1}
\end{bmatrix} = 
\begin{bmatrix}
h^3 \\ 2h^3 \\ 3h^3 \\ .\\ .\\ .\\ (n-2)h^3 \\ (n-1)h^3
\end{bmatrix}
$$