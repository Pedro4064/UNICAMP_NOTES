# Sistema Linear - Introdução

Aula: Aula 06
Created: September 27, 2021 11:55 AM

- SUMÁRIO
    
    

# Aplicações de Sistemas Lineares

$\hookrightarrow$ Em várias áreas das ciências nós encontramos sistemas lineares, como por exemplo em circuitos elétricos, utilizando as leis de Kirchoff.

# Tipos de Soluções Lineares

## Soluções Únicas

$\hookrightarrow$ Considerando o sistema:

$$
\begin{cases}
2x_1 + x_2 =3\\
x_1 - 3x_2 = -2
\end{cases}
$$

$\hookrightarrow$ Podemos resolve-lo através do método de substituição e encontramos que $x_1 = 1, x_2=1$.

$\hookrightarrow$ Concluímos então que esse sistema linear tem solução única. 

- REPRESENTAÇÃO GRÁFICA
    
    ![Screen Shot 2021-09-27 at 12.11.06 PM.png](Sistema%20Linear%20-%20Introduc%CC%A7a%CC%83o%209a1b39418880455fa5a9fedd109754bb/Screen_Shot_2021-09-27_at_12.11.06_PM.png)
    

## Infinitas Soluções

$\hookrightarrow$Se considerarmos, entretanto, o seguinte sistema:

$$
\begin{cases}
2x_1 + x_2 = 3 \\ 
4x_1 + 2x_2 = 6
\end{cases}
$$

$\hookrightarrow$ Vemos que $x_2 = 3, x_1 = 6/4 - 3x_2/4$, o que resulta em infinitas soluções.

<aside>
<img src="Sistema%20Linear%20-%20Introduc%CC%A7a%CC%83o%209a1b39418880455fa5a9fedd109754bb/kawasegaua.png" alt="Sistema%20Linear%20-%20Introduc%CC%A7a%CC%83o%209a1b39418880455fa5a9fedd109754bb/kawasegaua.png" width="40px" />  Nessas situações, **não** podemos utilizar métodos numéricos

</aside>

- REPRESENTAÇÃO GRÁFICA
    
    ![Screen Shot 2021-09-27 at 12.13.36 PM.png](Sistema%20Linear%20-%20Introduc%CC%A7a%CC%83o%209a1b39418880455fa5a9fedd109754bb/Screen_Shot_2021-09-27_at_12.13.36_PM.png)
    

## Sem Solução

$\hookrightarrow$ Considerando:

$$
\begin{cases}
2x_1 + x_2 = 3 \\ 
4x_1 + 2x_2 = 2
\end{cases}
$$

$\hookrightarrow$ Temos um cenário onde não há soluções que validem ambas as equações. 

- REPRESENTAÇÃO GRÁFICA
    
    ![Screen Shot 2021-09-27 at 12.15.24 PM.png](Sistema%20Linear%20-%20Introduc%CC%A7a%CC%83o%209a1b39418880455fa5a9fedd109754bb/Screen_Shot_2021-09-27_at_12.15.24_PM.png)
    

# Representação de Sistemas Lineares

$$
A_{m, n} \ x_{n,1} = b_{m,1}
$$

$\hookrightarrow$ $A$: Matriz

$\hookrightarrow$ $b$: Vetor

$\hookrightarrow$ $x$: Vetor com as incógnitas

$\hookrightarrow$ $n$ incógnitas

$\hookrightarrow$ $m$ equações;

# Unicidades de Solução

$\hookrightarrow$ Para verificarmos a unicidade da solução precisamos inicialmente criar a matriz estendida, isso é, adicionar $b$ como última coluna da matriz $A$, tal que fique $A|B$.

$\hookrightarrow$ Segue um checklist que precisa ser seguido para estipular a unicidade da solução do sistema linear em questão:

- [ ]  $Posto([A|b]) = Posto(A) = n$
- [ ]  Solução Única para $A_{n, n}$ $\iff$ $det(A) \ne 0 \therefore$  $\exists A^{-1}$

# Métodos Numéricos

$\hookrightarrow$ Podemos dividir os métodos numéricos para solução de sistemas lineares em dois tipos

- Métodos Diretos
- Métodos Iterativos