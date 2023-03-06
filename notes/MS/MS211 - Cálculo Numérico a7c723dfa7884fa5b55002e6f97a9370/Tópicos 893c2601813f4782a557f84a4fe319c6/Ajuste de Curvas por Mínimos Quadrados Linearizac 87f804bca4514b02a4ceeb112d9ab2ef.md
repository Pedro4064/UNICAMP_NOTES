# Ajuste de Curvas por Mínimos Quadrados: Linearização

Aula: Aula 22
Created: November 24, 2021 9:53 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ Como dito anteriormente, mesmo quando alguns problemas não são lineares é interessante o considerarmos como tal pois facilita sua análise e seu calculo.

$\hookrightarrow$ Levando isso em consideração iremos analizar algumas formas de linearização.

# Exemplo

## Exemplo 1

$\hookrightarrow$ Levando em consideração um cenário onde:

$$
y(x) \approx \varphi(x) =  \alpha_1 e^{\alpha_2 x}
$$

$\hookrightarrow$ Isso é, nossa função $y$ é aproximada de uma função exponencial, somos capazes de fazer a transformação de variável para que ela fique linear, tal que:

$$
z = \ln (y) \approx \overbrace{ \ln (\alpha_1)}^{\beta_1} + \underbrace{\alpha_2}_ {\beta_2} x = \beta_1 + \beta_2 x
$$

$\hookrightarrow$ E nesse caso, em todo lugar que temos $y$ nas formulas iremos utilizar $\ln (y)$.

## Exemplo 2

$$
y(x) \approx \varphi (x) = \frac{1}{\alpha_1 + \alpha_2 x}
$$

$\hookrightarrow$ Tal que, para obtermos a linearidade teremos que:

$$
z =  \frac{1}{y} \approx \alpha_1 + \alpha_2 x
$$

$\hookrightarrow$ Que é linear, e que não recebem novos nomes pois são os mesmos $\alpha_1$ e $\alpha_2$. A única diferença é que iremos fazer a regressão para $\frac{1}{y}$ ao invés dos valores de $y$.

## Exemplo 3

$$
y(x) \approx \varphi (x) = \alpha_1 + \alpha_2 \cos(x)
$$

$\hookrightarrow$ Nesse exemplo precisamos fazer a transformação em $x$ e não em $y$ tal que:

$$
t = \cos(x) \therefore z = \alpha_1 + \alpha_2 t
$$

$\hookrightarrow$ E nesse caso iremos aplicar ([nas formulas](Ajuste%20de%20Curvas%20por%20Mi%CC%81nimos%20Quadrados%20Caso%20Linea%20b241eed20c4a44b8bf8e1d8a66eb378b.md)) os valores de $\cos (x)$ e não diretamente so valores de $x$ tabelados