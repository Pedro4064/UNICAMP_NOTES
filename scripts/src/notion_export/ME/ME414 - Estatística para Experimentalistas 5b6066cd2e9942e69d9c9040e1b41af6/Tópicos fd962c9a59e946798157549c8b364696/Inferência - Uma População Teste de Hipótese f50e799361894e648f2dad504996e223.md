# Inferência - Uma População: Teste de Hipótese

Created: July 11, 2022 5:50 PM
Tags: P2

[Anotações de Aula](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Teste%20de%20Hipo%CC%81tese%20f50e799361894e648f2dad504996e223/Anotac%CC%A7o%CC%83es%20de%20Aula%20a5a914127c574ec999266170aa4069c9.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ O teste de hipóteses é uma ferramenta que utiliza a estatística para comparar, a partir de dados amostrais, duas hipóteses, sendo elas:

- Hipótese Nula $(H_0)$: Afirma que o parâmetro populacional assume um dado valor
- Hipótese Alternativa $(H_A)$: Afirma que o parâmetro populacional assume outros valores, diferentes do valor descrito por $H_0$

$\hookrightarrow$ Após a comparação, temos dois possíveis resultados, sendo eles:

- Rejeitamos a hipóteses nula
- Não podemos rejeitar a hipótese nula

$\hookrightarrow$ Podemos observar que nunca aceitamos a hipótese nula ou a hipótese alternativa, mas sim rejeitamos uma ou outra.

# Teste de Hipótese para uma Proporção

$\hookrightarrow$ Quando queremos aplicar o teste de hipótese para proporção temos as seguintes etapas:

## Definição de Hipóteses

- Como vimos anteriormente o teste de hipótese é feito para comparar duas hipóteses $\therefore$ devemos definir cada uma:
    
    ![Screen Shot 2022-07-11 at 6.06.52 PM.png](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Teste%20de%20Hipo%CC%81tese%20f50e799361894e648f2dad504996e223/Screen_Shot_2022-07-11_at_6.06.52_PM.png)
    

## Definir Estatística do Teste de $Z_{obs}$

- A partir de então definimos a estatística do nosso teste (i.e a fórmula), que é dada, para teste de proporção, por:

$$
Z = \frac{\hat p - p}{\sqrt{\frac{p(1-p)}{n}}}
$$

- Ao aplicar nossa hipótese nula, temos o que chamamos de $z_{osb}$, que segue uma normal $\mathcal N(0,1)$
    
    ![Screen Shot 2022-07-11 at 6.10.16 PM.png](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Teste%20de%20Hipo%CC%81tese%20f50e799361894e648f2dad504996e223/Screen_Shot_2022-07-11_at_6.10.16_PM.png)
    

## Valor-de-$p$

- Agora podemos calcular o que chamamos de valor-de-p, que será utilizado para compararmos as hipóteses:
    
    ![Screen Shot 2022-07-11 at 6.11.26 PM.png](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Teste%20de%20Hipo%CC%81tese%20f50e799361894e648f2dad504996e223/Screen_Shot_2022-07-11_at_6.11.26_PM.png)
    

## Conclusão

![Screen Shot 2022-07-11 at 6.12.32 PM.png](Infere%CC%82ncia%20-%20Uma%20Populac%CC%A7a%CC%83o%20Teste%20de%20Hipo%CC%81tese%20f50e799361894e648f2dad504996e223/Screen_Shot_2022-07-11_at_6.12.32_PM.png)

# Teste de Hipóteses para Média

$\hookrightarrow$ Análogo ao que foi feito para intervalo de confiança, para teste de hipótese também há um caso especial onde estamos tratando de algo contínuo e que precisamos fazer um teste para achar a média.

$\hookrightarrow$ O teste de hipótese para Média é dividido em dois casos:

## $\sigma$  Conhecido

- Quando $\sigma$ (e por consequência a variância populacional $\sigma^2$) é conhecida temos que nossa estatística é dada por:

$$
Z = \frac{\bar X - \mu}{\sigma / \sqrt{n}} \sim \mathcal N(0, 1)
$$

- E que nosso $z_{obs}$ basta substituirmos $\mu \rightarrow \mu_0$, isso é, a média da hipótese Nula.

## $\sigma$ Desconhecido

- Já para quando não se sabe a variância populacional temos que nossa estatística é:
    
    $$
    Z = \frac{\bar X - \mu}{s/ \sqrt{n}} \sim \mathcal t_{n-1}
    $$