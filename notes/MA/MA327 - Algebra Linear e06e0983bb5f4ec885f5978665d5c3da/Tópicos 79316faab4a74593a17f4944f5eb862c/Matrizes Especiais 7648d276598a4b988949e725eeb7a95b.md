# Matrizes Especiais

Semana: Semana 14

## Teoremas Chave

### $Reais$

1. Seja $A \in M_n(\R)$. Então, para todos os $x,y \in \R^n$ temos que: 
    
    $$
    \lang Ax, y\rang = \lang x, A^ty \rang
    $$
    
2. Seja $A \in M_n (\R)$  simétrica. Então para todos $x,y \in R^n$ tem-se que:
    
    $$
    \lang Ax, y \rang = \lang x, Ay\rang
    $$
    
    Tendo em vista que por ser simétrica $A = A^t$.
    
3. Seja $A \in M_n (\R)$ uma matriz Simétrica. Então, seus valores são todos reais. Além disso, seus autovetores associados são orgotonais.

### $Complexos$

1. Seja $A \in M_{n}(\mathbb{C})$. Então, para todos $x,y \in \mathbb{C}^n$ temos que:
    
    $$
    \lang Ax, y \rang = \lang x, A^*y\rang
    $$
    
2. Seja $A \in M_n (\mathbb{C})$ hermitiana. Então, para todos $x,y \in \mathbb{C} ^n$ tem-se: 
    
    $$
    \lang Ax, y \rang = \lang x, Ay\rang
    $$
    
    De forma análoga a como é com as matrizes simétricas em $\R$.
    
3. Seja $A \in M_n (\mathbb{C})$ uma matriz Hermitiana. Então, seus valores são todos reais. Além disso, seus autovetores associados são orgotonais.

## Matrizes Especiais

### Positiva-Definida

Seja $A \in M(\R)$ uma matriz **simétrica**. Dizemos que $A$ é uma matriz positiva-definida se:

$$
\lang Ax, x \rang > 0 \: \: ; \: \: \forall x \in \R^n \therefore x^t Ax > 0
$$

Se existir um elemento não nulo $x \in \R^n$ tal que $x^tAx = 0$  dizemos que $A$ é uma matriz **SEMIPOSITIVA-DEFINIDA**

**EXEMPLO:**

Considere a matriz simétrica $A \in M_2(\R)$ dada por:

$$
A = 
\begin{bmatrix}
2 & 1 \\ 
1 & 2 
\end{bmatrix}
$$

Mostre que a matriz $A$ é positiva-definida. 

$$
\lang Ax, x \rang  = x^tAx
$$

Onde $x = \begin{bmatrix} x_1 \\ x_2\end{bmatrix} \therefore  Ax = 
\begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix} \begin{bmatrix}
x_1 \\ x_2
\end{bmatrix} = 

\begin{bmatrix}
2x_1 + 1x_2 \\
x_1 + 2x_2
\end{bmatrix}$

Com isso temos que:

$$
\begin{bmatrix}
x_1 & x_2
\end{bmatrix} 
\begin{bmatrix}
2x_1 + 1x_2 \\
x_1 + 2x_2
\end{bmatrix} = 2x_1^2 +2x_2^2 + 2x_2x_1  = x_1^2 + x_2^2 + (x_1 + x_2)^2 > 0
$$

**OBS:** 

<aside>
<img src="Matrizes%20Especiais%207648d276598a4b988949e725eeb7a95b/LewdMegumin.png" alt="Matrizes%20Especiais%207648d276598a4b988949e725eeb7a95b/LewdMegumin.png" width="40px" /> Se a matriz for positiva-definida  seus autovalores são positivos, além disso seus autovetores são ortogonais.

</aside>