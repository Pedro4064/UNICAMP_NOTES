# Autovalores e Autovetores de uma Matriz

Semana: Semana 13

# Autovetor e Autovalores

## O que é um autovetor?

> Autovetores são direções preservadas por uma matriz, enquanto o autovalor é o nome do número que está mudando a norma do vetor.
> 

## Definição

Seja $A$ uma matriz quadrada. Um vetor não nulo $b \in Dom(A)$  é um autovetor associado ao autovalor $\lambda \in \ \R$ $\iff$ $Ab = \lambda b$

### Observações:

- Matrizes quadradas;
- Cada autovetor pode somente ter um autovalor;
- $\lambda$ pode ser zero, mas o o vetor deve ser não nulo;
- Diferentes autovetores podem ter o mesmo autovalor, quando isso acontece dizemos que o autovalor tem multiplicidade $n$, onde $n$ é a dimensão dos autoespaços aos quais o autovalor está associado;
- Se é pedido para provar que um vetor é um autovetor, não basta provar que $Ab = \lambda b$, precisa-se mostrar que $b \neq 0_b$ ($A.K.A$ não nulo)

# Autoespaços

- Um conjunto gerador de autovetores;

# Como calcular Autovalores e Autovetores

- Precisamos calcular as raizes do polinômio característico:

$$
p(\lambda) = det(A - \lambda I)
$$

Onde $A$ é a matriz e $I$ sua matriz identidade

- Exemplo: Tendo a matriz $A=
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}$, podemos calcular seus autovalores utilizando o polinômio característico:

$$

\begin{bmatrix}
2 & 0 \\ 
0 & 1
\end{bmatrix} - \lambda \begin{bmatrix}
2 & 0 \\ 
0 & 1
\end{bmatrix} = \begin{bmatrix}
2 - \lambda & 0 \\ 
0 & 1 - \lambda
\end{bmatrix}\Rightarrow  
 
det\left(\begin{bmatrix} 
2 - \lambda & 0 \\ 
0 & 1 - \lambda
\end{bmatrix} \right) = 0 \Rightarrow \\ 

(2 - \lambda)(1 - \lambda) = 0 \therefore \boxed{\lambda_1 = 2, \lambda_2=1}
$$

<aside>
💡 Algo interessante é que podemos calcular o traço e a determinante da matriz $A_{2\times2}$ com os autovalores: $det(A) = \lambda_1 \cdot \lambda_2$   e  $tr(A) = \lambda_1+\lambda_2$ 

OBS: A matriz $A$ precisa ser $2\times2$

</aside>