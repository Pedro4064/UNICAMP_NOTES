# Circuitos RC Autônomos

Aula: Aula 8
Created: May 19, 2021 10:23 AM
Prova: P2

# Variável Tempo

## Análise Transiente

- Analisa o comportamento das tensões e correntes do circuito quando o mesmo sofre alterações bruscas.

## Análise de Regime Permanente

- Analisa o comportamento das tensões e correntes do circuito depois que o circuito está estável ou em equilíbrio.

# Circuitos RC

- Estão presentes resistores e capacitores.
- Podem ser redesenhados como equivalente de Norton → para aplicarmos análise de nós, para não necessitarmos de integrais.

![Circuitos%20RC%20Auto%CC%82nomos%209e95066626534d348835dd730ff844e5/Screen_Shot_2021-05-19_at_10.29.50_AM.png](Circuitos%20RC%20Auto%CC%82nomos%209e95066626534d348835dd730ff844e5/Screen_Shot_2021-05-19_at_10.29.50_AM.png)

$$
i_r = \frac{v_c}{R}
$$

$$
i_c = C \cdot \frac{dv_c}{dt}
$$

$$
-i + \frac{v_c}{R} + C \cdot \frac{dv_c}{dt} = 0 \Rightarrow C\cdot \frac{dv_c}{dt} + \frac{v_c}{R} = i
$$

$\hookrightarrow$ Temos então uma $EDO$, para facilitar nossa EDO vamos deixar o coeficiente de $v_c'$ como 1:

$$
\frac{dv_c}{dt} + \frac{v_c}{RC} = \frac{i}{C}
$$

$\hookrightarrow$ Temos uma EDO linear de primeira ordem do tipo:

$$
y' + ay = f(x)
$$

$\hookrightarrow$ Podemos resolver essa EDO não homogênea encontrando a solução da homogênea associada e somando com a solução específica. 

$\hookrightarrow$ Damos um nome especial para a solução homogênea da EDO, sendo ele: 

$$
v_{c_H} = Ae^{-\frac{t}{RC}}
$$

chamado de Resposta Natural do Circuito.

<aside>
💡 Sabemos através da resposta natural do circuito que um capacitor demora $5(RC)$ segundos para descarregar

</aside>