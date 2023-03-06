# Integração Numérica: Quadratura Gaussiana

Aula: Aula 29
Created: November 28, 2021 5:48 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$   Até o momento vimos formas de integrar pelas diferentes fórmulas de Newton-Cotes. 

$\hookrightarrow$  Elas, entretanto, tinha a limitação de que os nossos dados tabelados estivessem distribuídos igualmente (i.e o nosso $\Delta x = h$ tinha que ser igual para todos os pontos).

$\hookrightarrow$  Iremos introduzir agora fórmulas similares às de Newton-Cotes , mas sem a limitação supracitada, mas que terá a necessidade da fórmula exata para polinômios de grau $\le (2n + 1)$.

# Formulação

$\hookrightarrow$  Tendo como exemplo:

$$
\int^{a = 2}_{b = 1} f(x) dx
$$

Onde $f(x) = \ln (x)$.

 

$\hookrightarrow$  Para aplicarmos precisamos primeiramente mudar os intervalos de integração de $[a, b]$ para  $t \in [-1, 1]$:

$$
\boxed{g(t) = \frac{1}{2}[a + b + t(b - a)]} \\ \Downarrow \\    \frac{3}{2} + \frac{1}{2} t
$$

e 

$$
\boxed{dx = \frac{b-a}{2}dt} \\ \Downarrow \\ \frac{1}{2} dt
$$

$\hookrightarrow$  Que resultará na seguinte integral:

$$
\int^2_1 \ln (x) dx = \frac{1}{2} \int^1_{-1} \ln(\frac{3}{2} + \frac{1}{2}t)dt = I
$$

$\hookrightarrow$  E é a partir dessa integral transformada $I$ que iremos aplicar a fórmula:

$$
\boxed{I \approx \frac{1}{2} [A_0 g(t_0) + A_1g(t_1)]}
$$

Onde, para TODOS OS CASOS:

$$
\begin{cases}
t_0 = \frac{-\sqrt{3}}{3} \\ 
t_1 = \frac{\sqrt{3}}{3} \\ 
A_0 = A_1 = 1
\end{cases}
$$