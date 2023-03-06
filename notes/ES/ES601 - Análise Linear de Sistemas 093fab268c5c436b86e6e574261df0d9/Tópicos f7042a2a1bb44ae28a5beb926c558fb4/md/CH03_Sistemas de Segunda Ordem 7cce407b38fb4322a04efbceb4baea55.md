# Sistemas de Segunda Ordem

Created: August 25, 2022 4:10 PM

[Anotações de Aula](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Anotac%CC%A7o%CC%83es%20de%20Aula%20f1f42d977d6e4b859d420fff2fed867d.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Vimos anteriormente sistemas físicos os quais eram modelados por equações diferenciais ordinárias de primeira ordem (os mais notórios circuitos elétricos $RC$).

$\hookrightarrow$ Iremos analizar, agora, sistemas físicos que necessitam de EDO$_s$ de **segunda ordem** para serem modelados, além de algumas técnicas para sua resolução e análise.

$\hookrightarrow$ Algo importante de ser dito é que iremos utilizar sistemas mecânicos como uma forma de exemplificação e motivação para sistemas de segunda ordem, mas que tais sistemas são estudados mais a fundo em outras matérias (principalmente Dinâmica e Sistemas de Vibrações).

# Sistema de Segunda Ordem - Sistemas Mecânicos Translacionais

## Componentes Mecânicos e suas Modelagens

$\hookrightarrow$ Antes de entrarmos na modelagem de sistemas como um todo, é de suma importância nos familiarizarmos com os principais componentes/modelos matemáticos utilizados em sistemas mecânicos.

### Molas

![Sistema de Mola Ideal](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-08-25_at_4.25.01_PM.png)

Sistema de Mola Ideal

- O primeiro componente de um sistema mecânico que vamos analizar é a mola.
- A mola apresenta duas principais características que precisam ser levadas em consideração quando a analisamos, sendo elas:
    1. **Rigidez $k$** → É uma característica Física da mola.
    2. **Posição da Mola sem carga** → O tamanho, a partir da ponta da mola (mas que também pode ser a partir de outro referencial) em que a mola está sem nenhuma deformação.
- A partir da lei de Hooke sabemos que a **forçada de restauração**, i.e a força de reação a uma certa deformação, é proporcional ao deslocamento de tal deformação $x$ e a rigidez da mola em análise $k$, resultando em:
    
    $$
    \begin{align}
    F = kx
    \end{align}
    $$
    

### Amortecedores Viscosos

![Amortecedor Ideal](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-08-25_at_4.37.07_PM.png)

Amortecedor Ideal

- O segundo mecanismos que iremos analizar é o amortecedor viscoso.
- Análogo à mola, o amortecedor possui algumas propriedades que são importantes durante sua análise:
    1. **Coeficiente de Amortecimento $c$** → Característica física do amortecedor.
- Além do coeficiente de amortecimento, a força de resistência aplicada pelo amortecedor também é dependente da velocidade da massa, resultando na seguinte fórmula:
    
    $$
    \begin{align}
    F = c\dot x
    \end{align}
    $$
    

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> **IMPORTANTE**: A velocidade que precisa ser levada em consideração é a velocidade relativa entre o “êmbolo” e o “corpo” do amortecedor, no nosso exemplo acima como o corpo do amortecedor está ligado a parede $\therefore$ ele está parado, com velocidade 0. Se possuísse uma velocidade $v$, e o êmbolo tivesse uma velocidade $V$, com $V > v$ temos que ficaria $F = c(V-v)$

</aside>

### Massas

![Princípio Fundamental da Dinâmica](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-08-25_at_4.51.46_PM.png)

Princípio Fundamental da Dinâmica

- A última coisa que é importante de ser revisada é a massa, juntamente com a segunda lei de Newton, que nos diz que a força resultante $F$ em um corpo de massa $m$ (que podemos interpretar como sendo a **inércia do corpo**) irá resultar em uma aceleração $a$. Dada pela seguinte equação:
    
    $$
    \begin{align}
    F = ma
    \end{align}
    $$
    

## Sistema Massa Mola

$\hookrightarrow$ Supondo um sistema simples composto por uma massa pendurada a uma mola, como mostrado na imagem ao lado.

$\hookrightarrow$ Onde $k$ representa a rigidez da mola e $\Delta$  representa o deslocamento em um certo momento $t$ tendo como referência a posição natural da mola sem carga.

![Sistema Massa Mola em um estante $t$](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-08-25_at_5.19.08_PM.png)

Sistema Massa Mola em um estante $t$

![$DCL$ do corpo em análise](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-08-25_at_5.21.28_PM.png)

$DCL$ do corpo em análise

$\hookrightarrow$ O primeiro passo para qualquer análise mecânica é a realização do $DCL$ (i.e diagrama de corpo livre), onde é feito um diagrama somente com os corpos de interesse, que em questão é a massa $m$. Além disso é incluindo no nosso diagrama todas as forças externas que são aplicadas (no nosso caso a força peso $F_p$ e a força de restauração elástica $F_e$).

$\hookrightarrow$ Algo que é de suma importância de ser estabelecido, ao se fazer um $DCL$ é o / os referenciais que são utilizados. Não há somente um referencial possível de ser escolhido, mas é imprescindível que tal referencial seja respeitado durante toda a análise.

$\hookrightarrow$ A partir do $DCL$, e do fato de que o corpo está em movimento com uma aceleração $\ddot\Delta$ , temos pela 2º Lei de Newton:

$$
\begin{align}
mg - k\Delta = m\ddot\Delta
\end{align}
$$

$\hookrightarrow$ Rearranjando a equação acima para facilitar nossa análise, temos:

$$
\begin{align}
\ddot\Delta + \frac{k}{m}\Delta = g
\end{align}
$$

$\hookrightarrow$ Que é uma Equação Diferencial Ordinária Linear de Segundo Grau Não Homogênea.

$\hookrightarrow$ Além disso, em matérias de mecânica nós chamamos $\sqrt{k/x}$ de frequência natural do sistema, denotado pela letra $\omega_n$, a qual representa a frequência de oscilação do sistema naturalmente (i.e caso não haja nenhuma força de dissipação/amortecimento ). Com isso podemos reescrever a equação acima em função da frequência natural:

$$
\begin{align}
\ddot \Delta  + \omega_n^2 \Delta = g
\end{align}
$$

$\hookrightarrow$ Com a modelagem do sistema feita, basta resolvermos a equação diferencial ordinária de segunda ordem, que veremos mais adiante.

## Sistema Massa Mola Amortecedor

![Screen Shot 2022-08-31 at 4.34.35 PM.png](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-08-31_at_4.34.35_PM.png)

$\hookrightarrow$ Para um sistema massa mola amortecedor, como o mostrado a cima, temos:

- Mola → Com força elástica de restauração proporcional ao deslocamento $x$.
- Amortecedor → Com força contrária ao movimento proporcional à derivada no tempo do deslocamento (i.e a velocidade) $\dot x$.

$\hookrightarrow$ Ao fazermos o DCL, considerando, pela lei de Newton, que a força resultante é igual à massa ($m$) vezes a aceleração resultante do sistema ($\ddot x$) temos a equação diferencial não homogênea que rege o comportamento do sistema:

$$
\begin{align}
m\ddot x + c\dot x + kx = p(t)
\end{align}
$$

$\hookrightarrow$ Essa equação, entretanto, pode ser reescrita na forma padrão de uma equação diferencial de segundo grau, que nos proporcionará uma análise sobre o comportamento do sistema de forma mais direta:

$$
\begin{align}
\ddot x(t) + 2\zeta \omega _n\dot x(t) + \omega^2_nx(t) = g(t)
\end{align}
$$

$\hookrightarrow$ Onde:

- $\zeta = c/(2\sqrt{ km})$ → Chamado de "Fator de Amortecimento” (ou damping factor).
- $\omega_n = \sqrt{k/m}$     → Chamado de "Frequência Natural”
- $g(t) = p(t) /m$   → Chamado de Fator Excitante/ Fator Forçante

# Solução de Sistemas de Segunda Ordem

$\hookrightarrow$ A forma mais fácil de solucionar sistemas de segunda ordem é, analogamente ao de primeira ordem, partindo de um formato da solução desejada.

$\hookrightarrow$ Vimos que para sistemas de primeira ordem a forma desejada, para a homogênea, era:

$$
y_h(x) = Ae^{\lambda t}
$$

$\hookrightarrow$ E a forma para não homogênea era:

$$
y = y_h + y_p
$$

$\hookrightarrow$ Onde $y_p$ é uma solução particular da mesma forma do fator excitante.

$\hookrightarrow$ Já para sistemas de segunda ordem teremos, até mesmo para de equações homogêneas, duas possíveis formas para nossa solução. Isso se deve ao fato de que, para cada caso, uma forma é mais útil para a análise linear da resposta do sistema.

$\hookrightarrow$ As formas depende se o fator de primeira ordem da EDO (i.e o valor de primeira derivada $\dot x$) é nulo ou não (se está presente ou não na EDO).

## Solução Homogênea

### Termo de Primeira Ordem Nulo

$\hookrightarrow$ Considerando uma equação diferencial de segunda ordem homogênea (homogênea pois o fator forçante é nulo), mas com o fator de primeira ordem (i.e $\dot x$ ) não presente na EDO, da forma:

$$
\ddot x + \omega^2_nx = 0
$$

$\hookrightarrow$ E com as condições iniciais:

$$
x(0) = x_0 \ \ \ e \ \ \ \dot x(0) = \dot x_0
$$

$\hookrightarrow$ Vamos resolver analogamente a como resolvemos problemas homogêneos de sistemas de primeira ordem, assumindo um formato para a solução.

$\hookrightarrow$ No caso de sistemas homogêneos de segunda ordem, entretanto, assumimos a solução como tendo o formato:

$$
x(t) = Z \cos(\omega_n t + \phi)
$$

$\hookrightarrow$ Onde:

- $Z$  → Amplitude das oscilações
- $\omega_n$ → Frequência natural
- $\phi$   → Ângulo de fase

$\hookrightarrow$ Sabendo o formato geral da solução nós:

1. **Substituímos na EDO**: Ao substituir na EDO nós vamos achar alguns dos fatores listados acima, resultando na Solução Geral da EDO (que será útil caso venhamos resolver a mesma EDO mas não homogênea).
2. **Substituímos os Valores Iniciais**: Sobrarão ainda duas variáveis não descobertas, para tal usamos as duas condições iniciais. No caso de sistemas de segunda ordem, ao utilizar os valores inicias, é muito comum precisar da identidade $\cos ^2 + \sin^2 = 1$ para isolar as variáveis, então é importante lembrar.

<aside>
<img src="https://www.notion.so/icons/thinking_purple.svg" alt="https://www.notion.so/icons/thinking_purple.svg" width="40px" /> Observação: Nós utilizamos o formato como sendo coseno, mas na realidade poderíamos resolver tomando como formato a exponencial (mas seria mais difícil pois envolveria números imaginários), levando em consideração a identidade de Euler.

</aside>

- Exemplo
    
    

### Termo de Primeira Ordem Não Nulo

$\hookrightarrow$ Para casos onde o termo de primeira ordem não é nulo, a primeira coisa que precisamos fazer é **botá-la no formato padrão**:

$$

\ddot x(t) + 2\zeta \omega _n\dot x(t) + \omega^2_nx(t) = 0

$$

$\hookrightarrow$ Precisamos, então, **supor** que o **resultado da nossa** **EDO tem o formato**:

$$
x(t) = e^{\lambda t}
$$

$\hookrightarrow$ Ao **substituirmos** tal valor na nossa EDO encontraremos:

$$
(\lambda^2)e^{\lambda t} + (2\zeta \omega_n \lambda )e^{\lambda t} + (\omega_n^2) e^{\lambda t} = 0
$$

$\hookrightarrow$ Para facilitar nossa análise, isolamos e agrupamos $e^{\lambda t}$, resultando em:

$$
(\lambda^2 + 2\zeta \omega_n \lambda + \omega_n^2) e^{\lambda t} = 0
$$

$\hookrightarrow$ Como $e^{\lambda t}$ é uma exponencial e nunca pode ser zero, temos então que:

$$
\lambda^2 + 2\zeta \omega_n \lambda + \omega_n^2= 0
$$

$\hookrightarrow$ Que nada mais é que uma equação de segundo grau, a qual, através de Bhaskara, teremos os **possíveis valores de lambda**:

$$
\lambda_1 = -\zeta\omega_n +\omega_n\sqrt{\zeta^2 - 1} \ \ \ \ \ \lambda_2 = -\zeta\omega_n -\omega_n\sqrt{\zeta^2 - 1}
$$

$\hookrightarrow$ A partir disso, podemos classificar nosso sistema a partir do valor do fator de amortecimento (damping factor) $\zeta$, pois é o termo que rege o comportamento das raizes da equação de segundo grau vista acima:

- $\zeta < 1$ → Sistema sub-amortecido, com 2 raizes imaginárias
- $\zeta > 1$ → Sistema Super-amortecido, com 2 raizes reais
- $\zeta = 1$ → Sistema Criticamente Amortecido, com 1 raiz real

$\hookrightarrow$ E para cada casos acima teremos uma forma para a nossa EDO.

<aside>
<img src="https://www.notion.so/icons/thinking_purple.svg" alt="https://www.notion.so/icons/thinking_purple.svg" width="40px" /> **Observação**: Na próxima parte iremos interpretar mais detalhadamente o comportamento do sistema para cada tipo de categoria do fator de amortecimento através de gráficos, etc. Então não se preocupe muito, no momento o importante é botar a EDO no formato descrito acima para podermos resolve-la.

</aside>

<aside>
<img src="https://www.notion.so/icons/thinking_purple.svg" alt="https://www.notion.so/icons/thinking_purple.svg" width="40px" /> **Observação**: Até agora, a substituição pelo formato geral $e^{\lambda t}$ é para acharmos os $\lambda$, é a partir de agora que iremos substituir novamente a função, que dependera do fator de amortecimento, na nossa EDO para acharmos finalmente a solução.

</aside>

- **Sistema Super-Amortecido** $\zeta > 1$
    - A partir do calculo de $\lambda_1$ e $\lambda_2$, iremos assumir o formato da solução da nossa EDO como sendo:
        
        $$
        x(t) = Ae^{\lambda_1t} + Be^{\lambda_2t}
        $$
        
    - Substituímos então tal forma, com os valores de $\lambda_1$ e $\lambda_2$ calculados anteriormente, nos valores da condição inicial, que resultará em um sistema:
        
        $$
        \begin{cases}
        x(0) &\rightarrow x_0 = A + B \\ 
        \dot x(0) &\rightarrow \dot x_0 = A\lambda_1  + B\lambda_2
        \end{cases} \Rightarrow 
        
        \begin{bmatrix}
        x_0 \\
         \dot x_0
        \end{bmatrix}
         = \begin{bmatrix}1 & 1 \\ \lambda _1 & \lambda _2\end{bmatrix} \begin{bmatrix}A \\ B\end{bmatrix}
        $$
        
    - Utilizando a propriedade de matriz inversa $A^{-1} A = I$ na matriz que contem $\lambda_1$ e $\lambda_2$ (e no outro lado da equação para mater a igualdade), conseguimos isolar a matriz que contem $A$ e $B$, que é o que queremos, resultando em:
        
        $$
        \begin{bmatrix}
        A \\
        B
        \end{bmatrix} = \frac{1}{\lambda_2 - \lambda_1}\begin{bmatrix}\lambda_2  & -1 \\ -\lambda_1 & 1\end{bmatrix}\begin{bmatrix}x_0 \\ \dot x_0\end{bmatrix}
        $$
        
    - Resultando em:
        
        $$
        A = \frac{\dot x_0 - \lambda_2 x_0}{\lambda_1 - \lambda_2} \ \ \ e \ \ \ B = \frac{- \dot x_0 - \lambda_1 x_0}{\lambda_1 - \lambda_2}
        $$
        
- **Sistema Sub-Amortecido** $\zeta < 1$
    - Como dito anteriormente, para $\zeta < 1$ teremos duas raizes imaginárias.
    - Para esse caso, temos que a solução terá o mesmo formato da solução para o sistema super-amortecido:
        
        $$
        x(t) = Ae^{\lambda_1t} + Be^{\lambda_2t}
        $$
        
    - Com:$\begin{aligned}
    
    \end{aligned}$
    
    $$
    \begin{aligned}
    A &= \frac{\dot x_0 + (\zeta \omega _n + j \omega_d)x_0}{2j\omega_d} \\
    B &= \frac{-\dot x_0 + (\zeta \omega _d - j \omega_n)x_0}{2j\omega_d}
    \end{aligned}
    $$
    
    - Onde:
        
        $$
        \omega_d = \omega_n\sqrt{1-\zeta^2}
        $$
        
    - Chamada de Frequência Natural Amortecida
- **Sistema Criticamente-Amortecido** $\zeta = 1$
    - Para esse caso, as duas raizes são iguais, i.e:
        
        $$
        \lambda_1 = \lambda_2 = -\omega_n
        $$
        
    - Tendo então, como solução geral:
        
        $$
        x(t) = Ae^{\lambda t} + Bte^{\lambda t}
        $$
        
    - Com:
        
        $$
        \begin{aligned}
        A &= x_0 \\ 
        B &= \dot x_0 + \omega_n x_0
        \end{aligned}
        $$
        
    

## Solução Não Homogênea

$\hookrightarrow$ O procedimento para achar a solução de equações não homogêneas de segundo grau é o mesmo de primeiro grau, onde nós supomos que a solução é a soma da solução particular e homogênea:

$$
x(t) = x_h(t) + x_p(t)
$$

$\hookrightarrow$ Onde a forma homogênea foi dada na parte anterior, e a solução particular nós supomos o mesmo formato do termo excitante/forçante.

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> IMPORTANTE: É de suma importância lembrar que, ao calcular a homogênea, nós usamos a mesma forma geral da homogênea (até o ponto onde se calcula as raízes $\lambda_1$ e $\lambda_2$, mas não até onde se calcula $A$ e $B$, pois eles serão calculados em conjunto com a solução particular, ao se substituir os valores inicias)

</aside>

# Interpretação de Sistemas de Segunda Ordem

$\hookrightarrow$ A forma mais direta de interpretarmos sistemas de segunda ordem é pelo valor de seu $\zeta$, chamado de fator de amortecimento ou ainda damping factor.

$\hookrightarrow$ Ele nos permite analizar o comportamento do sistema na fase transiente até atingir o estado permanente.

$\hookrightarrow$ Quando um sistema é sub-amortecido, com $\zeta < 1$ ele demora a convergir a um valor por ter um overshoot muito grande, sendo que com $\zeta = 0$ ele tende a ficar oscilante indefinidamente.

$\hookrightarrow$ Já para sistemas super-amortecidos, com $\zeta > 1$,  ele tende a um número sem "overshoot”.

$\hookrightarrow$ Em contra partida, sistemas criticamente amortecidos, com $\zeta = 1$, há a presença de overshoting, mas não tanto quanto um sistema sub-amortecido.

![Screen Shot 2022-09-01 at 4.15.29 PM.png](Sistemas%20de%20Segunda%20Ordem%207cce407b38fb4322a04efbceb4baea55/Screen_Shot_2022-09-01_at_4.15.29_PM.png)