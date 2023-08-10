# Revisão de Circuitos

Created: March 16, 2022 2:01 PM
Prova: P1

- SUMMARY

# Principais Bipolos

## Indutores

$\hookrightarrow$ Um indutor, no primeiro momento, impede a passagem de corrente, mas conforme entra em estado de equilíbrio (DC) ele age como um curto.

$\hookrightarrow$ Em contra partida, em um cenário de alta frequência (AC) ele age como um circuito aberto.

## Capacitores

$\hookrightarrow$ Um capacitor, em diferente do indutor, no primeiro momento ele possibilita a passagem de corrente, mas no momento que ele fica carregado ele age como um circuito aberto.

$\hookrightarrow$ Já em um cenário de alta frequência ele age como um curto, apresentando uma desvio de fase (a corrente está adiantado em até $90^{\circ}$).

# Leis de Kirchhoff

## 1º Lei

$\hookrightarrow$ A soma das correntes que entram em um nós precisa ser a mesma que sai.

## 2º Lei

$\hookrightarrow$ A somas das tensões em uma malha fechada deve ser nula

# Impedância Complexa

$\hookrightarrow$ Para alguns bipolos, mais notoriamente o capacitor e o indutor, a sua impedância é representa por números complexos, sendo:

- **Capacitor**
    
    $$
    Z_c = \frac{1}{j \omega c}
    $$
    
- **Indutor**
    
    $$
    Z_l = j \omega L
    $$
    

$\hookrightarrow$ Sendo $\omega$ a frequência, e isso está de acordo com o que foi dito anteriormente, que quando a frequência $\omega \rightarrow \infty$ para um capacitor a impedância (i.e a resistência a passagem de corrente) tende a zero (logo é tratado como um curto) enquanto para um indutor a impedância $Z_l \rightarrow \infty$ logo é tratado como um circuito aberto.

# Superposição

 $\hookrightarrow$ Assumindo que um circuito é composto por:

1. Fontes independentes 
2. Bipolos lineares (i.e resistores, capacitores ou indutores)

$\hookrightarrow$ Nós somos capazes de aplicar a teoria de superposição, isso é, estudarmos os efeitos de cada fonte separadamente, como:

![Screen Shot 2022-03-16 at 2.45.44 PM.png](Revisa%CC%83o%20de%20Circuitos%20dd9c107187a24ab2b1a9bf0dd9184255/Screen_Shot_2022-03-16_at_2.45.44_PM.png)

→ Nesse circuito, poderemos desconsiderar a fonte de corrente e considerar um circuito aberto onde ele está, fazer as equações necessárias.

→ Depois podemos desconsiderar a fonte de tensão como sendo um curto.

 

# Circuitos Equivalentes

## Thevenim

## Norton