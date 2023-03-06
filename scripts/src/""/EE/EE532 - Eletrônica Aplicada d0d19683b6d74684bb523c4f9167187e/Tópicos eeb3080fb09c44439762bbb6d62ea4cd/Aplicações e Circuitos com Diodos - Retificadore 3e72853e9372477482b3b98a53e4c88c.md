# Aplicações e Circuitos com Diodos - Retificadores

Created: March 25, 2022 4:52 PM
Prova: P1

- SUMMARY
    
    

# Retificador de Meia Onda

$\hookrightarrow$ Em uma fonte padrão, nós precisamos transformar uma alta tensão de corrente alternada em uma tensão menor de corrente contínua.

$\hookrightarrow$ Isso é feita em etapas, sendo elas:

![Screen Shot 2022-03-25 at 4.54.08 PM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-25_at_4.54.08_PM.png)

$\hookrightarrow$ Onde a primeira parte, de retificação, é feita através de diodos seguindo o [modelo](Modelos%20de%20Diodos%201d96f21a3964461ea9c42b794eae6be4.md) de queda de tensão constante.

![Screen Shot 2022-03-25 at 4.57.58 PM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-25_at_4.57.58_PM.png)

## Retificador com Capacitor de Filtro

### Sem Load - Ideal

$\hookrightarrow$ Como vimos acima, o diodo "trava” a passagem de corrente quando a tensão é negativa, e isso resulta em momentos onde há corrente positiva e outros momentos quando não há corrente.

$\hookrightarrow$ Para retificarmos a corrente (i.e retirar os períodos onde não há corrente passando pois a tensão é negativa) nós podemos botar um capacitor em paralelo com o diodo e a fonte, que servirá como um “reservatório” que irá liberar corrente quando houver a inversão da polaridade, como mostra a figura abaixo:

![Screen Shot 2022-03-30 at 11.34.19 AM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-30_at_11.34.19_AM.png)

### Com Load - Efeito Ripple

$\hookrightarrow$ Esse cenário onde o capacitor mantém constante o $V_{out}$ só ocorre quando não há uma carga anexada.

$\hookrightarrow$ Quando há uma carga ocorre o efeito ripple, onde haverá uma diminuição da tensão $V_{out}$ até o próximo ciclo de carregamento do capacitor. 

$\hookrightarrow$ Tal variação da tensão $V_{out}$ ocorre dentro de um intervalo de tensão que chamamos de Tensão de Ripple.

![Screen Shot 2022-03-30 at 11.38.31 AM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-30_at_11.38.31_AM.png)

$\hookrightarrow$ Tal tensão de Ripple é dada por:

$$
\boxed{V_R \approx \frac{I_L}{C_1 f}}
$$

$\hookrightarrow$ Além disso, é importante calcular a corrente média que passa pelo diodo, que é dada por:

$$
\boxed{I_{Dmédio} = I_L \left(\frac{1}{2\pi} \sqrt{\frac{2V_R}{V_{cap}} } + 1\right)}
$$

$\hookrightarrow$ Além de calcularmos a corrente de pico que passa pelo diodo:

$$
\boxed{i_{Dpico} = i_{Lmédio} (1 + 2\pi \sqrt{2V_{cap}/V_R})}
$$

<aside>
<img src="Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/yuru_camp.png" alt="Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/yuru_camp.png" width="40px" /> OBS: Devido ao efeito de tensão ripple, quando formos escolher o capacitor nós precisamos calcular o $V_{cap} = V_{cc} + V_R/2$

</aside>

<aside>
<img src="Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/ina-blanket.png" alt="Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/ina-blanket.png" width="40px" /> OBS$^2$: Quando estamos dimensionando a tensão do secundário nós temos que: $V_{sec} = V_{cap} + V_{Don}$ e se quisermos em $RMS$ só precisamos dividir por $\sqrt{2}$.

</aside>

### Corrente IFSM

$\hookrightarrow$ A corrente IFSM é a corrente de pior caso, no qual o capacitor está descarregado ($\therefore$ ele se comporta como um curto) e a tensão $AC$ está em pico.

$\hookrightarrow$ Ela é dada por:

$$
I_{FSM} = \frac{V_s}{R_s}
$$

$\hookrightarrow$ Onde:

- $V_s$ é a tensão do secundário do transformador
- $R_s$ é a resistência do secundário do transformador

## Projetando Um Transformador

$\hookrightarrow$ Para projetarmos um transformador de meia onda nós precisamos:

- Passo 1 - Capacitor:
    - Calcular o valor do capacitor baseado na tensão de ripple max aceita.
    - Calcular a tensão do capacitor, dada por $V_{out_{target}} + V_R/2$.
- Passo 2 - Secundário do Transformador:
    - Calcular a tensão no secundário: $V_{psec_{RMS}} = (V_{cap} + V_{Don})/2$
- Passo 3 - Diodo:
    - Tensão reversa no diodo $PIV$:
        
        $$
        PIV \approx 2 \cdot V_{psec}
        $$
        
    - Corrente Média no diodo
    - Corrente de Pico
    - Corrente $I_{FSM}$

# Retificador de Onda Completa

$\hookrightarrow$ Ao contrário do retificador de meia onda, que simplesmente impede a passagem de corrente quando a polarização é inversa, o retificador de onda completa vai conduzir todo o ciclo, rebatendo a inversa.

$\hookrightarrow$ Isso pode ser feito através da utilização de um transformador especial (i.e transformador com derivação central) ou com uma configuração de diodos chamado de full bridge rectifier.

## Transformador com Derivação Central

![Screen Shot 2022-03-30 at 12.15.42 PM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-30_at_12.15.42_PM.png)

## Ponte de Diodos

![Screen Shot 2022-03-30 at 12.18.19 PM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-30_at_12.18.19_PM.png)

 

<aside>
<img src="Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/mugi.gif" alt="Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/mugi.gif" width="40px" /> IMPORTANTE: É de suma importância lembrarmos que, como o tempo entre o carregamento do capacitor é cortado pela metade (já que todo o ciclo é retificado) a tensão de ripple é dada por $V_R = \frac{V_P}{2fVR}$. Valido para qualquer estratégia de retificação total.

</aside>

# Diodo Zener

$\hookrightarrow$ Quando polarizado diretamente, o diodo zener funciona da mesma forma que um diodo convencional.

$\hookrightarrow$ O grande diferencial, entretanto, é quando polarizamos ao inverso o Diodo zener, pois devido a sua dopagem, a tensão de break-down é específica de cada modelo.

$\hookrightarrow$ Com isso somos capazes de, a partir de certa tensão alvo, atingir a tensão de break-down do diodo zener e ele age como um curto, mesmo polarizado reversamente.

![Screen Shot 2022-03-30 at 5.01.46 PM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-30_at_5.01.46_PM.png)

## Regulador de Tensão

$\hookrightarrow$ Nós podemos usar a característica do valor de break-down do diodo zener para utiliza-lo como um regulador de tensão.

$\hookrightarrow$ Isso é possível pois se a tensão variar para acima da tensão de break-down do diodo zener ele abrirá e servirá como um divisor de tensão resistivo, como mostrado abaixo:

![Screen Shot 2022-03-30 at 5.04.48 PM.png](Aplicac%CC%A7o%CC%83es%20e%20Circuitos%20com%20Diodos%20-%20Retificadore%203e72853e9372477482b3b98a53e4c88c/Screen_Shot_2022-03-30_at_5.04.48_PM.png)