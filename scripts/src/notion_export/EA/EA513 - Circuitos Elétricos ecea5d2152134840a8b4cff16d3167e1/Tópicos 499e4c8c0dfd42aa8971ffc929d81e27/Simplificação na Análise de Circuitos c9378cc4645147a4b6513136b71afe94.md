# Simplificação na Análise de Circuitos

Aula: Aula 5
Created: April 21, 2021 10:35 AM
Prova: P1

# Expressão Matricial e Inspeção

## Análise de Nós por Inspeção

![Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/Screen_Shot_2021-04-21_at_10.57.09_AM.png](Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/Screen_Shot_2021-04-21_at_10.57.09_AM.png)

$$
\boxed{Y \cdot e = I_f}
$$

- Onde:

$$
e = \begin{bmatrix}

e_1 \\ 
e_2 \\
e_3
\end{bmatrix}
$$

Que representa a tensão de cada nó no circuito.

$$
I_f = \begin{bmatrix}
I \\ 
0 \\
0
\end{bmatrix}
$$

Que representa as fontes de tensão ligadas diretamente a cada nó.

### Matriz de Admitância dos Nós

- Matrix $Y$, com a seguinte estrutura:
- Para os elementos $Y_{kk}$ (da diagonal da matrix), temos a soma das condutâncias de todos os bipolos conectados ao nó de número $k$.
    
    <aside>
    <img src="Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/mugi.gif" alt="Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/mugi.gif" width="40px" /> Lembrando que o inverso da resistência é chamado de condutância: $G = \frac{1}{R}$
    
    </aside>
    
- Já para os elementos restantes, temos uma matriz simétrica, isso é, $Y_{jk} = Y_{kj}$, que representa o negativo da soma de condutâncias conectando diretamente os nós $k$ e $j$.

## Análise de Malhas por Inspeção

![Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/Screen_Shot_2021-04-21_at_11.09.39_AM.png](Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/Screen_Shot_2021-04-21_at_11.09.39_AM.png)

$$
\underbrace{\begin{bmatrix}
R_1 + R_3 & -R_3 \\ 
-R_3 & R_2 + R_3
\end{bmatrix}}_{matriz \ Impedância}
\begin{bmatrix}
i_1 \\ 
i_2
\end{bmatrix} = 
\begin{bmatrix}
v_1 \\ 
-v_2
\end{bmatrix}
$$

- Onde a diagonal da matriz Impedância  como cada elemento $Y_{kk}$  a soma das resistências da malha de número $k$.
- Onde os outros elementos $Y_{kj}$ são o negativo da somatória das resistências compartilhadas pelas malhas de número $k$ e $j$, com isso temos que é uma matriz simétrica onde $Y_{kj} = Y_{jk}$.
- A matriz de tensão são as fontes de tensão ligadas na malha.

<aside>
<img src="Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/sagiriBleh.png" alt="Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/sagiriBleh.png" width="40px" /> OBS: A matriz de tensão são o negativo soma das tensões (que tem o mesmo sinal relativo ao da análise de malhas ).

</aside>

<aside>
<img src="Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/Evangelion.gif" alt="Simplificac%CC%A7a%CC%83o%20na%20Ana%CC%81lise%20de%20Circuitos%20c9378cc4645147a4b6513136b71afe94/Evangelion.gif" width="40px" /> OBS: Utilizamos essas técnicas de Inspeção para circuitos com um tipo de fonte somente, caso contrário, utilizamos substituição de fontes

</aside>