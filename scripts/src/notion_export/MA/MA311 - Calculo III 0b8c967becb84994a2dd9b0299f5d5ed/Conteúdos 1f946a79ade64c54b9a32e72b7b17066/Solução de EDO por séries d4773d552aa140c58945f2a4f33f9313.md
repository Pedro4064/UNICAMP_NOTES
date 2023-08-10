# Solução de EDO por séries

Created: June 18, 2021 10:09 AM
Prova: P2

# Ponto Ordinário

Podemos resolver uma EDO por séries somente se o ponto $x_0$ for ordinário, isso é, para uma $EDO$  da forma:

$$
P(x)y'' + Q(x)y' + R(x)y= 0
$$

o ponto $x_0$ é ordinário si e somente si $P(x_0) \ne 0$

# Forma de Resolver uma $EDO$ por Séries

1. Verificar que o ponto $x_0$ é ordinário ($P(x_0) \ne 0$)
2. Definir e substituir na $EDO$:
    
    $$
    \begin{cases}
    y(x) = \sum_{n=0}^\infty a_nx^n \\
    y'(x) = \sum_{n=1}^\infty na_nx^{n-1} \\ 
    y''(x) = \sum_{n=2}^\infty n(n-1)a_nx^{n-2}
    \end{cases}
    $$
    
3. Igualar as potências de $x$, em geral, por $x^n$. Quando adicionar algum valor no termo geral da série, subtrair o mesmo valor inicial do índice $n$.
4. Caso não sejam iguais, igualar os índices dos somatórios pelo maior, colocando para fora do somatório os termos correspondentes aos índices anteriores.
5. Juntar os somatórios e colocar $x^n$ em evidência.
6. Como $x^n \ne 0$, por ser um ponto ordinário, encontramos a relação de recorrência. Se houver termos fora do somatório, também devemos igualar a zero.
7. Calcular alguns $a_n$'s (usando as informações iniciais problema) e encontrar uma (ou mais de uma) expressão em função de $n$ que os defina.
8. Substituir na série de potências essa expressão para $a_n$

# TIPS

## Fatorial Par

$$
2^k k!
$$

## Fatorial Impar

$$
\frac{(2K + 1)!}{k!2^k}
$$

<aside>
<img src="Soluc%CC%A7a%CC%83o%20de%20EDO%20por%20se%CC%81ries%20d4773d552aa140c58945f2a4f33f9313/Evangelion.gif" alt="Soluc%CC%A7a%CC%83o%20de%20EDO%20por%20se%CC%81ries%20d4773d552aa140c58945f2a4f33f9313/Evangelion.gif" width="40px" /> OBS: Para Fatorial Impar, é ESSA FRAÇÃO, logo se for no denominador multiplique pelo inverso!!!!!

</aside>