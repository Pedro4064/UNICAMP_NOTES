# Inferência - Duas Populações: Intervalo de Confiança

Created: July 12, 2022 2:35 PM
Tags: P2

[Anotações de Aula](Infere%CC%82ncia%20-%20Duas%20Populac%CC%A7o%CC%83es%20Intervalo%20de%20Confi%2044234fc0f577444e913eb7dd7a239553/Anotac%CC%A7o%CC%83es%20de%20Aula%20556abb2e062a432db199f86e15ebba71.md)

- SUMMARY
    
    

# Intervalo de Confiança para Diferença de Duas Médias

$\hookrightarrow$ Para um intervalo de confiança da diferença de duas médias, temos dois possíveis casos:

1. $\sigma^2$ conhecida
2. $\sigma^2$ desconhecida

$\hookrightarrow$ Nesse curso iremos estudar somente o caso onde a variância populacional é desconhecida, por ser o caso que mais acontece para experimentalistas.

$\hookrightarrow$ Nesse caso, o nosso intervalo de confiança é dado por:

$$
IC(\mu_1  - \mu_2, 1-\alpha) = (\bar x - \bar y)\pm t_{n+m-2, \alpha/2}\sqrt{s_p^2\left(\frac{1}{n} + \frac{1}{m}\right)}
$$

$\hookrightarrow$ Onde:

$$
s_p = \frac{(n-1)s_1^2 + (m-1)s_2^2}{n+m-2}
$$

<aside>
<img src="Infere%CC%82ncia%20-%20Duas%20Populac%CC%A7o%CC%83es%20Intervalo%20de%20Confi%2044234fc0f577444e913eb7dd7a239553/Evangelion.gif" alt="Infere%CC%82ncia%20-%20Duas%20Populac%CC%A7o%CC%83es%20Intervalo%20de%20Confi%2044234fc0f577444e913eb7dd7a239553/Evangelion.gif" width="40px" /> Importante Observar que o multiplicando $t$ é a partir da t-student com grau de liberdade $n+m-2$

</aside>

# Intervalo de Confiança para Diferença Duas proporções

$\hookrightarrow$ Já para o intervalo de confiança para a diferença de proporções temos:

$$
IC(p_1-p_2, 1-\alpha) = (\hat p_1 - \hat p_2) \pm z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1} + \frac{\hat p_2(1-\hat p_2)}{n_2}}
$$

<aside>
<img src="Infere%CC%82ncia%20-%20Duas%20Populac%CC%A7o%CC%83es%20Intervalo%20de%20Confi%2044234fc0f577444e913eb7dd7a239553/Evangelion%201.gif" alt="Infere%CC%82ncia%20-%20Duas%20Populac%CC%A7o%CC%83es%20Intervalo%20de%20Confi%2044234fc0f577444e913eb7dd7a239553/Evangelion%201.gif" width="40px" /> Importante Observar que o multiplicando $z$ é a partir da normal

</aside>