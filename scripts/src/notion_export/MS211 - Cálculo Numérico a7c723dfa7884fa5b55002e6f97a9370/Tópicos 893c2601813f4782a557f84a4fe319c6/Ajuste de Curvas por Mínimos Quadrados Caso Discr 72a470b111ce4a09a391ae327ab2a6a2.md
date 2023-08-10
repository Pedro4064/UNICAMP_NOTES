# Ajuste de Curvas por Mínimos Quadrados: Caso Discreto

Aula: Aula 21
Created: November 22, 2021 3:27 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Iremos dar início a aproximação de dados tabelados por funções contínuas. Algo que é extremamente útil em análise de dados.

$\hookrightarrow$ De modo geral existem dois tipos de aproximação, as chamadas interpolações → Que certificam que os pontos da função aproximada coincidam com todos os pontos tabelados, e os chamados regressão/ajuste → Que fazem aproximação geral dos pontos.

# Problema

$\hookrightarrow$ Normalmente nos é dado uma tabela de $x$ e $f(x)$.

$\hookrightarrow$ Além disso, é dado o tipo de função que queremos aproximar (no caso se é linear, logartmica, quadrática etc) e a partir disso iremos escolher funções $g_1(x), g_2(x), ..., g_n(x)$ contínuas em $[a, b]$ e obter constantes $\alpha_1, \alpha_2, ..., \alpha_n$ tais que $\varphi(x) = \alpha_1g_1(x) = \alpha_2g_2(x) + ... + \alpha_ng_n(x) \approx f(x)$ 

# Encontrando as Constantes $\alpha_n$

$\hookrightarrow$ Como vimos anteriormente, nossa solução $\varphi(x)$ é a junção de várias outras funções e suas respectivas constantes $\alpha$ que visam minimizar o erro da aproximação, dado por:

$$
F(\alpha_1, ..., \alpha_n) = \sum^m_{k=1}[f(x_k) - \varphi(x_k)]^2
$$

$\hookrightarrow$ E como queremos minimizar, sabemos que precisamos achar o ponto onde a derivada de $F$ é zero, mas como é dependente de mais uma variável precisamos zerar o vetor  gradiente:

$$
\min\{F(\alpha_1, ..., \alpha_n)\} \iff \nabla F = \vec 0
$$

$\hookrightarrow$ E através da igualdade $\nabla F = \vec{0}$ iremos encontrar o seguinte sistema linear:

$$
\begin{cases}
\sum^m_{k=1} [f(x_k) - \alpha_1g_1(x_k) - ... - \alpha_ng_n(x_k)]g_1(x_k) = 0 \\ 

\sum^m_{k=1} [f(x_k) - \alpha_1g_1(x_k) - ... - \alpha_ng_n(x_k)]g_2(x_k) = 0 \\ 

\sum^m_{k=1} [f(x_k) - \alpha_1g_1(x_k) - ... - \alpha_ng_n(x_k)]g_3(x_k) = 0 \\ 

. \\ . \\ . \\

\sum^m_{k=1} [f(x_k) - \alpha_1g_1(x_k) - ... - \alpha_ng_n(x_k)]g_n(x_k) = 0

\end{cases}
$$

$\hookrightarrow$ Onde temos como incógnita os valores dos $\alpha$.

$\hookrightarrow$ Re-arranjando nosso sistema temos:

$$
\boxed{
\begin{cases}

[\sum^m_{k=1} g_1(x_k) g_1(x_k)] \alpha_1 + ... + [\sum^m_{k=1} g_n(x_k) g_1(x_k)]\alpha_n = \sum^m_{k=1} f(x_k)g_1(x_k) \\ 

[\sum^m_{k=1} g_1(x_k) g_2(x_k)] \alpha_1 + ... + [\sum^m_{k=1} g_n(x_k) g_2(x_k)]\alpha_n = \sum^m_{k=1} f(x_k)g_2(x_k) \\ 
. \\ .\\ . \\ 

[\sum^m_{k=1} g_1(x_k) g_n(x_k)] \alpha_1 + ... + [\sum^m_{k=1} g_n(x_k) g_n(x_k)]\alpha_n = \sum^m_{k=1} f(x_k)g_n(x_k)

\end{cases}}
$$

$\hookrightarrow$ Que somos capazes de representar matricialmente  como sendo:

$$
A \alpha = b
$$

- Onde:

$$
A \rightarrow a_{ij} = <g_i, g_j> \\
b \rightarrow b_{i} = <f, g_i>
$$