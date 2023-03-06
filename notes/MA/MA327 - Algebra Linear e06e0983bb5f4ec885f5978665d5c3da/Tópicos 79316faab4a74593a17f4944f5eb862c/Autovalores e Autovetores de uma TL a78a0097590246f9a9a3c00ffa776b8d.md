# Autovalores e Autovetores de uma TL

Semana: Semana 13

# Autovetores e Autovalores de $T.L$

## Definição

- É extremamente similar ao que foi mostrado para matrizes, tendo em vista que podemos representar todas as matrizes como transformações lineares, tendo isso em mente, a definição para Autvalores e Autovetores para $TL$ é:

$$
Seja \ T:U\longrightarrow U \ linear.\  Um \ vetor\ não\ nulo\ u\in U \ é\ um\ autovetor\ associado\ ao\ autovalor \lambda \in \R \iff T(u) = \lambda u
$$

Onde $T$ é uma $T.L$ na base canônica 

## Calcular os Autovalores

- Assim como foi feito para achar os autovalores de matrizes, podemos acha-los para $TL$ utilizando o polinômio característico e achando suas raizes:

$$
p(\lambda) = det(A - \lambda I)
$$

- Entretanto estamos mexendo com transformações Lineares, então precisamos representar a $TL$ como uma matriz, da seguinte forma:

$$
T(x,y) = (2x,y) = x(2,0) + y(0,1) \therefore 
A = \begin{bmatrix}
2 & 0 \\ 
0 & 1
\end{bmatrix}
$$

<aside>
<img src="Autovalores%20e%20Autovetores%20de%20uma%20TL%20a78a0097590246f9a9a3c00ffa776b8d/LewdMegumin.png" alt="Autovalores%20e%20Autovetores%20de%20uma%20TL%20a78a0097590246f9a9a3c00ffa776b8d/LewdMegumin.png" width="40px" /> OBS: Botamos cada base como uma **coluna**, e não como uma linha

</aside>

- Agora podemos escrever o polinômio característico e calcular os autovalores:

$$
det(A - \lambda I) = 
det \left| 
\begin{bmatrix}
2 & 0 \\ 
0 & 1
\end{bmatrix} - 
\lambda \begin{bmatrix}
1 & 0 \\ 
0 & 1
\end{bmatrix}
\right| = 

det \left|
\begin{bmatrix}
2 - \lambda & 0 \\ 
0 & 1 - \lambda
\end{bmatrix}

\right|
\\
\Rightarrow (2 - \lambda)(1 - \lambda) \therefore \boxed{\lambda_1 = 2, \lambda_2 = 1}
$$

- Como temos os autovalores, podemos voltar para a definição de um autovetor para descobrir uma para essa transofrmação linear. Devemos então lembrar que um autovetor é um vetor não nulo $u$ tal que  $T(u) = \lambda u$, então substituimos o valor de $\lambda$ pelos autovalores e $T(u)$ pela $T.L$ dada no enunciado e temos:

$$
\begin{aligned} 
T(u) &= \lambda_1 u \\ 
(2x,y) &= \lambda_1(x,y) \\ 
(2x, y) &= 2(x,y) \\ 
(2x, y) &= (2x,2y) \iff y = 0

\end{aligned}

$$

Temos que a última igualdade só será real se $y = 0$, com isso temos que o autovetor para o autovetor $\lambda_1 = 2$ é o vetor  $(x,0) = x(1,0) \therefore span\{(1,0)\}$

- Agora iremos ver o autovetor do segundo autovalor $\lambda_2 = 1$

$$
\begin{aligned} 
T(u) &= \lambda_2 u \\ 
(2x,y) &= \lambda_2(x,y) \\ 
(2x, y) &= 1(x,y) \\ 
(2x, y) &= (x,y) \iff x = 0

\end{aligned}

$$

Temos que a última igualdade só será real se $x = 0$, com isso temos que o autovetor para o autovetor $\lambda_2 = 1$ é o vetor  $(0,y) = y(0,1) \therefore span\{(0,1)\}$