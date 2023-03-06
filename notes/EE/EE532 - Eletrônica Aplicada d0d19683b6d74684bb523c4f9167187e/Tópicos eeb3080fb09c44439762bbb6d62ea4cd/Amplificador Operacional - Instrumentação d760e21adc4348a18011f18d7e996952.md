# Amplificador Operacional - Instrumentação

Created: June 22, 2022 9:21 AM
Prova: P4

- SUMMARY

# Topologias de Instrumentação

## Subtrator

$\hookrightarrow$ Vimos na parte anterior que somos capazes de arquitetar uma topologia tal que $v_{out} = \frac{R_2}{R1}(v_{2} - v_1)$, que chamamos de subtrator. Ela, entretanto, não é ideal para instrumentação pois a impedância de entrada não é infinita $\therefore$ há uma corrente que está sendo "Desviada” do sistema para o AmpOP. 

$\hookrightarrow$ A fim de impedirmos isso, somos capazes de acoplar junto ao subtrator dois [Buffers](Amplificadores%20Operacionais%20-%20Ganho%20Malha%20Aberta%20e%207a15e1f8ea8b48e7bbe6ac52b6046b16.md) (um em cada entrada), pois eles tem impedância $\mathcal{Z}_{in} \rightarrow \infty$ e ganho de tensão igual a 1 (o que seria perfeito pois resolveria o problema da impedância mas não mudaria o sinal em análise).

$\hookrightarrow$ Se quisermos, entretanto, que haja um ganho de tensão antes da entrada do subtrator podemos ainda adicionar dois OpAmps implificador não inversor, como mostra a imagem abaixo.

![Screen Shot 2022-06-22 at 9.32.23 AM.png](Amplificador%20Operacional%20-%20Instrumentac%CC%A7a%CC%83o%20d760e21adc4348a18011f18d7e996952/Screen_Shot_2022-06-22_at_9.32.23_AM.png)

$\hookrightarrow$ Essa topologia, contudo, apresenta um problema, que é a possível saturação dos amplificadores não inversores e, por conseguinte, a diminuição da razão de rejeição de modo comum (fator de rejeição de ruídos comuns em ambas as entradas). A fim de compensar isso, podemos usar a seguinte topologia:

![Screen Shot 2022-06-22 at 9.46.55 AM.png](Amplificador%20Operacional%20-%20Instrumentac%CC%A7a%CC%83o%20d760e21adc4348a18011f18d7e996952/Screen_Shot_2022-06-22_at_9.46.55_AM.png)

## Conversor Corrente-Tensão

![Screen Shot 2022-06-22 at 9.52.03 AM.png](Amplificador%20Operacional%20-%20Instrumentac%CC%A7a%CC%83o%20d760e21adc4348a18011f18d7e996952/Screen_Shot_2022-06-22_at_9.52.03_AM.png)

$\hookrightarrow$ Como temos que $I_i$ não entra no OpAmp (tendo em vista sua impedância de entrada infinita) temos que:

$$
V_o = -R_f I_i
$$

## Circuito de Impedância Negativa

![Screen Shot 2022-06-22 at 9.54.53 AM.png](Amplificador%20Operacional%20-%20Instrumentac%CC%A7a%CC%83o%20d760e21adc4348a18011f18d7e996952/Screen_Shot_2022-06-22_at_9.54.53_AM.png)

$\hookrightarrow$ Essa topologia é utilizada principalmente como parte de uma fonte de corrente controlada por tensão com carga aterrada, como mostra o exemplo abaixo

- E.g
    
    ![Screen Shot 2022-06-22 at 9.56.59 AM.png](Amplificador%20Operacional%20-%20Instrumentac%CC%A7a%CC%83o%20d760e21adc4348a18011f18d7e996952/Screen_Shot_2022-06-22_at_9.56.59_AM.png)
    
    -