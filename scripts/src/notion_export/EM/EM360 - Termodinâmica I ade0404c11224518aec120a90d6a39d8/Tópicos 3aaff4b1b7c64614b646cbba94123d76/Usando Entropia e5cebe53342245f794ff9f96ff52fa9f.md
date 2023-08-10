# Usando Entropia

Aula: Aula17, Aula18, Aula19, Aula20
Cap.: Cap.6
Created: October 15, 2021 9:38 AM

[Anotações de Aula](Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/Anotac%CC%A7o%CC%83es%20de%20Aula%201d7757e4bf1e4efabbf67037b6da615e.md)

- SUMÁRIO

# Definição da Variação de Entropia

$\hookrightarrow$ Uma quantidade só pode ser chamada de propriedade se, e somente se, sua variação entre dois estados for independente do processo.

$\hookrightarrow$ Levando isso em consideração, juntamente com a Desigualdade de Clausius, temos que a variação de Entropia $S$ entre dois estados $1-2$  (por um processos internamente reversível) é dada por:

$$
S_2 - S_1 = \left(\int^2_1 \frac{\delta Q}{T}\right)_{int \ rev}
$$

$\hookrightarrow$ Isso implica que a transferência de entropia acompanha a transferência de calor.

$\hookrightarrow$ Outra interpretação, para processos internamente reversíveis, é:

$$
Q_{int \ rev} = \int^2_1 Tds
$$

# Avaliando a Entropia

- Valores para Vapor Superaquecido
    - Para substância no estado de vapor superaquecido temos que as tabelas oferecem a entropia específica juntamente com $u$ e $h$ em função da temperatura e pressão.
- Valores de Saturação
    - Para substâncias bifásicas de título $x$ somos capazes de encontrar sua entropia específica pelos valores de saturação $s_l$ para líquido saturado e $s_g$ para gasos:
    
    $$
    s = s_l + x(s_g - s_l)
    $$
    
- Valores para Líquidos e Líquido Comprimido
    - Para líquidos saturados temos as tabelas que nos informam qual que é $s_l$.
    - Já para os valores de líquido comprimido (também chamado de sub-cooled) podemos fazer a aproximação da entropia como sendo a mesma do que o valor da entropia do líquido saturado da tabela à temperatura.
    
    $$
    s(T, p) \approx s_l(T)
    $$
    

# Equações  $T$ $dS$

## Sistemas Compressíveis

$\hookrightarrow$ Primeira Equação $Tds$:

$$
\boxed{Tds = dU + pdV}
$$

$\hookrightarrow$ Utilizando $H = U + pV$ na primeira equação temos a segunda equação:

$$
\boxed{Tds = dH - Vdp}
$$

### Exemplo de Utilização

$\hookrightarrow$ Em uma mudança de fase ($\therefore T = const$ ) a vapor constante temos:

$$
ds = \frac{dh}{T}
$$

## Sistemas Incompressíveis

$\hookrightarrow$ Para sistemas incompressíveis, com $c$ (calor específico) constante temos:

$$
\boxed{s_2 - s_1 = c \ln \frac{T_2}{T_1}}
$$

<aside>
<img src="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/Screen_Shot_2021-09-23_at_11.49.01_PM.png" alt="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/Screen_Shot_2021-09-23_at_11.49.01_PM.png" width="40px" />  Para valores de calor específico das substâncias mais comuns temos a tabela $A-19$ do Shapiro.

</aside>

<aside>
<img src="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/mugi.gif" alt="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/mugi.gif" width="40px" /> Lembrando que quando o problema for de líquido podemos considerar um problema de sistema incompressível !!!

</aside>

## Sistemas de Gases Ideais

$\hookrightarrow$ Para gases ideais temos duas equações, uma em função de $v$ e $C_v$ e outra em função de $p$ e $C_p$:

$$
\boxed{s(T_2, v_2) - s(T_1, v_1) = \int^{T_2}_{T_1} c_v(T) \frac{dT}{T} + R \ln \frac{v_2}{v_1}}
$$

$$
\boxed{s(T_2, p_2) - s(T_1, p_1) = \int^{T_2}_{T_1} c_p(T) \frac{dT}{T} + R \ln \frac{p_2}{p_1}}
$$

$\hookrightarrow$ Lembrando que $c_p(T) = c_v(T) + R$ e que $R$ é uma const logo se souber a função de um dos $c$ somos capazes de achar a outra função.

$\hookrightarrow$ Outra possibilidade é de que $c$ é constante, temos então  as tabelas $A-20$ e $A-21$ com os valores de $c_v$ e $c_p$. Com isso a intergral vira somente:

$$
\boxed{\Delta S  =  c_v \ \ln\frac{T_2}{T_1} + R \ln \frac{v_2}{v_1}}
$$

$$
\boxed{\Delta S  =  c_p\ \ln\frac{T_2}{T_1} + R \ln \frac{p_2}{p_1}}
$$

### Utilização de Tabelas

$\hookrightarrow$ Se a substância tiver os valores de $s^\circ$ (como por exemplo na tabela $A-22$) temos que:

