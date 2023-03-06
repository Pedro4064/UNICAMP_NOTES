# Circuitos Lineares e Teoria de Superposição

Aula: Aula 6
Created: April 27, 2021 7:28 PM
Prova: P2

# Circuitos Lineares

- Circuitos formados por fontes de corrente e/ou tensão que são independentes ou possuem uma relação de dependência, só que linear.
- Bipolos que possuem relação entre tensão e corrente linear (e.g resistores).

> Um circuito é linear quando pode ser equacionado por uma combinação linear de elementos lineares
> 

## Elementos Lineares

$$
f(x) = k\cdot x
$$

- Tal que $k$ é uma constante.
- E.g: $i = \frac{v}{r}$

### Propriedade da Proporcionalidade (homogeneidade):

$$
f(Kx) = K\cdot f(x)
$$

<aside>
<img src="Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/mugi.gif" alt="Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/mugi.gif" width="40px" /> OBS: Propriedade análoga a característica de linearidade de uma transformação linear, das aulas de Algebra Linear

</aside>

### Propriedade da Adição

![Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-04-27_at_7.39.01_PM.png](Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-04-27_at_7.39.01_PM.png)

$$
f(x_1 + x_2) = f(x_1) + f(x_2)
$$

# Teorema de Superposição

> Num circuitos linear com número de fontes independentes (ou fontes dependentes lineares), a resposta do circuito pode ser encontrada somando-se as respostas de cada fonte de maneira individualmente, com todas as outras fontes zeradas.
> 

- A corrente total em qualquer ramo de um circuito linear é igual à soma algébrica das correntes resultantes da atuação de cada fonte separadamente;
- A tensão nodal é igual à soma algébrica das tensões resultantes da atuação de cada fonte separadamente.

- Para computar as correntes separadamentes:
    - Fontes de tensão deve ser substituídas por curto circuitos;
    - Fontes de corrente devem ser substituídas por circuitos abertos.
    

## Exemplo

![Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-04-27_at_7.48.43_PM.png](Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-04-27_at_7.48.43_PM.png)

- Nesse exemplo queremos achar o valor $v_0$.
- Iremos aplicar a teoria de superposição e linearidade do circuito, calculando primeiramente a influencia da primeira fonte de $5V$. Para isso precisamos transformar a nossa fonte de tensão em um curto circuito, resultando no seguinte circuito:

![Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-05-17_at_7.50.09_PM.png](Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-05-17_at_7.50.09_PM.png)

Onde sabemos que representa um divisor de tensão e temos: 

$$
V_{0_{(5V)}} = \frac{5}{2}
$$

- Agora iremos estudar a influencia da fonte de número 2, com $6V$. Para isso iremos considerar a fonte de $5V$ como um curto e teremos o seguinte circuito:

![Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-05-17_at_7.52.19_PM.png](Circuitos%20Lineares%20e%20Teoria%20de%20Superposic%CC%A7a%CC%83o%20c2b4dd062ef2415a898461daf751a5c8/Screen_Shot_2021-05-17_at_7.52.19_PM.png)

Onde também temos um divisor de tensão:

$$
V_{0_{(6V)}} = \frac{6}{2}
$$

- Podemos utilizar então a propriedade de linearidade de soma:

$$
\begin{aligned}
V_0 &= V_{0_{(5V)}} + V_{0_{(6V)}} \\ 
&= \frac{5}{2} + \frac{6}{2} \\ 
&= 5.5 V
\end{aligned}
$$