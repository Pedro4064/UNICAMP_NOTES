# Forças Internas - Desenvolvidas em Elementos Estruturais

Capítulo: Cap. 7
Created: December 2, 2021 4:41 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Nesse capitulo iremos basicamente introduzir e explorar o assunto de forças internas utilizando a análise de seções desenvolvida no [tópico anterior](Ana%CC%81lise%20Estrutural%20-%20Trelic%CC%A7as%20%5BMe%CC%81todos%20das%20Sec%CC%A7%209cfe0f3ea09c4ba29b15579b44952e73.md). 

# Forças Internas

$\hookrightarrow$ Assim como dito anteriormente, para analisarmos as forças interna de uma estrutura nós iremos aplicar o método de análise de seções. 

$\hookrightarrow$ Quando aplicarmos tal método de análise, surgiram foças para representar as forças e momentos internos, sendo eles:

![Screen Shot 2021-12-02 at 4.46.42 PM.png](Forc%CC%A7as%20Internas%20-%20Desenvolvidas%20em%20Elementos%20Estr%2001965df0ab8645118caac68bf3fb64b3/Screen_Shot_2021-12-02_at_4.46.42_PM.png)

- Força Normal: Atuando normal a viga na região de corte.
- Força de Cisalhamento: Atuando tangente a região de corte.
- Momento  Fletor: Momento tendo como eixo o mesmo momento resultante de $V \times r$ sendo $V$ a Força de Cisalhamento e $r$ o vetor distância até o ponto de apoio.

# Procedimento de Análise

![Screen Shot 2021-12-02 at 5.06.16 PM.png](Forc%CC%A7as%20Internas%20-%20Desenvolvidas%20em%20Elementos%20Estr%2001965df0ab8645118caac68bf3fb64b3/Screen_Shot_2021-12-02_at_5.06.16_PM.png)

# Equações e Diagramas de Forças de Cisalhamento e de Momento  de Fletores

$\hookrightarrow$ As variações de $V$ (força de Cisalhamento) e $M$ (Momento de Fletores) como funções da posição $x$ ao longo da viga podem ser obtidas utilizando-se o método das seções discutido anteriormente. 

$\hookrightarrow$ Assim que plotarmos tais valores em função da posição $x$ temos os chamados diagramas de forças de cisalhamento e diagrama de momentos feltores.

$\hookrightarrow$ Tais funções são descont;inuas em todos os pontos onde ocorrem mudanças nas cargas distribuídas ou onde  forças ou momentos concentrados são aplicados. Tendo isso em vista as funções devem ser determinadas entre quaisquer descontinuidades de carregamento.

## Convenção de Sinais

$\hookrightarrow$ Para forças internas de cisalhamento temos que elas são, por convenção, positivas quando fazem o objeto girar no sentido horário.

$\hookrightarrow$ Já para momentos fletores internos, eles são considerados positivos quando eles causam compressão na parte superior da peça.

## Caso de Carregamento Distribuídos

$\hookrightarrow$ Para o caso de um carregamento $w(x)$ distribuído ao longo de uma viga de tamanho $l$ temos uma relação diferencial para a função de força de ciscilhamento e momentos fletores, sendo elas:

$$
\boxed{\frac{dV}{dx} = -w(x) }
$$

$$
\boxed{\frac{dM}{dx} = V}
$$