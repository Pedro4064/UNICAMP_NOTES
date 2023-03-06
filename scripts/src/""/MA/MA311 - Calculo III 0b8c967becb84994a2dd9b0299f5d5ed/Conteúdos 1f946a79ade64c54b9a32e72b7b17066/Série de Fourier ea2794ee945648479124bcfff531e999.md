# Série de Fourier

Created: July 3, 2021 10:29 AM
Prova: P2

# Fórmula Geral

$$
\frac{a_0}{2} + \sum ^{\infty}_{n=1}\left(a_n \cos \frac{n\pi x}{L}  +b_n\sin \frac{n\pi x}{L}\right)
$$

- Onde:

$$
a_n = \frac{1}{L} \int^L_{-L}f(x) \cos \frac{n\pi x}{L}dx, n=0,1,2...
$$

$$
b_n = \frac{1}{L} \int^L_{-L}f(x) \sin \frac{n\pi x}{L}dx, n=0,1,2...
$$

# Teorema de Convergência de Fourier

<aside>
<img src="Se%CC%81rie%20de%20Fourier%20ea2794ee945648479124bcfff531e999/mugi.gif" alt="Se%CC%81rie%20de%20Fourier%20ea2794ee945648479124bcfff531e999/mugi.gif" width="40px" /> A série de Fourier é igual à função $f(x)$ onde a função $f$ for contínua. Mas em pontos de descontinuidade, a série assume o valor do ponto médio da descontinuidade.

</aside>

# Tips

## Funções Pares

- Para $f(x)$ como uma função par temos que:

$$
a_n = \frac{2}{L} \int^L_0 f(x) \cos(\frac{n\pi x}{L}) dx
$$

$$
b_n = 0
$$

## Funções Ímpares

- Para $f(x)$  como uma função ímpar temos que:

$$
a_n = 0
$$

$$
b_n = \frac{2}{L}\int^L_0 f(x) \sin \frac{n\pi x}{L}dx
$$