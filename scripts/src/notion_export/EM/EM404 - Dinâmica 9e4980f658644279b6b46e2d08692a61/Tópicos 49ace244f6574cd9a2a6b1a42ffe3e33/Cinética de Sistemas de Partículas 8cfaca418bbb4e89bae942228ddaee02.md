# Cinética de Sistemas de Partículas

Created: May 3, 2022 4:33 PM
Prova: P2

[Anotações de Aula](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Anotac%CC%A7o%CC%83es%20de%20Aula%202e372aee5d9b4784895e45487da83e5a.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Até o momento nós estudamos a cinética e a cinemática de somente uma partícula (ou então de duas partículas sob um único sistema para as análises de trabalho e energia cinética).

$\hookrightarrow$ Agora iremos, entretanto, trabalhar com um sistema de várias partículas, o que será de suma importância e servirá como ponte para o estudo de sistemas de corpos rígidos e não rígidos.

# Segunda Lei de Newton Generalizada

$\hookrightarrow$ Para generalizarmos a segunda Lei de Newton nós precisamos primeiro definir o centro de massa de um sistema, que é localizado pelo vetor $\bar r$ e que é dado a partir de:

![Screen Shot 2022-05-03 at 4.39.28 PM.png](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Screen_Shot_2022-05-03_at_4.39.28_PM.png)

$$
CG = m\bar r = \sum m_ir_i
$$

$\hookrightarrow$ Logo temos que a generalização da segunda lei de newton é:

$$
F_{resultante} = m  \ddot{\bar r} = m \bar a
$$

$\hookrightarrow$ Onde $\bar a$ é a aceleração do centro de massa do sistema de partículas.

$\hookrightarrow$ Podemos ainda expressar o princípio de movimento de centro de massa em componentes dada por:

$$
\begin{aligned}
\sum F_x &= m\bar a_x \\ 
\sum F_y &= m\bar a_y \\ 
\sum F_z &= m\bar a_z
\end{aligned}
$$

# Trabalho-Energia Para um Sistema de Partículas

## Relação Trabalho-Energia

$\hookrightarrow$ Para o sistema de várias partículas como um todo a relação de trabalho e energia vista anteriormente se mantém:

$$
\sum U_{1-2} = \sum \Delta K
$$

$\hookrightarrow$ Onde $\sum U_{1-2}$ representa a soma de todo o trabalho realizado pelas forças internas e externas sobre as partículas.

$\hookrightarrow$ Para um corpo rígido ou um sistema de corpos rígidos unidos por conexões ideais não há trabalho realizado por forças internas pois não haverá atrito.

$\hookrightarrow$ Se o sistema incluir membros elásticos capazes de armazenar energia temos que a equação acima deve incluir ao resultado da somatória dos trabalhos tanto a somatória da variação de energia cinética quanto, agora, a variação da energia potencial, resultando em:

$$
\sum U_{1-2} = \sum \Delta K + \sum \Delta V
$$

## Energia Cinética Para um Sistema de Partículas

$\hookrightarrow$ Se observarmos o somatório de energias cinéticas de forma que cada partícula está explícita teremos que:

$$
\sum K = \sum \frac{1}{2}m_iv^2_ i
$$

$\hookrightarrow$ Utilizando agora do conceito de velocidade relativa apresentada nos capítulos anteriores temos que a velocidade de cada partícula $i$ é dada por:

$$
\vec v_i = \vec{\bar v} + \dot{\vec\rho_i}
$$

$\hookrightarrow$ Onde:

- $\bar v$ → Velocidade do centro de massa
- $\dot \rho_i$ → Velocidade da partícula em análise $i$ com o referencial transladando junto com o centro de massa.

$\hookrightarrow$ Isso é a partir da fórmula de velocidade relativa:

$$
\vec V_A = \vec V_{A|B} + \vec V_{B}
$$

$\hookrightarrow$ Onde $V_A$ é a velocidade da partícula $i$, $V_{A|B}$ a velocidade da partícula em relação ao centro de massa e $V_B$
  a velocidade do centro de massa.

$\hookrightarrow$ Com isso temos que a fórmula final da energia cinética total é dada por:

$$
\boxed{T = \frac{1}{2}m \bar v^2 + \sum \frac{1}{2}m_i |\dot p_i|}
$$

# Impulso-Quantidade de Movimento Para um Sistema de Partículas

## Quantidade de Movimento Linear

$\hookrightarrow$ A partir do conceito de centro de massa temos que a quantidade de movimento linear total de um sistema de partículas será dada por:

$$
G = m\bar v
$$

$\hookrightarrow$ Onde:

- $m = \sum m_i$
- $\bar v$ → Velocidade do centro de massa

$\hookrightarrow$ Mantendo ainda que a derivada em respeito ao tempo da quantidade de movimento linear total é a força resultante:

$$
\sum F = \dot G
$$

## Quantidade de Movimento Angular

$\hookrightarrow$ Podemos agora determinar a quantidade de movimento angular tendo como referencial:

### Em torno de um Ponto Fixo $O$ → $H_O$

- Definimos a quantidade de movimento angular em torno de um ponto fixo $O$ como sendo o somatório dos momentos das quantidades de movimento linear entorno desse ponto, dado por:
    
    $$
    \vec H_O = \sum(\vec r_i \times m_i\vec v_i)
    $$
    
- Derivando em relação ao tempo temos:
    
    $$
    \begin{aligned}
    \dot {\vec H_O} &= \overbrace{\sum (\dot{\vec r_i} \times m_i\vec v_i)}^{dois \ vetores \ // \ \therefore \ 0} + \sum(\underbrace{\vec r \times m_i\dot{\vec{v}}}_{Momento}) \\ 
    
    &= \sum \vec M_O
    
    \end{aligned}
    $$
    

### Em torno do Centro de Massa $G$ → $H_G$

- Podemos definir a quantidade de movimento angular absoluta em torno do centro de Massa como:
    
    $$
    \vec H_G = \sum(\rho_i \times m_i \dot{\vec r_i})
    $$
    
- Mas podemos ainda representar a velocidade absoluta através das velocidades relativas $\vec{\dot r_i} = \vec{\dot{\bar r_i}}  + \vec{\dot{\rho _i}}$ tendo então a quantidade de movimento angular relativa:
    
    $$
    \vec H_G = \sum(\rho_i \times m_i \dot{\vec \rho_i})
    $$
    
- Derivando tanto uma quanto outra em relação ao tempo temos que:
    
    $$
    \begin{aligned}
    \dot{\vec{H_G}} &= \sum \vec\rho_i \times \vec F_i \\ 
    &= \sum \vec M_G
    \end{aligned}
    $$
    

### Em torno de um ponto arbitrário $P$ → $H_P$

- Temos que a quantidade de movimento em torno de um ponto arbitrário $P$ é composta pela quantidade de movimento angular de todas as partículas em torno do centro de massa $CG$ mais a quantidade de movimento angular do próprio $CG$ em torno desse ponto $\therefore$

$$
\vec H_P = \vec{H_G}+ \underbrace{\vec{\bar{\rho}} \times m \vec{\bar v}}_{H \ do \ CG}
$$

# Escoamento De Massa

## Escoamento Permanente de Massa

$\hookrightarrow$ A partir dos conceitos de quantidade de movimento somos capazes de estudar sistemas onde há fluxo de massas, mais especificamente aqueles onde a sua variação  de escoamento é permanente, isso é, a taxa de entrada mássica é igual a taxa de saída.

$\hookrightarrow$ A partir do fato do volume de controle estar em escoamento permanente de massa temos:

$$
\rho_1A_1v_1 = \rho_2A_2v_2 = m'
$$

$\hookrightarrow$ Onde:

- $\rho$    → Massa específica do fluido
- $A$   → Área de saída
- $v$    → Velocidade Normal a área de saída
- $m'$ → Escoamento permanente de massa

$\hookrightarrow$ Já para os estudos das forças que atuam nós podemos:

1. Isolar a mssa de fluido no interior do recipiente
2. Isolar o recipiente inteiro juntamente com o fluido no seu interior

$\hookrightarrow$ Onde usamos o primeiro volume de controle para descrever as forças entre o recipiente e o fluido e a segunda para descrever as forças externas ao recipiente.

$\hookrightarrow$ Nessa matéria iremos considerar a segunda abordagem, que será representado por um diagrama de corpo livre da massa dentro do volume de controle fechado definido pela superfície externa do recipiente e as superfícies de entrada e saída.

$\hookrightarrow$ A partir disso e da conservação de quantidade de movimento linear e angular temos:

![Screen Shot 2022-05-10 at 3.39.29 PM.png](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Screen_Shot_2022-05-10_at_3.39.29_PM.png)

$$
\sum \vec F = m' \Delta v
$$

$$
\sum \vec M_O = m'(\vec d_2 \times \vec v_2 - \vec d_1 \times \vec v_1)
$$

![Screen Shot 2022-05-10 at 3.40.16 PM.png](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Screen_Shot_2022-05-10_at_3.40.16_PM.png)

## Escoamento Variável de Massa

$\hookrightarrow$ Para os casos onde a massa não é constante, as fórmulas supracitadas não são mais válidas.

$\hookrightarrow$ Para o caso onde há desprendimento de massa temos que há uma força $R$ que acelera essa massa $m'$ de $v_0$ para $v$ dada por:

$$
R = m'(v- v_0) = \dot m u
$$

$\hookrightarrow$ Onde:

- $\dot m$ → Variação de massa no recipiente original que está perdendo a massa
- $u$ → Velocidade relativa entre a massa expelida e o recipiente

$\hookrightarrow$ Pela lei de Newton temos:

$$
\sum \vec F = m\dot {v} + \dot{ m} u
$$

- EXEMPLO
    
    ![Screen Shot 2022-05-10 at 3.57.10 PM.png](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Screen_Shot_2022-05-10_at_3.57.10_PM.png)
    
    ![Screen Shot 2022-05-10 at 3.57.18 PM.png](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Screen_Shot_2022-05-10_at_3.57.18_PM.png)
    
    ![Screen Shot 2022-05-10 at 3.57.32 PM.png](Cine%CC%81tica%20de%20Sistemas%20de%20Parti%CC%81culas%208cfaca418bbb4e89bae942228ddaee02/Screen_Shot_2022-05-10_at_3.57.32_PM.png)