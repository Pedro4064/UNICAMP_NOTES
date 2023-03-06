# Potência $AC$

Aula: Aula 15
Created: June 26, 2021 11:08 AM
Prova: P3

# Potência Instantânea

$$
p(t) = v(t) i(t)
$$

- Considerando:
    
    $$
    v(t) = V_m\cos(\omega t + \theta) \\ 
    i(t) = I_m\cos(\omega t + \phi)
    $$
    
- Temos que:

$$
\boxed{P(t) = \frac{1}{2} V_m I_m \cos (\theta - \phi) + \frac{1}{2} V_m I_m \cos (2\omega t + \theta + \phi) }
$$

<aside>
💡 Temos que a Potência tem um OFFSET no eixo $y$ e que ela tem o dobro da frequência comparado com a tensão e corrente.

</aside>

- Pela Natureza alternada do circuito, temos horas que a fonte da energia para o sistema mas também horas que o sistema da energia para a fonte, chamamos de Potência Média ou Potência Ativa o balanço final entre a potência que flui da fonte para a carga.

# Potência Média

$$
P_1 = \frac{1}{T} \int^{t_1 + T} _{t_1} p(t) dt
$$

- Levando em consideração:

$$
v(t) = V_m\cos(\omega t + \theta) \\ 
i(t) = I_m\cos(\omega t + \phi)
$$

- Percebemos que a potência média é dada por:

$$
\boxed{P(t) = \frac{1}{2} V_m I_m \cos (\theta - \phi)}
$$

# Valor Eficaz

- O valor eficaz uma corrente (ou tensão) periódica é aquela que se fosse aplicado de maneira direta (contínua) numa carga resistiva, entregaria a mesma potência média.

$$
I_{eff} = \sqrt{\frac{1}{T} \int_0 ^T i^2 dt}
$$

- Com a mesma coisa para a tensão.
- Fazendo a conta temos que:

$$
V_{eff} = \frac{1}{\sqrt{2}} V_m
$$

$$
I_{eff} = \frac{1}{\sqrt{2}} I_m
$$

# Potência Aparente e Fator de Potência

- Considerando:

$$
v(t) = V_m\cos(\omega t + \theta) \\ 
i(t) = I_m\cos(\omega t + \phi)
$$

- Com os valores eficazes, somos capazes de expressar a potência ativa como sendo:

$$
P = V_{eff}I_{eff}\cos(\theta - \phi)
$$

- A partir disso, podemos ver que o valor máximo da potência ativa é quando $\theta = \phi \therefore \cos(0) = 1$. o nome dessa potência ativa máxima é POTÊNCIA APARENTE.
- O fator de potência é dado por:

$$
Fator \ de \ Potência = \frac{Potência \ Ativa}{\ Potência \ Aparente}
$$

# Potência Complexa

![Pote%CC%82ncia%20$AC$%201ea32d2b97384eaa9cd5ed5335469a08/Screen_Shot_2021-06-26_at_4.58.13_PM.png](Pote%CC%82ncia%20$AC$%201ea32d2b97384eaa9cd5ed5335469a08/Screen_Shot_2021-06-26_at_4.58.13_PM.png)

$$
\hat{S} = \hat{V}\hat{I}^*
$$

$\hookrightarrow$ Com isso temos que $P$ é a parte real de $\hat{S}$ e