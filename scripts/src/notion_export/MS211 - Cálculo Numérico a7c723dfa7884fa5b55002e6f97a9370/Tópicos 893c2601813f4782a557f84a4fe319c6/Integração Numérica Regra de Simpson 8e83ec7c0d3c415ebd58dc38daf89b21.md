# Integração Numérica: Regra de Simpson

Aula: Aula 28
Created: November 28, 2021 5:20 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Vimos anteriormente que os diferentes métodos/regras para integração numérica depende da ordem do polinômio utilizado para a interpolação.

$\hookrightarrow$ Vimos também que quando a ordem é $1$ temos a chamada regra do trapézio. Mas veremos agora quando a ordem do polinômio de aproximação é $2$ → A chamada regra de Simpson.

# Formulação

$\hookrightarrow$ Assim como na regra do trapézio iremos encontrar o nosso polinômio através do método de lagrange. 

$\hookrightarrow$ No método de Simpson, entretanto, esse polinômio é de grau $n = 2$ e, por conseguinte, precisamos de $n+1 \therefore 3$ pontos.

$$
\begin{cases}
x_0 = a \\ 
x_1 = x_0 + h \\ 
x_2 = x_0 + 2h = b
\end{cases}
$$

$\hookrightarrow$ Resultando no polinômio:

$$
p_2(x) = \frac{(x - x_1)(x-x_2)}{(-h)(-2h)} f(x_0) + \frac{(x - x_0)(x-x_2)}{(h)(-h)} f(x_1) + \frac{(x - x_0)(x-x_1)}{(2h)(h)} f(x_2)
$$

$\hookrightarrow$ Que terá a seguinte fórmula para a integral:

$$
\boxed{\int^{x_2}_{x_0} f(x)dx \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)] = I_S}
$$

## Erro

$\hookrightarrow$ E terá como fórmula do erro:

$$
\boxed{E_S = \frac{-h^5}{90} f^{(IV)}(c),  \ \ \ c \in (x_0, x_2)}
$$

- Onde $f^{(IV)}$ é a derivada quarta.

# Regra de Simpson Repetida

$\hookrightarrow$ De forma análoga a como foi feita para a regra dos trapézios, iremos subdividir nosso conjunto $[a, b] = [x_0, x_m]$ em $m+1$ subconjuntos e aplicar a regra de Simpson para cada uma delas.

$$
\boxed{I_{SR} = \frac{h}{3}\{[f(x_0) + f(x_m)] +4[f(x_1) + f(x_3)+...+ f(x_{m-1})] + 2[f(x_2) + f(x_4) + ... + f(x_{m-2})]\}}
$$

- Basicamente tirando $x_0$ e $x_m$ nós multiplicamos por $4$ os que tiverem índice ímpar e por $2$ os que tiverem os índices pares.

## Erro

$$
\boxed{E_{SR} = - \sum^{m/2}_{k=1} \frac{h^5}{90}f^{(IV)}(c_k) ,  \ \ \ c_k \in (x_{2k - 2}, x_{2k})}
$$

$\hookrightarrow$ E se expressarmos por termo limitante temos:

$$
M_4 = \max_{x \in [x_0, x_m]}  |f^{(IV)}(x)|  \\ \Downarrow \\ 
\boxed{|E_{SR}| \le \frac{(b - a)h^4}{180} M_4}
$$