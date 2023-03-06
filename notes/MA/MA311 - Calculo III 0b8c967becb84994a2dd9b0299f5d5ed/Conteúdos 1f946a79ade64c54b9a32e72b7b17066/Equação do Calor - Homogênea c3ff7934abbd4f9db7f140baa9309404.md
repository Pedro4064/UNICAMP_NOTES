# Equação do Calor - Homogênea

Aula: Aula 25
Created: July 3, 2021 12:29 PM
Prova: P2

# Método da Separação de Variáveis

- Encontre a função da temperatura $u(x.t)$ da barra que satisfaz as seguintes condições:

$$
\begin{cases}
u_t = \alpha^2 u_{xx} \\ 
u(x,0) = f(x) \rightarrow & x \in [0,L] \\ 
u(0,t) = u(L,t) = 0 & t \ge 0
\end{cases}
$$

## Passo 1 - Separação de Variáveis

- Supondo que $u$ possa ser escrita como produto entre duas funções, uma apenas em função de $x$ e outra somente em função de $t$:

$$
u(x,t) = X(x) \cdot T(t)
$$

- Substituindo na equação de calor $u_t = \alpha ^2 u_{xx}$:

$$
X(x) \cdot T'(t) = \alpha^2 X''(x) \cdot T(t)
$$

- Resultando em:

$$
\frac{1}{\alpha^2}\frac{T'(t)}{T(t)} = \frac{X''(x)}{X(x)}
$$

- Igualando a uma constante $-\lambda$ temos:

$$
\begin{cases}
X'' + \lambda X = 0 \\ 
T' + \alpha^2\lambda T = 0
\end{cases}
$$

## Passo 2 - Resolver o Problema de Contorno

- Temos o seguinte problema de valor inicial em relação a $t$:

$$
\begin{cases}
T' + \alpha^2 \lambda T = 0 \\ 
u(x,0) = f(x)
\end{cases}
$$

- E o seguinte problema de valores de contorno em relação a $x$:

$$
\begin{cases}
X'' + \lambda X = 0 \\ 
X(0) = 0 \\ 
X(L) = 0
\end{cases}
$$

- A partir disso, precisamos achar primeiramente a função que temos as 2 condições de contorno (no caso $X$).
- Para isso, iremos calcular pelo método de problemas de autovalores, buscando uma solução não-trivial analisando a equação característica de $X'' + \lambda X = 0$:

$$
r^2 + \lambda  = 0 \\ 
r \pm \sqrt{-\lambda}
$$

- Para $\Delta = 0$ e $\Delta > 0$ temos soluções triviais, logo iremos analisar só o caso $\Delta < 0$:
    
    $$
    r = \pm \sqrt{-\lambda} = 0 \pm i \sqrt{\lambda} \therefore \beta = \sqrt{\lambda}, \alpha = 0
    $$
    
- Com isso temos:

$$
X(x) = c_1 \cos \sqrt{\lambda}x + c_2 \sin \sqrt{\lambda}x
$$

- Substituindo nos pontos de contorno para acharmos $c_1$ e $c_2$ vemos que:

$$
c_1 = 0 \\ 
X_n = \sin \left(\frac{n\pi x}{L}\right) \\ 
\lambda_n = \left(\frac{n\pi}{L}\right)^2
$$

## Passo 3 - Resolver o Problema de Valor Inicial

$$
T' + \alpha ^2 \lambda T = 0
$$

- Aplicando o método da separação de variáveis:

$$
\frac{dT}{dt} = -\alpha^2 \lambda T \\ 
\frac{dT}{T} = -\alpha^2 \lambda dt
$$

- Integrando temos:

$$
\ln T = -\alpha^2 \lambda t \\ 
T(t) = e^{-\alpha^2\lambda t} \\ 
T_n(t) = e^{-\alpha^2\pi^2n^2t/L^2} 
$$

- Como $u(x,t) = X(x) \cdot T(t)$ temos:

$$
u_n(x,t) \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha \pi^2n^2t/L^2}, \ \ \ \ n = 1,2,3...
$$

## Passo 4 - Escrever $u(x,t)$ como série:

$$
u(x,t) = \sum_{n=1} ^\infty b_n \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha \pi^2n^2t/L^2}
$$

- Para que siga a condição inicial $u(x,0) = f(x)$ temos que:

$$
u(x,0) = \sum_{n=1} ^\infty b_n \sin\left(\frac{n\pi x}{L}\right)  = f(x)
$$

- Que é uma série de Fourier, logo:

$$
b_n = \frac{2}{L}\int^L_0 f(x) \sin\left(\frac{n\pi x}{L}\right)
$$