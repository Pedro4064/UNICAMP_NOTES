# Variáveis Aleatórias Contínuas

Created: June 13, 2022 3:22 PM
Tags: P2

[Anotações de Aula](Varia%CC%81veis%20Aleato%CC%81rias%20Conti%CC%81nuas%20fa0129a20f6e423bb597767fac2e7928/Anotac%CC%A7o%CC%83es%20de%20Aula%20c14dcd36a18e4289861b1d952cc2933d.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Dizemos que uma variável aleatória é contínua quando existe a possibilidade de assumir qualquer valor dentro de um intervalo (podendo esse intervalo ser o dos números inteiros por completo ou um sub-conjunto).

$\hookrightarrow$ Para esse tipo de variável aleatória nós temos o conceito de Função de Densidade de Probabilidade (f.d.p).

# Função de Densidade de Probabilidade

$\hookrightarrow$ A função de densidade de probabilidade é uma função contínua, dentro de um intervalo de interesse,

$\hookrightarrow$ A integral de tal função representa a probabilidade do evento acontecer. 

$\hookrightarrow$ Mais especificamente, se integrarmos tomando como limites de integração $a$ e $b$, estaremos vendo a probabilidade:

$$
P(a \le X \le b)  = \int^b_a f(x) dx
$$

![Screen Shot 2022-06-13 at 3.26.07 PM.png](Varia%CC%81veis%20Aleato%CC%81rias%20Conti%CC%81nuas%20fa0129a20f6e423bb597767fac2e7928/Screen_Shot_2022-06-13_at_3.26.07_PM.png)

<aside>
<img src="Varia%CC%81veis%20Aleato%CC%81rias%20Conti%CC%81nuas%20fa0129a20f6e423bb597767fac2e7928/Hifumi_Surprised.png" alt="Varia%CC%81veis%20Aleato%CC%81rias%20Conti%CC%81nuas%20fa0129a20f6e423bb597767fac2e7928/Hifumi_Surprised.png" width="40px" /> Lembrando que a integral tomando como limite de integração $a$ e $b$ nada mais é do que a área embaixo da curva da função de densidade de probabilidade

</aside>

## Propriedades

1. $f_x(x) \ge 0$
2. $P(X=x) = \int^x_x f_x(x)dx = 0$ 
3. $E(x) = \int ^\infty _{-\infty} x f_x(x)dx$ → Esperança de $x$
4. $E(x) = \int ^\infty _{-\infty} x^2 f_x(x)dx$ → Esperança de $x^2$

e. $\int ^\infty _{-\infty} f_x(x) dx = 1$

f. $P(X\le x) = \int ^x_{-\infty}f_x(x) dx$ → Probabilidade Acumulada

g. $V(x) = E(x^2) - E^2(x)$ → Variância de $x$

## Principais Distribuições

### Distribuição Uniforme

![Screen Shot 2022-06-13 at 3.38.45 PM.png](Varia%CC%81veis%20Aleato%CC%81rias%20Conti%CC%81nuas%20fa0129a20f6e423bb597767fac2e7928/Screen_Shot_2022-06-13_at_3.38.45_PM.png)

$\hookrightarrow$ $f_x(x) = \frac{1}{b-a};  \ \ \ \ \ \ \ a\le x\le b$

$\hookrightarrow$ $X = U(a, b)$

$\hookrightarrow$ $E(X) = \frac{b+a}{2}$

$\hookrightarrow$ $V(X) = \frac{(b-a)^{2}}{12}$

### Distribuição Exponencial

![Screen Shot 2022-06-13 at 3.41.36 PM.png](Varia%CC%81veis%20Aleato%CC%81rias%20Conti%CC%81nuas%20fa0129a20f6e423bb597767fac2e7928/Screen_Shot_2022-06-13_at_3.41.36_PM.png)

$\hookrightarrow$ Pode ser interpretada como o "Contrário de Poisson” pois pergunta o tempo entre um número de acontecimentos enquanto Poisson vê o número em um intervalo

$\hookrightarrow$ $X = Exp(\lambda)$

$\hookrightarrow$ $f_x(x) = \lambda e^{-\lambda x} ; \ \ x>0$

$\hookrightarrow$ $F(x) = f_x(X \le x) = 1-e^{-\lambda x}$ → A função de probabilidade acumulada

$\hookrightarrow$ $E(x) = 1/\lambda$

$\hookrightarrow$ $V(x) = 1/\lambda^2$

$\hookrightarrow$ Onde:

- $\lambda$ → Taxa temporal
- $x$ → Var. Aleatória = Intervalo de tempo

### Distribuição Normal

$\hookrightarrow$ Notação → $X = \mathcal{N}(\mu, \sigma^2)$

$\hookrightarrow$ Densidade:

$$
f_x(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left\{ - \frac{(x  - \mu)^2}{2\sigma^2}\right\}
$$

$\hookrightarrow$ $E(X) = \mu$

$\hookrightarrow$ $V(X) = \sigma^2$

### Distribuição Normal - Padrão

- Quando estamos falando de Distribuição Normal temos uma em específica que serve como base para o calculo de outras distribuições normais por já termos tabelado os valores de suas integrais, a chamada de distribuição **Normal Padrão**, que é dada por:

$$
Z \sim \mathcal{N}(\underbrace{0}_{\mu}, \overbrace{1}^{\sigma^2})
$$

- Somos capazes de normalizar qualquer normal e utilizar tais valores tabelados através da seguinte operação:

$$
X \sim \mathcal N(\mu, \sigma^2) \Rightarrow Z = \frac{X - \mu}{\sigma} \sim \mathcal N(0, 1)
$$