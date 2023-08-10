# Funções de Várias Variáveis

Capitulo: 14.1
Semana: Semana 1

## Função de Duas Variáveis

- Uma função $f$ de duas variáveis é uma função que relaciona dois números de "input" $(x,y)$ pertencentes a um conjunto $D$ com um único número $f(x,y)$. Onde temos $D$ como o domínio da funções e sua imagem sendo todos os valores possíveis de $f$ $\{f(x,y) | (x,y) \in D\}$
- Tendo $z = f(x,y)$ temos que $z$ é uma variável dependente e $x,y$ são independentes

### Gráfico de duas variáveis

- Como temos 2 variáveis independentes que definem uma terceira, se um gráfico for feito ele será um plano, pois é o valor de $z$ em função de um $x$ específico e de um $y$ específico.

### Curvas de nível

- É basicamente uma forma de visualizar um gráfico 3D em duas dimensões $(x,y)$  através de linhas que representam o valor em $z$.
    
    ![Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_2.56.24_PM.png](Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_2.56.24_PM.png)
    
    ![Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_2.56.37_PM.png](Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_2.56.37_PM.png)
    

### Exercícios

![Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_3.04.12_PM.png](Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_3.04.12_PM.png)

- Desenvolvimento
    - a)
        
        $$
        f(x,y) = ln(9-x^2 - 9y^2) \\ 
        $$
        
        Tendo em vista que estamos mexendo com $ln$, o que está dentro do parênteses deve ser diferente de zero e positiva $\therefore$
        
        $$
        (9 - x^2 - 9y^2) \gt 0 \\ \therefore\\ x^2 + 9y^2 \lt 9
        $$
        
        Devemos, entretanto, deixar esse inequação de uma forma que nós consigamos identificar qual sua forma geometricamente (se é uma eclipse, circunferência, parábola ...). Como temos um número multiplicando uma das variáveis sendo diferente de 1, é bem difícl que seja uma circunferência, deve ser melhor "igualarmos" um lado da equação a 1, para que possamos identificar se é uma elipse or what not.
        
        $$
        \frac{x^2}{3^2} + \frac{y^2}{1^2} \lt 1
        $$
        
        Vimos que é exatamente a equação de uma elipse, e como é menor que 1, se fizermos a conta vemos que quando $x=0$ e $y=0$ isso é igual a $0$, o que significa que todos os pontos que estão dentro dessa elipse correspondem à inequação acima.
        
        ![Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_3.19.00_PM.png](Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Screen_Shot_2020-09-18_at_3.19.00_PM.png)
        
    - b)
        
        Teoricamente comoestamos trabalhando com funções no conjunto dos reais ($f:\mathbb{R^2} \rightarrow\mathbb{R}$)
        
        então as reizes não podem conter número negativos $\therefore$ $x,y \ge 0$. O que inplica no seu domínio ser todo o primeiro quadrante do plano cartesiano
        
    

## Relembrando o Desenho de Certas Funções

### Paraboloide

$$
z = x^2 + y^2
$$

![https://upload.wikimedia.org/wikipedia/commons/9/9c/ParaboloidOfRevolution.png](https://upload.wikimedia.org/wikipedia/commons/9/9c/ParaboloidOfRevolution.png)

### Esfera

$$
r^2 = x^2+y^2+z^2
$$

![https://i.stack.imgur.com/Fxw34.png](https://i.stack.imgur.com/Fxw34.png)

### Cônes

$$
z^2 = x^2 + y^2
$$

![https://tutorial.math.lamar.edu/classes/calciii/QuadricSurfaces_Files/image002.png](https://tutorial.math.lamar.edu/classes/calciii/QuadricSurfaces_Files/image002.png)

### Cilindro

$$
x^2 + y^2 = r^2
$$

![Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Untitled.png](Func%CC%A7o%CC%83es%20de%20Va%CC%81rias%20Varia%CC%81veis%20e07b4f0580854efbb1bb99625e0684c1/Untitled.png)