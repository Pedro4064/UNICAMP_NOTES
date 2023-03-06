# Multiplicidade Algébrica e Geométrica

Semana: Semana 13

# Definições

## Multiplicidade Algébrica

> A Multiplicidade Algébrica é a quantidade de vez que o autovalor $\lambda$ aparece nas raizes do polinômio característico.
> 

## Multiplicidade Geométrica

> A Multiplicidade Geométrica de um autovalor $\lambda$ é a dimensão do subespaço (ou também chamado de  [autoespaço](Autovalores%20e%20Autovetores%20de%20uma%20Matriz%2015a80f62559d4b8b86c4cf604db3e1cc.md)) $V_{\lambda}$ associado ao autovalor $\lambda$.
> 

## Exemplos:

Considerando a Matriz $A = 
\begin{bmatrix} 
2 & -1 & 1 \\
0 & 3 & -1 \\
2 & 1 & 3 
\end{bmatrix}$ 

Podemos determinar a multiplicidade algébrica através do polinômio característico: 

$$
\begin{aligned}

p(\lambda) &= det(A - \lambda I) \\
&= det
\left(
\begin{bmatrix} 
2 & -1 & 1 \\
0 & 3 & -1 \\
2 & 1 & 3 
\end{bmatrix}
- \lambda
\begin{bmatrix} 
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 
\end{bmatrix}

\right) \\

&= det
\left(
\begin{bmatrix} 
2 - \lambda & -1 & 1 \\
0 & 3 - \lambda & -1 \\
2 & 1 & 3 - \lambda
\end{bmatrix}
\right) \\

&= -(\lambda - 2)(\lambda - 2)(\lambda - 4)
\end{aligned}
$$

Com isso vemos que os autovalores são $\boxed{\lambda_1 = 2, \lambda_2 = 4}$, sendo que $\lambda_1$ tem multiplicidade algébrica $2$  e $\lambda_2$ tem multiplicidade algébrica 1.

 

Para encontrarmos a multiplicidade geométrica dos autovalores, entretanto, precisamos achar os seus respectivos autovetores.