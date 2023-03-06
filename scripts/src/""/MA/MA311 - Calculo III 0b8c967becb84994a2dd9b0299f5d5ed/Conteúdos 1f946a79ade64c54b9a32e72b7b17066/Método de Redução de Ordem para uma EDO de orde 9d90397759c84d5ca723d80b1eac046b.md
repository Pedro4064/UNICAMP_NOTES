# Método de Redução de Ordem para uma EDO de ordem 2 ou maior, homogênea e com uma solução conhecida

Aula: Aula 6
Created: April 12, 2021 7:25 PM
Prova: P1

# Modelo de Equação

$$
y'' + p(x)y' + q(x)y=0
$$

- Onde sabemos uma solução $y_1 \ne 0$

# Como Resolver

- Precisamos achar uma outra solução $y_2$ para nossa EDO Homogênea.

$$
\boxed{y_2(x) = y_1(x) \int \frac{e^{-\int p(x)dx}}{[y_1(x)]^2}dx}
$$

<aside>
<img src="Me%CC%81todo%20de%20Reduc%CC%A7a%CC%83o%20de%20Ordem%20para%20uma%20EDO%20de%20orde%209d90397759c84d5ca723d80b1eac046b/Evangelion.gif" alt="Me%CC%81todo%20de%20Reduc%CC%A7a%CC%83o%20de%20Ordem%20para%20uma%20EDO%20de%20orde%209d90397759c84d5ca723d80b1eac046b/Evangelion.gif" width="40px" /> OBS: Dentro da Integral é $p(x)$, da equação original com $y''$ sendo multiplicado por 1, se estiver sendo multiplicado por outra coisa, divida toda a equação.

</aside>

# Exemplo

$$
y'' + 4y' + 4y = 0, \ \ \ \ y_1(x) = e^{-2x}
$$

- Como sabemos $y_1$, podemos utilizar a formula para acharmos $y_2$

$$
\begin{aligned}
y_2(x) &= y_1(x) \int \frac{e^{-\int p(x)dx}}{[y_1(x)]^2}dx \\ 

y_2(x) &= e^{-2x} \int \frac{e^{-\int 4dx}}{[e^{-2x}]^2}dx \\ 

y_2(x) &= e^{-2x} \int \frac{e^{-4x}}{e^{-4x}}dx \\ 

y_2(x) &= xe^{-2x}
\end{aligned}
$$