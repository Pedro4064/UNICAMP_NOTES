# Cinemática de Partículas

Created: March 29, 2022 10:36 AM
Prova: P1

[Anotações de Aula](Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Anotac%CC%A7o%CC%83es%20de%20Aula%202463433eebc347d7b9d126f9b3200a0a.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$  Cinemática é o ramo da dinâmica que descreve o movimento dos corpos sem referência às forças que causam o movimento ou são geradas como resultado do movimento.

$\hookrightarrow$  Algo importante de ressaltar é que nesse ponto do curso nós estamos lidando com a cinemática de partículas $\therefore$ corpos que não possuem comprimento, isso é aceitável $\iff$suas dimensões forem muito menor do que a curvatura da trajetória que descreve (e.g um avião indo de $NY$ até $LA$)

# Movimento Retilíneo

## Velocidade e Aceleração

$\hookrightarrow$  Temos que a velocidade média da partícula é dada por:

$$
v_{med} = \frac{\Delta s}{\Delta t}
$$

$\hookrightarrow$  Quando, entretanto, o intervalo de tempo tende a zero (i.e $\Delta t \rightarrow 0)$ temos o que chamaos de velocidade instantânea:

$$
v = \lim _{\Delta t \rightarrow 0}\frac{\Delta s}{\Delta t} = \frac{ds}{dt} = \dot s
$$

<aside>
<img src="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/yuru_camp.png" alt="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/yuru_camp.png" width="40px" /> Podemos observar que a velocidade é dada pelo deslocamento sobre o intervalo de tempo $\therefore$  se o deslocamento for negativo temos que a velocidade também será negativa.

</aside>

$\hookrightarrow$  De forma análoga ao que acontece na velocidade, a aceleração média é a variação da velocidade no intervalo do tempo:

$$
a_{med} = \frac{\Delta  v}{\Delta t}
$$

$\hookrightarrow$  E quando $\Delta t \rightarrow 0$ temos a chamada aceleração instantânea, dada por:

$$
a = \frac{dv}{dt} = \dot v = \ddot{s}
$$

<aside>
<img src="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Evangelion.gif" alt="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Evangelion.gif" width="40px" /> Ao contrário da velocidade, entretanto, a aceleração tera o sinal positivo se a velocidade estiver crescendo em módulo e negativa se estiver diminuindo em módulo

</aside>

$\hookrightarrow$  Mexendo um pouco nas equações acima temos a equação mais importante de cinemática, dada por:

$$
\boxed{v \ dv = a \ ds}
$$

$\hookrightarrow$  Que também pode ser escrita como:

$$
\boxed{\dot s \ \  d\dot s  = \ddot s \ \ ds}
$$

## Principais Fórmulas

### Aceleração Constante

- Temos:

$$
\begin{aligned}
v &= v_0 + at \\ 
v^ 2&= v_0^2 + 2a(s-s_0)
\end{aligned}
$$

- Além de:

$$
s = s_0 + v_0t + \frac{1}{2}at^2
$$

### Aceleração Dada como uma Função do Tempo

- Temos:

$$
\begin{aligned}
v &= v_0 + \int^t_0 a(t) dt \\ 
s &= s_0 + \int^t_0 vdt
\end{aligned}
$$

### Aceleração Dada como uma Função da Velocidade

- Temos:

$$
s = s_0 + \int^v_{v_0} \frac{v}{a(v)} dv
$$

<aside>
<img src="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Hifumi_Surprised.png" alt="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Hifumi_Surprised.png" width="40px" /> Para os casos onde queremos a velocidade em função do tempo e nós temos aceleração em função do tempo podemos simplesmente fazer $\frac{dv}{dt} = a(t)$, separar os termos $v$ e $t$ e integrar.

</aside>

### Aceleração Dada como uma Função do Deslocamento

- Temos:

$$
v^2 = v_0^2 + 2\int^s_{s_0} a(s) ds
$$

# Movimento Curvilíneo Plano

## Velocidade

$\hookrightarrow$ Para movimentos curvilíneos é importante analisarmos sua trajetória a partir de um referencial pré-definido que chamaremos de $O$, como na imagem ao lado.

$\hookrightarrow$ Através da figura podemos ver que a velocidade média é dada por:

![Screen Shot 2022-04-23 at 9.27.27 AM.png](Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Screen_Shot_2022-04-23_at_9.27.27_AM.png)

$$
\vec V_{med} = \frac{\Delta \vec r}{\Delta t}
$$

$\hookrightarrow$ Que é um vetor com direção de $\Delta \vec r$ e cujo o módulo é $|\Delta \vec r|/\Delta t$

$\hookrightarrow$ Além disso temos o que chamamos de velocidade escalar média, dada por $\Delta s / \Delta t$, que como o nome indica é um escalar.

$\hookrightarrow$ As duas velocidades supracitadas tendem a ser igual em módulo conforme $\Delta t \rightarrow 0$ $\therefore |\Delta \vec r| \rightarrow \Delta s$

$\hookrightarrow$ Quando $\Delta t \rightarrow 0$ temos a velocidade instantânea:

$$
\vec V = \frac{d \vec r}{dt} = \dot{\vec r}
$$

$\hookrightarrow$ Cujo seu módulo damos o nome de velocidade escalar:

$$
v = |\vec V| = \frac{ds}{dt} = \dot s
$$

## Aceleração

$\hookrightarrow$ A aceleração também é um vetor, tendo a mesma direção do vetor $\Delta \vec V$.

$\hookrightarrow$ Tendo como valor:

$$
\vec a = \frac{d \vec V}{dt} = \dot{\vec V} = \ddot{\vec r}
$$

$\hookrightarrow$ Como podemos ver, a aceleração é dependente da variação da velocidade que, por sua vez, é uma grandeza vetorial $\therefore$  a aceleração depende não somente da mudança em módulo da velocidade mas também da mudança de sentido.

<aside>
<img src="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Evangelion%201.gif" alt="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Evangelion%201.gif" width="40px" /> A Aceleração de uma partícula em movimento curvilíneo não é nem tangencial nem normal a trajetória → mas a componente normal aponta para o centro de curvatura da trajetória

</aside>

## Coordenadas

$\hookrightarrow$ Iremos estudar principalmente 3 sistemas de coordenadas  diferentes para solucionarmos problemas de movimento curvilíneo.

$\hookrightarrow$ O grande desafio será escolher quando cada um é mais adequado para ser utilizado.

### Coordenadas Retangulares

- Este sistema de coordenadas é útil para a descrição de movimentos onde as componentes $x$e $y$ da aceleração são determinados independentemente.
- Possui a seguinte representação vetorial:

$$
\boxed{
\begin{aligned}
\vec r = x \hat i + y \hat j \\ 
\vec V= \dot{\vec r} = \dot x \hat i + \dot y \hat j \\ 
a = \dot{\vec V} = \ddot{\vec r} = \ddot x \hat i + \ddot y \hat j
\end{aligned}}
$$

- Resultando nas seguintes equações (relembrando as operações de vetores de algebra linear):

$$
\begin{aligned}
v = \sqrt{v_x^2 + v_y^2} \\ 
a = \sqrt{a_x^2 + a_y^2}
\end{aligned}
$$

- Além disso, é importante relembrarmos a relação entre o ângulo entre os vetores velocidade:

$$
\tan \theta = \frac{v_y}{v_x}
$$

### Coordenadas Tangencial e Normal

- Como o próprio nome diz, essa coordenada é composta de uma componente que é tangencial ao movimento e uma que é normal, apontando para o interior da curvatura.
- Utilizado principalmente em problemas de Movimento Circular.
- Isso é uma representação muito natural $\therefore$ muito usada.
    
    ![Screen Shot 2022-04-23 at 2.25.50 PM.png](Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Screen_Shot_2022-04-23_at_2.25.50_PM.png)
    

**Velocidade e Aceleração**

- Antes de introduzirmos a velocidade e a aceleração nesse novo sistema de coordenadas é importante introduzirmos dois novos vetores unitários:

$$
\begin{cases}
\hat e_t & \rightarrow & Direção \ Tangencial \\ 
\hat e_n & \rightarrow & Direção \ Normal 
\end{cases}
$$

- Com isso temos:

$$
\boxed{\begin{aligned}
\vec V &=\rho \dot \beta \hat e_t \\  
\vec a &= \frac{v^2}{\rho}\hat{e}_n + \dot v \hat{e_t}
\end{aligned}}
$$

- Onde:
    
    $\hookrightarrow$ $\rho$ → Raio de curvatura
    
    $\hookrightarrow$ $\beta$ → Angulo em Radianos
    

- E por conseguinte:

$$
a = \sqrt{a_n^2 + a_t^2}
$$

<aside>
<img src="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Hifumi_Surprised%201.png" alt="Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Hifumi_Surprised%201.png" width="40px" /> Podemos ainda calcular $a_t$ derivando em respeito a $t$ a fórmula da velocidade, que, através da regra do produto: $a_t = \dot \rho \dot \beta + \rho \ddot \beta$

</aside>

**Movimento Circular**

- Esse tipo de coordenada é usado principalmente em movimentos circulares (i.e onde $\rho$, raio de curvatura, é constante).
- Com isso temos as seguintes fórmulas:

$$
\boxed{\begin{aligned}
v &= r \dot \theta \\ 
a_n &=\frac{v^2}{r} = r\dot \theta^2 = v\dot \theta \\ 
a_t &= \dot v = r \ddot \theta
\end{aligned}}
$$

### Coordenadas Polares

- Neste tipo de coordenada nós localizamos o ponto através de uma distância radial $r$ e um  angulo $\theta$.
- Essa coordenada é especialmente útil ando o movimento é restringido por meio do controle de uma distância radia e de uma posição angular ou quando o movimento sem restrição é observado por medida de distância radia e posição angular.

**Velocidade**

- Podemos dividir em duas velocidades:

$$
\boxed{
\begin{aligned}
v_r &= \dot r \\
v_\theta &= r\dot\theta
\end{aligned}}
$$

**Aceleração**

- De forma análoga à velocidade, podemos também separar em duas componentes a aceleração:

$$
\boxed{
\begin{aligned}
a_r &= \ddot r - r \dot\theta^2 \\ 
a_\theta &= r\ddot\theta + 2 \dot r \dot\theta
\end{aligned}}
$$

### Coordenadas Cilíndricas

- Análogo as coordenadas polares mas em 3D.
- Possui 3 velocidades e 3 acelerações, sendo elas:
    - $V_z$ → Velocidade no sentido $Z$ (i.e de subida) no cilindro
    - $V_\theta$ → Velocidade de "giro” no cilindro
    - $V_r$ → Velocidade de mudança do raio tendo como referência o centro do cilindro

$$
\boxed{\begin{aligned}
v_r &= \dot r \\ 
v_\theta &= r \dot \theta \\ 
v_z &= \dot z \\ 
\end{aligned}}
$$

$$
\boxed{\begin{aligned}
a_r &= \ddot r - r \dot\theta ^2 \\ 
a_\theta &= r \ddot\theta + 2\dot r \dot \theta \\ 
a_z &= \ddot z
\end{aligned}}
$$

### Coordenadas Esféricas

- Também para 3 dimensões, é composta por um raio e dois ângulos, sendo eles:
    - $\theta$ → Ângulo no plano $x-y$
    - $\phi$ → Ângulo do plano $x-y$ para o objeto a uma altura $z$
    
    ![Screen Shot 2022-04-24 at 4.20.13 PM.png](Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Screen_Shot_2022-04-24_at_4.20.13_PM.png)
    

# Movimento Relativo

$\hookrightarrow$ A coisa mais importante do movimento relativo é lembrar que precisamos somar VETORIALMENTE.

$\hookrightarrow$ As principais fórmulas são para Velocidade e Aceleração relativa entre dois referenciais, dada por:

$$
\vec V_B = \vec V_A + \vec V_{B|A} \\ 
\vec a_B = \vec a_A + \vec a_{B|A}
$$

$\hookrightarrow$ Onde lemos $B|A$ → "De $B$ no referencial $A$” $\therefore$ lemos a primeira fórmula como: "A velocidade de B é igual a soma vetorial da velocidade do referencial $A$ com a velocidade de $B$ no referencial $A$”.

# Movimento Restrito de Partículas Conectadas

## Um Grau de Liberdade

$\hookrightarrow$ Para casos com um grau de liberdade o que precisamos fazer é analisar o diagrama (como o ao lado) e achar uma expressão para o comprimento total do cabo $L$ que conecta as partículas.

$\hookrightarrow$ A partir dessa expressão de $L$ podemos derivar e ficar em função de somente as outras variáveis não constantes (nesse caso seria $x$ e $y$).

![Screen Shot 2022-04-24 at 5.12.41 PM.png](Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Screen_Shot_2022-04-24_at_5.12.41_PM.png)

## Dois Graus de Liberdade

$\hookrightarrow$ De forma análoga ao como foi feito para o sistema com um grau de liberdade, para 2 (ou mais) graus de liberdade precisamos fazer uma equação de comprimento para cada corda envolvida, mas nós só "medimos” da carga até novas polias.

$\hookrightarrow$ No caso ao lado teremos duas equações.

$\hookrightarrow$ Nessa caso podemos simplesmente desconsiderar o tamanho de corda que passa pelas polias.

![Screen Shot 2022-04-24 at 5.20.28 PM.png](Cinema%CC%81tica%20de%20Parti%CC%81culas%20d63bf620dd844a0d8bf5ed5e876e973c/Screen_Shot_2022-04-24_at_5.20.28_PM.png)