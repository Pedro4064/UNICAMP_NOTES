# Ajuste de Curvas por Mínimos Quadrados: Múltiplas Variáveis

Aula: Aula 23
Created: November 24, 2021 10:32 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ A grande diferença para as demonstrações a seguir é que elas trabalham com mais de um $x$, e por conseguinte são funções vetoriais.

$$
x = \begin{bmatrix}
x_1 \\ x_2 \\ . \\ .\\. \\ x_n
\end{bmatrix}
$$

$\hookrightarrow$ Tal que:

$$
\varphi : \R ^2 \rightarrow \R
$$

# Problema

$\hookrightarrow$ De forma análoga a como é o ajuste normal por meio dos mínimos quadrados somos capazes representar o sistema linear resultante (para acharmos os valores de $\alpha$) da forma:

$$
A \alpha = b 
$$

$$
\begin{aligned}A \rightarrow a_{ij} &= \sum^k_{k=1} g_i(x_k)g_i(x_k) \\ 
b \rightarrow b_i &= \sum^k _{k=1} y_k g_i (x_k), \ \ \ i, j = 1,..., m
\end{aligned}
$$

$\hookrightarrow$ De forma geral, todas as fórmulas continuam válidas, a única diferença é que as funções $g$ recebem um vetor $x$ e retornam um escalar, isso é, $g (x): \R^2 \rightarrow \R$.

# Exemplo

![Screen Shot 2021-11-24 at 11.30.10 PM.png](Ajuste%20de%20Curvas%20por%20Mi%CC%81nimos%20Quadrados%20Mu%CC%81ltiplas%205c17a29868134b778fbe1d75bc62512f/Screen_Shot_2021-11-24_at_11.30.10_PM.png)

- 1º Passo: Identificação
    - O primeiro passo é identificar as funções $g$ para cada $\alpha$.
    - Depois disso é de suma importância identificar cada uma das múltiplas variáveis (que nesse caso é $x, y$)
- 2º Passo: Montar Matriz A
    - Agora que temos as nossas funções $g$ (no caso temos 4)e  sabemos os números de pontos (no nosso caso 5) iremos montar a matriz $A_{4\times 4}$:
    
    $$
    \begin{aligned}
    a_{11} &= \sum^5 _{k=1} g_1(x_k, y_k)g_1(x_k, y_k) = \sum^5_{k=1}1 \cdot 1 = 5 \\ 
    a_{12} &= \sum^5_{k=1}g_1(x_k, y_k)g_2(x_k, y_k) = \sum^5_{k=1}1\cdot x_k = 0 \\ 
    a_{13} &= \sum^5_{k=1} g_1(x_k, y_k)g_2(x_k, y_k) = \sum^5_{k=1}1\cdot y = 0 \\ ...
    \end{aligned}
    $$
    
- 3º Passo: Montar a Matriz $b$
    - No caso teremos uma matriz $b_{4\times 4}$ onde cada elemento:
    
    $$
    b \rightarrow b_i = \sum^k _{k=1} Z_k g_i (x_k), \ \ \ i, j = 1,..., m
    $$
    
    - Exemplo:
    
    $$
    b_1 = \sum^5_{k=1} Z_k g_1(x_k) = (4.09) \cdot 1 + (0.7) \cdot 1 + (1.67) \cdot 1 + (0.15) \cdot 1 + (-2.38) \cdot 1 = 4.23
    $$
    
- 4º Pass: Solucionar o Sistema Linear