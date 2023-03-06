# Circuitos RC com fontes DC

Aula: Aula 9
Created: May 19, 2021 10:59 AM
Prova: P2

# Circuitos RC

- Anteriormente vimos a solução homogênea da EDO, e como ela representa a resposta natural do circuito.
- Agora iremos estudar a solução específica para a nossa $EDO$, que é chamada de Reposta Forçada.
- A partir do nosso conhecimento do comportamento de capacitores em estado estável, somos capazes de considerar a solução particular como uma constante:

$$
V_{c_p} = RI_0
$$

- Com isso temos como solução geral:

$$
v_c(t) = RI_0 + A \cdot e^{-\frac{t}{RC}}
$$

- Precisamos então achar a constante $A$, resultando na seguinte solução:

$$
\boxed{v_c(t) = RI_0 + (v_c(0) - RI_0) \cdot e^{-\frac{t}{RC}}}
$$

- A partir dessa modelagem matemática, somos capazes de concluir que:

<aside>
<img src="Circuitos%20RC%20com%20fontes%20DC%209e5946a33730489a93f75ed4a9b99850/mugi.gif" alt="Circuitos%20RC%20com%20fontes%20DC%209e5946a33730489a93f75ed4a9b99850/mugi.gif" width="40px" /> Para tempos muito grande, a tensão no capacitor se estabiliza em $IR$ e não a corrente passando por ele. Já em tempos muito pequenos, o capacitor se comporta como um curto, fazendo com que toda a corrente passe por ele.

</aside>

<aside>
🧠 Para circuitos com fonte de tensão, e $v_{c_0} = 0$ temos: 
$V_C = E_{} \left(1 - e^{-\frac{t}{RC}}\right)$

</aside>

<aside>
🧠 Podemos ainda calcular a corrente para casos onde $v_{c_0} = 0$:
$i_c = \frac{E}{R} * e^{-\frac{t}{RC}}$,  onde $*$ é a convolução

</aside>