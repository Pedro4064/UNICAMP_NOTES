# Sistemas Não Lineares

Aula: Aula 11
Created: September 28, 2021 9:42 AM
Prova: P1

- SUMÁRIO
    
    

# Método de Newton para Várias Variáveis

## Vetor Gradiente

$$
\nabla f_i(x) = 
\begin{bmatrix}
\frac{\partial f_i}{\partial x_1} \\ 
\frac{\partial f_i}{\partial x_2}\\
...\\
\frac{\partial f_i}{\partial x_n}
\end{bmatrix}
$$

$\hookrightarrow$  De forma análoga a como usamos a derivada de $f(x)$ no método de Newton para equações, usamos o vetor gradiente par ao método de newton para sistemas de várias variáveis.

$$
f_i \approx f_i (x^{(k)}) + \nabla f_i (x^{(k)})^T (x - x^{(k)})
$$

## Jacobiana

$\hookrightarrow$ Acima vimos o gradiente para somente uma linha, i.e somente uma equação de múltiplas variáveis.

$\hookrightarrow$  Como estamos trabalhando com um sistema, podemos representar todos os gradientes de todas as linhas pela matriz jacobiana:

$$
J(x) \begin{bmatrix} 
\nabla f_1(x)^T \\
\nabla f_2(x)^T  \\
... \\ 
\nabla f_n(x)^T
\end{bmatrix}
$$

$\hookrightarrow$  Resultando em:

$$
F(x) \approx F(x^{(k)}) + J(x^{(k)})(x - x^{(k)})
$$

$\hookrightarrow$  Igualando a zero temos:

$$
-F(x^{(k)}) =  J(x^{(k)})\underbrace{(x^{(k+1)} - x^{(k)})}_{Passo \ de \ Newton}
$$

$\hookrightarrow$ Com isso temos:

$$
\boxed{-F(x^{(k)}) =  J(x^{(k)})s^{(k)}}
$$

e 

$$
\boxed{x^{(k+1)} = x^{(k)} + s^{(k)}}
$$

# Critérios de Parada

## Critério Absoluto

$$
||x^{(k+1)} - x^{(k)}||_\infty \le \varepsilon
$$

## Critério Relativo

$$
\frac{||x^{(k+1)} - x^{(k)}||_\infty}{||x^{(k+1)}||_\infty} \le \varepsilon
$$

## Norma

$$
||F(x^{(k+1)}||_\infty \le \varepsilon
$$

# Exemplo

$\hookrightarrow$  Tendo como sistema:

$$
\begin{cases}
x_2 = 3 - x_1 \\ 
x^2_1 + x_2^2 = 9
\end{cases}
$$

- 1º Passo - Organizar nosso sistema
    - Precisamos organizar o nosso sistema para acharmos nossas $f_i$, igualando cada linha a zero:
    
    $$
    \begin{cases}
    x_2 = 3 - x_1 \rightarrow x_1 + x_2 - 3 = 0  \rightarrow f_1 \\ 
    x^2_1 + x_2^2 = 9 \rightarrow x_1^2 + x_2^2 - 9 = 0  \rightarrow f_2
    \end{cases}
    $$
    
- 2º Passo - Definir nossa função $F(x)$
    - $F(x)$ é composta  pelas linhas organizadas do passo anterior:
    
    $$
    F(x) = \begin{bmatrix}f_1(x) \\ f_2(x)\end{bmatrix}
    $$
    
- 3º Passo - Definir a Jacobiana
    - Nada mais é do que o vetor gradiente de cada uma das funções.
    
    $$
    J(x) = \begin{bmatrix}1 & 1 \\ 2x_1 & 2x_2\end{bmatrix}
    $$
    
- 4º Passo - Iniciar as iterações
    - Inicialmente temos um chute $x_0$ que substituímos em $F(X)$.
    - Além disso calculamos o jacobiano substituindo $x_0$.
    - Agora, utilizando a equação  ${-F(x^{(k)}) =  J(x^{(k)})s^{(k)}}$ temos um sistema linear onde temos $J$, $F$ e queremos achar $s$.
    - Assim conseguimos calcular o x da iteração:
        
        $$
        {x^{(k+1)} = x^{(k)} + s^{(k)}}
        $$