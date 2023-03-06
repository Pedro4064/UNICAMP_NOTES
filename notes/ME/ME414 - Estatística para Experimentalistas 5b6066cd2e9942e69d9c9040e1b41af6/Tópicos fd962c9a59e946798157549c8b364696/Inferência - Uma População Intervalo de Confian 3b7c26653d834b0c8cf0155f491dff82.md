# Inferência - Uma População: Intervalo de Confiança

Created: July 11, 2022 3:49 PM
Tags: P2

[Anotações de Aula](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Intervalo%20de%20Confian%203b7c26653d834b0c8cf0155f491dff82/Anotac%CC%A7o%CC%83es%20de%20Aula%201d554d076a1349a885a85c680894df9b.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Vimos, anteriormente, que podemos utilizar uma estatística, como $\bar X(\hat p)$, para estimar um parâmetro populacional, como a média populacional $\mu$.

$\hookrightarrow$ Após coletarmos nossa amostra calcularemos nosso $\bar x$, que é a estimativa para $\mu$  populacional.

$\hookrightarrow$ Ao fazermos isso, entretanto, estamos estimando o comportamento populacional somente a partir de uma amostra, o que significa que se pegarmos outra amostra esse comportamento pode, e muito provavelmente irá, mudar.

$\hookrightarrow$ Levando isso em consideração é ideal não reportar somente a estimativa, mas também sua precisão. Podemos fazer isso de duas formas:

- Fornecer, juntamente com a estimativa, o seu erro padrão.
- Fornecer um intervalo de valores plausíveis, chamado de intervalo de de confiança.

# Intervalo de Confiança como Estimativa de $p$

$\hookrightarrow$ Como dito, somos capazes de fornecer um intervalo de confiança para uma estimativa sobre uma população.

$\hookrightarrow$ Tomando, por exemplo, uma população com uma proporção $p$ e variância $p(1-p)$, ambos desconhecidos, ao se retirar uma amostra aleatória de tamanho $n$ e calcular a proporção $\hat p$ (dessa amostra, e não da população), temos então que $\hat p$ é a estimativa para o parâmetro populacional desconhecido $p$, que possui a seguinte propriedade:

$$
\begin{aligned}
E(\hat p ) &= p \\ 
Var(\hat p ) &=\frac{p(1-p)}{n} \\ 
EP(\hat p ) &= \sqrt{\frac{p(1-p)}{n}}
\end{aligned}
$$

$\hookrightarrow$ Onde:

- $E$ → Esperança
- $Var$ → Variância
- $EP$ → Erro padrão

$\hookrightarrow$ Além disso, pelo teorema do limite central temos que:

$$
\hat p \sim \mathcal N\left(p, \frac{p(1-p)}{n}\right)
$$

$\hookrightarrow$ Isso é extremamente valioso, pois ao seguir uma normal conseguimos identificar o intervalo que haja $x\%$ dos possíveis valores dentro dele, como ilustrado na imagem ao lado:

![Screen Shot 2022-07-11 at 4.14.38 PM.png](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Intervalo%20de%20Confian%203b7c26653d834b0c8cf0155f491dff82/Screen_Shot_2022-07-11_at_4.14.38_PM.png)

$\hookrightarrow$ Com isso, a porcentagem acima é o que chamamos de porcentagem de confiança.

<aside>
<img src="Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Intervalo%20de%20Confian%203b7c26653d834b0c8cf0155f491dff82/mugi.gif" alt="Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Intervalo%20de%20Confian%203b7c26653d834b0c8cf0155f491dff82/mugi.gif" width="40px" /> Basicamente por ser uma normal nós facilmente encontramos as extremidades do intervalo de confiança de $x\%$, que nada mais é do que " $x\%$ de qualquer amostra estar dentro desse intervalo”

</aside>

$\hookrightarrow$ A fórmula para o intervalo de de confiança é dado por:

$$
IC(p, (1-\alpha) \%) = \left[ \hat p - z_{a/2}\sqrt{\frac{p(1-p)}{n}} ; \hat p + z_{a/2}\sqrt{\frac{p(1-p)}{n}} \right]
$$

$\hookrightarrow$ Onde o $z_{a/2}$ é o chamado multiplicador, e é obtido analizando a tabela da normal padrão para o valor de $(1-\alpha/2)\%$.

$\hookrightarrow$ Um exemplo é, se quisermos um intervalo de confiança de $95\% \therefore \alpha = 5 \therefore$ a porcentagem que temos que olhar na tabela é de $97.5\% \Rightarrow M=1.96$ 

$\hookrightarrow$ Ao observamos atentamente, entretanto, não temos $p$ (que representa a proporção da população total. Para resolvermos esse problema temos duas possibilidades:

### Aproximação Arriscada

- Simplesmente aproximamos $p \approx \hat p$  e  substituímos na fórmula.

### Aproximação Conservadora

$$
\frac{p(1-p)}{n}\approx \frac{1}{4n}
$$

# Intervalo de de Confiança Como Estimativa de $\mu$

$\hookrightarrow$ Um caso específico do relatado acima é quando queremos encontrar, em um certo intervalo de de confiança, a média $\mu$ da população (Tratando de uma variável continua, e não mais binários como possui ou não uma característica).

$\hookrightarrow$ Analisando o exemplo anterior temos que:

$$
IC(\mu, 1-\alpha) = \left[\bar x - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}; \bar x +z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \right]
$$

$\hookrightarrow$ A partir disso, temos duas possíveis análises:

### $\sigma$ Conhecido

- Se a variância (e por conseguinte o desvio padrão) da população for conhecido podemos simplesmente substituir na fórmula e analisar a partir da normal.

### $\sigma$  Desconhecido

- Se a variância for desconhecida, devemos utilizar a variância amostrar $s^2$:

$$
s^2 = \frac{1}{n-1}\sum (x_i - \bar x)^2
$$

- E a partir disso utilizar a aproximação da distribuição $t-$Student, e não a normal.
- A t-student possui, além do $\alpha/2$, outro parâmetro, chamado de graus de liberdade, que é dado por $n-1$.
- É importante, também, lembrar que quanto maior o $n$ mais próximo da normal $t-$Student fica.