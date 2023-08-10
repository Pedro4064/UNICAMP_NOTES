# Transistores Bipolares Amplificadores - Polarização

Created: April 28, 2022 10:33 AM
Prova: P2

- SUMMARY

# Polarização: Ponto de Operação

$\hookrightarrow$ Como vimos anteriormente, para um transistor se comportar como um amplificador precisamos que ele esteja na região ativa $\therefore V_{CE} \ge V_{BE}$.

$\hookrightarrow$ Devido a essa restrição nós definimos o Ponto $Q$ como o ponto de operação do transistor tal que a máxima excursão do sinal de entrada não sature.

$\hookrightarrow$ Esse ponto $Q$ é composto por $(I_C, V_{CE})$

$\hookrightarrow$ Uma vez definido o ponto $Q$ (por meio da análise CC) basta fazermos uma análise de pequenos sinais → $\Delta I_C < 10\%$

![Screen Shot 2022-04-28 at 10.38.39 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.38.39_AM.png)

# Principais Tipos de Polarização

## Polarização Direta

![Screen Shot 2022-04-28 at 10.42.14 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.42.14_AM.png)

## Polarização Por Divisor de Tensão

![Screen Shot 2022-04-28 at 10.43.22 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.43.22_AM.png)

<aside>
<img src="Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Evangelion.gif" alt="Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Evangelion.gif" width="40px" /> OBS → Esse modelo de equivalência de Thev vai ser usada somente na análise de grandes sinais (i.e análise CC). Na análise de pequenos sinais utilize o modelo híbrido-$\pi$ com a fonte e configuração de resistores original.

</aside>

<aside>
<img src="Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/mugi.gif" alt="Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/mugi.gif" width="40px" /> BIZU → Achar o equivalente de Thevenin para a parte pontilhada (i.e divisor resistivo na base) e fazer análise a partir dai

</aside>

## Polarização com Degeneração de Emissor

![Screen Shot 2022-04-28 at 10.49.00 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.49.00_AM.png)

![Screen Shot 2022-04-28 at 10.49.07 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.49.07_AM.png)

## Autopolarização

![Screen Shot 2022-04-28 at 10.51.24 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.51.24_AM.png)

# Impedâncias de Entrada e Saída

![Screen Shot 2022-04-28 at 10.52.46 AM.png](Transistores%20Bipolares%20Amplificadores%20-%20Polarizac%CC%A7%200d7060ef84b1483fb9c945737fa826f0/Screen_Shot_2022-04-28_at_10.52.46_AM.png)

$\hookrightarrow$ Para calcularmos a impedância de entrada basta considerarmos a tensão de entrada como $V_x$, calcular a corrente $I_x$ e achar $R_{in} = Z_{in}$

$\hookrightarrow$ Já para o calculo da impedância de saída precisamos botar em curto nossa fonte de entrada original e botar no nosso $V_{out}$ uma fonte $V_{x}$ e repetir o procedimento acima.