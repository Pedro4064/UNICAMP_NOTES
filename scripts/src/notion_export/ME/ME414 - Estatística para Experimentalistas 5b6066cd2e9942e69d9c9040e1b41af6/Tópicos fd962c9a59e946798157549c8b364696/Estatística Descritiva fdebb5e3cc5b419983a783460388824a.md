# Estatística Descritiva

Created: April 20, 2022 2:12 PM
Tags: P1

[Anotações de Aula](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Anotac%CC%A7o%CC%83es%20de%20Aula%20bfa24e23199745aa91ded7fbc1e903cc.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ A estatística Descritiva trata, como o nome sugere, de dados discretos, isso é, um número finito de dados que podem ser dispostos em tabelas.

# Análise Descritiva

$\hookrightarrow$ Análise descritiva se refere a métodos para resumir e descrever os dados.

$\hookrightarrow$ De modo geral, podemos resumir os dados discretos por meio de:

- Métricas Quantitativas → Se refere medidas resumo tais como média, mediana, desvio padrão, proporções, etc.
- Ferramentas Visuais → Gráficos, etc.

$\hookrightarrow$ A ferramenta mais adequada, entretanto, depende do tipo de variável

## Tipos de Variáveis

$\hookrightarrow$ As variáveis podem ser agrupadas em dois principais tipos, sendo eles:

### Dados Quantitativos

- Os quais possuem um valor numérico associado.
- Ainda pode ser dividida em:
    - Contínuos
    - Discretos

### Dados Qualitativos

- Representam categorias e não valores numéricos.
- Podem ainda ser divididos em:
    - Nominais → Não existe ordenação.
    - Ordinais → Possuem uma certa ordem.

## Análise Descritiva Univariada

$\hookrightarrow$ Consiste basicamente em, para cada uma das variáveis individualmente:

- Classificar a variável quanto a seu tipo
- Obter table, gráfico e/ou medidas resumo apropriados

$\hookrightarrow$ E então a partir disso montar um resumo geral dos dados.

## Análise Descritiva Bivariada

$\hookrightarrow$ Na análise Descritiva Bivariada nós temos por objetivo estudar a correlação (i.e grau de dependência) entre duas variáveis (e.g a relação de número de drinks $VS$ homem, mulher).

$\hookrightarrow$ Levando em consideração os diferentes [tipos de variáveis](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a.md) nós temos os seguintes casos para análise bi-variada:

### Duas Variáveis Qualitativas

- Usamos Tabelas de Frequências.
- Muitas das vezes os números de cada variável qualitativa não são iguais no total, quando isso ocorre podemos comparar as frequências relativas, isso é, a frequência em relação ao total daquela variável e não o total absoluto.
    
    ![Screen Shot 2022-05-07 at 11.38.46 AM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-05-07_at_11.38.46_AM.png)
    
    - Um exemplo disso é a tabela acima, onde o número de Mulheres e Homens são diferentes. Nesse caso podemos transformar essa table e uma de frequência relativa ao gênero, como abaixo:
        
        ![Screen Shot 2022-05-07 at 11.45.27 AM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-05-07_at_11.45.27_AM.png)
        

### Duas Variáveis Quantitativas

- Comparamos como a mudança de uma variável afeta a outra variável.
- Utilizamos Scatterplot (gráfico) e o coeficiente de Correlação (medida resumo).

![Screen Shot 2022-05-07 at 11.55.29 AM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-05-07_at_11.55.29_AM.png)

![Screen Shot 2022-05-07 at 11.58.14 AM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-05-07_at_11.58.14_AM.png)

### Uma variável é Quantitativa e a Outra Qualitativa

## Medidas Resumo

$\hookrightarrow$ Temos por objetivo resumir todos os dados que possuímos em relação a alguma característica (e.g posição, dispersão, etc.) através de valores.

### Medidas De Posição Central

- **Média Aritmética**
    - Pode ser interpretada como o ponto de equilíbrio de uma distribuição, dado por:
    
    $$
    \bar x = \frac{1}{n} \sum ^{n} _{i = 1} x_i
    $$
    
- **Mediana ou $Q_2$**
    - Outro valor muito utilizado é a mediana, que é o valor que separa os dados em dois grupo de tamanhos iguais.
    - É dada por:
    
    $$
    Q_2 = \begin{cases}
    X_{\left( \frac{n+1}{2} \right)},  & se \ n \ é \ \ ímpar \\ 
    \frac{1}{2}\left(X_{\left( \frac{n}{2} \right)} + X_{\left( \frac{n}{2} + 1 \right)} \right),  & se \ n \ é \ \ par
    \end{cases}
    $$
    
- **Moda**
    - Mais utilizado quando tempos variáveis categóricas.
    - Representa o número com maior ocorrência.

- RELAÇÃO DE DISPERSÃO E MEDIANA E MÉDIA
    
    ![Screen Shot 2022-05-06 at 8.19.39 PM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-05-06_at_8.19.39_PM.png)
    
    - Dizemos que há:
        - Assimetria à Direita (positiva): Média > Mediana > Moda
        - Assimetria à Esquerda (negativa): Média < Mediana < Moda

<aside>
<img src="Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Evangelion.gif" alt="Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Evangelion.gif" width="40px" /> IMPORTANTE! Dizemos que a mediana é mais robusta do que a média pois a média é muito influenciada por valores muito extremos e discrepantes. Por isso para casos em que temos outliers positivos nossa média > Mediana e  quando temos outliers negativos temos que nossa Média < Mediana

</aside>

### Medidas De Dispersão

- **Amplitude**
    - A Amplitude é dada pela diferença entre o maior e o menos valor do nosso dataset.
- **Variância**
    - Variância representa a média dos desvios (i.e a distância média de cada observação a média do dataset) ao quadrado.
    - Temos que é ao quadrado para medirmos as distâncias e elas não se anularem (pois como é até a média iriam se anule).
    - A variância, assim como a amplitude, são medidas de dispersão do dataset.
    - É dada por:
    
    $$
    s^2 = \frac{1}{n-1}\sum^n_{i=1}(x_i  - \bar x)^2
    $$
    
- **Desvio Padrão**
    - Se observarmos a unidade da variância temos que está ao quadrado (logo seria algo do tipo preço ao quadrado etc) e isso não é interessante para utilizarmos em interpretações.
    - Logo temos o desvio padrão, que nada mais é do que a raiz da variância:
    
    $$
    s = \sqrt{\frac{1}{n-1}\sum^n_{i=1}(x_i  - \bar x)^2}
    $$
    
    <aside>
    <img src="Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Hifumi_Surprised.png" alt="Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Hifumi_Surprised.png" width="40px" /> IMPORTANTE → NÃO podemos comparar dois datasets pelo desvio padrão se suas escalas forem muito diferentes (e.g $\{1, 2, 3\}$ e $\{101, 102, 103\}$)
    
    </aside>
    
- **Coeficiente de Variação**
    - Como vimos no Desvio Padrão, não podemos utiliza-lo para comparar datasets com escalas muito diferentes.
    - Para esses casos nós temos o que chamamos de Coeficiente de Variação, ou o também chamado de Desvio Padrão Relativo, que é a razão do desvio padrão pela média:
    
    $$
    CV = \frac{s}{\bar x}
    $$
    
- **Quartis**
    - Nos Quartis nós dividimos o nosso dataset tal que cada quartil cubra $25\%$ das amostras.
    - Podemos observar, ainda, que o $Q2$ é a nossa Mediana.
    - A partir da Mediana nós calculamos o $Q1$ como sendo a mediana do subconjunto inferior e o $Q3$ como sendo a mediana do subconjunto superior.
    - De forma análoga a como somos capazes de relacionar a dispersão dos dados com a mediana e média nós somos capazes de a relacionar com as distâncias entre os quartis;
        - Assimetria à Direita (Positiva) → $Q_2 - Q_1 < Q_3 - Q_2$
        - Assimetria à Esquerda (Negativa) → $Q_2 - Q_1 > Q_3 - Q_2$
        - Simétrico:
            
            $\hookrightarrow$ $Q_2 - Q_1 \approx Q_3 - Q_2$
            
            $\hookrightarrow$ $Q_2 - Q1$ e $Q_3 - Q_2$ $<$ Extremos até $Q_1$ e $Q_3$
            
    - Além disso, a partir dos quartis nós temos o chamado **Intervalo Interquartílico ($IQ$)**, que representa o intervalo entre $Q_1$ e $Q_3$, que por definição abrange $50\%$ dos dados.
    - A partir desse intervalo interquartílico nós somos criamos uma régua para possíveis outliers como sendo os dados:
        
        $$
        \begin{cases}
        Acima \ de \ Q_1 - 1.5 \times IQ \\ 
        Abaixo \ de \ Q_3 + 1.5 \times IQ
        \end{cases}
        $$
        

## Principais Métodos Visualização De Sumarização

### **Resumo**

| Nome | Variável | Descrição | Observação |
| --- | --- | --- | --- |
| Tabela de Frequências | • Qualitativa Nominal/Ordinais
• Quantitativa Discreta | Lista todos os possíveis valores que a variável pode assumir e conta quantas vezes cada uma aparece. | Quando lidando com variáveis Ordinais temos que sempre representar na ordem da variável e não na ordem de maior ou menor frequência. |
| Gráfico de Barras | • Qualitativa Nominal/Ordinais
• Quantitativa Discreta | Lista todos os possíveis valores que a variável pode assumir e representa, através do comprimento da barra, quantas vezes cada uma aparece. | Quando lidando com variáveis Ordinais temos que sempre representar na ordem da variável e não na ordem de maior ou menor frequência. |
| Histograma | • Quantitativa Contínua | É análogo a um gráfico de barras, mas como estamos lidando com dados quantitativos contínuos nós agrupamos em intervalos e, através do comprimento da barra, representamos o número de ocorrências que caem dentro de cada intervalo. | Os principais comportamentos de um histograma são: 
1. Bimodal - Duas Normais.
2. Comb - Com picos intermitentes  muito acima do restante da distribuição.
3. Edge Peak - Com um grande pico nos extremos.
4. Normal - Bell shape
5. Skewed - Semelhante à normal mas arrastada para um dos lados e cortada ao meio. 
6. Uniform - uniformimente distribuida. |
| Stem-and-Leaf | • Quantitativa Contínua/Discreta | Possui a mesma função do histograma mas não há perda de informação. Ela é feita separando os dados (que são numéricos) em duas partes, “Stem” que são todos os algarismos menos o último e a folha “leaf”, que é a unidade do número. Agrupamos então os números com os primeiros dígitos iguais, separamos com uma linha e botamos todos os algarismos das unidades dos respectivos números. | Pode ser usado tanto para variáveis quantitativas contínuas quanto discretas, mas não é muito utilizado. |

### Histograma

$\hookrightarrow$ É análogo a um gráfico de barras, mas como estamos lidando com dados quantitativos contínuos nós agrupamos em intervalos e, através do comprimento da barra, representamos o número de ocorrências que caem dentro de cada intervalo.

$\hookrightarrow$ Os principais comportamentos de um histograma são: 

1. Bimodal - Duas Normais.
2. Comb - Com picos intermitentes  muito acima do restante da distribuição.
3. Edge Peak - Com um grande pico nos extremos.
4. Normal - Bell shape
5. Skewed - Semelhante à normal mas arrastada para um dos lados e cortada ao meio. 
6. Uniform - Distribuida de forma uniforme 

![Screen Shot 2022-04-20 at 3.28.45 PM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-04-20_at_3.28.45_PM.png)

### Stem-and-Leaf

$\hookrightarrow$ Possui a mesma função do histograma mas não há perda de informação.

$\hookrightarrow$ Ela é feita separando os dados (que são numéricos) em duas partes, “Stem” que são todos os algarismos menos o último e a folha “leaf”, que é a unidade do número. 

$\hookrightarrow$ Agrupamos então os números com os primeiros dígitos iguais, separamos com uma linha e botamos todos os algarismos das unidades dos respectivos números.

![Untitled](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Untitled.png)

### BoxPlot

- Representação do esquema dos 5 números.
- Possibilita a visualização de importantes características dos dados, como posição, dispersão, assimetria e facilita a identificação de possíveis outliers:
    
    ![Screen Shot 2022-05-07 at 11.21.58 AM.png](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a/Screen_Shot_2022-05-07_at_11.21.58_AM.png)
    

- Onde os limites inferiores e superiores são números dentro do nosso dataset que estão dentro dos limites sem possíveis outliers comentados na [parte de Quartis e Intervalos Interquartílicos](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a.md).
- Logo os Limites NÃO são $Q_1 - 1.5IQ$ e $Q_3 + 1.5 IQ$, mas sim os menores e maiores números, respectivamente, do nosso dataset que caem dentro desse intervalo.