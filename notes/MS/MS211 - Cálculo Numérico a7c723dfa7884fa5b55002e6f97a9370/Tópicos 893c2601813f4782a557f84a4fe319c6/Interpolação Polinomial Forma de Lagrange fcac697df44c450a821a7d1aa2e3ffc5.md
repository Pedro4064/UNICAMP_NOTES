# Interpolação Polinomial: Forma de Lagrange

Aula: Aula 24
Created: November 25, 2021 10:07 AM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Vimos anteriormente que somos capazes de encontrar um polinômio pela forma de Vandermonde tal que possamos fazer a interpolação polinomial de dados tableados.

$\hookrightarrow$ Esse método, entretanto não é perfeito, devido principalmente ao fato da matriz de Vandermonde $V$ ser mal considicionada (i.e qualquer pequena variação resulta em uma grande diferença no resultado, o que é ruim pois ela pode haver errors) e devido ao fato de estarmos trabalhando com um sistema linear que, no mundo rela, tende a ser muito grande e computacionalmente demorado.

$\hookrightarrow$ A fim de sanar as dores supracitadas iremos apresentar a forma de Lagrange.

# Forma de Lagrange

$\hookrightarrow$ Há duas principais diferenças para a forma de Lagrange:

1. Não iremos tentar encontrar os $a$ para cada $ax^k$ do nosso polinômio. Ao invés disso, iremos utilizar a propriedade de composição de polinômio de ordem $n$ por soma de outros polinômios de ordem $\le n$ (chamados e Funções-Base), resultando em uma matriz A:
    
    $$
    Aa = y \Rightarrow A = \begin{bmatrix} g_0(x_0) & g_1 (x_0) & ... & g_n(x_0) \\ 
    g_0(x_1) & g_1 (x_1) & ... & g_n(x_1) \\ 
    ... \\ 
    g_0(x_n) & g_1 (x_n) & ... & g_n(x_n)
    \end{bmatrix}
    $$
    
2. Para sanarmos a dor do sistema linear iremos escolher as nossas funções-base de forma estratégica tal que $A$ é identidade $I$:
    
    $$
    L_i(x_k) = \begin{cases}
    1, \ se \ i = k \\
    0,  \ se \ i \ne k
    \end{cases}
    $$
    
    - Resultando em:
    
    $$
    \boxed{L_i(x) = \frac{(x-x_0)(x - x_1) ... (x-x_{i-1})(x - x_{i+1}) ... (x - x_n)}{(x_i - x_0)(x_i - x_1) ...(x_i-x_{i-1})(x_i - x_{i+1}) ... (x_i - x_n)} = \prod_{k\ne i}^n \frac{(x - x_k)}{(x_i - x_k)}}
    $$
    

$\hookrightarrow$ Logo temos que:

$$
A a = Ia = y \Rightarrow a = y
$$

$\hookrightarrow$ E por conseguinte temos que:

$$
\boxed{p_n(x) = \sum^n_{k=0} y_kL_k(x)}
$$