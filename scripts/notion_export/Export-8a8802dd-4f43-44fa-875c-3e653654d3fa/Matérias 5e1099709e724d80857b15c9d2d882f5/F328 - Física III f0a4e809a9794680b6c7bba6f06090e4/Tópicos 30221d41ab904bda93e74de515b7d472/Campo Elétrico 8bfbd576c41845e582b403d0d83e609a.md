# Campo Elétrico

Capítulo: 22
Semana: Semana 2

## O que é um campo elétrico?

- Um campo elétrico é um campo vetorial, construído pela distribuição de vetores, um para cada ponto de uma região em torno de um objeto eletricamente carregado.
- Um campo elétrico só depende de uma carga "fonte" para que gere um campo $\vec{E}$ em um ponto no espaço $p$.

$$
\vec{E} = \frac{\vec{F}}{q_0}
$$

## Linhas de Campo

- Uma forma de visualizar um campo elétrico.
- O número de linhas de campo é proporcional ao módulo do campo $\vec{E}$ nesse ponto $\therefore$ quanto mais próximo da fonte maior o número de linhas por unidade de área $\therefore$maior o campo.
- Cargas $+$ tem campo de afastamento.
- Cargas $-$ tem campo de aproximação.

![Campo%20Ele%CC%81trico%208bfbd576c41845e582b403d0d83e609a/Screen_Shot_2020-09-30_at_9.50.05_AM.png](Campo%20Ele%CC%81trico%208bfbd576c41845e582b403d0d83e609a/Screen_Shot_2020-09-30_at_9.50.05_AM.png)

## Campo Oriundo de Uma Carga Puntiforme

$$
\vec{E} = \frac{kq}{r^2} \hat{r}
$$

- Onde $q$ é a carga puntiforme;
- $r$ é a distância entre ponto e carga;
- $\hat{r}$ é o vetor versos que indica a direção do campo.

## Princípio de Superposição

- Assim como a força elétrica, o campo também segue o princípio de superposição, isso é, o campo resultante em um ponto $p$ é a soma vetorial de todos os campos, que agem de forma independentes umas das outras no ponto.

## Dipolo Elétrico  e Momento Dipolar

- Um dipolo elétrico é constituído de duas cargas que apresentam a mesma carga $q$ só que com sinais opostos, separados por uma distância $d$.
- O Momento Dipolar é o produto entre a carga $q$ e a distância $d$:

$$
p = d\cdot q
$$

- Normalmente calculamos o campo produzido por um dipolo em um ponto $z$ que está muito distante do dipolo  $z \ \texttt{>>} \ d$, com isso podemos utilizar a seguinte fórmula:

$$
E  = \frac{1}{2\pi \varepsilon_0}\frac{p}{z^3}
$$

## Campo Elétrico Produzido Por Uma Linha de Cargas

- Para problemas que envolvem uma distribuição cargas contínuas, é mais fácil pensarmos em uma densidade de cargas ao invés de carga total.

- O método é melhor explicado com um exemplo:

![Campo%20Ele%CC%81trico%208bfbd576c41845e582b403d0d83e609a/Screen_Shot_2020-09-30_at_10.13.01_AM.png](Campo%20Ele%CC%81trico%208bfbd576c41845e582b403d0d83e609a/Screen_Shot_2020-09-30_at_10.13.01_AM.png)

- Como dito anteriormente, é mais fácil pensarmos em uma densidade de cargas $\lambda = \frac{dq}{ds}$, onde $dq$ é a carga de um elemento e $ds$ é o comprimento desse elemento (nós dividimos o anel em infinitos elemento para que possamos trata-los como cargas puntiformes).
- Com isso podemos definir que a carga dessa unidade de anel infinitesimal é:
    
    $$
    dq = \lambda \cdot ds
    $$
    
- Essa carga produz um campo $d\vec{E}$ no ponto $p$, que está a uma distância $r$ do elemento.

$$
d\vec{E} = \frac{k\cdot dq}{r^2} = \frac{k \cdot \lambda \cdot ds}{r^2} = \frac{k \cdot \lambda \cdot ds}{(z^2 + R^2)}
$$

