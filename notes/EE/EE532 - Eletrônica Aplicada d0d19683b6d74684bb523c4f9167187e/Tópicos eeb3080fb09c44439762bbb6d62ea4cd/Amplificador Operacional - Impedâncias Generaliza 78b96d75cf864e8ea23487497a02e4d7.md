# Amplificador Operacional - Impedâncias Generalizadas

Created: June 22, 2022 10:41 AM
Prova: P4

- SUMMARY

# Introdução

$\hookrightarrow$ Quando falamos de impedâncias generalizadas estamos falando de diferentes bipolos sendo utilizados em conjunto com OpAmp, sendo os principais deles:

- Resistores
- Capacitores
- Indutores

$\hookrightarrow$ Devido a natureza de algum deles (principalmente resistores e capacitores) é mais vantajoso nós analisarmos o circuito no domínio da frequência, e não no domínio do tempo, através de transformada de Laplace.

$\hookrightarrow$ Na transformada de Laplace, conseguimos modelar nosso sistema de equações diferenciais no plano $S$ e  extrairmos a Função de Transferência (que é a função da razão entre o input e o output da nossa malha), que no nosso caso é $v_{out}/v_{in}$

# Principais Impedâncias no Domínio da Frequência

## Capacitor

$$
\begin{cases}
X_C  = \frac{1}{j\omega C } & \rightarrow Tempo \\ 
\mathcal Z_C = \frac{1}{SC} & \rightarrow Frequência
\end{cases}
$$

## Resistor

$$
\begin{cases}
X_R  = R & \rightarrow Tempo \\ 
\mathcal Z_R = R & \rightarrow Frequência
\end{cases}
$$

<aside>
<img src="Amplificador%20Operacional%20-%20Impeda%CC%82ncias%20Generaliza%2078b96d75cf864e8ea23487497a02e4d7/mugi.gif" alt="Amplificador%20Operacional%20-%20Impeda%CC%82ncias%20Generaliza%2078b96d75cf864e8ea23487497a02e4d7/mugi.gif" width="40px" /> IMPORTANTE → Temos que a transformada de Fourier é uma forma de decompor qualquer sinal (ou função) em uma somatória de senos. Isso, entretanto, nem sempre representa o sistema em sua plenitude, pois eles possuem, além do comportamento senoidal, um comportamento exponencial (crescimento ou decaimento exponencial), principalmente pois o sistema é descrito por uma equação diferencial que tem como possível solução uma combinação de senoides e exponenciais. Para representar em sua plenitude o sistema nós representamos ela no plano $S$ (plano que possui tanto parte imaginária, para representar as senoides, quanto parte real para o representar a exponencial).

</aside>

<aside>
<img src="Amplificador%20Operacional%20-%20Impeda%CC%82ncias%20Generaliza%2078b96d75cf864e8ea23487497a02e4d7/yuru_camp.png" alt="Amplificador%20Operacional%20-%20Impeda%CC%82ncias%20Generaliza%2078b96d75cf864e8ea23487497a02e4d7/yuru_camp.png" width="40px" /> IMPORTANTE → É importante relembrar que uma senoide é o exponencial $e^{ix} = \cos x + j \sin x$. Com isso fica mais fácil também entender que na representação no plano $S$ uma senoide temos componente somente no eixo imaginário, como mostrado na imagem abaixo:

</aside>

![Untitled](Amplificador%20Operacional%20-%20Impeda%CC%82ncias%20Generaliza%2078b96d75cf864e8ea23487497a02e4d7/Untitled.png)

# Análise no Domínio de Fourier

$\hookrightarrow$ Como dito acima, o domínio de Fourier é o de senoides puras, que representa parte do domínio de Laplace onde $s = j\omega$, isso é, somente o eixo dos imaginários puros de Laplace.

$\hookrightarrow$ Além disso, quando estamos analisando o domínio da frequência, mais especificamente o domínio de Fourier, nos é interessante analisar o ganho em decibéis, dado por:

$$
A_{dB} = \left | \frac{V_{out}}{V_{in}}\right |_{dB} = 20 \log \left | \frac{V_{out}}{V_{in}}\right | 
$$

![Screen Shot 2022-06-22 at 4.13.32 PM.png](Amplificador%20Operacional%20-%20Impeda%CC%82ncias%20Generaliza%2078b96d75cf864e8ea23487497a02e4d7/Screen_Shot_2022-06-22_at_4.13.32_PM.png)