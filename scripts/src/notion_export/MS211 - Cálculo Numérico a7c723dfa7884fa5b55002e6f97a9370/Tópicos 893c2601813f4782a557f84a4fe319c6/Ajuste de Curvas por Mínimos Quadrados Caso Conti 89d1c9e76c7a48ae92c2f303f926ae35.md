# Ajuste de Curvas por Mínimos Quadrados: Caso Contínuo

Aula: Aula 23
Created: November 25, 2021 8:58 AM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ O caso que iremos abordar agora para o uso de mínimos quadrados não é, ao contrário do que vimos até agora, utilizado em dados discretos e tabelado, mas sim em funções contínuas, com o intuito de simplifica-las.

# Problema

$\hookrightarrow$ Seja $f(x)$ contínua em $[a, b]$ e $g_1, ..., g_m$ funções-base contínuas. Obtenha $\alpha_1, ..., \alpha_m$ tais que:

$$
\varphi(x) = \alpha_1 g_1(x) = \alpha_2g_2(x) + ...+ \alpha_mg_m(x)
$$

seja a melhor aproximação para $f(x)$ em $[a,b]$.

$\hookrightarrow$ E sabemos que para ser a melhor aproximação (pelo método de mínimos quadrados) temos que o erro da aproximação é dada por (tendo em vista que agora estamos em um caso contínuo):

$$
F(\alpha_1,..., \alpha_m) = \int^b_a [\varphi (x) - f(x)]^2 dx
$$

$\hookrightarrow$ Além disso, sabemos que para minimizar queremos achar um ponto onde a derivada tende a zero, isso é:

$$
\frac{\partial F}{\partial \alpha_j} = 0,  \ \ \ j=1, ..., m
$$

## Derivação Sobre O Sinal de Integração

$\hookrightarrow$ Levando em consideração a derivação sobre o sinal de integração temos que:

$$

\frac{\partial F}{\partial \alpha_j} = \int^b_a \frac{\partial}{\partial \alpha_j}([\varphi(x) - f(x)]^2)dx\\

\Downarrow \\
\int^b_a \alpha_1g_1(x)g_j(x)dx + ...+ \int^b_a \alpha_mg_m(x)g_j(x)dx = \int^b_af(x)g_j(x)dx,  \ \ j=1, ..., m
$$

$\hookrightarrow$ Aplicando então a nomenclatura de produto interno para funções da área de análise funcional podemos reescrever a equação acima como sendo:

 

$$
A\alpha  = b
$$

$$
\boxed{
\begin{aligned}
aij &= \lang g_i, g_j\rang = \int^b_a g_i(x)g_j(x)dx  \\ 

bi &= \lang f, g_i\rang = \int^b_a f(x)g_i(x)dx 

\end{aligned}}
$$

# Exemplo

- Aproxime $f(x) = 4x^3$ por uma reta $\varphi(x) = \alpha_1 x + \alpha_2$ em $[0, 1]$.

- 1º Passo: Identificação
    - Identificação da nossa função $f(x)$ além das funções $g_1(x) = x, g_2(x) = 1$
    
- 2º Passo: Calculo de $A$
    - Levando em consideração que:
    
    $$
    aij = \lang g_i, g_j\rang = \int^b_a g_i(x)g_j(x)dx  \\ 
    
    $$
    
    - Onde $a, b$ são os extremos do intervalo $[0, 1] \therefore a = 0, b = 1$
    
- 3º Passo: Calculo de $b$
- 4º Passo: Resolver sistema linear