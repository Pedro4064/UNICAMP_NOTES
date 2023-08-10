# Circuito RLC com Fontes $DC$

Aula: Aula 11
Created: June 9, 2021 7:08 PM
Prova: P3

# Circuitos RLC paralelo não-autônomo

![Circuito%20RLC%20com%20Fontes%20$DC$%20fe1d557ce9bf44d2a959ecc228a770a3/Screen_Shot_2021-06-09_at_7.11.55_PM.png](Circuito%20RLC%20com%20Fontes%20$DC$%20fe1d557ce9bf44d2a959ecc228a770a3/Screen_Shot_2021-06-09_at_7.11.55_PM.png)

$\hookrightarrow$ Utilizando as equações para indutores e capacitores temos:

$$
C\frac{dV_c}{dt} + \frac{V_c}{R} + \frac{1}{L}\int V_cdt = i_{IN}
$$

$\hookrightarrow$ Podemos derivar a equação acima para eliminarmos a integral.

$$
\frac{d^2 V_c}{d^2t}+ \frac{1}{RC}\frac{dV_c}{dt}+ \frac{1}{LC}V_c = \frac{1}{C}\frac{di_{IN}}{dt}
$$

$\hookrightarrow$ Observamos, entretanto, que não temos mais uma $EDO$ (pois temos a derivada de mais de uma função).

$\hookrightarrow$ Precisamos então outro método para equacionar. Iremos fazer isso equacionando não em função da tensão do capacitor, mas sim com a corrente do indutor, resultando em:

$$
\boxed{\frac{d^2 i_L}{dt^2} + \frac{1}{RC} \frac{di_L}{dt} + \frac{i_L}{LC} = \frac{i_{IN}}{LC}}
$$