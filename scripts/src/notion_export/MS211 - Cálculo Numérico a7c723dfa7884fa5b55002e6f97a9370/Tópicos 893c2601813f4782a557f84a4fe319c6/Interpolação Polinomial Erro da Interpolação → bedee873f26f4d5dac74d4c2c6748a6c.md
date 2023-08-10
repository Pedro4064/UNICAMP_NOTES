# Interpolação Polinomial:  Erro da Interpolação → Dados Discretos

Aula: Aula 26
Created: November 28, 2021 11:01 AM
Prova: P2

- SUMÁRIO

# Calculo

$\hookrightarrow$ Ao contrário do caso onde temos uma função contínua que aproxima dos dados tabelados, agora temos somente os dados descretos, o que significa que não temos o valor de $M_{n+1}$ (valor maximo da derivada de ordem $n+1$).

$\hookrightarrow$ Levando isso em consideração, iremos utilizar a aproximação da derivada de ordem $n+1$ pela máxima diferença divididas até a ordem $n+1$:

$$
\boxed{E_n(x) \approx \prod ^n_{k=0} |x - x_k|f_{max}}
$$

- Onde $f_{max}$ e a máxima diferença dividida em valor absoluto até a ordem $n+1$