# Integração Numérica: Regra dos Trapézios

Aula: Aula 27
Created: November 28, 2021 1:29 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Iremos introduzir agora a integração numérica de dados discretos tabelados.

$\hookrightarrow$ Muito utilizado nas ciências e engenharias, como por exemplo quando queremos achar a distância por valores tabelados de velocidade etc. 

$\hookrightarrow$ Além disso podemos utilizar no cenário de séries numéricas (como de Taylor etc).

# Expressão Numérica

$\hookrightarrow$ Somos capazes de integrar numericamente substituindo $f(x)$ que queremos integrar pelo polinômio em $[a, b]$ tal que:

$$
\boxed{\int ^b _ a f(x) fx \approx A_0f(x_0)  + A_1f(x_1) + ... + A_n f(x_n), \ \ \ x_i \in [a, b],  \ \ i = 0, ..., n}
$$

$\hookrightarrow$ E teremos como objetivo dos diferentes métodos numéricos encontrar $A_1, ..., A_n$.

# Fórmulas de Newton-Cotes

$\hookrightarrow$ Método numérico utilizando interpolação polinomial em pontos igualmente espaçados com passos $h = \frac{b - a}{n}$.

## Fórmulas Fechadas

$\hookrightarrow$ No caso das fórmulas fechadas de Newton-Cotes temos que os limites de integração coincidem com os extremos dos pontos:

$$
x_0 = a, \ \ \ x_n = b \therefore \int^b_a f(x)dx = \int^{x_n}_{x_0} f(x) dx \approx \sum_{i = 0}^n A_i f(x_i)
$$

$\hookrightarrow$ Onde os coeficientes $A_i$ dependem do grau do polinômio interpolador.

# Regra dos Trapézios

$\hookrightarrow$ A regra dos trapézios são quando o polinômio interpolador da [forma de Lagrange](Interpolac%CC%A7a%CC%83o%20Polinomial%20Forma%20de%20Lagrange%20fcac697df44c450a821a7d1aa2e3ffc5.md)  $p_n(x)$ é de ordem $1$.

$\hookrightarrow$ Como é um polinômio de ordem 1 temos a necessidade de $n+1$ pontos (no nosso caso são **2 pontos**), resultando em:

$$
\int^b _a f(x0 \approx \int^{x_1}_{x_0} p_1(x)dx = \int^{x_1}_{x_0} \sum^n _{k=0} y_k L_k(x)dx = I_T
$$

$\hookrightarrow$ Que após algumas substituições teremos que:

$$
\boxed{I_T = \frac{h}{2} [f(x_0) + f(x_1)]}
$$

![Screen Shot 2021-11-28 at 2.02.20 PM.png](Integrac%CC%A7a%CC%83o%20Nume%CC%81rica%20Regra%20dos%20Trape%CC%81zios%20f093406d96ee49529062896b18988714/Screen_Shot_2021-11-28_at_2.02.20_PM.png)

## Erro de Aproximação

$\hookrightarrow$ O erro de aproximação tem influência do erro do polinômio, resultando na seguinte expressão para o erro:

$$
E_T = \frac{1}{2}\int^{x_1}_{x_0} g(x) f''(\xi) dx,  \ \ \ g(x) = (x-x_0)(x-x_1),  \ \  \xi \in [x_0, x_1]
$$

$\hookrightarrow$ Não sabemos, entretanto, $f''(\xi)$. Mas através do teorema do valor médio geral podem desenvolver a expressão do erro acima para:

$$
\boxed{E_T = \frac{-h^3}{12} f''(c),  \ \ c \in (x_0, x_1)}
$$

# Regra dos Trapézios → Versão Repetida

$\hookrightarrow$ Como vimos anteriormente, para a regra do trapézio  nós calculamos a integral como sendo a área do trapézio com bases no limite de integração. Isso resulta em um erro muito grande quando os extremos são muito distântes.

$\hookrightarrow$ Para combater isso fazemos uma versão iterativa da regra dos trapézios, dividindo $[a,b]$ em espaçamentos iguais e aplicamos a regra do trapézio em cada subintervalo.

$$
\begin{aligned}
\int^b_a f(x)dx &= \sum^{m-1}_{i=0}\int ^{x_{i+1}}_{x_i}  f(x)dx\\
&=  \sum^{m-1}_{i=0}(\frac{h}{2} [f(x_i) + f(x_{i+1})])-\frac{h^3}{12}{}f''(c_i)
\end{aligned}
$$

$\hookrightarrow$ Resultando em:

$$
\boxed{I_{TR} = \frac{h}{2} \{f(x_0) + 2[f(x_1) + f(x_2) + ... + f(x_{m-1})] + f(x_m) \}}
$$

$$
\boxed{E_{TR} = \frac{-mh^3 f''(\xi)}{12},  \ \ \xi \in (a, b)}
$$

$\hookrightarrow$ Além disso, para o erro temos:

$$
M_2 = \max_{x \in [a, b]} |f''(x)| \\ \Downarrow \\ 
\boxed{|E_{TR}| \le \frac{b-a}{12} h^2 M_2}
$$