# Equações Exatas

Aula: Aula 3
Created: March 29, 2021 7:00 PM
Prova: P1

# O Que é Uma Equação Exata?

- Uma equação diferencial ordinária é dita exata quando tem o seguinte modelo e segue os seguintes pré-requisitos

## Modelo de Equação

$$
y ' = f(x,y) \Rightarrow \boxed{M(x,y) + N(x,y)y' = 0}
$$

Tal que

$$
M, N: \Omega \rightarrow \R  \ \ | \Omega \ é \ subconjunto \ aberto\ de\ \R^{2}
$$

## Condições de Existência

1. $\Omega$  (Domínio das funções $M, N$ e subconjunto aberto de $\R^2$)é uma região simplesmente conexa, isso é, não possui "furos", é um subespaço "contínuo".
2. $\frac{\partial M}{\partial y}(x,y) = \frac{\partial N}{\partial x}(x,y), \forall(x,y) \in \Omega$, isso é, a derivada parcial de $M$ em função de $y$ é igual a derivada parcial de $N$ em função de $x$.
3. Todas as derivadas parciais de $M, N$ são contínuas em todos $\Omega$, sendo elas: $\frac{\partial M}{\partial y},\frac{\partial M}{\partial x}, \frac{\partial N}{\partial y},\frac{\partial N}{\partial x}$

# Como Resolver?

- Primeiramente precisamos averiguar se é uma equação exata, isso é, que está de acordo com todas as condições de Existência de uma equação exata listados anteriormente.
- Assim que verificarmos que é uma equação exata, e identificarmos o seu $M$ e $N$, sabemos que existe uma equação do tipo:

$$
\psi(x,y)
$$

- Tal que essa equação $\psi$  tenha a seguinte característica:

$$
\frac{\partial \psi}{\partial x}(x,y) = M(x,y) \ \ \ e \ \ \ \frac{\partial \psi}{\partial y}(x,y) = N(x,y)
$$

<aside>
<img src="Equac%CC%A7o%CC%83es%20Exatas%200f143b276ede4b70b428de610b67dbc1/Hifumi_Surprised.png" alt="Equac%CC%A7o%CC%83es%20Exatas%200f143b276ede4b70b428de610b67dbc1/Hifumi_Surprised.png" width="40px" /> **OBSERVAÇÃO**: Nas condições de existência nó usamos $\frac{\partial M}{\partial y}(x,y) = \frac{\partial N}{\partial x}(x,y)$, enquanto aqui nós invertemos e estamos usando $M$ em relação a $x$ da função $\psi$ e $N$ em relação a $y$ da função $\psi$, não se confundir!!!!!!

</aside>

- Com a característica acima, teremos um sistema linear com duas equações, o que irá nos possibilitar a resolução para encontrarmos nossa função $\psi(x,y)$.

## Exemplos

### Ex.1

$$
2x + y^2 + 2xyy' = 0 
$$

1- Precisamos definir se é um equação exata, para isso iremos identificar quem é a função $N$ e $M$:

$a:$ $N(x,y) = 2xy \rightarrow$ A função $N$ possui a parcela com a derivada $y'$ (mas **não** adicionamos ela).

$b:$ $M(x,y) = 2x+y^2 \rightarrow$ A função $M$ é o resto da equação.

2- Agora que identificamos as funções, podemos verificar se está de acordo com as condições de Existência, isso é: 

$a:$ Todas as derivadas parciais de ambas as funções são contínuas em seu domínio (que no caso seria $\R$)$\checkmark$;

$b:$ Seu domínio é uma região simplesmente conexa(no caso seria $\R$  então é sim Conexa) $\checkmark$

$c:$ $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, para isso precisamos fazer as contas: 

$$
\frac{\partial M}{\partial y} = 2y  = \frac{\partial N}{\partial x}  \ \ \ \checkmark
$$

com isso vimos que também satisfaz a última (assim como todas) os pré-requisitos para ser uma equação exata, agora podemos fazer um sistema linear para acharmos nossa função $\psi(x,y)$

3- Agora iremos definir nosso sistema linear: 

$$
\begin{cases}
\frac{\partial \psi}{\partial x}(x,y) = M(x,y) \\ 
\frac{\partial \psi}{\partial y}(x,y) = N(x,y)
\end{cases} \Rightarrow

\begin{cases}
\frac{\partial \psi}{\partial x}(x,y) = 2x + y^2 \ \ \ (i) \\ 
\frac{\partial \psi}{\partial y}(x,y) = 2xy \ \ \ \ \ \ \ \ \ (ii)
\end{cases} 
$$

4- Para resolvermos nosso sistema linear, precisamos integrar  a equação $i$  (em função a $x$) :

$$
(i)\\ 
\begin{aligned}
\frac{\partial \psi}{\partial x}(x,y) &= 2x + y^2 \\ 
\psi(x,y) &= \int 2x + y^2 dx \\ 
\psi(x,y) &= x^2 + y^2x + \underbrace{g(y)} 
\end{aligned} 

$$

<aside>
<img src="Equac%CC%A7o%CC%83es%20Exatas%200f143b276ede4b70b428de610b67dbc1/mugi.gif" alt="Equac%CC%A7o%CC%83es%20Exatas%200f143b276ede4b70b428de610b67dbc1/mugi.gif" width="40px" /> Onde $g(y)$ é uma função arbitrária, análoga à constante $c$ que adicionamos após integrarmos.

</aside>

- Agora podemos derivar parcialmente em função de $y$  a expressão que encontramos para $\psi$  e igualar a equação $ii$, com isso teremos o valor de $g(y)$ e assim teremos resolvido o problema de achar $\psi(x,y)$

$$
\begin{aligned}

\frac{\partial}{\partial y} \psi(x,y) &= ii \\ 

\frac{\partial}{\partial y} \psi(x,y) &= 2xy \\ 

\frac{\partial}{\partial y}(x^2 + y^2x + g(y)')&= 2xy \\ 

(0 + 2yx + g(y)')&= 2xy \\ 
g'(y)&= 2xy - 2xy \\ 
g'(y)&=0 
\end{aligned}
$$

- Para que a derivada de $g(x)$ seja $0$, ela precisa ser constante, com isso temos que:

$$
g(x) = c
$$

onde $c$ é um constante, com isso temos que:

$$
\boxed{\psi(x,y) \Rightarrow x^2 + y^2x = -c }
$$

Que é a resolução implícita da nossa $EDO$