# Variáveis Discretas Aleatórias

Created: May 8, 2022 5:11 PM
Tags: P1

[Anotações de Aula](Varia%CC%81veis%20Discretas%20Aleato%CC%81rias%20cd1bb274dadb496f921ed161527a9b1c/Anotac%CC%A7o%CC%83es%20de%20Aula%20c48dd4e1beb64350967cf00370afad46.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Uma variável aleatória representa os possíveis resultados de um experimento aleatório.

$\hookrightarrow$ Com isso podemos ainda falar da probabilidade de uma variável aleatória → E representamos as probabilidades de todos os possíveis valores que essa variável pode assumir em uma tabela que chamamos de **Tabela de Distribuição de Probabilidade.**

$\hookrightarrow$ Por convenção nomeamos as variáveis aleatórias com letras maiúsculas e seus possíveis valores com a mesma letra só que minúscula.

# Esperança

$\hookrightarrow$ Quando estamos falando de variáveis discretas aleatória, que possuem uma distribuição de probabilidade composta pela probabilidade de cada valor ser assumido temos a chamada Esperança, que representa uma média ponderada de todos os valores possíveis de $X$, onde o peso é a probabilidade do valor ocorrer:

$$
\mu = E(X) = \sum_{i=0} ^n x_iP(X=x_i)
$$

<aside>
<img src="Varia%CC%81veis%20Discretas%20Aleato%CC%81rias%20cd1bb274dadb496f921ed161527a9b1c/Hifumi_Surprised.png" alt="Varia%CC%81veis%20Discretas%20Aleato%CC%81rias%20cd1bb274dadb496f921ed161527a9b1c/Hifumi_Surprised.png" width="40px" /> Podemos interpretar a esperança como a média dos valores assumidos depois de várias repetições de um experimento. (e.g a esperança de um lançamento de dado será $3.5$ $\therefore$ depois de muitos lançamentos a média dos valores obtidos será $3.5$)

</aside>

# Variância

$\hookrightarrow$ A esperança, como vimos anteriormente, nos dá a média pondera de todos os possíveis resultados da nossa variável pelas suas probabilidades.

$\hookrightarrow$ Isso entretanto não nos descreve a dispersão dos dados.

$\hookrightarrow$ Para isso temos a chamada variância → Que é uma medida de dispersão que mede a distância de cada valor da esperança do dataset.

$\hookrightarrow$ Algo importante de notarmos é que a variância é a soma do quadrado da distância pois como estamos medindo a distância até a esperança que é a média ela iria zerar (análogo como vimos na [variância de um dataset normal](Estati%CC%81stica%20Descritiva%20fdebb5e3cc5b419983a783460388824a.md)).

$$
\sigma^2 = Var(X) = \sum_{i=0}^n(x_i-\mu)^2p_i
$$

$\hookrightarrow$ Ou para facilitar na prática:

$$
\sigma^2 = Var(X) = E(X^2) - [E(X)]^2
$$

# Medidas de Posição para Variáveis Discretas Aleatórias

## Mediana (Md)

- A moda será um valor, não necessariamente de $X$, que satisfaz:
    
    $$
    P(X \ge Md) \ge \frac{1}{2} \\ 
    P(X \le Md) \ge \frac{1}{2}
    $$
    

## Moda (Mo)

- Já a moda de uma variável aleatória discreta será o valor de $X$ que possui a maior probabilidade.