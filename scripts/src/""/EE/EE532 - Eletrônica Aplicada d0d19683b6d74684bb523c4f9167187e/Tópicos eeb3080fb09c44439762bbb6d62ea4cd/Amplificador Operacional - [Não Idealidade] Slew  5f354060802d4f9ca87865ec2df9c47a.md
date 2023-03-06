# Amplificador Operacional - [Não Idealidade] Slew Rate

Created: June 23, 2022 10:14 AM
Prova: P4

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Para pequenos sinais, a forma do sinal de saída de um amplificador operacional não sofre alteração quando comparado com o de entrada (a não ser pela amplificação).

$\hookrightarrow$ Já para grandes sinais ocorre o fenômeno de 'Slewing’, que é a deformação da forma de onda

$\hookrightarrow$ Para impedir tal inflexão temos que a inclinação máxima de saída tem que ser menor ou igual a taxa de inflexão $SR$ do OpAmp.

$\hookrightarrow$ A inclinação máxima depende da amplitude de entrada, da frequência de entrada e do ganho de malha fechada:

$$
V_{out} = V_0 A_{v_{n.ideal}}(\omega) \sin(\omega t)
$$

![Screen Shot 2022-06-23 at 10.17.06 AM.png](Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Slew%20%205f354060802d4f9ca87865ec2df9c47a/Screen_Shot_2022-06-23_at_10.17.06_AM.png)

# Frequência Máxima

$\hookrightarrow$ Como vimos anteriormente temos alguns parâmetros que influenciam $V_{out}$ e que por conseguinte influenciam na inclinação.

$\hookrightarrow$ A principal delas é a frequência máxima do sinal de entrada, que é dada por:

$$
\omega_{max} = \frac{SR}{V_0A_{v_{n.ideal}}(\omega_{max})}
$$

<aside>
<img src="Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Slew%20%205f354060802d4f9ca87865ec2df9c47a/Evangelion.gif" alt="Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Slew%20%205f354060802d4f9ca87865ec2df9c47a/Evangelion.gif" width="40px" /> Relembrando que $A_{v_{n.ideal}}(\omega_{max})$ é o ganho não ideal, que é em função da frequência $\omega_{max}$

</aside>

$\hookrightarrow$ Enquanto estamos projetando é importante, então, escolhermos $\omega < \omega_{corte}$ ($\omega_{corte}$ é a frequência onde o ganho começa a decair) de tal forma que:

$$
\omega_{max} = \frac{SR}{V_0A_{v_{ideal}}}
$$

$\hookrightarrow$ Se observarmos, $V_0 A_{v_{ideal}} = V_{out_{MAX}}$, onde:

$$
V_{out_{MAX}} = \frac{V_{max} - V_{min}}{2}
$$

$\hookrightarrow$ Pois pode não estar em torno do zero.

![Screen Shot 2022-06-23 at 10.30.12 AM.png](Amplificador%20Operacional%20-%20%5BNa%CC%83o%20Idealidade%5D%20Slew%20%205f354060802d4f9ca87865ec2df9c47a/Screen_Shot_2022-06-23_at_10.30.12_AM.png)