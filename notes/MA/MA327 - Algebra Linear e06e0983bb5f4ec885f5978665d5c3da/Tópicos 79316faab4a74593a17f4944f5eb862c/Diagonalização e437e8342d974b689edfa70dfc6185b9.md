# Diagonalização

Semana: Semana 15

## Definição

<aside>
<img src="Diagonalizac%CC%A7a%CC%83o%20e437e8342d974b689edfa70dfc6185b9/sagiriBleh.png" alt="Diagonalizac%CC%A7a%CC%83o%20e437e8342d974b689edfa70dfc6185b9/sagiriBleh.png" width="40px" /> dizemos que uma matriz quadrada $A$ é **diagonalizável** se existe $P$ invertível tal que $P^{-1}AP = D$, com $D$ diagonal

</aside>

- Podemos reorganizar esa equação de tal forma:
    
    $$
    A = PDP^{-1}
    $$
    
    e a chamamos de decomposição espectral de uma Matriz.
    

<aside>
<img src="Diagonalizac%CC%A7a%CC%83o%20e437e8342d974b689edfa70dfc6185b9/8026_Anime_Surprised.png" alt="Diagonalizac%CC%A7a%CC%83o%20e437e8342d974b689edfa70dfc6185b9/8026_Anime_Surprised.png" width="40px" /> A Matriz $D$ é a **matriz coluna** dos **autovetores** da matriz

</aside>

- Com essa nova informação, conseguimos ver que:

<aside>
<img src="Diagonalizac%CC%A7a%CC%83o%20e437e8342d974b689edfa70dfc6185b9/LewdMegumin.png" alt="Diagonalizac%CC%A7a%CC%83o%20e437e8342d974b689edfa70dfc6185b9/LewdMegumin.png" width="40px" /> Diagonalizar uma matriz nada mais é do que representar sua transformação $T$ indo de uma base (normalmente a canônica) para a base dos **autovetores.**

</aside>

## Montar a Diagonalização

$$
D = P^{-1}AP
$$

- Onde $D$  é ma matriz com os autovalores de $A$ em sua diagonal;
- $P$ é a matriz coluna dos autovetores.

## Quando uma $TL$ é diagonalizável ?

- Uma Transformação Linear é diagonalizável $\iff$sua representação matricial for diagonalizável.
- Existe, entretanto, um método mais fácil de verificar se uma matriz $\boxed{A_{n\times n}}$ é ou não diagonalizável:
    1. Calcule os autovalores através das raízes do polinômio característico: $p(\lambda) = det(A - \lambda I)$.
    2. Encontre os autovetores para cada $\lambda$ .
    3. Junte todos os autovetores, se tivermos $n$ autovetores $LI$, então $A$ é diagonalizável.
    
    <aside>
    💡 Se todos seus autovalores forem distintos, então ela é diagonalizável, pois todos os autovetores associados a diferentes autovalores são linearmente independentes.
    
    </aside>