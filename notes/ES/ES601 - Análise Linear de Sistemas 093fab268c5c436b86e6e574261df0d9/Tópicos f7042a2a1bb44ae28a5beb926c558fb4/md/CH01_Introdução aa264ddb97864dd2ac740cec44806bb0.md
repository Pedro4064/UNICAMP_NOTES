# Introdução

Created: August 18, 2022 4:18 PM

[Anotações de Aula](Introduc%CC%A7a%CC%83o%20aa264ddb97864dd2ac740cec44806bb0/Anotac%CC%A7o%CC%83es%20de%20Aula%2051a1ddd1cc1647bea039caa1228fac4f.md)

- SUMMARY
    
    

# Sistemas Lineares

$\hookrightarrow$ Estudamos sistemas lineares pois eles aparecem em diversos sistemas físicos (como circuitos, sistemas mecânicos, processamento de sinais, etc).

$\hookrightarrow$ Além disso, muitos sistemas, mesmo que não lineares, podem, em uma pequena faixa, serem tratados como lineares, para então aplicarmos as ferramentas/técnicas que serão abordadas nesse curso.

$\hookrightarrow$ No primeiro momento, a principal ferramenta que iremos utilizar para modelar tais sistemas do mundo real são Equações Diferenciais, que vimos em calculo 3.

# Relembrando Equações Diferenciais Ordinárias

$\hookrightarrow$ Podemos interpretar equações diferencias como sendo equações onde, como resultado, teremos uma função, que descreve certo comportamento do sistema.

$\hookrightarrow$ Para facilitar o nosso estudo, nós categorizamos as equações diferenciais de acordo com certos parâmetros.

## Linearidade

$\hookrightarrow$ Uma equação Diferencial pode ser Linear se e somente si:

1. A variável dependente e suas derivadas estiverem elevadas somente a $1$.
2. Os coeficientes (que multiplicam a variável dependente e suas derivadas) forem compostos apenas da variável independente.

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> ***E o que é Variável dependente e Independente?*** 
Uma **variável dependente**, como o nome sugere, é aquela que está em função de outra variável, aqui no nosso caso, normalmente teremos sempre variáveis dependentes em **função do tempo**, que por sua vez é chamada de variável independente.

</aside>

- **Exemplos**
    
    $$
    x^5 \frac{d^5 y}{dx^5} + x^3 \frac{d^3 y}{dx^3}  \rightarrow É \ Linear
    $$
    
    $$
    \boxed{y\frac{dy}{dx}} + \frac{dy}{dx} \rightarrow Não \ é \ Linear
    $$
    
    $$
    \frac{d^2 \theta}{dt^2} + \frac{g}{L} \boxed{\sin \theta} = 0 \rightarrow Não \ é \ Linear
    $$
    

## Homogeneidade

$\hookrightarrow$ No geral, EDOs tem a seguinte estrutura:

$$
q(x)\frac{dy}{dx} + r(x)y = g(x)
$$

$\hookrightarrow$ Dizemos que a EDO é homogênea si e somente si $g(x) = 0$, i.e se **não** houver componente sem a variável dependente.

# Em Suma

$\hookrightarrow$ Após termo definido que, para o estudo de sistemas,  iremos utilizar equações diferenciais, e suas diferentes categorizações, iremos introduzir diversos modelos de sistemas do mundo real e os diferentes tipos de EDO que são utilizados para descreve-los, além de técnicas para sua solução.