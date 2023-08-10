# Energia e Primeira Lei da Termodinâmica

Aula: Aula03, Aula04, Aula05
Cap.: 2.1 → 2.6
Created: August 9, 2021 9:27 PM

[Anotações de Aula](Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Anotac%CC%A7o%CC%83es%20de%20Aula%20bbf8fdfc447a4406b54e2df4e9aee60a.md)

- SUMÁRIO
    
    

# Trabalho

$$
W = \int F\cdot ds
$$

## O que é Trabalho?

$\hookrightarrow$ Podemos classificar uma interação como trabalho se e somente se seguir a seguinte definição termodinâmica do trabalho:

> Um sistema realiza trabalho sobre suas vizinhanças se o único efeito sobre tudo aquilo externo ao sistema puder ser o levantamento de um peso.
> 

$\hookrightarrow$ Observamos que isso é uma tradução direta do conceito de trabalho na mecânica, mas para os casos termodinâmicos, podemos simplesmente ver se **poderia** ser representado como o levantamento de um peso.

<aside>
<img src="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Amazon_com__animal_shirt_women.jpeg" alt="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Amazon_com__animal_shirt_women.jpeg" width="40px" /> OBS: O trabalho e uma forma de transferência de energia!!

</aside>

## Convenções de Sinais e Notação

$$
\begin{cases}
W > 0: Trabalho \ realizado\ pelo\ sistema\\
W < 0: Trabalho \ realizado\ no\ sistema
\end{cases}
$$

$\hookrightarrow$ Com a unidade no $S.I\rightarrow [J]$

# Potência

$\hookrightarrow$ Potência nada mais é do que a taxa de variação de trabalho ao longo do tempo.

$\hookrightarrow$ Obtemos tal taxa de variação tirando a derivada em respeito ao tempo → $\frac{d W}{dt}$ que representamos por $\dot{W}$.

<aside>
<img src="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Amazon_com__animal_shirt_women%201.jpeg" alt="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Amazon_com__animal_shirt_women%201.jpeg" width="40px" /> Qualquer lugar que ver a notação de ponto em cima de algo, representa a derivada temporal daquilo.

</aside>

$\hookrightarrow$ Como temos trabalho por segundo $\therefore$ energia por segundo $\therefore J/s$ a unidade no $SI$ para potência é  o $Watt$.

$$
[W] = \left[\frac{J}{s}\right]
$$

<aside>
<img src="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Amazon_com__animal_shirt_women%202.jpeg" alt="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Amazon_com__animal_shirt_women%202.jpeg" width="40px" /> OBS: Como temos que a potência nada mais é do que a derivada temporal do trabalho, que nada mais é do que o produto entre força e deslocamento, temos que a potência é igual ao produto da força com a velocidade (derivada temporal do deslocamento) → $\dot{W} = F\cdot v$

</aside>

# Modelando o Trabalho

## Expansão ou Compressão

$\hookrightarrow$ Em um caso de um fluido dentro de um cilindro-pistão, onde ocorre sua expansão (e por conseguinte a movimentação do pistão), observamos que:

- Na interface do fluido com o pistão há uma pressão;
- A pressão resulta em uma força normal no pistão dada por $F = p\cdot A$

![Screen Shot 2021-08-16 at 4.49.19 PM.png](Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Screen_Shot_2021-08-16_at_4.49.19_PM.png)

$\hookrightarrow$ Com isso, temos que o trabalho realizado pelo sistema em função do deslocamento é descrito por:

$$
\delta W = pA dx
$$

$\hookrightarrow$ Podemos ainda, observar que podemos representar a área e o deslocamento como sendo o volume dentro do pistão. Com isso, temos:

$$
\delta W = pdV
$$

### Convenções de Sinais

$\hookrightarrow$ Pela equação, vemos que, quando o volume do recipiente aumenta, tanto o trabalho quanto a potência são positivas. Caso esteja comprimindo, são negativos.

### Processos Politrópicos

$\hookrightarrow$ Um processo é dito politrópico quando $P\cdot V^n$ é constante. 

$\hookrightarrow$ Para esse tipo de processos, temos duas formas de calcular o trabalho:

- $n = 1$
    
    $$
    W = P_1 \cdot V_1 \cdot \ln\frac{V_2}{V_1}
    $$
    
- $n\ne 1$
    
    $$
    W = \frac{P_2 \cdot V_2 - P_1 \cdot V_1}{1-n}
    $$
    

# Calor

$\hookrightarrow$ O calor $Q$ representa a quantidade de energia que foi passada entre dois objetos devido à sua diferença de temperatura.

$\hookrightarrow$ Quando falamos de calor, levamos em consideração a seguinte convenção de sinais:

$$
Q > 0 \rightarrow Sis. \ Recebeu \ Calor\\
Q < 0 \rightarrow Sis. \ Perdeu \ Calor
$$

$\hookrightarrow$Ainda no que tange calor, existem processos nos quais não há a troca de calor, os chamados processos adiabáticos (e.g: Uma seringa sendo abaixada).

<aside>
<img src="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Evangelion.gif" alt="Energia%20e%20Primeira%20Lei%20da%20Termodina%CC%82mica%208912ce72f6b2490ab1d29ace272e49ed/Evangelion.gif" width="40px" /> O calor $(Q)$ não é uma propriedade termodinâmica do sistema!!! (isso implica que não podemos derivar usando $dQ$ e sim $\delta Q$, por ser uma derivada )

</aside>

## Condução

$\hookrightarrow$ Na condução, existem 3 fatores que influenciam:

1. Área da superfície onde acontece a transferência de energia.
2. A diferença de temperatura
3. A capacidade do material de conduzir energia na forma de calor

$\hookrightarrow$ Com isso temos a Lei de Fourier:

$$
\dot{Q} = \left|kA \frac{dT}{dx}\right|
$$

$\hookrightarrow$ Onde:

- $\dot{Q}$: Derivada temporal da quantidade de energia transferida por condução $[W]$
- $k$: Condutividade térmica do material.
- $A$: área da superfície onde ocorre transferência
- $\frac{dT}{dx}$: derivada da temperatura (também chamada de gradiente de temperatura) na direção $x$

## Convecção

$\hookrightarrow$ O processo de troca de energia por calor entre uma superfície sólido e um fluido (líquido, vapor e gás) em movimento é chamado de convecção.

$\hookrightarrow$  Para descrevermos esse processo, temos a Lei do Resfriamento de Newton.

$$
\dot{Q} = h \cdot A \cdot |T_s - T_f|
$$

$\hookrightarrow$ Onde:

- $h$: é o coeficiente de transferência por convecção.
- $A$: área da superfície.
- $T_s$: temperatura do sólido
- $T_f$: temperatura do fluido

## Radiação

$\hookrightarrow$ Para descrever a radiação, nós na realidade calculamos  a maior taxa de troca de calor teoricamente possível, pela lei de Stefan-Boltzmann

$$
\dot{Q}_{max} = \sigma \cdot A \cdot T^4_s
$$

$\hookrightarrow$ Se quisermos descrever a taxa de radiação por uma superfície real, temos:

$$
\dot{Q} =\varepsilon \cdot  \sigma \cdot A \cdot T^4_s
$$

- $\varepsilon$: emissividade da superfície
- $\sigma$: constante de stefan-Boltzmann
- $A$: Área da superfície
- $T_s$: Temperatura da superfície $[K]$

# Primeira Lei da Termodinâmica