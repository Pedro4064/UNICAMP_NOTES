# Probabilidade

Created: May 7, 2022 5:31 PM
Tags: P1

[Anotações de Aula](Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Anotac%CC%A7o%CC%83es%20de%20Aula%20d9e6f7d059894433b0b72ce5d601bb0d.md)

- SUMMARY
    
    

# Principais Conceitos

## Nomenclatura

$\hookrightarrow$ **Experimento**: Qualquer processo que produza uma observação ou resultado.

$\hookrightarrow$ **Experimento Determinístico**: Aquele experimento em que, dada uma ação controlada, sabemos exatamente qual será o resultado obtido.

$\hookrightarrow$ **Experimento Aleatório**: É aquele em que não se tem certeza sobre seus resultados, a priori. Múltiplos resultados podem ser obtidos a partir de uma única ação. Cada vez que se repete o experimento, o resultado pode ser diferente.

## Lei dos Grandes Números

> Dizemos que se um evento de probabilidade $p$ é observada repetidamente em ocasiões independentes, a proporção da frequência observada deste evento em relação ao total número de repetições converge em direção a $p$ à medida que o número de repetições se torna arbitrariamente grande.
> 

## Probabilidade

$\hookrightarrow$ Através da Lei dos Grandes Números descrita acima podemos dizer que: 

> A probabilidade de um resultado acontecer é a proporção de vezes que o resultado ocorreu quando consideramos muitas observações de um fenômeno.
> 

## Espaço Amostral

$\hookrightarrow$ Dizemos que o espaço amostral é o conjunto de todos os resultados possíveis do experimento aleatório, denotado por $\Omega$.

## Evento

$\hookrightarrow$ Um evento é um subconjunto do espaço amostral, denotado por letras maiúsculas (e.g $A, B,...$)

# Probabilidades: Modelo Teórico

![Screen Shot 2022-05-07 at 5.52.52 PM.png](Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Screen_Shot_2022-05-07_at_5.52.52_PM.png)

## Interseção de Eventos

$\hookrightarrow$ A Interseção de $A$ e $B$ consiste de elementos do espaço amostral que pertencem ao avento $A$ **e** ao evento $B$, denotado por $A \cap B$.

![Screen Shot 2022-05-07 at 5.57.52 PM.png](Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Screen_Shot_2022-05-07_at_5.57.52_PM.png)

![Screen Shot 2022-05-07 at 5.59.15 PM.png](Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Screen_Shot_2022-05-07_at_5.59.15_PM.png)

$\hookrightarrow$ Já a união de $A$ com $B$ contém elementos que estejam tanto em $A$ **ou** em $B$, denotado por $A \cup B$.

$\hookrightarrow$ Importante de notarmos que no segundo exemplo laranja ao lado a interseção de $A$ e $B$ não existe $\therefore A \cap B = \empty$ e são chamados de disjuntos.

$\hookrightarrow$ Algo importante de se reparar quando estamos falando da união e sua probabilidade temos a fórmula ao lado.

$\hookrightarrow$ Precisamos subtrair a interseção, caso contrário estaríamos a contando duas vezes.

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

## Eventos Complementares

$\hookrightarrow$ Dizemos que dois eventos $A$ e $B$ são complementares se $A \cap B = \empty$ e $A\cup B = \Omega$.

$\hookrightarrow$ Com isso podemos representar: $B = A^C$ ou então "B é o complemento de A”

# Técnicas de Contagem

$\hookrightarrow$ Para experimentos simples que possuem poucas possibilidades é fácil de elaborar de forma manual o espaço amostral do nosso experimento para o calculo das probabilidades.

$\hookrightarrow$ Para experimentos e análises mais complexas, entretanto, isso não é viável, por isso iremos ver regras e técnicas de contagem → Para montarmos nossos espaços amostrais.

## Regra da Adição

- Supondo que temos dois procedimentos possíveis para executarmos uma tarefa, o procedimento $P_1$ tem $n_1$ formas enquanto o procedimento $P_2$ tem $n_2$ formas.
- Temos no total $n_1 + n_2$ formas.

- **Exemplo**: Sobremesas de um Restaurante
    
    ![Screen Shot 2022-05-07 at 8.04.19 PM.png](Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Screen_Shot_2022-05-07_at_8.04.19_PM.png)
    

## Regra da Multiplicação

- Supondo que temos dois procedimentos que precisam ser feitos, o procedimento $P_1$ tem $n_1$ formas enquanto o procedimento $P_2$ tem $n_2$ formas.
- Temos no total, para realizar $P_1$ e $P_2$:  $n_1 \times n_2$ formas.

