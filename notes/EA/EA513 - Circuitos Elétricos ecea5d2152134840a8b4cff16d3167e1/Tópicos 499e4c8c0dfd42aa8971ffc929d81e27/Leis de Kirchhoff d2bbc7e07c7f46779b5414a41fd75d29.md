# Leis de Kirchhoff

Aula: Aula 2
Created: March 23, 2021 7:21 PM
Prova: P1

![Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Screen_Shot_2021-03-23_at_7.22.57_PM.png](Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Screen_Shot_2021-03-23_at_7.22.57_PM.png)

## Terminologia

### Nós:

- Ponto de conexão de dois ou mais elementos (bipolos)

### Ramo:

- Caminho que liga dois nós (ex: a-e)

### Laço

- Caminho fechado(circuito) por bipolos conectados entre si e não passa duas ou mais vezes por um bipolo.

### Circuito Plano

- Um circuito é plano se é possível desenhá-los sem o cruzamento de bipolos.

### Malha

- Laço em um circuito plano que não contém bipolos em seu interior. (e.g   $a-e-g-b$)

## Lei de Kirchhoff da Corrente

<aside>
<img src="Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/mugi.gif" alt="Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/mugi.gif" width="40px" /> Toda corrente que entra no nó de um circuito deve sair. 

Todas as correntes que saem do nó são negativas e todas as correntes que entram no nó são positivas

</aside>

$\hookrightarrow$ Isso é: A soma algébrica das correntes de todos os ramos conectados a um nó deve ser zero.

<aside>
<img src="Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Hifumi_Surprised.png" alt="Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Hifumi_Surprised.png" width="40px" /> Em um circuito com $n$ nós, há $n-1$ equações de corrente independentes que podem ser usadas para formar um sistema de equações $L.I$

</aside>

### Exemplo

![Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Screen_Shot_2021-03-23_at_8.06.15_PM.png](Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Screen_Shot_2021-03-23_at_8.06.15_PM.png)

Temos: 

$$
\begin{cases}
Nó \ 1\rightarrow 0 = -i_1 - i_2 -i_3 \\ 

Nó \ 2\rightarrow 0 = +i_1 + i_4 - i_6 \\ 

Nó \ 3\rightarrow 0 = +i_2 - i_4 - i_5 \\

\cancel{Nó \ 4\rightarrow 0 = +i_5 + i_6 + i_3} \\
\end{cases}
$$

$\hookrightarrow$ podemos riscar a última equação pois é um combinação linear das outras, com isso temos: 

- Circuito com $4$ nós e $3$ equações $LI$

## Lei de Kirchhoff da Tensão

<aside>
<img src="Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Amazon_com__animal_shirt_women.jpeg" alt="Leis%20de%20Kirchhoff%20d2bbc7e07c7f46779b5414a41fd75d29/Amazon_com__animal_shirt_women.jpeg" width="40px" /> A soma algébrica das tensões em qualquer percurso fechado do circuito deve ser nula.

Ao "caminhar" por um laço, assumimos o sinal de entrada do bipolo (i.e positivo para passivos e negativos para ativos)

</aside>

$\hookrightarrow$ precisamos aplicar a lei de Kirchhoff de tensão somente nas malhas, pois se aplicarmos em laços que não são malhar iremos acabar com uma equação $LD$, que não nos auxiliará na solução do sistema linear.

$$
\begin{cases}
0 = +v_2 + 2V - 5V \rightarrow \boxed{v_2 =  3V}\\ 
0 = +v_1 - 2V - 3V \rightarrow \boxed{v_1 = 5V}
\end{cases}
$$