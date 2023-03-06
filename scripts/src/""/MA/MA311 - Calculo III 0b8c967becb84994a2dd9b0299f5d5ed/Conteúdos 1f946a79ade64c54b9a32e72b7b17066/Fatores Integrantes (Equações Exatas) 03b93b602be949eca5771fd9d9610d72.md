# Fatores Integrantes (Equações Exatas)

Aula: Aula 3
Created: March 29, 2021 8:15 PM
Prova: P1

# Introdução

Algumas vezes, é possível tornar uma EDO que **não** é exata em uma EDO exata, multiplicando-a por um fator integrante $\mu(x, y)$ apropriado.

# Encontrando o Fator Integrante

$$
\mu(x) = \exp \left(\int \frac{M_y - N_x}{N} dx \right) \iff  só \ depender\ de\ x
$$

$$
\mu(y) = \exp \left(\int \frac{N_x - M_y}{M} dy \right) \iff  só \ depender\ de\ y
$$

- Assim multiplicamos ambos os lados da nossa $EDO$ pelo fator integrante, e teremos uma equação exata, que podemos resolver normalmente como [mostrado anteriormente](Equac%CC%A7o%CC%83es%20Exatas%200f143b276ede4b70b428de610b67dbc1.md).