$$
\boxed{s(T_2, p_2) - s(T_1, p_1) = s^\circ (T_2) - s^\circ (T_1) - R\ln\frac{p_2}{p_1}}
$$

# Balanço de Entropia

## Sistemas Fechados

$[\hookrightarrow](https://app.respondeai.com.br/materias/solucionario/livro/28/edicao/46/exercicio/65093)$ Matematicamente, o balanço de entropia para um sistema fechado é descrito como sendo:

 

$$
\overbrace{dS}^{Var. \ Entropia} = \underbrace{\left(\frac{\delta Q}{T}\right)_b}_{Transferência} + \overbrace{\delta \sigma}^{Geração}
$$

$[\hookrightarrow](https://app.respondeai.com.br/materias/solucionario/livro/28/edicao/46/exercicio/65093)$ Onde:

- $dS$ é a variação de entropia
- $\delta \sigma$ é a geração de entropia no interior do sistema
- $\delta Q_b$ é a variação de calor na fronteira
- $T_b$ é a temperatura da fronteira em análise

ou se $T_b$ for constante temos:

$$
S_2 - S_1 = \frac{Q}{T_b} + \sigma
$$

<aside>
<img src="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/kawasegaua.png" alt="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/kawasegaua.png" width="40px" /> Quando não há presença de irreversibilidades, $dS=0 \therefore \left(\frac{\delta Q}{T}\right)_b =  \delta \sigma$

</aside>

### Interpretando o Balanço de Entropia para um Sistema Fechado

$\hookrightarrow$ Se observarmos a equação de balanço de entropia podemos ver que a variação de entropia em um sistema é dividida em duas partes:

- Transferência de Entropia Associada à Transferência de Calor
    - Representado pela equação: $\left(\frac{\delta Q}{T}\right)_b$
    - O sentido da transferência de entropia é o mesmo sentido da transferência de calor, e segue a mesma convenção de sinais:
    
    $$
    + \rightarrow Para\ dentro \ do \ sistema \\ 
    - \rightarrow Para\ \ fora \ \ do \ sistema
    $$
    
- Geração de Entropia
    - Representado pelo termo sigma: $\delta \sigma$
    - É oriundo da presença de irreversibilidades dentro do sistema.
    - Pode ser $+$ quando há irreversibilidades $\therefore$ ocorre geração de entropia ou pode ser $\delta \sigma = 0$ quando não há irreversibilidades.
    
    $$
    \sigma:\begin{cases}> 0  & Presença \ de\ irreversibilidades \\
    = 0 & Ausência \ de\ irreversibilidades 
    \end{cases}
    $$
    

## Volmes de Controle

$$
\overbrace{\frac{dS_{vc}}{dt}}^{Tax. \ Variação} = \underbrace{\sum \frac{\dot Q}{T} + \sum \dot m_e s_e - \sum \dot m_s s_s}_{Tax. \ de \ Transferência} + \overbrace{\dot \sigma_{vc}}^{Taxa. \ Gerão}
$$

# Eficiências Isentrópicas

$\hookrightarrow$ A eficiência isentrópica é a relação do trabalho que ocorreria em processo ideal (i.e sem irreversibilidades $\therefore$ isentrópico) e o que realmente ocorre (com a presença de irreversibildiades).

$\hookrightarrow$ Podemos calcular essa eficiência dependendo de cada "dispositivo" termodinâmico a seguir:

- Turbinas
    
    $\hookrightarrow$ Para um turbina, a eficiência isentrópica é:
    
    $$
    \eta_t = \frac{h_1 - h_2}{h_1 - h_{2s}}
    $$
    
    $\hookrightarrow$ Onde:
    
    - $h_{2s}$ → Entalpia "Teórica" na saída da turbina, considerando $s_2 = s_1$.
    - $h_2$ → Entalpia real do estado dois.
    
    <aside>
    🧠 Temos para turbinas que $h_2 > h_{2s}$ logo temos que o trabalho real (com $h_{2}$) é menor que o trabalho ideal (em um cenário de expansão isentrópica e $h_{2s}$)
    
    </aside>
    
- Bocais
    
    $\hookrightarrow$ De forma análoga, temos que a eficiência isentrópica para um bocal é a razão entre a energia cinética real do gás saindo do bocal e a energia de descarga em uma expansão isentrópica ideal:
    
    $$
    \eta _{bocal} = \frac{V^2_2 / 2}{(V^2_2 / 2)_s}
    $$
    
- Bombas e Compressores
    
    $\hookrightarrow$ Tanto para bombas quanto para compressores temos que:
    
    $$
    \eta_c = \frac{h_{2s} - h_1}{h_2 - h_1}
    $$
    
    <aside>
    <img src="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/Hifumi_Surprised.png" alt="Usando%20Entropia%20e5cebe53342245f794ff9f96ff52fa9f/Hifumi_Surprised.png" width="40px" /> Para bombas e Compressores, que exercem trabalho, temos que o trabalho real é maior que o trabalho isentrópico pois $h_2 > h_{2s}$. Isso faz sentido pois em um cenário real (com $h_2$) temos que a presença de irreversibilidades cria a necessidade de um maior trabalho.
    
    </aside>