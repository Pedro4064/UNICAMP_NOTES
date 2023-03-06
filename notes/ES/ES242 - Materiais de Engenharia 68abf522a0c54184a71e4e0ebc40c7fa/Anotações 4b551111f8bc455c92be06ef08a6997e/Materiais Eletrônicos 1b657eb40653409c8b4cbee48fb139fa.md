# Materiais Eletrônicos

Aula: Aula 13
Capitulo: Cap. 19
Created: June 30, 2021 10:03 AM

# Introdução - Materiais Eletrônicos

- Microeletrônicos baseados em $Si$, como computadores, celulares, máquinas etc.
- A microeletrônica inclui materiais de todas as classes → $Cu$, $Au$, $GaAs$, ...

# Condutividade Elétrica

- Condutividade elétrica é regida pela Lei de Ohm:

$$
V = IR
$$

- Onde podemos destrinchar a resistência em:

$$
R = p \frac{l}{\sigma A}\\ p:resistividade \ \\ 
\sigma : condutividade
$$

- Tal que a resistividade depende da microestrutura e composição (i.e $Cu$ puro possui menor resistividade que $Cu$ comercial), pois as impurezas espalham os elétrons.
- Além disso, podemos descrever a Lei de Ohm como uma densidade de carga, que representa de forma mais explícita a influência das impurezas e imperfeições no deslocamento dos elétrons:
    
    $$
    J = nq\bar{V}
    $$
    
    $\hookrightarrow n:$ Número de portadores de cargas → Elétrons 
    
    $\hookrightarrow q:$ Carga de cada elétron → $1.6 \times 10^{-19} C$
    
    $\hookrightarrow \bar{V}:$ Velocidade média de deriva (velocidade para percorrer um certo período de tempo, que não é a velocidade da Luz pois os elétrons, por conta das imperfeições, não se deslocam em linha reta) .
    
    $\hookrightarrow J:$ Densidade de Corrente.
    
- Em suma, temos que a condutividade elétrica de um material é dado por:
    
    $$
    \sigma = nq \mu
    $$
    
    $\hookrightarrow \mu:$ Mobilidade dos carregadores de carga
    

- Que nos diz que a condutividade elétrica dos materiais pode ser alterada através do:
    1. Controle do número de portadores de carga $(n)$
    2. Controle da mobilidade (facilidade de movimento dos elétrons, $\mu$)

## Ligações Atômicas e Condutividade

- Elétrons de valência em metais se movem com facilidade.
- Ligações covalentes devem ser quebradas em semicondutores não dopados.
- Em sólidos com ligações iônicas, os íons devem se mover para que ocorra condução elétrica.

## Classificação de Materiais Elétricos

- Supercondutores: Resistividade nula em baixas temperaturas.
- Condutores: Condutividade $> 10^3 \Omega^{-1}\cdot cm^{-1}$
- Semicondutores: Condutividade $< 10^3 \Omega^{-1}\cdot cm^{-1}$ e $>10^{-12}\Omega^{-1}\cdot cm^{-1}$
- Isolantes ou Dielétricos: Condutividade $< 10^{-12}\Omega^{-1}\cdot cm^{-1}$

# Estrutura de Bandas de Sólidos

- Princípio de exclusão de Pauli → no máximo 2 elétrons ocupam um nível de energia (orbital).
- Sólido com $N$ átomos → os níveis de energia se dividem formando bandas.
- Os elétrons ocupam primeiro o orbital com menor energia.
- Mais átomos = Menor espaçamento entre os orbitais.

<aside>
<img src="Materiais%20Eletro%CC%82nicos%201b657eb40653409c8b4cbee48fb139fa/sagiriBleh.png" alt="Materiais%20Eletro%CC%82nicos%201b657eb40653409c8b4cbee48fb139fa/sagiriBleh.png" width="40px" /> In a Nutshell →  Band Gap é o $\Delta$ de energia que precisa ser vencida pelos elétrons para que eles passem da banda de valência para a banda de condução.

</aside>

- Existe uma relação direta do band gap com a condutividade:
    - Metais
        - Nos metais temos que há um overlapping da banda de valência e de condução $\therefore$ uma quantidade infinitesimal é necessária para a condução.
    - Semicondutores
        - Ao contrário do que acontece com Metais, nos semicondutores ocorre uma facilitação da transição de banda quanto maior a temperatura, e quando $T = 0K$ não ocorre a condução.
    - Isolantes
        - Band Gap muito grande para ser vencido

# Semicondutores

- Semicondutores podem ser divididos  em dois tipos:
    1. Semicondutores Intrínsecos → propriedades não controladas por elementos dopantes.
    2. Semicondutores Extrínsecos → Tipo p ou tipo n, condutividade controlada por dopantes.
- Semicondutores se tornam mais condutores quanto maior a temperatura pois a energia térmica promove os elétrons até a banda de condução.
    - Elétrons → cargas negativas;
    - Buracos → cargas positivas;
    - Condutividade:
    
    $$
    \sigma = nq \mu_n + pq\mu_p
    $$
    

# Processamento de Circuitos Integrados

- Circuitos Integrados ou microships fabricados em wafers de $Si$.
- Atualmente podem incluir bilhões de componentes.
- Feito por Litografia.

# Isolantes

- Baixa condutividade, normalmente cerâmicos.
- Aproximadamente $80\%$ do mercado de cerâmicos industriais são utilizados para eletrônica → e.g capacitor de placas planas.

# Piezoelétricos

- Eletrestricção → quando um material é polarizado, íons e nuvens de elétrons são deslocados gerando uma deformação e vice versa.