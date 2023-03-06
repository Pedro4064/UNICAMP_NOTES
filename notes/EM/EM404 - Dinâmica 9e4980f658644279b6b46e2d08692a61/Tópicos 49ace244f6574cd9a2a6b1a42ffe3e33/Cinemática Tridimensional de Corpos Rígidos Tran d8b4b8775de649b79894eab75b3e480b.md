# Cinemática Tridimensional de Corpos Rígidos: Translação e Rotação

Created: July 1, 2022 3:22 PM
Prova: P3

[Anotações de Aula](Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Tran%20d8b4b8775de649b79894eab75b3e480b/Anotac%CC%A7o%CC%83es%20de%20Aula%2096bfd16366734b7abd37716657b4d09b.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Ao se adicionar mais uma dimensão, quando comparado com a cinemática plana, nós não somente adicionamos mais uma componente para velocidades e forças, nós também adicionamos mais dois possíveis movimentos de rotação como um todo. 

$\hookrightarrow$ Levando isso em consideração, a complexidade cresce, mas veremos casos específicos e vetores apropriados para lidarmos com a cinemática em 3 dimensões.

# Principais Conceitos

## Plano de Movimento

$\hookrightarrow$ Quando todos os pontos de um corpo rígido se deslocam em planos paralelos, tem-se uma forma geral do movimento em plano (que vimos anteriormente).

$\hookrightarrow$ Levando isso em consideração, a cinemática do movimento plano apresentado fornece uma descrição completa do movimento, quando aplicado ao plano de referência $p$, que é paralelo aos planos de movimento.

$\hookrightarrow$ Tal plano $p$ de referência é escolhido através do centro de massa $G$ e é chamado de plano de movimento.

## Rotação e Vetores Apropriados

$\hookrightarrow$ A principal coisa que se deve saber é que **Rotações Finitas não podem ser tratadas como vetores**.

$\hookrightarrow$ **Rotações Infinitesimais**, por outro lado, obedecem os conceitos de adição de vetores e, portanto, **podem ser considerados como vetores**.

<aside>
<img src="Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Tran%20d8b4b8775de649b79894eab75b3e480b/Hifumi_Surprised.png" alt="Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Tran%20d8b4b8775de649b79894eab75b3e480b/Hifumi_Surprised.png" width="40px" /> No curso iremos tratar majoritariamente de rotações infinitesimais, então não tem problema

</aside>

## Eixo Instantâneo de Rotação

$\hookrightarrow$ Quando analisamos qualquer corpo com um ponto fixo, podemos observar que eles está girando instantaneamente em torno de um eixo específico que passa através do ponto de fixação.

$\hookrightarrow$ Este conceito pode ser interpretado como uma extensão do ponto instantâneo de velocidade nula que vimos em cinemática plana.

$\hookrightarrow$ Podemos ainda introduzir o conceito de cones de movimento. Um corpo possui 2 cones de movimento, sendo eles:

1. Cone do Corpo → Cone gerado pela rotação do eixo instantâneo de rotação com o eixo de rotação do corpo.
2. Cone Espacial → Cone gerado pelo eixo instantâneo de rotação com o eixo de rotação espacial

![Screen Shot 2022-07-01 at 3.41.47 PM.png](Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Tran%20d8b4b8775de649b79894eab75b3e480b/Screen_Shot_2022-07-01_at_3.41.47_PM.png)

![Screen Shot 2022-07-01 at 3.42.09 PM.png](Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Tran%20d8b4b8775de649b79894eab75b3e480b/Screen_Shot_2022-07-01_at_3.42.09_PM.png)

# Análise Cinemática

$\hookrightarrow$ Agora que vimos o caso geral onde há rotação em dois sentidos (gerando tanto o cone do corpo quanto o cone espacial) podemos analisar a aceleração angular e a velocidade.

## Aceleração Angular

$\hookrightarrow$ A aceleração angular $\alpha$ de um corpo rígido em movimento tridimensional é a derivada no tempo da sua velocidade angular. A velocidade angular, por sua vez, é um vetor $\therefore$ apresenta tanto módulo quanto direção, e a aceleração angular deve refletir isso.

$\hookrightarrow$ Levando isso em consideração temos, para sistemas onde a velocidade angular de rotação e de precessão são constantes em módulo:

$$
\vec \alpha = \vec \Omega \times \vec \omega
$$

$\hookrightarrow$ Onde $\vec \Omega$ é o vetor da velocidade angular do cone espacial.

$\hookrightarrow$ Nesse caso, o $\vec \alpha$ representa somente a variação de direção pois não há mudança em módulo, se houvesse ficaria:

$$
\vec\alpha = (\dot{\vec\Omega} + \dot{\vec\omega}) +  \vec \Omega \times \vec \omega
$$

$\hookrightarrow$ Podemos observar que se não houver o movimento espacial (somente o do corpo) voltamos para o caso de Plano de movimento e se $|\omega| = const$ teremos $\alpha = \dot \omega = 0$.

## Aceleração Total

$$
\vec a = \dot{ \vec \omega} \times \vec r + \vec \omega \times (\vec \omega \times \vec r)
$$

$\hookrightarrow$ Que também pode ser escrito como:

$$
\vec a =  \vec \alpha \times \vec r + \vec \omega \times (\vec v)
$$

$\hookrightarrow$ Onde $\vec r$ é o vetor da origem do sistema até o ponto de interesse.

## Velocidade

$$
\vec v = \vec \omega \times \vec r 
$$

$\hookrightarrow$ Onde $\vec r$ é o vetor da origem do sistema até o ponto de interesse.