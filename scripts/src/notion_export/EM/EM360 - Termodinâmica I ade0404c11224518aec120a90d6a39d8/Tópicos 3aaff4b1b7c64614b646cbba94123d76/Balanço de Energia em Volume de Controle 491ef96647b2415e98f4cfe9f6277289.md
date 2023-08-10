# Balanço de Energia em Volume de Controle

Aula: Aula09, Aula10, Aula11, Aula12
Created: September 10, 2021 10:42 AM

[Anotações de Aula](Balanc%CC%A7o%20de%20Energia%20em%20Volume%20de%20Controle%20491ef96647b2415e98f4cfe9f6277289/Anotac%CC%A7o%CC%83es%20de%20Aula%204eed14668cd94d0aa2433b123ec65f27.md)

- SUMÁRIO
    
    

# Conservação de Massa para um Volume de Controle

## Balanço da Taxa de Massa

$\hookrightarrow$ Levando em consideração um volume de massa com fluxo de entrada de massa $m_e$ e saída de massa $m_s$ temos que o princípio da conservação de massa estabelece que:

![Screen Shot 2021-09-10 at 10.46.29 AM.png](Balanc%CC%A7o%20de%20Energia%20em%20Volume%20de%20Controle%20491ef96647b2415e98f4cfe9f6277289/Screen_Shot_2021-09-10_at_10.46.29_AM.png)

$$
\boxed{\frac{dm_{vc}}{dt} = \dot m_e - \dot m_s}
$$

$\hookrightarrow$ Isso é, a variação temporal da massa dentro do volume de controle é igual a diferença entre a vazão mássica de entrada e a vazão mássica de saída.

$\hookrightarrow$ De forma mais geral ainda, podemos descrever um volume de controle que possui mais de uma entrada e mais de uma saída de massa, logo temos que:

$$
\frac{d m_{vc}}{dt} = \sum_e \dot m_e - \sum_s \dot m_s
$$

## Vazão de Massa

$\hookrightarrow$ Podemos calcular a taxa de vazão de massa passando por uma área $A$ do volume de controle por:

$$
\dot m  = \int_A \rho V_n \  dA
$$

$\hookrightarrow$ Onde $\rho$  é a massa específica (i.e $kg/m^3$)

$\hookrightarrow$ $V_n$ é a componente (paralela à normla da área) da velocidade de saída da massa.

$\hookrightarrow$ $A$ área de saída

# Formas do Balanço de Massa em Termos de Taxa

$\hookrightarrow$ Muitas das vezes a aplicação da fórmula básica do balanço da taxa de massa, dada por $\frac{d m_{vc}}{dt} = \sum_e \dot m_e - \sum_s \dot m_s$ não é a melhor a ser aplicada. 

$\hookrightarrow$ Levando isso em consideração, iremos estudar alguns casos mais específicos da formulação do balanço da taxa de Massa:

- Escoamento Unidimensional
    - Para que o escoamento seja unidimensional precisa que:
        - [ ]  O escoamento é normal à fronteira nas posições onde a massa entra ou sai do volume de controle.
        - [ ]  Todas as propriedades intensivas (incluindo velocidade e massa específicas) são uniformes com relação à posição ao longo de cada área de entrada ou saída através da qual a massa escoa.
        
    - Para Escoamentos unidimensionais temos:
        
        $$
        \dot m = \rho AV
        $$
        
        ou, em função do volume específico:
        
        $$
        \dot m = \frac{AV}{v}
        $$
        
    - Onde $[AV] = m^2 \cdot m/s = m^3/s$ e é chamado de vazão volumétrica.
- Regime Permanente
    - Um sistema é considerado em regime permanente se nenhuma das propriedades mudar ao longo do tempo.
    - Levando isso em consideração, temos que $\frac{dm_{vc}}{dt} = 0 \therefore$
        
        $$
        \sum_e \dot m_e = \sum_s \dot m_s
        $$
        
        <aside>
        <img src="Balanc%CC%A7o%20de%20Energia%20em%20Volume%20de%20Controle%20491ef96647b2415e98f4cfe9f6277289/Evangelion.gif" alt="Balanc%CC%A7o%20de%20Energia%20em%20Volume%20de%20Controle%20491ef96647b2415e98f4cfe9f6277289/Evangelion.gif" width="40px" /> OBS: O fato de um sistema ter a taxa de entrada igual à taxa de saída não o torna em regime permanente. Para isso TODAS as suas propriedades são independentes do tempo.
        
        </aside>