# Circuito RLC Paralelo Autônomo

Aula: Aula 10
Created: May 27, 2021 7:06 PM
Prova: P3

# Equacionamento

![Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_7.09.09_PM.png](Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_7.09.09_PM.png)

- Levando em consideração o circuito acima, e aplicando a análise nodal temos:

$$
i_C + i_R + i_L = 0
$$

$\hookrightarrow$ Onde:

$$
i_C = C\frac{dv_c}{dt} = C\frac{dv}{dt}
$$

$$
i_R = \frac{v}{R}
$$

$$
i_L = \int^\infty_0 \frac{v}{L} dt
$$

$\hookrightarrow$ Com isso temos:

$$
C\frac{dv}{dt} + \frac{v}{R} + \frac{1}{L}\int^\infty_0vdt = 0
$$

$\hookrightarrow$ Para tirarmos a integral podemos derivar tudo em função do tempo, o que nos resultará em uma $EDO$ de segundo grau:

$$
C\frac{d^2v}{dt} + \frac{dv}{dt}\frac{1}{R} + \frac{v}{L} = 0
$$

$\hookrightarrow$  Deixando na forma padrão de uma EDO de segundo grau linear (i.e sem o coeficiente $C$ no termo da segunda derivada) temos:

$$
\boxed{\frac{d^2v}{dt} + \frac{1}{R\cdot C}\frac{dv}{dt} + \frac{v}{L\cdot C} = 0}
$$

- Sabemos que a $EDO$ acima tem como solução geral:

$$
v(t) = A_1e^{s_1t} + A_2e^{s_2t}
$$

$\hookrightarrow$ Onde $A_1$ e $A_2$ são constantes;

$\hookrightarrow$ E $s_1$ e $s_2$ são: 

$$
s_1 = -\alpha + \sqrt{\alpha^2 - \omega_0^2} \\ 
s_2 = -\alpha - \sqrt{\alpha^2 - \omega_0^2}
$$

Onde:

$$
\alpha = \frac{R}{2L} \rightarrow Fator\ de\ Amortecimento
$$

$$
\omega_0 = \sqrt{\frac{1}{LC}} \rightarrow Frequência\ de\ Ressonância
$$

- Ambos com unidade $s^{-1} \therefore$ $frequência$
- Dependendo da relação entre o fator de Amortecimento e da frequência de Ressonância, o comportamento do circuito irá mudar.

<aside>
<img src="Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Amazon_com__animal_shirt_women.jpeg" alt="Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Amazon_com__animal_shirt_women.jpeg" width="40px" /> • $\alpha > \omega_0:$ $s_1$ e $s_2$ são reais → CASO SUPERAMORTECIDO

• $\alpha = \omega_0:$ $s_1$ $=$ $s_2 = -\alpha$ → CASO CRITICAMENTE AMORTECIDO

• $\alpha < \omega_0:$ $s_1$ e $s_2$ são complexas → CASO SUB-AMORTECIDO

</aside>

## SUPERAMORTECIDO

 

![Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_7.52.27_PM.png](Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_7.52.27_PM.png)

- Com o comportamento superamortecido, temos uma ameaça de pico de tensão, mas depois ela é amortecida.

## CRITICAMENTE AMORTECIDO

<aside>
<img src="Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Evangelion.gif" alt="Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Evangelion.gif" width="40px" /> Para sistemas criticamente amortecidos, a solução geral da $EDO$  proposta anteriormente não é mais válida, mas ss: 
$v = e^{-\alpha t}(A_1t  + A_2)$

</aside>

![Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_8.03.39_PM.png](Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_8.03.39_PM.png)

## SUB-AMORTECIDO

![Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_8.06.21_PM.png](Circuito%20RLC%20Paralelo%20Auto%CC%82nomo%20b188f45c91c940c192651a3afc7a2e67/Screen_Shot_2021-05-27_at_8.06.21_PM.png)