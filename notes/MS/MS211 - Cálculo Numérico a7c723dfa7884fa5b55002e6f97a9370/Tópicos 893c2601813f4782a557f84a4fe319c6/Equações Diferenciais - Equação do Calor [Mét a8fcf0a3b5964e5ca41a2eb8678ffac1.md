# Equações Diferenciais - Equação do Calor [Método Implícito]

Aula: Aula 20
Created: November 22, 2021 3:02 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ A grande diferença entre o método implícito e o método explícito é que o método implícito utiliza a diferença atrasada para a derivada primeira:

$$
u_t(x_i, t_i) \approx \frac{u_{ij} - u_{i, j-1}}{\Delta t}
$$

$\hookrightarrow$ Que, quando substituido na EDP original ficará:

$$
\boxed{-\alpha u_{i-1, j} + (1 + 2\alpha) u_{ij} - \alpha u_{i+1, j} = u_{i, j-1}}
$$

# Sistema Linear

$\hookrightarrow$ Assim como no método explicito, somos capazes de representar nossa solução numérica por um sistema linear:

![Screen Shot 2021-11-22 at 3.07.52 PM.png](Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Equac%CC%A7a%CC%83o%20do%20Calor%20%5BMe%CC%81t%20a8fcf0a3b5964e5ca41a2eb8678ffac1/Screen_Shot_2021-11-22_at_3.07.52_PM.png)