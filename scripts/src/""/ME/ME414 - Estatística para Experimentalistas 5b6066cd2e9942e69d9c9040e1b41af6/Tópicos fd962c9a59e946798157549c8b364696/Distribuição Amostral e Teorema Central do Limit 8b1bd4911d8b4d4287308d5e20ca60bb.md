# Distribuição Amostral e Teorema Central do Limite

Created: July 10, 2022 1:54 PM
Tags: P2

[Anotações de Aula](Distribuic%CC%A7a%CC%83o%20Amostral%20e%20Teorema%20Central%20do%20Limit%208b1bd4911d8b4d4287308d5e20ca60bb/Anotac%CC%A7o%CC%83es%20de%20Aula%20e2250946ab5a405aa3159e1350a24864.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$  Até o momento vimos a distribuição de uma variável aleatória qualquer. A partir de agora, vamos analisar variáveis aleatórias oriundas de amostras (i.e parte do total) para, então, inferirmos o comportamento da população.

$\hookrightarrow$  Isso é extremamente importante pois na vida real é quase impossível (ou então muito custoso) ao analisarmos uma certa característica da população irmos até cada indivíduo e fazer a pesquisa com ele. Fazemos, então, a pesquisa com parte da população para então, através de ferramentas estatísticas, inferirmos o comportamento da população total a partir de uma amostra.

# Conceitos Iniciais

## Estimador e Estatística

$\hookrightarrow$  Considerando $x_i$ como sendo a $i-$ésima pessoa da amostra de $n$ participantes, que pode assumir:

$$
x_i=\begin{cases}
0 \rightarrow Saudável \\ 
1 \rightarrow Doente
\end{cases}
$$

$\hookrightarrow$  Temos que:

$$
\bar x = \underbrace{\frac{1}{n}\sum x_i}_{Estatística} = \hat p
$$

$\hookrightarrow$  Onde:

- $\hat p$ → É a probabilidade, a partir da amostra, de estar doente (nesse caso). Chamada de **Estimador** ou **Estimativa**
- $\frac{1}{n}\sum x_i$ → A fórmula é chamada de **Estatística**

## Teorema Central do Limite

$\hookrightarrow$  O Teorema Central do Limite diz que:

> Independente da distribuição, a média vai seguir uma distribuição normal $\iff$ $Var(X) << \infty$
> 

$\hookrightarrow$  A partir disso, e ao observarmos que $\hat p$  nada mais é do que a média amostral $\bar x$. Podemos analizar $\hat p$ , assim como qualquer média amostral, como uma distribuição normal.

$\hookrightarrow$  No caso do nosso exemplo, onde $x$ segue uma distribuição de Bernoulli (por ser binário), tem:

$$
\begin{aligned}
E(\bar x) &= \frac{1}{n}\sum E(x) = p \\ 
V(\bar x) &= \frac{p(1- p)}{n}
\end{aligned}
$$

$\hookrightarrow$  Resultando em:

$$
\bar x = \hat p  \sim \mathcal N \left(p, \frac{p(1-  p)}{n}\right)
$$