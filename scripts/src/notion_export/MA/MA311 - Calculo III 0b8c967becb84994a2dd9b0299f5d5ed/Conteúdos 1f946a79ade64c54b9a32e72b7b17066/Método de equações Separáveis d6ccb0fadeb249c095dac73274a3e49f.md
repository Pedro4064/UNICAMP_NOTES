# Método de equações Separáveis

Aula: Aula 2
Created: March 15, 2021 7:04 PM
Prova: P1

# Equações Separáveis

## Principal Forma

$$
g(y)\frac{dy}{dx} = f(x)
$$

- Onde $y \equiv y(t)$

## Exemplos e Resolução

### Ex.1

$$
\frac{dy}{dx} = \frac{x^2}{1 + y^2}
$$

- 1º Passo: Separar os termos que tem $y$ juntamente com o termo $\frac{dy}{dx}$ do lado esquerdo da equação:

$$
(1 + y^2)\frac{dy}{dx} = x^2
$$

- 2º Passo: Integrar ambos os lados com respeito a $x$, tendo em mente que $dy = \frac{dy}{dx} dx$ por definição.

$$
\begin{aligned}
\int (1 + y^2)dy &= \int x^2 dx \\
y + \frac{y^3}{3} &= \frac{x^3}{3} + c
\end{aligned}
$$

### Ex.2

$$
\frac{dy}{dx} = \frac{y - 3}{x^2}
$$

- 1º Passo: Separar os termos que tem $y$ para o lado esquerdo da equação, juntamente com o termo $\frac{dy}{dx}$:

$$
\begin{aligned}
\frac{dy}{dx} &= \frac{y - 3}{x^2} \\ 

\frac{dy}{dx} &= (y - 3)(x^{-2})\\

(y - 3)^{-1}\frac{dy}{dx} &=(x^{-2})
\end{aligned}
$$

- 2º Passo: Agora podemos integrar ambos os lados em respeito a $x$, sabendo que $\frac{dy}{dx}dx = dy$ por definição:

$$
\begin{aligned}
(y - 3)^{-1}\frac{dy}{dx} &=(x^{-2})\\

\int (y - 3)^{-1}dy &=\int (x^{-2}) dx\\

ln|y - 3| &= -x^{-1} + C

\end{aligned}
$$

- Podemos deixar $y$ na forma explícita, aplicando a exponencial em ambos os lados ficando:

$$
\begin{aligned}
y-3 &= e^{-t^{-1} + C} = e^{-t^{-1}}\underbrace{e^{C}}_{C_2} \Rightarrow y = 3 + C_2e^{-t^{-1}}

\end{aligned}
$$