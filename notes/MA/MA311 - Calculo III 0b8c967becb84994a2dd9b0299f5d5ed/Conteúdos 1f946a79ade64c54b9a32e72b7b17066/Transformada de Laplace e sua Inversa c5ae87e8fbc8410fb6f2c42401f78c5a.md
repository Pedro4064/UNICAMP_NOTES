# Transformada de Laplace e sua Inversa

Aula: Aula 9
Created: April 26, 2021 7:28 PM
Prova: P1

# Transformada de Laplace - Definição

- Seja $f(t)$ uma função definida para $t \ge 0$. A transformada de Laplace de $f$é uma função $F$ definida por:

$$
F(s) = \mathcal{L} \{f(t)\} = \int^{\infty}_{0} e^{-st}f(t)dt
$$

- Para todos os valores de $s$ para os quais a integral imprópria converge.

# Existência da Transformada de Laplace

- Para que a transformada de Laplace de uma função $f(t)$ exista, ela precisa:
    1. $f(t)$ ser seccionalmente contínua (ou contínua por partes) no intervalo $0 \le t \le A$ para qualquer $A > 0$, isto é, $f$ é contínua em $[0,A]$, exceto em um número finito de descontinuidades do tipo "salto finito". 
    2. $f(t)$ é de ordem exponencial, ou seja, existem constantes $M, \alpha > 0$ tais que para todo $t$suficientemente grande: 
        
        $$
        |f(t)| \le Me^{\alpha t}
        $$
        

# Linearidade da Transformada de Laplace

$$
\mathcal{L}\{c_1f(t) + c_2g(t)\} = c_1\mathcal{L}\{f(t)\} + c_2\mathcal{L}\{g(t)\}
$$

$\hookrightarrow$ onde $c_1$ e $c_2$ são constantes

### Exemplo:

- Determine a transformada de Laplace da Função:

$$
f(t) = 3e^{2t} + 2\sin^2(3t)
$$

Sabemos que: 

$$
\sin^2(3t) = \frac{1}{2}[1-\cos(6t)] 
$$

Com isso podemos aplicar a propriedade de linearidade da transformada e teremos:

$$
\begin{aligned}
\mathcal{L}\{3e^{2t} + 2\sin^2(3t)\} &= 3\mathcal{L}\{e^{2t}\} + \mathcal{L}\{ 1 \} - \mathcal{L}\{\cos(6t)\}
\\
&= \frac{3}{s - 2} + \frac{1}{s} - \frac{s}{s^2 + 36}
\end{aligned}
$$

# Transformada de Laplace Inversa

$$
f(t) = \mathcal{L}^{-1}\{F(s)\} \iff \mathcal{L}\{f(t)\} = F(s)
$$

- Assim como a transformada de Laplace, sua inversa também é linear.