- Se observarmos, $d\vec{E}$ tem componentes no eixo $x$ e $y$. As componentes no eixo $x$, entretanto, são simétricas(por estarem distribuídas em uma circunferência) $\therefore$ se anulam, o que significa que o campo resultante no ponto é apenas a somatória das componentes $y$.
- Para  acharmos $d\vec{E}_y$ (componentes $y$ de $d\vec{E}$) podemos usar relações trigonométricas:

$$
\cos{\theta} = \frac{d\vec{E}_y}{d\vec{E}} \therefore d\vec{E}_y = d\vec{E} \cdot \cos{\theta}
$$

- Onde temos que:

$$
\cos{\theta} = \frac{z}{r} = \frac{z}{(z^2 + R^2)^{\frac{1}{2}}}
$$

- Substituindo temos:

 

$$
d\vec{E}_y = \frac{k \cdot \lambda \cdot ds}{(z^2 + R^2)} \cdot \frac{z}{(z^2 + R^2)^{\frac{1}{2}}}  
$$

- Precisamos agora somar todas as componentes $d\vec{E}_y$ em torno de todo anel, como é uma soma infinitesimal podemos integrar em relação a $ds$:

$$
E = \int \frac{k\lambda z}{(z^2 + R^2)^{\frac{3}{2}}} ds = \frac{k\lambda z}{(z^2 + R^2)^{\frac{3}{2}}} \int^{2\pi R}_{0} ds = \frac{k\lambda z (2 \pi R)}{(z^2 + R^2)^{\frac{3}{2}}}
$$

- Como $\lambda$ representa a carga por unidade e está sendo multiplicada por todo o comprimento ($2\pi R$) resulta e $q$ (a carga total) $\therefore$

$$
E = \frac{k z q}{(z^2 + R^2)^{\frac{3}{2}}}
$$

## Campo Elétrico Produzido por um Disco Carregado

![Campo%20Ele%CC%81trico%208bfbd576c41845e582b403d0d83e609a/Screen_Shot_2020-09-30_at_11.23.09_AM.png](Campo%20Ele%CC%81trico%208bfbd576c41845e582b403d0d83e609a/Screen_Shot_2020-09-30_at_11.23.09_AM.png)

- Podemos calcular pesando que o disco carregado não passa de infinitos anéis concêntricos(que já sabemos calcular).
- De forma análoga ao que fizemos nos anéis, podemos dividir o disco em infinitos elementos para que possamos considera-los cargas puntiformes.
- Temos $dq$ como a carga de um elemento;
- $\sigma$  é a densidade de cargas;
- $dA$ é a área de um elemento;

$$
\sigma = \frac{dq}{dA} \therefore dq = \sigma \cdot dA = \sigma \cdot (2\pi r dr)
$$

- Baseado na fórmula de $d\vec{E}$ encontrada no cálculo de campo em anéis temos a seguinte equação para discos (só trocamos $\lambda$ pro $\sigma$ , $ds$ por $2\pi rdr$ e $R$ por $r$):

$$
dE = \frac{\sigma z}{4\varepsilon_0} \frac{2rdr}{(z^2+r^2)^{\frac{3}{2}}}
$$

- Agora precisamos somente integrar para achar a soma de todos os campos para diferentes $r$:

$$
E = \frac{\sigma z}{4\varepsilon_0}\int_{0}^{R} (z^2+r^2)^{-\frac{3}{2}}(2r)dr
$$

- Podemos fazer essa integração por substituição, onde:

$$
z^2+r^2 = u\\du=0 + 2r dr \therefore dr = \frac{du}{2r}
$$

- Teríamos então:

$$
E = \frac{\sigma z}{4\varepsilon_0} \left[ \frac{(z^2 + r^2)^{-\frac{1}{2}}}{-\frac{1}{2}}\right]^{R}_{0}
$$

- Se completarmos teremos:

$$
E = \frac{\sigma}{2\varepsilon_0}\left(1 - \frac{z}{\sqrt{z^2 + R^2}}\right)
$$

<aside>
💡 OBS: Se o plano for infinito ($R \rightarrow \infty$) temos que $E = \frac{\sigma}{2\varepsilon_0}$.  Podemos ver então que quando o disco é infinito (em proporção a $z$, a distância entre placa e ponto não importa, temos então um campo contínuo)

</aside>