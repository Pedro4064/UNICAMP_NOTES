# Séries de Potências

Aula: Aula 16
Created: June 1, 2021 10:27 AM
Prova: P2

# O que são ?

$\hookrightarrow$ Série de potência nada mais é do que um polinômio (ou uma potência) escrito condensadamente em um somatório:

$$
c_0 + c_1x + c_2 x^2 + ... = \sum^{\infty}_{n=0} c_nx^n
$$

$\hookrightarrow$ Onde $c_n$ são os coeficientes do polinômio e os coeficientes da série.

# Convergência de Séries de Potências

$\hookrightarrow$ Diferentemente de séries normais, séries de potência apresentam a incógnita $x$.

$\hookrightarrow$ Tendo isso em vista, o caráter convergente  ou divergente de tais séries é possível de ser encontrada somente em função de $x$, por isso falamos em intervalo e raio de convergência:

1. O intervalo é a informação de quais valores de $x$ dentro de um conjunto a série converge.
2. O raio é o resultado do somatório desse conjunto contido no intervalo → Pode ser considerado a distância do centro da série até um limite do intervalo de convergência.

## Teste da razão para achar o raio

$\hookrightarrow$ Somos capazes de achar o raio pelo teste da razão, que consiste em:

$$
\lim_{n\rightarrow\infty} \left|\frac{a_{n+1}}{a_n}\right| = L
$$

$\hookrightarrow$ Onde temos que $L$ precisa ser maior ou igual a zero e menor que um para que seja convergente. 

$\hookrightarrow$ Com isso, somos capazes de determinar o raio pela relação: 

$$
R = \frac{1}{L}
$$