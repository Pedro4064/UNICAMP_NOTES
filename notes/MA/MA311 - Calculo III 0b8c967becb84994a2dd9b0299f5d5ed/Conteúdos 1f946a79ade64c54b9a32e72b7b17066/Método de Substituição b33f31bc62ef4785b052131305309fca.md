# Método de Substituição

Aula: Aula 2
Created: March 28, 2021 2:16 PM
Prova: P1

## O que é?

- Em alguns casos podemos substituir uma equação diferencial que seria muito difícil ou que não saberíamos como resolver substituindo as variáveis por uma variável.

## Exemplos

### Exemplo 1

Resolva a EDO: 

$$
x\frac{dy}{dx} = y + xe^{\frac{y}{x}}
$$

- Podemos dividir ambos os lados por $x$:

$$
\frac{dy}{dx} = \frac{y}{x} + e^{\frac{y}{x}}
$$

- Agora podemos substituir $\frac{y}{x} = u \Rightarrow y = ux 
 \therefore \frac{dy}{dx} = u + x\frac{du}{dx}$

$$
\begin{aligned}
u + x\frac{du}{dx} &= u + e^u \\ 
xu' &=  u - u + e^u \\
xu' &=  e^u \\
u' &= e^u \frac{1}{x} \\
e^{-u} u' &=  \frac{1}{x} \\
\int e^{-u} du &= \int x^{-1}dx\\
-e^{-u} &= ln|x| + c \\
u &= -ln(-ln|x| - c) \\
\end{aligned}
$$

- Agora podemos fazer a substituição de volta:

$$
y = -x \ \ln(-ln|x| - c)
$$

Nesse exemplo que foi dado, após fazermos a substituição $u = \frac{y}{x}$ a equação virou uma EDO separável, o que facilitou a resolução. Esse caso especial é chamado de equação homogência de primeira ordem da seguinte forma:

$$
\boxed{\frac{dy}{dx} = f\left(\frac{y}{x}\right),  \ \ \ x\ne 0}
$$