# Teorema de Existência e Unicidade

Aula: Aula 4
Created: March 30, 2021 11:08 AM
Prova: P1

# EDO Linear

- Considerando a forma padrão de PVI:

$$
y'+ p(x)y = g(x), \ \ \ \ y(x_0) = y_0
$$

Temos que a EDO é tem valor único se ambas as funções $p(x)$ e $g(x)$ forem contínuas no intervalo aberto contendo $x_0$ e $y_0 \in \R$.

## Exemplo

$$
xy'+ 2y = 4x^2, \ \ \  y(1) = 2
$$

- Primeiramente precisamos reorganizar a nossa função:

$$
xy'+ 2y = 4x^2 \rightarrow y' + \frac{2}{x}y = 4x
$$

- Agora identificamos nossas funções:

$$
y' + \underbrace{\frac{2}{x}}_{p(x)}y = \overbrace{4x}^{g(x)}
$$

- Verificamos se são contínuas em algum subespaço de $\R$ que inclua os valores do PVI, que são $x = 1, y=2$. Tal subespaço seria $x,y \in \R \ \ | x > 0$, então para esse intervalo (que contém os valores do PVI) essa EDO tem somente uma única solução.

# EDO Não Linear

Considerando a seguinte forma de uma EDO não linear:

$$
y' = f(x,y),  \ \ \ y(x_0) = y_0
$$

Onde $f: \R^2 \longrightarrow \R$, temos que a EDO tem valor único se a derivada parcial  em relação a $y$ de $f, \frac{\partial f}{\partial y}$, é contínua em uma reunião retangular: 

$$
R = \{(x,y) \in \R^2: \alpha < x < \beta, \lambda<y<\delta \}
$$

A qual contém os pontos $x_0$ e $y_0$

## Exemplo

$$
y' = x\sqrt{y},  \ \ \ \ y(0) = 0
$$

Primeiramente identificamos nossa função $f$ sendo $f(x,y) = x\sqrt{y}$, agora podemos verificar sua derivada parical em relação à $y$:

$$
\frac{\partial }{\partial y } (x \sqrt{y}) = \frac{1}{2}xy^{-\frac{1}{2}} = \frac{x}{2 \sqrt{y}}
$$

Devido ao seu denominador, essa EDO só possui um valor para o subconjunto $\{(x,y) \in \R^2 | y>0 \}$, mas devido ao valor de PVI, sabemos que não possui solução para esse valor inicial.