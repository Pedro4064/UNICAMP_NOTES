# Equações Diferenciais - Equações de Ordem Superior

Aula: Aula 18
Created: November 10, 2021 10:18 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ A partir de agora iremos abordar equações diferenciais de ordem superior, isso é, de ordem maior que 1 (i.e contendo derivadas segundas, terceiras, etc).

$\hookrightarrow$ Tendo como forma geral:

$$

y^{(m)} = f(x, y, y'', y''', ..., y^{(m-1)})

$$

- Onde $y^{(m)}$ é a derivada de maior ordem, que fica isolada.

$\hookrightarrow$ A partir daí, iremos ter como estratégia transformar essa EDO em um sistema de EDOs de ordem 1:

$$
y \rightarrow z_1 \\ 
y' \rightarrow z_2 \\ 
y'' \rightarrow z_3 \\ 
... \\ 
y^{(m-1)} \rightarrow z_m \\ 
y^{(m)} = f(x, z_1, z_2, ..., z_m)
$$

$\hookrightarrow$ Com condições iniciais para cada derivada no mesmo ponto $x_0$.

# Passo a Passo

$$
\begin{cases}
y'' = 4y' - 3y - x \\ 
y(0) = \frac{4}{9} \\ 
y'(0) = \frac{7}{5}
\end{cases}
$$

- Tendo $h = 0.25$

- 1º Passo - Isolar Derivada de Maior ordem
    - No nosso exemplo já está isolado, mas precisamos sempre lembrar de isolar a derivada de maior ordem na nossa EDO.
- 2º Passo - Identificar Pontos de interesse
    
    $$
    f(x, y, y') = 4y' - 3y - x
    $$
    
    $$
    x_0 = 0
    $$
    
- 3º Passo - Reescrever como sistema de EDOs de primeira ordem
    
    $$
    \begin{cases}
    y \rightarrow z_1 \\ 
    y' \rightarrow z_2 \\
    y'' = f(x, z_1, z_2) = 4z_2 - 3z_1 - x
    \end{cases}
    $$
    
- 4º Passo - Representação Matricial
    
    $$
    Z = \begin{bmatrix}z_1 \\ z_2\end{bmatrix}, Z_0 = \begin{bmatrix}
    z_1(x_0) \\ 
    z_2(x_0)
    \end{bmatrix}, 
    Z' = \begin{bmatrix}
    z_1' \\
     z_2'
    \end{bmatrix}
    $$
    
- 5º Passo - Representar o PVI vetorialmente
    
    $$
    \begin{cases}
    Z' = F(x, Z) \\ 
    Z_0 = \begin{bmatrix}y(x_0) \\ y'(x_0)\end{bmatrix}
    \end{cases} \rightarrow \boxed{\begin{cases}
    Z' = F(x, Z) =  \begin{bmatrix}z_2 \\ f(x_1 ,z_1, z_2)\end{bmatrix} \\ 
    Z_0 = \begin{bmatrix}y(x_0) \\ y'(x_0)\end{bmatrix}
    \end{cases}}
    $$
    
- 6º Passo - utilização do algoritmo
    - Para isso precisamos somente transformações a formulação padrão dos métodos em suas respectivas versões vetoriais, como iremos mostrar abaixo
    

# Heun → Forma Vetorial

$$
\boxed{Z_{k+1} = Z_k + \frac{h}{2} [F(x_k, Z_k) + F(x_k + h, Z_k + hZ'_k)]}
$$