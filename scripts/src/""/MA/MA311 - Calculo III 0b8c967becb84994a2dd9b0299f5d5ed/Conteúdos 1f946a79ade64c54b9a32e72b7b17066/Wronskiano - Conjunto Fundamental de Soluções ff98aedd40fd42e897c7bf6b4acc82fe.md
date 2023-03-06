# Wronskiano -  Conjunto Fundamental de Soluções

Aula: Aula 5
Created: April 7, 2021 10:30 PM
Prova: P1

# Wronskiano

- O calculo do Wronskiano nos possibilita averiguar se um conjunto de soluções de uma EDO são Linearmente Independentes ou não.
- O conjunto de soluções é dito $L.I$ em um conjunto específico $I$ tal que $W(y_1,...,y_n) \ne 0$, logo podemos ter um conjunto que é Independentes em um intervalo mas não em outro.

## Calculo do Wronskiano

- Nada mais é do que o Determinante de uma matriz composta pelas  soluções (e as derivadas das soluções) de uma $EDO$:

$$
W(f_1,...,f_n) = 
\begin{vmatrix}
f_1 & ...& f_n \\ 
f_1' & ... & f_n'\\ 
... &...&...
\end{vmatrix}
$$

Até ter $n$ linhas e $n$ colunas (tendo assim uma matriz quadrada), onde cada linha é uma derivada de ordem maior do que a linha anterior, tendo como primeiro linha as soluções.

$$
\begin{cases}
W \ne 0 \longrightarrow L.I \\ 
W = 0 \longrightarrow L.D
\end{cases}
$$

## Conjunto Conjunto Fundamental de Soluções

- Quando um conjunto de $n$ soluções de uma $EDO$ de ordem $n$ é $L.I$, temos que esse conjunto, para esse intervalo, é o conjunto fundamental de soluções.