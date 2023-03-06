# Física de Transistores Bipolares

Created: April 27, 2022 3:41 PM
Prova: P2

- SUMMARY

# Introdução

$\hookrightarrow$ De forma muito simplificada temos que um transistor bipolar pode ser visto como uma fonte de corrente controlada por uma tensão, que isso pode ser usada como amplificador.

$\hookrightarrow$ Um resistor é um dispositivo com três terminais (que chamamos de base, coletor e emissor) e que tem uma corrente de saída em função exponencial de $V_1$ como mostra a imagem ao lado. 

![Screen Shot 2022-04-27 at 3.49.04 PM.png](Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2022-04-27_at_3.49.04_PM.png)

# Estrutura de Transistores Bipolares

$\hookrightarrow$ Internamente, um transistor bipolar é composto de 3 diferentes regiões alternadas, que podem ser $PNP$ ou $NPN$ (que correspondem ao tipo de dopagem do semicondutor) e, como dito anteriormente, possuem 3 terminais.

$\hookrightarrow$ O emissor "emite“ portadores de carga enquanto o coletor os "coleta”, sendo que a quantidade de portadores de carga que fazem esse percurso é controlado pela base.

![Screen Shot 2022-04-27 at 3.57.12 PM.png](Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2022-04-27_at_3.57.12_PM.png)

$\hookrightarrow$ Podemos pensar em um transistor bipolar $NPN$ como a junção de dois diodos $pn$ na configuração ao lado.

$\hookrightarrow$ Pelo diagrama pode parecer que as espessuras dos semicondutores são as mesmas mas na realidade não são, e a base tende a ser muito menor.

# Transistor Bipolar no Modo Ativo

## Pré-Requisitos

$\hookrightarrow$ Dizemos que para um transistor estar na região ativa precisamos:

$$
\boxed{V_{CE} \ge V_{BE}}
$$

e por conseguinte:

$$
V_{BC} < 0
$$

$\hookrightarrow$ Significando que a junção base-coletor está com polarização reversa.

## Fórumlas

$\hookrightarrow$ Podemos ainda calcular as correntes de cada um dos terminais enquanto na região ativa através das fórmulas:

$$
\begin{aligned}
I_C &= I_s \exp \frac{V_{BE}}{V_T} \\
I_B &=\frac{1}{\beta} I_s \exp \frac{V_{BE}}{V_T}  = \frac{1}{\beta}I_C \\ 
I_E &= \frac{\beta + 1}{\beta}
I_S\exp\frac{V_{BE}}{V_T} = I_C \left(1 + \frac{1}{\beta}\right)\end{aligned}
$$

$\hookrightarrow$ Se observarmos a fórmula para a corrente do emissor e comprar com a fórmula da corrente do coletor podemos observar o ganho de corrente:

$$
\alpha = \left(1 + \frac{1}{\beta}\right)
$$

<aside>
<img src="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/mugi.gif" alt="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/mugi.gif" width="40px" /> OBS: $\beta$ e $V_T$ são constantes que são dadas

</aside>

<aside>
<img src="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Hifumi_Surprised.png" alt="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Hifumi_Surprised.png" width="40px" /> OBS$^2$: Todas as fórmulas apresentadas são para transistores $NPN$, que tem como principais portadores de cargas os elétrons. Para os transistores do tipo $PNP$, que possuem como principais portadores as lacunas, você deve trocar $V_{BE}$ por $V_{EB}$ nas fórmulas e nos diagramas lembre que a perna do transistor que tem a seta sempre é o emissor e que os sinais de tensão para análise de malhas seguem a direção da seta (a seta aponta do mais para o menos).

</aside>

## Transcondutância

$\hookrightarrow$ Sabemos que o transistor atua como um amplificador por se comportar como uma fonte de corrente ao estar atuando na região ativa.

$\hookrightarrow$ Precisamos então de uma valor que caracterize a "qualidade” dessa fonte de corrente controlada por tensão.

$\hookrightarrow$ Aí que entra o conceito de transcondutância, que é a medida de conversão de tensão e corrente (que por sua vez está associada à amplificação) dada por:

$$
g_m = \frac{I_C}{V_{T}}
$$

$\hookrightarrow$ A transcondutância tem como unidade de medida o "Siemens” que é o inverso da resistência $\Omega^{-1}$

<aside>
<img src="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/yuru_camp.png" alt="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/yuru_camp.png" width="40px" /> A Transcondutância também pode ser interpretada como a inclinação da reta característica $I_C \times V_{BE}$

</aside>

## Análise de Circuito

$\hookrightarrow$ Uma análise sempre começa com a análise de grandes sinais (i.e de corrente contínua, onde não levamos em conta variações com o tempo como ruídos etc) e posteriormente passamos para a análise de pequenos sinais.

### Análise de Grandes Sinais

- Para análise de grande sinais nós não precisamos substituir nada no circuito, precisamos somente lembrar dos sinais quando formos fazer lei das malhas e considerar as tensões $V_{BE}$ e $V_{CE}$ → (Coletor Positivo, Base Positiva e Emissor Negativo).
- Com isso vamos achar as tensões supracitadas e as 3 correntes de interesse $(I_B, I_C, I_E)$ → E teremos o nosso ponto de operação (Dado por $(I_C, V_{BE})$).
- E por fim calculamos $g_m$, que será usado na análise de pequenos sinais a seguir.

<aside>
<img src="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2021-09-23_at_11.49.01_PM.png" alt="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2021-09-23_at_11.49.01_PM.png" width="40px" /> BIZU → Na análise de Grandes Sinais nós consideramos Capacitores como Circuitos Abertos

</aside>

### Análise de Pequenos Sinais → Pi-Híbrido

- Para análise de pequenos sinais nós zeramos fontes constantes ($\therefore$ fontes de tensão constantes se tornam curto-circuitos e fontes de corrente constantes se tornam circuitos abertos) e substituímos o transistor pelo modelo pi-híbrido:
    
    ![Screen Shot 2022-04-27 at 4.56.34 PM.png](Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2022-04-27_at_4.56.34_PM.png)
    

<aside>
<img src="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2021-09-23_at_11.49.01_PM.png" alt="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2021-09-23_at_11.49.01_PM.png" width="40px" /> BIZU → Na análise de Pequenos Sinais nós consideramos Capacitores como Curto Circuitos

</aside>

<aside>
<img src="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2021-09-23_at_11.49.01_PM.png" alt="Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2021-09-23_at_11.49.01_PM.png" width="40px" /> BIZU$^2$ → Quando formos achar o ganho (i.e $V_{out}/V_{in}$) Fica mais fácil se deixarmos tudo em função de $V_\pi$ pois se cancela no final

</aside>

# Transistor Bipolar no Modo de Saturação

$\hookrightarrow$ O transistor está no modo de saturação se:

$$
V_{CE} < V_{BE}
$$

ou seja:

$$
V_{BC} > 0
$$

$\hookrightarrow$ Quando está no modo de saturação usamos o seguinte modelo:

![Screen Shot 2022-04-28 at 10.28.19 AM.png](Fi%CC%81sica%20de%20Transistores%20Bipolares%203ec74dd5b7334d80a30d7b223187db37/Screen_Shot_2022-04-28_at_10.28.19_AM.png)