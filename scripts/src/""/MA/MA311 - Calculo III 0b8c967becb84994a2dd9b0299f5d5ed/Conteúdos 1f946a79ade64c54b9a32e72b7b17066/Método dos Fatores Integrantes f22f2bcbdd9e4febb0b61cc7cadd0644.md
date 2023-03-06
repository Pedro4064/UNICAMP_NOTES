# Método dos Fatores Integrantes

Aula: Aula 1
Created: March 15, 2021 7:04 PM
Prova: P1

## Introdução

Algumas vezes, o método de resolução direto não é suficiente para resolvermos nossa EDO, por isso existem outros métodos. O que iremos cobrir aqui será o método de fatores integrantes, que consiste na multiplicação de toda a equação por uma função $\mu(x)$ com a finalidade de tornar mais fácil a identificação da derivada da função original, isso é, a nossa integral fique reconhecível.

Iremos levar em consideração a estrutura básica da EDO como sendo:

$$
\frac{dy}{dx} + ay = g(x) \ \ \ \ \ [1]
$$

- Onde $a$ pode ser em função de $x$ e $g(x)$ uma função dada.

## Achando a Função Integrante

<aside>
<img src="Me%CC%81todo%20dos%20Fatores%20Integrantes%20f22f2bcbdd9e4febb0b61cc7cadd0644/mugi.gif" alt="Me%CC%81todo%20dos%20Fatores%20Integrantes%20f22f2bcbdd9e4febb0b61cc7cadd0644/mugi.gif" width="40px" /> De modo Geral, a função integrante $\mu(x) = exp \int a \: \:  dx$

</aside>

- Assim que acharmos a função integrante, basta multiplicar ambos os lados da EDO por ele e integrar, isolando o $y$ do lado esquerdo.

## Exemplos

### Exemplo 1

$$
\frac{dy}{dx} - 2y = 4 - x 
$$

- Primeiro passo é arrumar a função para que fique no formato da equação de número $1$:

$$
\frac{dy}{dx} \underbrace{- 2}_{a}y = \overbrace{4 - x }^{g(x)}
$$

- Com isso sabemos que a função integrante $\mu(x) = exp \int -2 dx = e^{-2x}$, e podemos multiplicar ambos os lados da equação por ele:

$$
\begin{aligned}
e^{-2t}( \frac{dy}{dx} - 2y ) &= e^{-2t}(4 - x) \\ 

\underbrace{e^{-2x} \frac{dy}{dx} - e^{-2x}2y}  &= 4e^{-2x} - e^{-2x}x \\ 

\end{aligned}
$$

Devido à multiplicação pelo fator integrante, somos capazes de identificar que isso nada mais é do que a derivada: $\frac{d}{dx} \mu(x)y$. Para facilitar iremos reescrever a equação

$$
\boxed{
\frac{d}{dx} (e^{-2x}y) = 4e^{-2x} - e^{-2x}x
}
$$

- Agora é bem mais fácil, precisamos apensar integrar em ambos os lados para acharmos $y$:

$$
\begin{aligned}

\int \frac{d}{dx}(e^{-2x}y) &= \int (4e^{-2x} - e^{-2x}x )dx \\

e^{-2x}y &= - \left( - \frac{1}{4} e^{-2x} (2x+1)\right) + C \\

e^{-2x}y &= -2e^{-2x} + \frac{1}{2} xe^{-2x} + \frac{1}{4}e^{-2x} + C\\

\end{aligned}
$$

$$
\boxed{y = -\frac{7}{4} + \frac{1}{2}x + Ce^{2x}}
$$

Onde $C$ é uma constante