- **Exemplo**: Spoleto
    
    ![Screen Shot 2022-05-07 at 8.06.02 PM.png](Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Screen_Shot_2022-05-07_at_8.06.02_PM.png)
    

## Permutação

- A permutação nos dá o número total de formas de dispormos (a.k.a permutarmos) $n$ elementos únicos sem reposição.
- Dado por $n!$ ($n$ fatorial)
- Há, entretanto, uma fórmula diferente para quando há repetição de elementos, ela é dada por:

$$
\frac{n!}{n_1!n_2!...n_r!}
$$

- Que representa o número de divisões possíveis de $n$ objetos distintos em $r$ grupos distintos de respectivos tamanhos $n_1, n_2, ..., n_r$.

<aside>
<img src="Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/sagiriBleh.png" alt="Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/sagiriBleh.png" width="40px" /> Basicamente temos que agrupar os elementos iguais, contar quantos iguais de cada tipo tem e botar no denominador na forma fatorial.

</aside>

## Arranjo

- Representa o número de maneiras que podemos dispor $r$ elementos de um total de $n$ elementos.
- Basicamente a quantidade de arranjarmos em grupos de quantidade menor um total de $n$ elementos.
- Dado por:

$$
A(n, r) = \frac{n!}{(n-r)!}
$$

<aside>
<img src="Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Evangelion.gif" alt="Probabilidade%201e58631cb2cc4f66af67e0f5c1710c56/Evangelion.gif" width="40px" /> Importante ressaltarmos que Arranjo leva em consideração as posições

</aside>

## Combinação

- De forma análoga ao arranjo, a combinação visa contar a quantidade total de formas de agruparmos em um grupo de $r$ elementos um set total de $n$ elementos.
- A grande diferença é que o arranjo leva em consideração a posição, enquanto combinação não leva em consideração.
- A combinação é dada por:

$$
C\begin{pmatrix}n \\ r\end{pmatrix} = \frac{n!}{r!(n-r)!} = \frac{A(n, r)}{r!}
$$

## Amostragem Aleatória Simples com Reposição

- Quando temos um set de $N$ elementos, queremos obter um subset de $n$ elementos temos, mas que há reposição, temos que o número total é de:
    
    $$
    AAS_c = N^n
    $$
    
- Exemplo:
    - Temos um set binário $(0, 1)$ e queremos calcular o número total de possibilidades de um conjunto de $8bits$.
    - Nesse caso $N = 2$ e $n = 8$ $\therefore$ $n^\circ (\Omega) = 2^8$

# Probabilidade Condicional e Independência

## Probabilidade Condicional

$\hookrightarrow$ Probabilidade condicional é encontrar a probabilidade de um evento quando você tem alguma outra informação sobre o evento. 

$\hookrightarrow$ De modo geral temos que a probabilidade de $B$ sabendo que $A$ ocorreu é dada por:

$$
\boxed{P(B|A) = \frac{P(A\cap B)}{P(A)}}
$$

- Um exemplo é:
    - Imagine que você vai lançar dois dados. Você lança o primeiro e da $4$, qual a probabilidade de, ao lançar o segundo, a soma dar $10$ ?
    - Nesse caso temos:
        - O evento $A$ que já aconteceu (o primeiro ter dado $4$)
        - O evento $B$ que é a soma dar $10$
    - Queremos então encontrar $P(B|A)$ → A probabilidade de $B$ dado que $A$ aconteceu.
    - Nesse caso o novo espaço amostral será baseado nos eventos de $A \therefore \Omega_1 = \{(4,1), (4,2), (4,3), (4,4), (4,5), (4,6)\}$
    - E os casos favoráveis serão os que a soma de $10 \therefore \{(4,6)\}$
    - Logo:
        
        $$
        P(B|A) = \frac{1}{6}
        $$
        

## independência

$\hookrightarrow$ Falamos que dois eventos $A$ e $B$ são independentes quando:

$$
P(B|A) = P(B)
$$

$\hookrightarrow$ Logo:

$$
P(A \cap B) = P(A)P(B)
$$

# Teorema as Probabilidades Totais e Teorema de Bayes

## Probabilidades Totais

$$
P(A) = P(A|B)P(B) + P(A|B^C)P(B^C)
$$

> A probabilidade do evento $A$ é uma média ponderada de $P(A|B)$ e $P(A|B^C)$. Onde o peso de cada probabilidade condicional é a probabilidade do evento qu está sendo levando em conta ao calcular a probabilidade condicional de $A$
> 

## Teorema de Bayes

$$
P(B|A) = \frac{P(A|B)P(B)}{P(A|B)P(B) + P(A|B^c)P(B^c)}
$$