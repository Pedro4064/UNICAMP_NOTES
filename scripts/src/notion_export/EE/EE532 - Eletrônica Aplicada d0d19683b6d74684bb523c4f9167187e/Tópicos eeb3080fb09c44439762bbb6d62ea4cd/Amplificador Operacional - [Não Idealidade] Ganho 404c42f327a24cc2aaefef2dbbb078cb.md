# Amplificador Operacional - [Não Idealidade] Ganho Não Ideal

Created: June 23, 2022 9:45 AM
Prova: P4

- SUMMARY

# Introdução

$\hookrightarrow$ Como vimos anteriormente, enquanto estávamos fazendo os Bode Plots, o ganho do nosso sistema Linear só é constante até certo ponto (chamado de Polo), o qual a partir dele o ganho diminui.

$\hookrightarrow$ Isso também acontece com o nosso circuito de ganho utilizando OpAmps. Sendo mais específico, o ganho inato do OpAmp $(A_0)$ é dependente da frequência do sinal de entrada $\therefore$ podemos descreve-lo como uma função de Transferência e fazer seu Bode Plot, como mostrado a seguir:

![Screen Shot 2022-06-23 at 9.49.44 AM.png](Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Ganho%20404c42f327a24cc2aaefef2dbbb078cb/Screen_Shot_2022-06-23_at_9.49.44_AM.png)

$\hookrightarrow$ E como $A_0$ depende da frequência, o ganho não ideal, que é calculado a partir dele tanto para malha aberta quanto para malha fechado também irá depender da frequência edeverá ser descrito utilizando $A_0(s)$ e não o $A_0$ ideal constante para valores de $\omega$  maiores do valor da $\omega_c$, que é o valor da frequência de corte, a qual começa o decaimento (como mostrado na figura).

# Ganho em Malha Aberta

$\hookrightarrow$ Para malha aberta temos o seguinte comportamento:

![Screen Shot 2022-06-23 at 9.51.01 AM.png](Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Ganho%20404c42f327a24cc2aaefef2dbbb078cb/Screen_Shot_2022-06-23_at_9.51.01_AM.png)

$\hookrightarrow$ Que resulta em um ganho de malha aberta dependente da frequência $\omega$, dado por:

![Screen Shot 2022-06-23 at 9.52.10 AM.png](Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Ganho%20404c42f327a24cc2aaefef2dbbb078cb/Screen_Shot_2022-06-23_at_9.52.10_AM.png)