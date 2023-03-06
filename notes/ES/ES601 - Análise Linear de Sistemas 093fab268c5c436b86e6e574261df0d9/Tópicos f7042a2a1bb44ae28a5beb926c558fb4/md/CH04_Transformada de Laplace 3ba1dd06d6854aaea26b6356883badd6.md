# Transformada de Laplace

Created: September 8, 2022 3:41 PM

[Anotações de Aula](Transformada%20de%20Laplace%203ba1dd06d6854aaea26b6356883badd6/Anotac%CC%A7o%CC%83es%20de%20Aula%20449f385a0f564b3a95858cc2a4879d34.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ A transformada de Laplace é uma ferramenta muito importante pois passa nossa função em análise do domínio dos números reais $\R$ para o domínio dos números complexos, que pode ser interpretado como como a mudança do domínio do tempo $t$ para o domínio da frequência.

$\hookrightarrow$ Além desse novo domínio de análise, as equações diferenciais se tornam problemas meramente algébricos e polinomiais, o que facilita a sua solução. Ademais, ao descrevermos nosso sistema no domínio de Laplace (denominado domínio $s$) seremos capazes de descrever nosso sistema através de Funções de Transferência (que são muito úteis na análise da resposta do nosso sistema para diferentes formas de entradas/termos forçantes).

$\hookrightarrow$ A transformada é dada pela seguinte integral:

$$
\begin{align}
\mathcal L\{f(t)\}  = F(s) = \int_{0^-}^{\infty}f(t)e^{-st}dt
\end{align}
$$

$\hookrightarrow$ Em que:

$$
\begin{align}
s = \underbrace{\sigma}_{real} + \overbrace{j\omega}^{Imaginário}
\end{align}
$$

$\hookrightarrow$ Onde é importante salientar que a transformada acima é chamada de "transformada unilateral de Laplace”, pois vai, nos limites de integração, de $0^- \rightarrow \infty$ , e não de $-\infty \rightarrow \infty$. 

# Requisito de Existência

$\hookrightarrow$ O principal requisito de existência para a transformada de Laplace de uma função $f(t)$ é que haja uma ***abcissa de convergência***, i.e um ponto no plano $s$ onde a integral que define a transformada converge, e não vá para infinito.

$\hookrightarrow$ Tal abcissa de convergência existe sempre que houver um $\sigma$ que, para $t$ tendendo a $\infty$, a função abaixo tende a ir para zero, e não a infinito:

$$
\begin{align}
\lim_{t\rightarrow \infty}|f(t)|e^{\sigma t} = 0
\end{align}
$$

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> Em suma, antes de aplicar a transformada de Laplace é necessário averiguar se há um $\sigma$  tal que o limite descrito acima tenda a zero, e não a infinito. Caso não houver a transformada de Laplace não pode ser aplicada.

</aside>

# Transformadas das Principais Funções

$\hookrightarrow$ Nos problemas que iremos analisar, encontraremos, de forma recorrente, algumas funções que por sua vez possuem transformadas de Laplace bem conhecidas.

$\hookrightarrow$ Iremos, nessa parte do Capítulo, derivar a partir das funções comuns suas Transformadas.

## Função Exponencial

- Seja a função exponencial dada por:

$$
f(t) = \begin{cases}
Ae^{-\alpha t} & , t\ge0 \\ 
0 & , t<0
\end{cases}
$$

- Ao aplicarmos a definição da transformada de Laplace, como estamos calculando a Laplace Unilateral, logo só iremos analizar a partir de $t\ge0$ temos:
    
    $$
    
    \mathcal L\{f(t)\} = \int_{0^-}^{\infty}Ae^{-\alpha t}e^{-st}dt
    
    $$
    
- A partir de agora precisamos, antes de dar continuidade e resolver a integral, verificar se há a abcissa de convergência, isso é, se existe um $\sigma$ tal que $\lim_{t\rightarrow \infty Ae^{-\alpha t} e^{-\sigma t}} = 0$:
    
    $$
    \begin{aligned}
    \lim_{t\rightarrow\infty}\left(Ae^{-\alpha t} e^{-\sigma t}\right) &= \lim_{t\rightarrow\infty}\left(Ae^{-\alpha t +(-\sigma t)}\right)  \\ 
    &= \lim_{t\rightarrow\infty}\left(Ae^{-t (\alpha + \sigma)}\right)  
    \end{aligned}
    $$
    
- Onde:
    
    $$
    \begin{aligned}
    \lim_{t\rightarrow\infty}\left(Ae^{-t (\alpha + \sigma)}\right)    = 0&\iff (\alpha + \sigma) > 0 \\ &\therefore \sigma = -\alpha
    \end{aligned}
    $$
    
- Pois, caso o parênteses que está presente na exponencial de negativo, juntamente com o sinal de negativo do $t$, ao invés de termos o $t$, que tende ao infinito, no denominador (e por conseguinte levando a zero o limite), teremos ele no numerador (o que resultará em uma indeterminação pois vai a $\infty$).
- A partir desse ponto, provamos que existe a abcissa de convergência $\therefore$ a existência da transformada de Laplace para a função em questão, podemos resolver a integral:
    
    $$
    \begin{aligned}
    \mathcal L\{f(t)\} &= \int_{0^-}^{\infty}Ae^{-\alpha t}e^{-st}dt \\ 
    &= \int_{0^-}^{\infty}Ae^{-t(\alpha +s)}dt \\ 
    &= A\frac{-1}{(\alpha + s) }\left[\lim _{t\rightarrow\infty} (e^{-t(\alpha + s)}) - e^0\right]
    
    \end{aligned}
    $$
    
- No que tange o limite acima, como, ao provar a existência da abcissa de convergência, averiguamos a existência de um $\sigma$ tal que $f(t) e^{-t\sigma} \rightarrow 0$ quando $t \rightarrow \infty$ e que, por definição, $s= \sigma + j\omega$, podemos decompor o limite acima deixando explicito o $\sigma$, e decompondo a parte imaginaria pela identidade de Euler em seno e cosseno, resultando em:
    
     
    
    $$
    \begin{aligned}
    \lim_{t\rightarrow \infty} (e^{-t(\alpha + s)}) &= \lim_{t\rightarrow \infty} (e^{-t(\alpha + \sigma + j\omega)}) \\ 
    &= \lim_{t\rightarrow \infty} (e^{-t(\alpha + \sigma)} \cdot e^{ j\omega}) \\ 
    
    &= \lim_{t\rightarrow \infty} (e^{-t(\alpha + \sigma)} \cdot e^{ j\omega t}) \\ 
    
    &= \lim_{t\rightarrow \infty} (\underbrace{e^{-t(\alpha + \sigma)}}_{0} \cdot (\cos (\omega t) - j\sin (\omega t))) \\ 
    
    &= 0
    \end{aligned}
    $$
    
- A partir desse ponto, provamos que o limite tende a zero logo temos:
    
    $$
    \mathcal L \{A e^{-\alpha t }\} = +A\frac{1}{(\alpha + s)}
    $$
    
- Por fim, é importante introduzir o conceito de Polo de uma função no plano $S$, que representa o valor de $s$ para o qual a função vai para infinito, nesse caso temos um polo em  $s = -\alpha$.

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> IMPORTANTE: Uma função de ordem $n$ terá $n$ polos, mesmo se forem repetidos é importante falar o valor do polo e ressaltar a multiplicidade (quantidade de vezes que o valor é polo)

</aside>

## Função Degrau

- Para a função degrau (também chamada de Heaviside Function), que é dada por:
    
    $$
    f(t) = \begin{cases}
    1 & , t \ge 0 \\ 
    0 & , t < 0
    \end{cases}
    $$
    
- 

## Função Rampa

## Função Impulso (Delta de Dirac)