# Vetores Força

Aula: Aula03
Capítulo: Cap. 2
Created: August 9, 2021 9:28 PM
Prova: P1

[Anotações de Aula](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Anotac%CC%A7o%CC%83es%20de%20Aula%205b1316c9d7144611a5a709a8b2c2ca40.md)

- SUMÁRIO
    
    

# Escalares e Vetores

## Escalares

$\hookrightarrow$ Escalares nada mais são do que quantidades caracterizadas por um número.

## Vetores

$\hookrightarrow$ Já os vetores são quantidades que possuem intensidade e direção.

$\hookrightarrow$ Graficamente, vetores são descritos por flechas, onde:

- Intensidade
    - Representada pelo tamanho da flecha
- Direção
    - Definida pelo ângulo entre o eixo de referência e a flecha.
- Sentido
    - Indicado pela ponta da flecha

# Operações Vetoriais

## Multiplicação e Divisão por Escalar

$\hookrightarrow$ Para multiplicarmos um vetor por um escalar $a$,  basta multiplicarmos cada coordenada por $a$.

$\hookrightarrow$ Com isso, temos que a direção do vetor não muda, mas sua intensidade muda (se $|a|\ne 1$) e seu sentido também pode mudar (se $a < 0$).

![Screen Shot 2021-08-17 at 9.51.40 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_9.51.40_AM.png)

## Adição e Subtração Vetorial

$\hookrightarrow$ Podemos realizar tais operações de três formas:

- Lei do Paralelogramo
    - juntamos dois vetores pela sua cauda, completamos o paralelogramo e o vetor resultante será a diagonal do paralelogramo:
        
        ![Screen Shot 2021-08-17 at 9.58.15 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_9.58.15_AM.png)
        
    - Se observarmos bem, podemos ainda tratar como um triângulo:
        
        ![Screen Shot 2021-08-17 at 9.59.28 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_9.59.28_AM.png)
        
    
- Vetores Colineares
    - Para vetores colineares (que possuem a mesma direção) podemos simplesmente somar suas coordenadas.
        
        ![Screen Shot 2021-08-17 at 10.07.14 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_10.07.14_AM.png)
        
- Decomposição Vetorial
    - podemos tanto decompor em função do eixo de referência como também em função de quaisquer outros dois vetores desde que sejam perpendiculares.

## Adição de Forças Vetoriais

$\hookrightarrow$ É corriqueiro que haja mais de duas forças sendo aplicadas sobre um corpo.

$\hookrightarrow$ Tendo isso em mente, é recomendado utilizar a decomposição de vetores (pois facilitará as contas e não serão tão extensas como seriam se utilizar a lei do paralelogramos várias vezes).

## Adição de um Sistema de Forças Coplanares

$\hookrightarrow$ Como dito anteriormente, é mais fácil decompormos as forças em relação a um sistema cartesiano comum, soma-los e depois calcular sua resultante.

$\hookrightarrow$ Quando temos forças coplanares, isso se torna ainda mais fácil, pois precisamos decompor somente nos dois eixos principais $(x,y)$ representados respectivamente pelos vetores unitários $(\vec{i}\ \ \ , \ \vec{j})$.

$\hookrightarrow$ Com esse decomposição, podemos simplesmente somar todas as componentes $\vec{i}$ e depois somar todas as componentes $\vec{j}$ para, no fim, calcularmos a resultante.

# Vetores Cartesianos

$\hookrightarrow$ Para operações vetoriais tridimensionais, as contas são bastante simplificadas se os vetores forem representados na forma Vetorial Cartesiana.

$$
\vec{A} = \vec{A_x} + \vec{A_y} + \vec{A_z}
$$

![Screen Shot 2021-08-17 at 10.53.05 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_10.53.05_AM.png)

## Vetores Cartesianos Unitários

$\hookrightarrow$ São vetores adimensionais que representam a direção e o sentido de um vetor.

$\hookrightarrow$ Para acharmos o vetor unitário de um vetor, precisamos somente dividi-lo pelo seu módulo (que é igual à raiz do seu produto interno):

$$
u_A = \frac{\vec{A}}{||A||} = \frac{\vec{A}}{\sqrt{\lang \vec{A}, \vec{A} \rang}}
$$

$\hookrightarrow$ De tal forma que:

$$
\vec{A} = ||A|| u_A
$$

$\hookrightarrow$ De modo geral, utilizamos os vetores unitários cartesianos $(i, j, k)$ que representam, respectivamente $(x, y, z)$.

$\hookrightarrow$ Com isso temos que:

$$
\vec{A} = A_xi + A_yj + A_zk
$$

e 

$$
||\vec{A}|| = \sqrt{A_x^2 + A_y^2 + A_z^2}
$$

## Cosenos Diretores

$\hookrightarrow$ São os cosenos dos ângulos de vetores em relação ao plano cartesiano:

![Screen Shot 2021-08-17 at 11.15.19 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_11.15.19_AM.png)

![Screen Shot 2021-08-17 at 11.15.53 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-08-17_at_11.15.53_AM.png)

# Vetor Posição

$\hookrightarrow$ Quando queremos achar achar o vetor que une dois outros vetores de tal forma que:

$$
r_a + r = r_b
$$

![Screen Shot 2021-09-04 at 9.43.11 AM.png](Vetores%20Forc%CC%A7a%20ab67a7622b2f4030b5ab60cd5a2f09ff/Screen_Shot_2021-09-04_at_9.43.11_AM.png)

$\hookrightarrow$ Podemos resolver isolando o $r$:

$$
r = r_b - r_a
$$

$\hookrightarrow$  E sabemos pelas operações vetoriais que precisamos somente subtrair o índice para cada componente:

$$
r = (x_b - x_a)i + (y_b - y_a)j + (z_b - z_a)k
$$

# Produto Escalar

$\hookrightarrow$ O produto escalar entre dois vetores, dado por:

$$
\vec A \cdot \vec B =|A||B| \cos \theta
$$

$\hookrightarrow$ Nos ajuda a encontrar algumas coisas que são muito importantes na estática, sendo elas:

1. Ângulo entre dois vetores
2. Projeção de um vetor em outro

## Ângulo Entre Vetores

$\hookrightarrow$ Levando em consideração a fórmula citada anteriormente, para encontrarmos o ângulo entre dois vetores fazemos:

$$
\theta = \cos^{-1}\left(\frac{\vec A\cdot \vec B}{|A||B|}\right)
$$

## Projeção

$\hookrightarrow$ A projeção de um vetor $\vec{A}$ sobre um linha $a$ é:

$$
A_a = \vec A \cdot u_a
$$

$\hookrightarrow$ Onde $u_a$ é o vetor unitário da linha $a$.

$\hookrightarrow$ Com isso encontramos a intensidade do vetor $A$ na linha $a$.

$\hookrightarrow$ Depois disso, somos ainda capazes de determinar a componente perpendicular $A_\perp:$

$$
\vec A_\perp = \vec A - \vec A_a
$$