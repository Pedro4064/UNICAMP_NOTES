# Equações de 2a Ordem Redutíveis

Aula: Aula 4
Created: March 31, 2021 11:19 AM
Prova: P1

# Introdução

Uma equação diferencial ordinária de segunda ordem, na forma mais geral, pode ser escrita como: 

$$
F(x,y,y',y'') = 0
$$

Uma EDO de segunda ordem pode ser reduzida à uma EDO de primeira ordem se ou $x$  (variável independente) ou $y$ (variável dependente) não aparece na equação.

# Equação sem a variável $y$

Em tais casos, a EDO apresenta somente as derivadas da variável $y$, como $y' \ e \ y''$.

Para reduzirmos, precisamos fazer a seguinte substituição: 

$$
V = y' \therefore V' = y''
$$

## Exemplo

$$
xy''+ 2y'= 6x
$$

- Primeiramente fazemos a mudança de variável:

$$
v = y' \therefore v'= y'' \\
\Downarrow
$$

$$
xv' + 2v = 6x
$$

- Com isso temos um exemplo clássico de EDO linear no qual podemos utilizar o método de fatores integrantes:

$$
v' + \underbrace{\frac{2}{x}}_{A}v = 6
$$

- Com isso precisamos encontrar o fator integrante $\mu$ que é igual à :

$$
\begin{aligned}
\mu &= \exp \int A dx \\ 
\mu &= \exp\int2x^{-1}dx \\
\mu &= \exp 2\ln|x| \\
\mu &= e^{2\ln|x|} \\
\mu &= e^{\ln|x^2|} \\
\mu &= x^2
\end{aligned}
$$

- Agora podemos multiplicar toda a EDO pelo fator integrante:

$$
\begin{aligned}
\frac{d}{dx} (\mu v) &= 6x^2 \\ 
\mu v &= \int 6x^2 dx \\ 
\mu v &= 2x^3 + c_1 \\ 
x^2 v &= 2x^3 + c_1 \\ 
v &= 2x + c_1x^{-2}
\end{aligned}
$$

- Com temos o valor de $v$, podemos fazer a transformação de volta para $y$:

$$
\begin{aligned}
y(x) &= \int 2x+c_1x^{-2} \\ 
&= x^2 - \frac{c_1}{x} + c_2
\end{aligned}
$$

# Equação sem a variável $x$

Quando temos uma EDO onde a variável $x$ não está presente, podemos fazer a seguinte substituição:

$$
v = y' \therefore y''=vv'
$$

## Exemplo

$$
yy''=(y')^2
$$

- Nesse caso não temos a variável independente $x$, logo podemos fazer a substituição demonstrada anteriormente.

$$
yvv' = v^2
$$

- Com isso temos uma equação separável.

$$
v^{-1}v' = \frac{1}{y}
$$

- Integrando temos:

$$
\begin{aligned}
\int v^{-1} dv &= \int y^{-1}dy \\ 
\ln|v| &= \ln|y| + c_1
\end{aligned}
$$

- Para nos livrarmos dos logs podemos fazer:

$$
\begin{aligned}
\ln|v| &= \ln|y| + c_1 \\ 
e^{\ln|v|} &= e^{\ln|y| + c_1 } \\ 
v &= ye^{c_1} \\ 
\end{aligned}
$$

- Agora podemos fazer a transformação de volta:

$$
\begin{aligned}
\frac{dy}{dx} &= ye^{c_1} \\ 
y^{-1}\frac{dy}{dx} &=e^{c_1} \\ 
\ln|y| &= \int e^{c_1}dx \\ 
\ln|y| &= e^{c_1}x + c_2 \\ 
\end{aligned}
$$