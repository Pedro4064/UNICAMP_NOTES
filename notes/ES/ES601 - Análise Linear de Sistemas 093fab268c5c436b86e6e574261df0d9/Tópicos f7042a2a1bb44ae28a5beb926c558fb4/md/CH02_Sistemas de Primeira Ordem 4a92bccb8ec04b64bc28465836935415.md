# Sistemas de Primeira Ordem

Created: August 18, 2022 4:17 PM

[Anotações de Aula](Sistemas%20de%20Primeira%20Ordem%204a92bccb8ec04b64bc28465836935415/Anotac%CC%A7o%CC%83es%20de%20Aula%20ae75928b9b3641cf8b22e4fdb1b6b467.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ O primeiro tipo de sistema que iremos modelar são os chamados sistemas de primeira ordem, que nada mais são que sistemas que são descritos por equações diferencias ordinárias (EDO$_s$) de primeira ordem (como o próprio nome sugere), isso é, que a maior derivada presente (da variável dependente) é de primeira ordem.

# Sistema de Primeira Ordem - Resistor e Capacitor

$\hookrightarrow$ O exemplo clássico de um sistema de primeira ordem é um circuito elétrico composto de fonte, resistor e capacitor, como mostrado na figura ao lado, em que queremos descrever o comportamento da tensão no capacitor $(v_c)$ ao longo do tempo.

![Screen Shot 2022-08-18 at 5.03.46 PM.png](Sistemas%20de%20Primeira%20Ordem%204a92bccb8ec04b64bc28465836935415/Screen_Shot_2022-08-18_at_5.03.46_PM.png)

$\hookrightarrow$ Ao fazermos a análise de malha, temos que:

$$
\begin{align}v_E = v_R + v_c\end{align}
$$

$\hookrightarrow$ Além disso, como não temos divisão de nós, temos que há somente uma corrente no circuito como um todo, levando isso em consideração, mais o fato de que a corrente de um capacitor é dado por:

$$
\begin{align}i_c(t) = C \frac{d}{dt}v_c(t)\end{align}
$$

$\hookrightarrow$ Com isso, juntamente com a lei de ohm, podemos botar a equação de número $1$ em função de $v_c$, o que queremos achar. Resultando em:

$$
\begin{align}(RC)\dot{v_c} + v_c = v_E\end{align}
$$

$\hookrightarrow$ Resultando em uma EDO Linear de primeira ordem **não homogênea**, devido a componente $v_E$, que é chamada de **termo forçante**, ou também de **excitação** ou **entrada**.

# Solução de Sistemas de Primeira Ordem

## Solução Homogênea

$\hookrightarrow$ Uma das formas mais básicas de resolução de EDOs homogêneas é usando o o método onde se assume o formato da solução, e posteriormente substituímos na EDO para calcularmos os coeficientes.

$\hookrightarrow$ Sabemos que, no geral, a solução de uma EDO de primeiro grau padrão, dada por $\dot y + a_1y = 0$ tem o seguinte forma:

$$
y(x) = Ae^{\lambda x}
$$

$\hookrightarrow$ Ao substituir na EDO original, como mostrado no exemplo abaixo, encontramos a Solução Geral. Posteriormente nós substituímos (na solução proposta, no nosso caso na eq de y(x) e NÃO na EDO novamente) os valores da condição inicial para acharmos os valores de $A$ e $\lambda$, encontrando finalmente a solução da EDO.

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> IMPORTANTE: É de suma importância deixarmos o termo $\dot y$ com coeficiente $1$. Se houver algo multiplicando ele basta multiplicarmos toda a EDO pelo seu inverso.

</aside>

- **Exemplo**
    
    ![Screen Shot 2022-08-23 at 10.52.57 AM.png](Sistemas%20de%20Primeira%20Ordem%204a92bccb8ec04b64bc28465836935415/Screen_Shot_2022-08-23_at_10.52.57_AM.png)
    

## Solução Não Homogênea

$\hookrightarrow$ Há diferentes formas de solucionar EDOs de primeira ordem não homogêneas, mas em Análise Linear de Sistemas, nesse primeiro momento, vamos ver as seguintes:

### Método do Fator Integrante

- Nesse método nós temos, na EDO, nenhum coeficiente (i.e nada multiplicando) para a derivada da variável dependente, mais a soma de um fator dependente da variável dependente, como mostrado abaixo:

$$
\frac{dy}{dx} + ay = g(x)
$$

- A partir disso, temos que seguir os seguintes passos:
    1. Encontrar o Fator Integrante: Que é denotado por $\mu(x)$ e que é encontrado por: 
        
        $$
        \mu(x) = \exp \int a \  dx
        $$
        
    2. Multiplicar Ambos os lados pelo fator integrante:  Após multiplicarmos ambos os lados pelo nosso fator integrante temos, como resultado:
        
        $$
        \frac{d}{dx}\big(\mu(x)\cdot y(x)\big) = \mu(x) \big(g(x)\big)
        $$
        
    3. Integrar: A partir daqui podemos integrar de ambos os lados, que resultaria em:
        
        $$
        \mu(x)\cdot y(x) \big |^{x_f}_{x_i} = \int^{x_f}_{x_i}\mu(x)g(x) \ dx
        $$
        
    4. Agora basta Isolar $y(x)$ no lado esquerdo, sendo que o lado direito vai depender do valor inicial de $y(0)$.
    

### Método de Suposição

- Outro método bastante útil separa a solução de uma EDO não homogênea em duas partes:
    
    $$
    y(t) = y_h(t) + y_p(t)
    $$
    
- Onde:
    - $y_h(t)$ → Tem o formato da solução da EDO homogênea
    - $y_p(t)$ → Pode assumir o formato de qualquer combinação linear da solução homogênea e o fator forçante (que é o que chamamos o termo não zero do lado direito da equação). Normalmente utilizamos o mesmo formato do fator forçante (e.g se for uma constante nós usamos uma constante, se for $\sin$  nós usamos $\sin$, etc).
- Assim que determinamos a forma de cada componente nós substituímos, uma de cada vez, na EDO para acharmos alguns dos coeficientes.
- Após isso, nós substituímos a condição inicial dada na fórmula de $y(t) = y_h(t) + y_p(t)$ para acharmos os restantes dos coeficientes que não foram achados acima.

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> Nós usamos somente o FORMATO da solução homogênea, e não os valores que iríamos encontrar se desenvolver a EDO na sua forma homogênea.

</aside>

# Interpretação de Sistemas de Primeira Ordem

$\hookrightarrow$ Assim que resolvermos nossa EDO de primeiro grau nós teremos duas partes:

- **Resposta Homogênea do Sistema** → Parte que depende da condição inicial do nosso problema.
- **Resposta Forçada do Sistema** → Parte que não depende dos nossos valores iniciais.

$\hookrightarrow$ Além disso, poderemos analizar a resposta do nosso sistema no que tange seu comportamento no tempo:

- **Parte Transiente** → Dependente do tempo
- **Parte Permanente** → Não depende do tempo $\therefore$   se $t \rightarrow \infty$ a parte permanente vai representar nosso sistema