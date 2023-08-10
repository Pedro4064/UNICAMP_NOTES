# Equações Não Homogêneas com Coeficientes Constantes e o Método dos Coeficientes Indeterminados

Aula: Aula 7
Created: April 14, 2021 10:52 AM
Prova: P1

# O que É uma Equação não homogênea?

- Uma EDO é dita não homogênea quando não está igualada a zero, como na forma:

$$
y'' + p(x)y' + q(x) = \underbrace{f(x)}_{\ne 0}
$$

- Importante frisar que pode ser de ordem maior que dois.

# Solução Geral

- Para achar a solução geral da EDO não homogênea, precisamos:
    1. Obter a solução geral $y_h$ da equação homogênea associada, que seria a versão da EDO em  questão mas com $f(x) = 0$, onde podemos usar os métodos citados nos capítulos anteriores de como resolver;
    2. Obter uma solução particular $y_p$ da equação não homogênea, pelo método dos coeficientes indeterminados ou pelo método variação de parâmetros;
    3. A solução geral da equação não homogênea é dada por:
    
    $$
    y = y_h + y_p
    $$
    

## Métodos dos Coeficientes Indeterminados

- Como dito anteriormente, para acharmos $y_p$, a solução particular da não homogênea, podemos utilizar o método dos coeficientes Indeterminados ou o método de variação de parâmetros. Para utilizarmos o método dos coeficientes indeterminados, entretanto, existe um critério que a função $f(x)$ deve seguir . Ela seria:

<aside>
<img src="Equac%CC%A7o%CC%83es%20Na%CC%83o%20Homoge%CC%82neas%20com%20Coeficientes%20Const%20d7bd739d467b4ac2b430270adf67cb62/mugi.gif" alt="Equac%CC%A7o%CC%83es%20Na%CC%83o%20Homoge%CC%82neas%20com%20Coeficientes%20Const%20d7bd739d467b4ac2b430270adf67cb62/mugi.gif" width="40px" /> $f(x)$ deve ser a soma de funções do tipo: 

1. Polinomial;
2. Produto de Polinômios por exponenciais;
3. Produto de polinômios por exponenciais ou seno/coseno.

</aside>

<aside>
<img src="Equac%CC%A7o%CC%83es%20Na%CC%83o%20Homoge%CC%82neas%20com%20Coeficientes%20Const%20d7bd739d467b4ac2b430270adf67cb62/Evangelion.gif" alt="Equac%CC%A7o%CC%83es%20Na%CC%83o%20Homoge%CC%82neas%20com%20Coeficientes%20Const%20d7bd739d467b4ac2b430270adf67cb62/Evangelion.gif" width="40px" /> Os coeficientes não podem estar em função $x$ !!!!!

</aside>

- Se a função $f(x)$ não pertencer à classe de funções acima, deverá utilizar o método de variação de parâmetros.

## Achando as soluções

- Levando em consideração que $f(x)$ é uma soma de funções dos $3$ tipos citados anteriormente, podemos descrever $f(x)$ como sendo:

$$
f(x) = f_1(x) + ...+f_k(x)
$$

- Com isso temos que a solução $y_p = y_{p_1} + ... + y_{p_2}$, isso é, a soma das soluções de cada função que compõe $f(x)$.
- A forma de achar a solução de cada $f_i(x)$ que compões nossa $f(x)$, entretanto, muda dependendo de qual tipo ela é. As formas são:

- Tipo 1 - $f_i(x)$ é uma função polinomial;
    - $f_i(x) = b_mx^m + ...+ b_1x + b_0$
    - A solução de $f_i(x)$ tem o seguinte formato:
    
    $$
    \boxed{y_{p_i}(x) = x^s(A_mx^m + ... + A_1x + A_0)}
    $$
    
    - Onde $s$ é a multiplicidade de $r = 0$ como raiz da equação característica da EDO homogênea associada. (OBS: Se não for raiz, a multiplicidade será $0$).
    - Assim que tivermos $y_{p_i}$, ela estará em função das constantes $A_n$, para descobrirmos elas precisamos substituir $y_{p_{i}}$ na nossa EDO para acharmos seus valores.
    
- Tipo 2 - $f_i(x)$ é um produto de polinômios por exponenciais;
    - $f_i(x) = P_m(x)e^{ax}$
    - A solução de $f_i(x)$  tem o seguinte formato:
    
    $$
    \boxed{y_{p_i}(x) = x^s(A_mx^m + ... + A_1x + A_0) e^{ax}}
    $$
    
    - Onde $s$ é a multiplicidade de $r=a$ como raiz da equação característica da EDO homogênea associada.
    - Assim que tivermos $y_{p_i}$, ela estará em função das constantes $A_n$, para descobrirmos elas precisamos substituir $y_{p_{i}}$ na nossa EDO para acharmos seus valores.
    
- Tipo 3 - $f_i(x)$ é um produto de polinômios por exponenciais ou seno/coseno.
    - $f_i(x) = P_m(x)e^{ax}\sin(\beta x)$ ou $f_i(x) = P_m(x)e^{ax}\cos(\beta x)$
    - A solução de $f_i(x)$ tem o seguinte formato:
    
    $$
    \boxed{y_{p_i}(x) = x^s(A_mx^m + ... + A_1x + A_0) e^{ax}\cos(\beta x) + x^s(B_mx^m + ... + B_1x + B_0) e^{ax}\sin(\beta x)}
    $$
    
    - Onde $s$ é a multiplicidade de $r=a + i\beta$ como raiz da equação característica da EDO homogênea associada.
    - ssim que tivermos $y_{p_i}$, ela estará em função das constantes $A_n$ e $B_n$ , para descobrirmos elas precisamos substituir $y_{p_{i}}$ na nossa EDO para acharmos seus valores.