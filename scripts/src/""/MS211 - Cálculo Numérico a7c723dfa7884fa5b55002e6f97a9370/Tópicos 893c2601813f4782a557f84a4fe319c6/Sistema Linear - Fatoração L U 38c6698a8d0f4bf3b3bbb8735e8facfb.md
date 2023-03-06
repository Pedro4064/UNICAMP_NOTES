# Sistema Linear - Fatoração L.U.

Aula: Aula 08
Created: September 27, 2021 4:27 PM

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ Como visto anteriormente, o método de Gauss é muito bom por poder ser aplicada à maioria dos sistemas lineares.

$\hookrightarrow$ Um ponto fraco, entretanto, do método de Gauss é que ele tem complexidade $O(n^3)$.

$\hookrightarrow$ Visando diminuir o impacto da sua grande complexidade em um cenário onde vários sistemas lineares possuem uma mesma matriz $A_{m, n}$ mudando somente a matriz $b$ (e.g no processo de inversão de uma Matriz), aplicamos o método de fatoração $L.U$. 

# Fatoração $L.U$

$\hookrightarrow$ A fatoração LU tem como base a decomposição da matriz $A$ em duas matrizes triangulares (uma inferior e outra superior):

$$
A = LU
$$

Tal que: 

$\hookrightarrow$ $L$ (Lower) é triangular inferior com diagonal unitária.

$\hookrightarrow$ $U$ é triangular superior (upper).

$\hookrightarrow$ Com isso teremos que:

$$
Ax = b \iff LUx = b
$$

e

$$
y = Ux
$$

Logo

$$
Ax = b \iff
\begin{cases}
Ly = pb \\ 
Ux = y

\end{cases}
$$

$\hookrightarrow$ Resultand o em dois sistemas triangulares, com complexidade $O(n^2)$, e não $O(n^3)$ igual ao problema original.

<aside>
<img src="Sistema%20Linear%20-%20Fatorac%CC%A7a%CC%83o%20L%20U%2038c6698a8d0f4bf3b3bbb8735e8facfb/Hifumi_Surprised.png" alt="Sistema%20Linear%20-%20Fatorac%CC%A7a%CC%83o%20L%20U%2038c6698a8d0f4bf3b3bbb8735e8facfb/Hifumi_Surprised.png" width="40px" /> OBS: Se observarmos bem, fazemos sim uma decomposição de Gauss ao decompor $A$ em $LU$. Por isso só é melhor utilizar essa estratégia quando tempos mais de um sistema com o mesmo $A$, pois faremos a sua decomposição somente uma vez ao invés de $n$, onde $n =$  Número de sistemas.

</aside>

## Calculo de $LU$

$\hookrightarrow$ Fazemos através da eliminação de gauss.

$\hookrightarrow$ A parte inferior da matriz $L$ será composta pelos multiplicadores que calculamos na eliminação de Gauss.

$\hookrightarrow$ Já $U$ será a matriz resultante da eliminação de Gauss.

## Teorema da Fatoração $L.U$

> Seja $A$ quadrada de ordem $n$ e $A_k$ a sub-matriz com as $k-$primeiras linhas e colunas de $A$. Se $\det(A_k) \ne 0, k=1,2,3,..,(n-1)$ então existe uma única fatoração $L.U$ para $A$.
>