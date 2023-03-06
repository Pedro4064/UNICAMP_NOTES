# Matriz de Incidência, Análise Nodal e de Malhas

Aula: Aula 3
Created: April 6, 2021 8:03 PM
Prova: P1

# Matriz de Incidência

![Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.10.24_PM.png](Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.10.24_PM.png)

- Temos sempre um Nó de referência, nesse caso o nó $0$ (normalmente podemos utilizar GND como nó referência);
- Levando em consideração que Correntes que $SAEM$  do nó são $+$ e as que entram são $-$;
- Temos as seguintes equação:

$$
\begin{cases}
nó_1: \ \ i_1 + i_5 + i_6 = 0 \\
nó_2: \ \ -i_1 + i_2 + i_3 = 0 \\
nó_3: \ \ -i_3 + i_4 - i_7 = 0 \\ 
nó_4: \ \ -i_5 + i_7 = 0
\end{cases}
$$

- Podemos fazer a representação matricial desse sistema linear:

$$
\underbrace{\begin{bmatrix}
+1 & 0 & 0 & 0 & +1 & +1 &0 \\
-1 & +1 & +1 & 0 & 0 & 0 &0 \\
0 & 0 & -1 & +1 & 0 & 0 &-1 \\
0 & 0 & 0 & 0 & -1 & 0 &+1 \\
\end{bmatrix}}_{Matriz \ de \ Incidência \ \ A}

\begin{bmatrix}
i_1 \\ 
i_2 \\
i_3 \\
i_4 \\
i_5 \\
i_6 \\
i_7 \\
\end{bmatrix} = 0
$$

- Conseguimos refazer a topologia  do nosso circuito apenas observando a $Matriz \ de \ incidência$.
- Podemos guardar de maneira fácil a Topologia do nosso circuito em memória (em processadores).

## Matriz de Tensões

![Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.34.19_PM.png](Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.34.19_PM.png)

- Levando em consideração a tensão no nó de referência como sendo $0V$, e considerando a nomenclatura $e_i$ para a tensão no nó de número $i$. Temos que:

$$
\begin{cases}
v_1 = e_1 - e_2 \\ 
v_2 = e_2 - 0\\
v_3 = e_2 - e_3 \\ 
v_4 = e_3 - 0 \\ 
v_5 = e_1 - e_4 \\ 
v_6 = e_1 - 0 \\ 
v_7 = e_4 + e_3
\end{cases}
$$

- Que pode ser escrita na forma Matricial:

$$
\begin{bmatrix}
v_1 \\ 
v_2 \\ 
v_3 \\ 
v_4 \\ 
v_5 \\ 
v_6 \\ 
v_7
\end{bmatrix} = 
\underbrace{
\begin{bmatrix}
+1 & - 1 & 0 & 0 \\ 
0 & + 1 & 0 & 0 \\ 
0 & +1 & -1 & 0 \\ 
+1 & 0 & +1 & -1 \\ 
+1 & 0 & 0 & 0 \\ 
0 & 0 & -1 & +1 \\ 
\end{bmatrix}}_{A^T}
\begin{bmatrix}
e_1 \\ 
e_2 \\
e_3 \\
e_4 \\
\end{bmatrix}
$$

Conseguimos observar que a matriz de tensões é a transposta da matriz de incidência de Correntes vezes a matriz de tesão dos nós:

$$
v = A^Te
$$

# Análise Nodal e Análise de Malhas

- Abordagem Metódica de resolução de circuitos;
- Criação de um algoritmo.

## Análise Nodal

![Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.47.00_PM.png](Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.47.00_PM.png)

1. Conte o número de nós (Redesenhe se for necessário):
    
    ![Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.47.35_PM.png](Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.47.35_PM.png)
    
2. Defina o nó de referência(nó com maior número de ramos conectados a ele);
3. Nomeie as tensões dos nós (existem $n-1$ tensões ):
    
    ![Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.50.01_PM.png](Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_8.50.01_PM.png)
    
4. Escreva as equações da Lei de Kirchhoff da corrente para os nós

## Análise de Malhas

1. Determinar se o circuito é plano (i.e: é possível desenhá-lo numa superfície sem cruzamento);
2. Determine as malhas (não pode haver bipolos internos)
    
    ![Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_9.06.03_PM.png](Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Screen_Shot_2021-04-06_at_9.06.03_PM.png)
    
3. Nomear as correntes de determinar os sentidos (há uma corrente em cada malha)
4. Escreva as equações da Lei de Kirchhoff de Tensão para cada malha.

<aside>
<img src="Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Hifumi_Surprised.png" alt="Matriz%20de%20Incide%CC%82ncia,%20Ana%CC%81lise%20Nodal%20e%20de%20Malhas%2007df38c606d14992ae8529296614602d/Hifumi_Surprised.png" width="40px" /> Se houver um componentes que é compartilhado em mais de uma malha, a corrente que passa nele na Lei de Kirchhoff de Tensão é a soma se das correntes se estiverem no mesmo sentido, e a subtração se estiverem em sentidos diferentes.

</aside>