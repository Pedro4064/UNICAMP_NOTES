# Potencial Elétrico

Capítulo: 24
Semana: Semana 4

# Energia Potencial e Trabalho

Quando tratamos de energia potencial e trabalho, existem três situações possíveis:

1. Cargas espalhadas no espaço 
2. Dipolo elétrico;
3. Densidade de carga.

## 1. Cargas Espalhadas no Espaço

### Energia Potencial

Quando há somente duas cargas interagindo, podemos calcular a energia potencial da seguinte forma:

![Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Screen_Shot_2020-10-19_at_5.13.55_PM.png](Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Screen_Shot_2020-10-19_at_5.13.55_PM.png)

$$
U = K \frac{Qq}{r}
$$

<aside>
<img src="Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/a6ada7178c8b6b762e47f8ff1f841cfa.gif" alt="Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/a6ada7178c8b6b762e47f8ff1f841cfa.gif" width="40px" /> Muito parecido com o calculo da força, mas o denominador é elevado somente a um (em contra partida na lei de Coulomb a distância é ao quadrado)

</aside>

Nos exercícios, entretanto, é muito comum a interação entre mais de duas cargas, quando esse é o caso, precisamos entender que a energia potencial se dá através da interação de um par cargas (como explicitado na equação de $U$), logo precisamos observar e interpretar o sistema proposto duas cargas de cada vez. No final, a energia potencial elétrica total do sistema seria a soma aritmética das energias potenciais de cada par.

![Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Untitled.png](Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Untitled.png)

$$
U = k\frac{q_1q_2}{r_{12}} + k\frac{q_1q_3}{r_{13}} + k\frac{q_2q_3}{r_{23}}
$$

### Trabalho

A definição de trabalho é:

$$
W = \Delta E_{cinética} = -\Delta U
$$

## 2. Dipolo Elétrico

### Energia Potencial

Precisamos, primeiramente, relembrar o que é o momento de dipolo elétrico:

![Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Untitled%201.png](Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Untitled%201.png)

$\vec{p} = q\vec{d}$

Para acharmos a energia potencial armazenada no dipolo temos que:

$$
U = -\vec{p} \cdot\vec{E} = -pE\cos{\theta}
$$

Que consiste no produto escalar entre o negativo do momento de dipolo e o campo elétrico.

Quando você coloca um dipolo numa região com campo externo uniforme $\vec{E}$, o dipolo tende a girar (pois gera torque). Se você manter esse dipolo fixo, haverá um armazenamento de energia potencial na configuração abaixo:

 

![Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Untitled%202.png](Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/Untitled%202.png)

### Trabalho

Trabalho Continua sendo $-\Delta U$

## 3.Densidade de Carga

A densidade de energia ($u$) é :

$$
 u = \frac{\epsilon_0|E|^2}{2}
$$

> A densidade de energia é a quantidade infinitesimal de energia sobre uma unidade infinitesimal de volume do espaço.
> 

Ou seja:

$$
u = \frac{dU}{dV}
$$

### Exemplo

Dado um campo elétrico de uma esfera condutora carregada de raio $R$:

$$
\vec{E}= \frac{kQ}{r^2} \:\:|\:\:r>R
$$

Para encontrarmos a energia armazenada por essa carga em todo espaço:

$$
\frac{dU}{dV} = \frac{\epsilon_0|E|^2}{2} \rightarrow dU = \frac{\epsilon_0}{2} |E|^2dV
$$

$$
U = \frac{\epsilon_0}{2}\int_{V} |E|^2 dV
$$

# Potencial Elétrico gerado por Carga Pontual

$$
\Delta V = -\int\vec{E}\cdot d\vec{r}
$$

- É uma propriedade que depende somente do campo externo.

<aside>
<img src="Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/8026_Anime_Surprised.png" alt="Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/8026_Anime_Surprised.png" width="40px" /> Definimos nosso potencial de referência como sendo $0$ no infinito $\infty$.

</aside>

<aside>
<img src="Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/LewdMegumin.png" alt="Potencial%20Ele%CC%81trico%2078cbbf63af864bddb9c0e7db5c981322/LewdMegumin.png" width="40px" /> Podemos ainda definir o potencial sendo $V = \frac{kq}{r}$

</aside>

### Exemplo:

- Um campo é dado como: $\vec{E} = k\frac{Q}{r^2}\hat{r}$, calcule o potencial em um ponto arbitrário $r$ onde nossa carga está.
    
    
    Para calcularmos precisamos saber ao menos o potencial em um ponto, e para isso usamos o infinito como sendo 0.
    
    $$
    \begin{aligned}
    \Delta V &= -\int_{\infty}^{r} \vec{E}\cdot d\vec{x} \\
    
    V(x) - V(0) &= -\int_{\infty}^{r} \vec{E}\cdot d\vec{x} \\
    
    V(x) - 0 &= -\int_{\infty}^{r} (k\frac{q}{x^2})\cdot d\vec{x} \\
    
    V(x)  &= -kq\int_{\infty}^{r} \frac{dx}{x^2}\\
    
    V(x)  &= -kq(x^{-1})\\
    \end{aligned}
    $$
    
    ## Campo Elétrico a Partir do Potencial
    
    $$
    \vec{E} = -\nabla V \Rightarrow \nabla V = <\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z}>
    $$