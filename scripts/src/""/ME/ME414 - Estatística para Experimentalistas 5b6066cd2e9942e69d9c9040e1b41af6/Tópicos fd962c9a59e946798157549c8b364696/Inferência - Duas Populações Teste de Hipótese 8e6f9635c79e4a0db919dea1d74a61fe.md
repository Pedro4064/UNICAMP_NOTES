# Inferência - Duas Populações: Teste de Hipótese

Created: July 12, 2022 3:54 PM
Tags: P2

[Anotações de Aula](Infere%CC%82ncia%20-%20Duas%20Populac%CC%A7o%CC%83es%20Teste%20de%20Hipo%CC%81tese%208e6f9635c79e4a0db919dea1d74a61fe/Anotac%CC%A7o%CC%83es%20de%20Aula%20a8ba5c8be0324f16927238524c001f70.md)

- SUMMARY
    
    

# Teste de Hipótese para Diferença de duas Médias

$\hookrightarrow$ Nessa matéria iremos focar no caso onde $\sigma$  é desconhecido mas supostamente iguais.

$\hookrightarrow$ Com isso temos que nossa estatística ficará:

$$
T = \frac{(\bar X - \bar Y) - \overbrace{(\mu_1 - \mu_2)}^{\Delta _0}}{\sqrt{s_p^2\left(\frac{1}{n} + \frac{1}{m}\right)}} \sim t_{n+m-2}
$$

$\hookrightarrow$ Onde $\Delta_0$ será ditado pela hipótese nula, que na maioria das vezes dirá que $\Delta_0 = 0$.

$\hookrightarrow$ Além disso temos que:

$$
s_p = \frac{(n-1)s_1^2 + (m-1)s_2^2}{n+m-2}
$$

$\hookrightarrow$ A partir das nossas hipóteses formuladas, nossa estatística feita podemos calcular nosso $t_{obs}$ ao olharmos o valor na distribuição $t$-student e então vermos se rejeitamos a hipótese nula ($\iff$ $t_{obs} < \alpha$ )

# Teste de Hipótese para Duas Proporções

$\hookrightarrow$ Já para o teste de hipótese para duas proporções temos