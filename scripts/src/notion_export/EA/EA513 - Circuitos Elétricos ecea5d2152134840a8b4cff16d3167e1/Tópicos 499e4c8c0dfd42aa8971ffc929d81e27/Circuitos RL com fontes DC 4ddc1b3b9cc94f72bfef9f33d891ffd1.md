# Circuitos RL com fontes DC

Aula: Aula 9
Created: May 19, 2021 11:33 AM
Prova: P2

![Circuitos%20RL%20com%20fontes%20DC%204ddc1b3b9cc94f72bfef9f33d891ffd1/Screen_Shot_2021-05-19_at_11.48.57_AM.png](Circuitos%20RL%20com%20fontes%20DC%204ddc1b3b9cc94f72bfef9f33d891ffd1/Screen_Shot_2021-05-19_at_11.48.57_AM.png)

- Temos um circuito com fonte de tensão → Logo temos um circuito equivalente de Thevenin.
- Equacionamos de forma análoga ao que foi feito com o circuito RC

## Circuito RL Autônomo

### Solução Homogênea - Reposta Natural

- Representado pela solução oriunda da equação homogênea associada a nossa $EDO$:

$$
\begin{aligned}
\frac{di}{dt} + \frac{R}{L}i_L =& 0  \\ 
i_{L_{H}} &= Ae^{\frac{R}{L}t}
\end{aligned}
$$

<aside>
🧠 Temos então como constante temporal $\frac{L}{R}$, o que implica em um tempo de $5(\frac{L}{R})$ segundos para o descarregamento do indutor

</aside>

### Solução Particular - Resposta Forçada

- Haverá a estabilização da corrente com o passar do tempo. Tendo isso em vista podemos atribuir como valor da solução particular uma constante:

$$
i_{L_P} = \frac{V}{R}
$$

### Solução Gerla

$$
I_L(t) = \frac{V}{R} + Ae^{-\frac{R}{L}t}
$$

$\hookrightarrow$ Para encontrarmos a constante $A$ precisamos substituir na $EDO$, que resulta em:

$$
\boxed{i_L(t) = \frac{V}{R} + \left[i_L(0) - \frac{V}{R} \right] e^{-\frac{R}{L}t}}
$$

$\hookrightarrow$ Através dessa modelagem matemática somos capazes de concluir que:

<aside>
🧠 No regime permanente o indutor se comporta como um curto-circuito para a excitação contínua. 
Já para o regime transiente, temos que o indutor se comporta como um circuito aberto, tendo a queda de tensão toda sobre ele, e não sobre o resistor.

</aside>

![Circuitos%20RL%20com%20fontes%20DC%204ddc1b3b9cc94f72bfef9f33d891ffd1/Screen_Shot_2021-05-19_at_12.11.36_PM.png](Circuitos%20RL%20com%20fontes%20DC%204ddc1b3b9cc94f72bfef9f33d891ffd1/Screen_Shot_2021-05-19_at_12.11.36_PM.png)

![Circuitos%20RL%20com%20fontes%20DC%204ddc1b3b9cc94f72bfef9f33d891ffd1/Screen_Shot_2021-05-19_at_12.12.35_PM.png](Circuitos%20RL%20com%20fontes%20DC%204ddc1b3b9cc94f72bfef9f33d891ffd1/Screen_Shot_2021-05-19_at_12.12.35_PM.png)