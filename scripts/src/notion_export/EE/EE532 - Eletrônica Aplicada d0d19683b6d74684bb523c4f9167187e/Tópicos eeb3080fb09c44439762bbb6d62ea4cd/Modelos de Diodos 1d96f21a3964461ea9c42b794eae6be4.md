# Modelos de Diodos

Created: March 16, 2022 2:01 PM
Prova: P1

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Como vimos anteriormente, um diodo nada mais é do que um bipolo oriunda de uma jução de dois semicondutores dopados, um do tipo $N$ e outra do tipo $P$.

$\hookrightarrow$ Com isso, nós podemos representar matematicamente um diodo como sendo somente a junção dopada, mas podemos também fazer simplificações e chegarmos em outros modelos. 

# Modelos De Diodos

## Modelo Exponencial

$\hookrightarrow$ Para o modelo exponencial temos:

![Screen Shot 2022-03-23 at 4.19.17 PM.png](Modelos%20de%20Diodos%201d96f21a3964461ea9c42b794eae6be4/Screen_Shot_2022-03-23_at_4.19.17_PM.png)

$$
I_D = I_S (\exp \frac{V_D}{V_T}) \\ \Downarrow \\ V_D = V_T \ln \left(\frac{I_D}{I_S}\right)
$$

## Modelo Ideal

$\hookrightarrow$ Podemos ainda representar o diodo em um cenário ideal, onde ele é um simplesmente um circuito fechado quando polarizado diretamente e um circuito aberto quando polarizado inversamente.

![Screen Shot 2022-03-23 at 4.24.32 PM.png](Modelos%20de%20Diodos%201d96f21a3964461ea9c42b794eae6be4/Screen_Shot_2022-03-23_at_4.24.32_PM.png)

$\hookrightarrow$ Resultando no seguinte perfil:

![Screen Shot 2022-03-23 at 4.25.51 PM.png](Modelos%20de%20Diodos%201d96f21a3964461ea9c42b794eae6be4/Screen_Shot_2022-03-23_at_4.25.51_PM.png)

## Modelo Com Queda de Tensão Constante

$\hookrightarrow$ Ao contrário do Modelo Ideal supracitado, o modelo com queda de tensão constante diz que a corrente que passa pelo diodo é nula enquanto for negativo (igual o modelo ideal) mas que continua sendo zero até que a tensão ($V_D$) seja maior que $0, 7 V$, que chamamos de $VD_{on}$.

![Screen Shot 2022-03-23 at 4.38.29 PM.png](Modelos%20de%20Diodos%201d96f21a3964461ea9c42b794eae6be4/Screen_Shot_2022-03-23_at_4.38.29_PM.png)

$\hookrightarrow$ Com isso dizemos que no momento que que o diodo fecha e possibilita a passagem de corrente sempre haverá uma perda constante de $0.7V$.

## Modelo De Pequenos Sinais

$\hookrightarrow$ Para problemas onde há uma pequena variação nos sinais $(v_d(t) << V_T)$ nós podemos utilizar um outro modelo, o chamado Modelo de Pequenos Sinais.

$\hookrightarrow$ Nesse modelos nós simplificamos a corrente por tensão no diodo como sendo uma reta tangente ao ponto de operação.

$\hookrightarrow$ Nesse modelo nós:

- Analisamos o circuito sem variação pelo modelo exponencial
- Analisamos o circuito  somente com a variação e trocando os diodos por resistências dadas por:
    
    $$
    r_d = \frac{V_t}{I_d}
    $$
    
- E depois pelo teorema de linearidade e superposição somamos o resultado encontrado

![Screen Shot 2022-03-25 at 3.50.05 PM.png](Modelos%20de%20Diodos%201d96f21a3964461ea9c42b794eae6be4/Screen_Shot_2022-03-25_at_3.50.05_PM.png)