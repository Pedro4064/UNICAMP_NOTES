# Sequências Numéricas

Aula: Aula 14
Created: May 23, 2021 10:19 AM
Prova: P2

# O que são?

- Uma lista ordenada de números reais:

$$
a_1, a_2, a_3, ...,a_n,...
$$

- De infinitos elementos, os quais podem ser representados como:

$$
\{a_n\} \ ou\ \{a_n\}_{n=1}^{\infty}
$$

# Termo Geral

- Podemos ainda definir uma sequência apresentado uma fórmula para o termo geral ($n$ - ésimo termo), como por exemplo:
    
    $$
    \left\{ \frac{n}{n+1}\right\}^\infty _{n = 1} = \left\{ \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, ...\right\}
    $$
    

# Limite de uma Sequência

Uma sequência $\{a_n\}_{n=1}^{\infty}$ tem um limite $L \in \R$ e escrevemos: 

$$
\lim_{n\rightarrow \infty} a_n = L
$$

Se o limite existir e for finito, dizemos que a sequência converge (ou é convergente). Caso contrário dizemos que a sequência diverge (ou é divergente).

## Propriedades de Limite

1. $\lim_{n \rightarrow \infty}(a_n \pm b_n) = \lim_{n \rightarrow \infty}(a_n) \pm \lim_{n \rightarrow \infty}(b_n)$
2. $\lim_{n \rightarrow \infty}(ca_n) = c \cdot \lim_{n \rightarrow \infty}(a_n)$
3. $\lim_{n \rightarrow \infty} (a_nb_n) = \lim_{n \rightarrow \infty}(a_n) \cdot \lim_{n \rightarrow \infty}(b_n)$
4. $\lim_{n \rightarrow \infty}(a_n^p) = (\lim_{n \rightarrow \infty}(a_n))^p$
5. $\lim_{n \rightarrow \infty} \left(\frac{a_n}{b_n}\right) = \frac{\lim_{n \rightarrow \infty} (a_n)}{\lim_{n \rightarrow \infty}(b_n)}$

Além disso temos que o teorema de confronto também se aplica!

## Propriedade de limites de funções

Se $\lim _{n\rightarrow \infty} a_n = L$ e $f$ é uma função contínua em $L$, então: 

$$
\lim_{n \rightarrow \infty} f(a_n) = f(L)
$$

### Exemplo

$$
\lim _{n\rightarrow \infty} \cos(\pi/n)=\cos\left(\lim _{n\rightarrow \infty}(\pi/n) \right) = cos (0) = 1
$$

# Sequência monótona

Uma sequência é:

1. Crescente se $a_n < a_{n+1}$, para todo $n \ge 1$
2. Decrescente se $a_n > a_{n+1}$, para todo $n \ge 1$

A sequência é dita monótona se for crescente ou decrescente.

## Exemplo

Mostre que a sequência $\left\{a_n = \frac{n}{n^2 + 1} \right\}^\infty_{n=1}$ é decrescente:

- Temos que é decrescente se:

$$
\begin{aligned}
a_n &> a_{n+1} \\ 
\frac{n}{n^2 + 1} &> \frac{(n+1)}{(n+1)^2 + 1} \\ 
n[(n^2 + 1)+1] &> (n+1)(n^2 + 1) \\ 
n^2 + n &> 1, \forall n\ge 1 \therefore \ Decrescente
\end{aligned}
$$

# Sequência Limita

Uma sequência pode ser caracterizada em:

1. Limita superiormente, se existir um número $M$ tal que
    
    $$
    a_n \le M, \forall n\ge 1
    $$
    
2. Limitada inferiormente, se existir um número $m$ tal que:
    
    $$
    m \le a_n, \forall n\ge 1
    $$
    
3. Limitada, se for limitada superiormente e inferiormente.

<aside>
<img src="Seque%CC%82ncias%20Nume%CC%81ricas%205108e8d066774a9fba5a6821d828836c/mugi.gif" alt="Seque%CC%82ncias%20Nume%CC%81ricas%205108e8d066774a9fba5a6821d828836c/mugi.gif" width="40px" /> Toda sequência monótona limitada é convergente

</aside>