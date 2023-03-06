# Mecânica Analítica: Vínculos, Graus de Liberdade, Coordenadas Generalizadas e Princípio do Trabalho Virtual

Created: July 3, 2022 10:16 AM
Prova: P3

[Anotações de Aula](Meca%CC%82nica%20Anali%CC%81tica%20Vi%CC%81nculos,%20Graus%20de%20Liberdade%20a520064aec28464fa856bcd6ea74a39f/Anotac%CC%A7o%CC%83es%20de%20Aula%209af64416d52f4ec4bc97dab655a0f081.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Até o momento nós utilizamos uma abordagem que utiliza as equações de movimento, formuladas por Newton, e  vetores, para representar as grandezas de interesse como força, velocidade, etc. Tal abordagem é chamada de Mecânica Vetorial.

$\hookrightarrow$ Iremos, entretanto, analizar uma abordagem diferente para resolução de problemas de dinâmica, chamada de Mecânica Analítica.

$\hookrightarrow$ A mecânica analítica, atribuída a Leibnitz e Lagrange, considera o sistema como um todo, formulando o problema da mecânica a partir de duas quantidades escalares fundamentais: A Energia Cinética e a Energia Potencial.

$\hookrightarrow$ A grande questão da Mecânica analítica é que ela leva em consideração as restrições cinemáticas do movimento sem que seja necessário o cálculo das forças internas que as mantêm, além da formulação geral ser analítica e não vetorial.

# Conceitos Iniciais

## Vínculos

- São limitações às possíveis posições e velocidades das partículas de um sistema mecânico, restringindo a priori o seu movimento.

## Vínculos Holônomos

- São vínculos que dependem somente de tempo e posição

## Graus de Liberdade

- Os graus de liberdade de um sistema são o número mínimo de parâmetros independentes necessários e suficientes para definir complemente sua posição no espaço em cada instante no tempo.
- Tal número pode ser estimada pela diferença entre o número de possíveis movimentos e pelo número de limitações de movimento.

<aside>
<img src="Meca%CC%82nica%20Anali%CC%81tica%20Vi%CC%81nculos,%20Graus%20de%20Liberdade%20a520064aec28464fa856bcd6ea74a39f/Amazon_com__animal_shirt_women.jpeg" alt="Meca%CC%82nica%20Anali%CC%81tica%20Vi%CC%81nculos,%20Graus%20de%20Liberdade%20a520064aec28464fa856bcd6ea74a39f/Amazon_com__animal_shirt_women.jpeg" width="40px" /> Para analizar a quantidade de movimentos que um corpo gera no outro (para casos de junta/vínculo entre dois corpos) basta você travar  um deles e ver quais movimentos o outro ainda pode fazer (desconsiderando todas as outras limitações). Se você subtrair esse numero de ainda possíveis movimentos do número geral que um corpo com aquelas dimensões pode fazer (e.g 2D → 3 movimentos) você terá o número de limitações para aquela junta.

</aside>

## Coordenadas Generalizadas

- Coordenadas Generalizadas nada mais são do que qualquer sistema de coordenadas que tem as seguintes características:
    1. São Independentes entre si
    2. Caracterizam univocamente a configuração do sistema
    3. Tornam os vínculos identicamente satisfeitos.

## Deslocamento Virtual

- Um deslocamento virtual de um sistema é uma mudança na sua configuração que resulta de uma variação arbitrária das suas coordenadas, consistente com os seus vínculos, em um dado instante $t \rightarrow 0$ (i.e instantâneo).
- Possui as seguintes características:
    1. Quantidade infinitesimal: Representado por $\delta$
    2. É postulado (i.e) proposto $\therefore$ não ocorre realmente
    3. Respeita os Vínculos
- Além disso temos que $\delta$ é um operador similar ao operador diferencial $d$:
    
    ![Screen Shot 2022-07-03 at 11.03.08 AM.png](Meca%CC%82nica%20Anali%CC%81tica%20Vi%CC%81nculos,%20Graus%20de%20Liberdade%20a520064aec28464fa856bcd6ea74a39f/Screen_Shot_2022-07-03_at_11.03.08_AM.png)
    

# Trabalho Virtual

$\hookrightarrow$ A partir do conceito de deslocamento virtual somos capazes de introduzi um novo conceito, chamado de trabalho virtual:

$$
\delta W = \sum F_i \delta x_i
$$

$\hookrightarrow$ Como podemos ver acima, o trabalho virtual $\delta W$ é a soma do produto entre as forças aplicadas e os deslocamentos virtuais na direção da força.

$\hookrightarrow$ Com isso conseguimos ver a importância do trabalho virtual, pois nos permite desconsiderar forças de restrição e forças internas no cálculo (pois não há movimento em suas direções).

## Trabalho Virtual e Coordenadas Gerais

$\hookrightarrow$ Podemos, ainda, aplicar coordenadas gerais para o nosso sistema de coordenadas $r_1, r_2, ..., r_i$ de tal forma que $r_1 = f(q_1, q_2, ..., q_n)$ , i.e as nossas coordenadas normais $r$ estão em função das coordenadas gerais $q_1, q_2, ..., q_n$.

$\hookrightarrow$ Nesse caso, ao aplicarmos o operador $\delta$ do deslocamento e trabalho virtual teremos:

$$
\begin{aligned}
\delta W &= F_1\delta r_1 + F_2 \delta r_2 + ...+F_i\delta r_i \\ 
&= F_1\left(\frac{\partial r_1}{\partial q_1} \delta q_1 + \frac{\partial r_1}{\partial q_2} \delta q_2 + ...+ \frac{\partial r_1}{\partial q_n} \delta q_n\right ) + F_2\left(\frac{\partial r_2}{\partial q_1} \delta q_1 + \frac{\partial r_2}{\partial q_2} \delta q_2 + ...+ \frac{\partial r_1}{\partial q_n} \delta q_n\right ) + ...
\end{aligned}
$$

$\hookrightarrow$ Que pode ser rearranjada como:

$$
\begin{aligned}
\delta W
&= \delta q_1\left(\frac{\partial r_1}{\partial q_1} F_1 + \frac{\partial r_2}{\partial q_1} F_2 + ...+\frac{\partial r_i}{\partial q_1} F_i\right ) + ...
\end{aligned}
$$

$\hookrightarrow$ Como o trabalho virtual é zero $\therefore \delta W = 0$ e temos que as coordenadas gerais $q_1, ..., q_n$ são independentes teremos $n$ equações (o que estão dentro do parênteses igualados a zero).

<aside>
<img src="Meca%CC%82nica%20Anali%CC%81tica%20Vi%CC%81nculos,%20Graus%20de%20Liberdade%20a520064aec28464fa856bcd6ea74a39f/yuru_camp.png" alt="Meca%CC%82nica%20Anali%CC%81tica%20Vi%CC%81nculos,%20Graus%20de%20Liberdade%20a520064aec28464fa856bcd6ea74a39f/yuru_camp.png" width="40px" /> Basicamente o que precisamos fazer é montar a equação do trabalho virtual (utilizando as coordenadas que forem mais fáceis de visualizar nos diagramas) e posteriormente fazer a troca das coordenadas para as coordenadas gerais (utilizando o operador $\delta$ e as derivadas parciais) para então botar as coordenadas gerais $\delta q_1, ..., \delta q_n$ em evidência e então você terá as $n$ equações independentes igualadas a zero.

</aside>