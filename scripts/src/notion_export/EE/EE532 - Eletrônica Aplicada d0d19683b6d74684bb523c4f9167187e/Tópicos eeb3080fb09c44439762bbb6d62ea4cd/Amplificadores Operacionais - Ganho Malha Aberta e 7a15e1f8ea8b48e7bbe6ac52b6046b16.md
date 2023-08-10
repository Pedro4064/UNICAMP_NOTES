# Amplificadores Operacionais - Ganho Malha Aberta e Malha Fechada - Buffer

Created: June 8, 2022 3:11 PM
Prova: P4

- SUMMARY

# Introdução

$\hookrightarrow$ Utilizado ou como comparador ou como amplificador

$\hookrightarrow$ Extremamente linear

$\hookrightarrow$ Possuem Duas entradas:

- Uma inversora $-$
- Uma não inversora $+$

$\hookrightarrow$ Além da alimentação, que normalmente precisa ser simétrica (i.e No positivo precisa ter $5V$ e  no negativo a mesma tensão em módulo mas negativo $\therefore$ $-5V$).

![Screen Shot 2022-06-08 at 3.13.31 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.13.31_PM.png)

$\hookrightarrow$ A partir dads tensões de entrada (i.e a inversora e a não inversora) teremos o nosso $V_{out}$ dado por:

$$
V_{out} = A_0 (V_{n \ inversor} - V_{inversor})
$$

$\hookrightarrow$ Onde $A_0$ é característico do amplificador operacional e é chamado de "Ganho de Malha Aberta”

$\hookrightarrow$ Com isso podemos ver que a relação entre a tensão inversora e não inversora afeta diretamente o comportamento de $V_{out}$:

![Screen Shot 2022-06-08 at 3.19.16 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.19.16_PM.png)

## Características Ideais

$\hookrightarrow$ Um OpAmp ideal temos as seguintes características:

![Screen Shot 2022-06-08 at 3.23.59 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.23.59_PM.png)

$\hookrightarrow$ Esse ganho diferencial "infinito” na realidade implica que o sistema tenderia a gerar um $V_{out} \rightarrow \infty$ já que $A_0 \rightarrow \infty$ mas o OpAmp Satura na tensão de alimentação.

$\hookrightarrow$ Outra coisa que vemos do fato acima é que é um sistema muito instável e de malha aberta. Para tirar a instabilidade utilizamos a realimentação negativa em um sistema de malha fechada.

# Malha Fechada

## Seguidor de Tensão - Buffer

![Screen Shot 2022-06-08 at 3.29.13 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.29.13_PM.png)

![Screen Shot 2022-06-08 at 3.29.40 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.29.40_PM.png)

$\hookrightarrow$ Se Observarmos o ganho de tensão é somente 1 (logo não há) mas o ganho de correte é enórme, assim como a impedância de entrada, por isso é utilizado como um buffer (assim como tinhamos algumas topologias para amplificação com MOSFET com dois estágios, sendo o segundo de Buffer).

$\hookrightarrow$ Além disso temos $V_{in1} = V_{in1}$, o que chamamos de curto virtual, o que facilita bastante na hora das contas.

## Amplificador Inversor

![Screen Shot 2022-06-08 at 3.34.00 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.34.00_PM.png)

![Screen Shot 2022-06-08 at 3.39.35 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.39.35_PM.png)

## Somador Inversor

![Screen Shot 2022-06-08 at 3.35.32 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.35.32_PM.png)

![Screen Shot 2022-06-08 at 3.37.54 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.37.54_PM.png)

## Amplificador não Inversor

![Screen Shot 2022-06-08 at 3.41.15 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.41.15_PM.png)

![Screen Shot 2022-06-08 at 3.42.18 PM.png](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16/Screen_Shot_2022-06-08_at_3.42.18_PM.png)