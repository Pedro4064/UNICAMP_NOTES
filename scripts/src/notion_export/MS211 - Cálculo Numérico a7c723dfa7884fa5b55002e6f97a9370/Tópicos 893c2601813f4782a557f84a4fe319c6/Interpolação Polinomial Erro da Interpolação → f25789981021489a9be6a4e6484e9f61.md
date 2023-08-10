# Interpolação Polinomial:  Erro da Interpolação → Função Contínua

Aula: Aula 25
Created: November 25, 2021 8:21 PM
Prova: P2

- SUMÁRIO

# Definição

$\hookrightarrow$ Sejam os pontos tabelados $(x_0, y_0), ..., (x_n, y_n)$, isto é, $y_k = f(x_k),  \ \ k= 0, ..., n$, e $p_n$ o polinômio interpolador temos que:

$$
x \in [x_0, x_n]: \\
E_n(x)= f(x) - p_n(x)
$$

$\hookrightarrow$ Sendo que para $x$ tabelado teremos erro $0$, pois ele foi condicionado para isso acontecer.

# Aproximação

$\hookrightarrow$ Vimos anteriormente que o erro de uma interpolação nada mais é do que a diferença entre o calculado e o valor real. Nos cenários onde utilizamos interpolação polinomial, entretanto, não sabemos o valor real. Levando isso em consideração precisamos calcular um valor aproximado do erro:

- Seja $p_{n+1}(x)$ o polinômio interpolador em $x_0, x_1, ..., x_n$ e $\bar x \in [x_0, x_n]$.
- Logo teremos:
    
    $$
    p_{n+1}(x) = p_n(x) + f[x_0, ..., x_n, \bar x] \prod^n _{j=0}(x-x_j)
    $$
    
- Que resultara em um erro:
    
    $$
    f(\bar x) - p_n(\bar x) = f[x_0, ..., x_n, \bar x] \prod^n_{j=0}(\bar x - x_j)
    $$
    
- Não sabemos, entretanto, o valor de $f[x_0, ..., x_n, \bar x]$ logo precisamos aproximar esse valor, que é possível através da derivada de ordem $n+1$ da função que gerou os pontos do gráfico.

$$
f[x_0, ..., x_n, \bar x] \approx f^{n+1}(\bar x)
$$

- Que resulta no teorema $1$ e $2$ e no corolário do erro da interpolação.

## Teorema $2$ do erro da interpolação

$$
f(\bar x) - p_n (\bar x) = \frac{f^{n+1} (\xi)}{(n+1)!} \prod^n_{j=0}(\bar x - x_j),  \ \ \forall \bar x \in (x_0, x_n),  \ \ x_0 \le \xi \le x_n
$$

## Corolário $1$

$\hookrightarrow$ Se:

$$
M_{n+1} = \max _{x \in [x_0, x_n]} |f^{(n+1)}(x)|
$$

$\hookrightarrow$ Então:

$$
\boxed{E_n(x) \le \frac{M_{n+1}}{(n+1)!} \  \left| \prod^n_{j=0}(\bar x - x_j)\right|}
$$

## Corolário 2 → Nós Igualmente Espaçados

$\hookrightarrow$ Seja:

$$
x_k = x_0 + kh,  \ \ k=0, ..., n
$$

$\hookrightarrow$ E:

$$
M_{n+1} = \max _{x \in [x_0, x_n]} |f^{(n+1)}(x)|
$$

$\hookrightarrow$ Então:

$$
\boxed{|E_n(x)| \le \frac{M_{n+1}h^{n+1}}{4(n+1)}}
$$

<aside>
<img src="Interpolac%CC%A7a%CC%83o%20Polinomial%20Erro%20da%20Interpolac%CC%A7a%CC%83o%20%E2%86%92%20f25789981021489a9be6a4e6484e9f61/Screen_Shot_2021-09-23_at_11.49.01_PM.png" alt="Interpolac%CC%A7a%CC%83o%20Polinomial%20Erro%20da%20Interpolac%CC%A7a%CC%83o%20%E2%86%92%20f25789981021489a9be6a4e6484e9f61/Screen_Shot_2021-09-23_at_11.49.01_PM.png" width="40px" /> Que não depende de $\bar x$. Logo somos capazes de determinar um $h$ específico para que esteja de acordo com nosso erro alvo.

</aside>