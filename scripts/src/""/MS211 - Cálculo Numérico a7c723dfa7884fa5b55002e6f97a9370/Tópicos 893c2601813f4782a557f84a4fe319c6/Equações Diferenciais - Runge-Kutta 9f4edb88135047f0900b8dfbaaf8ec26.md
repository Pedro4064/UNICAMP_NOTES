# Equações Diferenciais - Runge-Kutta

Aula: Aula 17
Created: November 9, 2021 11:14 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ A família de métodos de EDOs chamado de Runge-Kutta (RK de forma abreviada) visa juntar o melhor do método de Euler (baixo preço computacional) com o melhor do método de Taylor (menor numero de iterações e precisão).

$\hookrightarrow$ Levando isso em consideração, o método de Runge-Kutta coincide com o método de Taylor de mesma ordem, mas não contém as derivadas que existem em taylor (pois são caras computacionalmente).

<aside>
<img src="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Runge-Kutta%209f4edb88135047f0900b8dfbaaf8ec26/Hifumi_Surprised.png" alt="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Runge-Kutta%209f4edb88135047f0900b8dfbaaf8ec26/Hifumi_Surprised.png" width="40px" /> O Método de Euler é uma RK de primeira ordem !!

</aside>

# Método de Heun (Euler Aperfeiçoado)

## Interpretação Geométrica

![Screen Shot 2021-11-10 at 11.36.09 AM.png](Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Runge-Kutta%209f4edb88135047f0900b8dfbaaf8ec26/Screen_Shot_2021-11-10_at_11.36.09_AM.png)

## Interpretação Analítica

$\hookrightarrow$ Como podemos ver acima, no método de Heun temos 3 linhas, sendo elas:

- $L_1$ - Com inclinação $y'_{k} = f(x_k, y_k)$
- $L_2$ - Com inclinação $y'(x_{k+1}, \bar{y}_{k+1}) = f(x_{k+1}, y_{k} + hy'_k)$
- $L_0$ - Com inclinação igual a média das inclinações de $L_1$ e $L_2$ que passa por $(x_k, y_k)$, como mostrado abaixo:

$$
L(x) = y_k + h\frac{[f(x_k, y_k) + f(x_k + h, y_k + hy'_{k})]}{2}
$$

$\hookrightarrow$ E diferente do método de Euler convencional, no método de Heun  temos que o nosso $y_{k+1}$ vai estar na linha $L_0$ no ponto $x_{k+1}$, resultando na seguinte formula iterativa geral:

 

$$
\boxed{y_{k+1} = y_k + \frac{h}{2} \left[ f(x_k, y_k) + f(x_k + h, y_k + hf(x_k, y_k)) \right]}
$$

# R.K Segunda Ordem Geral

$$
\boxed{y_{k+1} = y_k + h[(1 - w) f(x_k, y_k) + wf(x_k + \frac{h}{2w}, y_k + \frac{h}{2w} f(x_k, y_k))],  \forall w \ne 0}
$$

$\hookrightarrow$ Onde temos que o Metodo de Heun é um caso especial de R.K de segunda ordem onde $w=\frac{1}{2}$

$\hookrightarrow$ Além disso, quando $w=1$ temos que o método é chamado de R.K de ponto médio.

# R.K Terceira Ordem Geral

$\hookrightarrow$ Para RK de terceira ordem nós iremos pegar três retas (ao invees de duas como é no de segunda ordem) e fazer uma média ponderada entre suas inclinações para achar a inclinação da reta que usaremos como aproximação para $y(x_k)$.

$\hookrightarrow$ Essas retas tem inclinação:

$$
\begin{aligned}
k_1 &=  h\cdot f(x_k, y_k) \\ 
k_2 &= h \cdot f(x_k + \frac{h}{2}, y_k + \frac{k_1}{2}) \\ 
k_3 &= h \cdot f(x_k + \frac{3h}{4}, y_k + \frac{3k_2}{4}) \\ 

\end{aligned}
$$

$\hookrightarrow$ resultando em:

$$
y_{k+1} = y_k + \frac{2}{9}k_1 + \frac{1}{3}k_2 + \frac{4}{9}k_3
$$

# R.K Quarta Ordem Geral

$$
\begin{aligned}
k_1 &= h \cdot f(x_k, y_k) \\
k_2 &= h \cdot f(x_k + \frac{h}{2}, y_k + \frac{k_1}{2}) \\ 
k_3 &= h \cdot f(x_k + \frac{h}{2}, y_k + \frac{k_2}{2}) \\ 
k_4 &= h \cdot f(x_k + h, y_k + k_3) \\
\end{aligned}
$$

$\hookrightarrow$ Resultando em:

$$
y_{k+1} = y_k + \frac{1}{6} (k_1 + 2k_2 + 2k_3 + k_4)
$$

# Exemplo de Implementação

$\hookrightarrow$ Para o seguinte problema de valor inicial:

$$
\begin{cases}
y' = y - x^2 + 1 \\ 
y(0) = 0.5
\end{cases}
$$

$\hookrightarrow$ Onde $h = 0.2$. Encontre $y(0.2) = ?$ Utilizando Heun.

- 1º Passo - Isolar nossa EDO
    - Precisamos isolar nossa derivada de um lado da EDO, para então encontrarmos $f(x,y) = y - x^2 + 1$.
    
- 2º Passo - Identificar os Pontos de interesse
    - Nesse caso temos:
    
    $$
    y_0 = 0.5, x_0 = 0
    $$
    
- 3º Passo - Calcular quantidade de passos
    - Diferente do método de Euler, no método de Heun ele dará no problema o $h$ pois não somos capazes de calcular o erro para acha-lo.
    - Com isso temos que o número de iterações é:
    
    $$
    nº  \ Iterações = \frac{\overbrace{0.2}^{x \ alvo}}{\underbrace{0.2}_{Passo \ (h)}} = 1
    $$
    
- 4º Passo - Aplicar o algoritmo