# Questão 1

Created: May 21, 2021 11:18 AM
Tags: Quase Batata, Revisar

# Questão 1

$$
i(t) = 14 \cdot e^{-t}
$$

## Letra a

Esboce graficamente a corrente, a tensão e a potência no indutor indicando as expressões utilizadads:

- Já temos a fórmula da corrente em função do tempo
- Sabemos que $v = L \cdot \frac{di}{dt}$
- Sabemos que $p = vi = L\cdot i\cdot \frac{di}{dt}$

Considerando o fato de que já temos a corrente em função de $t$, e que a indutância $L = 1H$somos capazes de resolver a questão, mas antes precisamos achar a derivada temporal de $i$:

$$

\begin{aligned}
i(t) &= 14 \cdot e^{-t} \\
i'(t) &= 14 \cdot \frac{d}{dt} \left( e^{-t} \right) \\
i'(t) &= -14 e^{-t}
\end{aligned}

$$

Agora podemos plotar os resultados:

![Corrente, tensão e potência, respectivamente](Questa%CC%83o%201%20e56821eec1ff4f60a7cf2b8c4664fd96/Questo_1_plt.png)

Corrente, tensão e potência, respectivamente

## Letra B

- Além disso, queremos também identificar a energia máxima armazenada no indutor, para um $t \rightarrow \infty$.  Para tal, sabemos que:

$$
E = \frac{1}{2} L \left\{ [i(t)]^2 - [i(t_0)]^2\right\}
$$

Onde sabemos que:

- $i_0 = 14 A$
- $L = 1H$
- $t \rightarrow \infty$

Com isso temos:

$$
\begin{aligned}
E &= \lim_{t \rightarrow \infty} \frac{1}{2}(1) \left\{14 \cdot e^{-t} - 14^{2}\right\} \\ 
&= \frac{1}{2} \cdot -14^2 \\ 
&= -98 J
\end{aligned}
$$