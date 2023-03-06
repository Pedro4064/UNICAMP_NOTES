# Amplificador Operacional - Diagrama de Bode

Created: June 22, 2022 4:33 PM
Prova: P4

- SUMMARY

# Diagrama de Bode

## Introdução

$\hookrightarrow$ Vimos anteriormente que podemos analisar no domínio da frequência um sistema de impedâncias generalizadas, mais especificamente podemos analisar no domínio de Fourier o sistema em "Steady State” (regime permanente), isso é, quando não há decaimento nem crescimento exponencial do sinal e somente a parcela senoidal contínua, resultando em:

$$
S = \underbrace{\cancel \sigma}_{0} +  j\omega  \Rightarrow S = j\omega
$$

$\hookrightarrow$ Com isso podemos descrever nossa função de transição (que no nosso caso é o ganho) em função da frequência $\omega$ do sinal de entrada, e como isso altera tanto a magnitude do sinal de saída quanto sua defasagem, chamado de diagrama de Bode.

$\hookrightarrow$ É importante ressaltar que como estamos tratando de sinais senoidais (por estarmos no domínio de Fourier) a única alteração do sinal de saída para o de entrada é sua magnitude (medida em $dB$) e defasagem (medida em ângulo). Por isso plotamos essas duas característica em função do $\omega$, que é a frequência de entrada e por consequência a frequência de saída.

![Screen Shot 2022-06-22 at 5.01.01 PM.png](Amplificador%20Operacional%20-%20Diagrama%20de%20Bode%2022660c14bfd7467eb2f80cb595b98478/Screen_Shot_2022-06-22_at_5.01.01_PM.png)

## Diagrama Assintótico

$\hookrightarrow$ Como vimos acima um diagrama de Bode é muito importante pois nos permite descrever o comportamento do nosso sistema para uma entrada de diferentes frequências. 

$\hookrightarrow$ Para entendermos um pouco melhor, é importante sermos capazes de fazer uma versão simplificada do Bode Plote da nossa planta, chamada de Diagrama Assintótico. Ela é simplificada pois usaremos linhas retas para descrever o diagrama, que irão conectar os principais pontos de interesse, sendo eles os Poles e o Zeros, sendo eles:

1. Poles → Um Pole é um valor de $S$ ($\therefore$ de $\omega$) o qual faz com que nossa função de transferência $H(s) \rightarrow \infty$
2. Zero → Um Zero é um valor de $S$ tal que faça com que nossa função de transferência $H(s) \rightarrow 0$

### Construção à Mão: FT Simples

1. Passo: Identificação do Pole → Como dito anteriormente o Polo é o valor de $S$ tal que a função de transferência tende a infinito. A partir disso marcamos no nosso diagrama (tanto de magnitude quanto de Phase) esse valor no eixo da frequência.
2. Passo: Gráfico de Ganho → De forma geral, o ganho é zero até o ponto de polo, a partir dele que poderão haver duas possibilidades, como estamos falando de Funções de Transferências (FT) Simples:
    1. Função de Transferência somente com Denominador → Para esse caso temos que o ganho é zero até o polo e, a partir dele, haverá um decaimento linear com coeficiente angular de $-20dB/dec$
    2. Função de Transferência somente com Numerador → Assim como acima, o ganho será zero até o polo e então crescerá linearmente a $20dB/dec$
3. Passo: Gráfico de Phase → Assim como no gráfico de Ganho, haverão dois comportamentos, mas para ambos a phase será de zero até uma década antes do polo, e então:
    1. Função de Transferência somente com Denominador → Teremos que é zero até uma década antes do polo e ele irá decair até uma década até depois do polo, onde estabilizará em $-90^\circ$
    2. Função de Transferência somente com numerador → Teremos que é zero até uma década antes do polo, onde ele irá crescer e estabilizar em $+90^\circ$ ao atingir uma década depois do polo

- Exemplos
    
    ![Screen Shot 2022-06-23 at 9.19.04 AM.png](Amplificador%20Operacional%20-%20Diagrama%20de%20Bode%2022660c14bfd7467eb2f80cb595b98478/Screen_Shot_2022-06-23_at_9.19.04_AM.png)
    
    ![Screen Shot 2022-06-23 at 9.19.37 AM.png](Amplificador%20Operacional%20-%20Diagrama%20de%20Bode%2022660c14bfd7467eb2f80cb595b98478/Screen_Shot_2022-06-23_at_9.19.37_AM.png)
    

### Construção à Mão: FT "Composto”

$\hookrightarrow$ Vimos anteriormente casos onde a função de transferência é simples (ou possui somente numerador ou somente denominador).

$\hookrightarrow$ Haverão casos, entretanto, onde será uma composição dos dois casos. Para resolver esse tipo de problema basta aplicarmos a teoria de superposição de sistemas lineares, isso é, fazer as curvas do numerador, fazer as curvas do denominador e depois somar elas.

![Screen Shot 2022-06-23 at 9.24.32 AM.png](Amplificador%20Operacional%20-%20Diagrama%20de%20Bode%2022660c14bfd7467eb2f80cb595b98478/Screen_Shot_2022-06-23_at_9.24.32_AM.png)