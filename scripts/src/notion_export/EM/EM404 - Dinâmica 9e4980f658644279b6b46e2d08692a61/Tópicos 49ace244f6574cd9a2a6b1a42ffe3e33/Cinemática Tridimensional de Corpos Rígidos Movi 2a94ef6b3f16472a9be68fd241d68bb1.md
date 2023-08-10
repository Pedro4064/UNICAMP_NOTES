# Cinemática Tridimensional de Corpos Rígidos: Movimento Geral

Created: July 2, 2022 11:54 AM
Prova: P3

[Anotações de Aula](Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Movi%202a94ef6b3f16472a9be68fd241d68bb1/Anotac%CC%A7o%CC%83es%20de%20Aula%20cf56194ec68043d5a28859f615bbc80b.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Anteriormente vimos o movimento de translação e rotação em 3 dimensões de forma separadas. Agora, entretanto, iremos analisar o movimento geral em 3 dimensões, e para tal é mais vantajoso analisarmos por movimento relativo.

# Efeitos de Referência

## Efeitos de Referência em Translação

$\hookrightarrow$ Para análises onde o sistema de coordenadas variante só translada temos:

$$
\vec V_A =  \vec V_B + \vec\omega \times \vec r_{A|B}
$$

$$
\vec a_A = \vec a_B + \dot{\vec{\omega}}\times \vec r_{A|B} + \vec \omega \times (\vec \omega \times \vec r_{A|B})
$$

## Efeitos de Referência em Rotação

$\hookrightarrow$ Para análises onde o sistema de coordenadas variante também sofre rotação temos:

$$
\vec V_A = \vec V_B + \vec\Omega\times \vec r_{A|B} + \vec V_{rel}
$$

$$
\vec a_A = \vec a_B + \dot{\vec{\Omega}}\times \vec r_{A|B} + \vec \Omega \times (\vec \Omega \times \vec r_{A|B}) + 2\vec\Omega \times \vec v_{rel} + \vec a_{rel}
$$

<aside>
<img src="Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Movi%202a94ef6b3f16472a9be68fd241d68bb1/yuru_camp.png" alt="Cinema%CC%81tica%20Tridimensional%20de%20Corpos%20Ri%CC%81gidos%20Movi%202a94ef6b3f16472a9be68fd241d68bb1/yuru_camp.png" width="40px" /> $\vec{\Omega}$ representa a velocidade angular dos eixos (logo é a soma vetorial das velocidades angulares que atual sobre o eixo/haste em análise)e pode ser diferente da velocidade angular do corpo

</aside>