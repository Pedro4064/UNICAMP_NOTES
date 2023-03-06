# Equação de Bernoulli

Aula: Aula 2
Created: March 28, 2021 2:41 PM
Prova: P1

## O que é?

- Podemos simplificar e falar que a equação de Bernoulli é uma equação por substituição especial, quando a variável dependente $y$ está elevada a alguma potência:

$$
\frac{dy}{dx} + p(x)y = q(x)y^{\alpha} \ \ \ \ \ \ \ [1]
$$

## Como resolver

- Para resolvermos as equações de Bernoulli, precisamos realizar a seguinte substituição:

$$
u = y^{1- \alpha}
$$

- Depois disso precisamos achar sua derivada:

$$
\frac{du}{dx} = \underbrace{(1-\alpha)y^{-\alpha}}_{A}\frac{dy}{dx}
$$

- Após isso precisamos multiplicar ambos os membros da equação 1 pelo elemento $A$ destacado anteriormente, oriundo da derivada $u'$:

$$
\begin{aligned}
(1-\alpha) y^{-\alpha}\frac{dy}{dx} + (1-\alpha) y^{-\alpha} \ p(x)y &= (1-\alpha) y^{-\alpha} q(x)y^{\alpha} \\

(1-\alpha) y^{-\alpha}\frac{dy}{dx} + (1-\alpha) y^{1 -\alpha} \ p(x) &= (1-\alpha)q(x) \\ 

(1-\alpha) y^{-\alpha}\frac{dy}{dx} + (1-\alpha) u \ p(x) &= (1-\alpha)q(x) \\ 
\end{aligned}
$$

- Assim que realizarmos a multiplicação, iremos perceber que podemos substituir o elemento contendo $dy/dx$ pelo $du/dx$:

$$
\begin{aligned}
\underbrace{(1-\alpha) y^{\alpha}\frac{dy}{dx}} + + (1-\alpha) u \ p(x) &= (1-\alpha)q(x)\\ 

\frac{du}{dx}+ + (1-\alpha) u \ p(x) &= (1-\alpha)q(x) \\ 

\end{aligned}
$$

- A partir de agora pode-se resolver por fator integrante normalmente.

## Exemplo

### Exemplo 1

$$
x\frac{dy}{dx} + 6y = 3xy^{4/3}
$$

- Primeiramente podemos dividir tudo por $x$ para facilitar

$$
\frac{dy}{dx} + 6\frac{y}{x} = 3\frac{y^{4/3}}{x}
$$

- Agora podemos identificar como uma equação de Bernoulli pois o termo dependente $y$ está elevado à um número $\alpha$ que nesse caso é $\alpha = \frac{4}{3}$.
- Com isso podemos efetuar a substituição característica de Bernoulli:

$$
u = y^{1-\alpha} \Rightarrow u = y^{-1/3}
$$

- Agora podemos calcular sua derivada em função de $x$

$$
u' = \underbrace{-\frac{1}{3}y^{4/3} }_{A}\frac{dy}{dx}
$$

- Podemos então multiplicar toda a equação original pelo termo $A$:

$$
\begin{aligned}
\overbrace{\left(-\frac{1}{3}y^{4/3} \frac{dy}{dx}\right)}^{u'} + \left(-\frac{1}{3}y^{4/3}\right)\left(6\frac{y}{x}\right) &= \left(-\frac{1}{3}y^{4/3}\right)\left(3\frac{y^{4/3}}{x}\right) \\ 

u' + \left(-2y^{-1/3}\right)\left(\frac{1}{x}\right) &= -\left(\frac{1}{x}\right) \\ 

u' + \left(-2u\right) &= -1 \\ 
\end{aligned}
$$

- Sabemos agora que podemos resolver por meio do fator integrante, que é: $\mu = \exp\int-2dx = e^{-2x}$
- Com isso podemos multiplicar ambos os lados pelo fator integrante $\mu$.

$$
\begin{aligned}
\frac{d}{dx}(\mu(x)u) &= -e^{-2x} \\ 
\end{aligned}
$$

- Se fizermos a derivada e isolarmos $u$, poderemos depois substituir novamente para achar $y$.