# Norma de um Vetor e Distância entre dois Vetores

Semana: Semana 11

# Norma de Um Vetor

- Primeiramente, norma é a mesma coisa que módulo de um vetor.
- Levando em consideração o produto interno de um vetor com ele mesmo, sendo $u = (u_1,...,u_n)$:

$$
\lang u,v\rang = u_1(u_1)+...+u_n(u_n)\Rightarrow \lang u,v\rang = u^2_1+...+u^2_n
$$

Considerando a definição do módulo de um vetor:

$$
||u|| = \sqrt{u_1^2+...+u_n^2} \Rightarrow ||u||^{2} = u_1^2 + ...+ u_n^2
$$

Juntando a expressão do módulo com a expressão do produto interno, temos que:

$$
\boxed{||u|| = \sqrt{\lang u,u\rang}}
$$

<aside>
<img src="Norma%20de%20um%20Vetor%20e%20Dista%CC%82ncia%20entre%20dois%20Vetores%2062e0965bc40d446d87d50f1fbfc1dcbc/8026_Anime_Surprised.png" alt="Norma%20de%20um%20Vetor%20e%20Dista%CC%82ncia%20entre%20dois%20Vetores%2062e0965bc40d446d87d50f1fbfc1dcbc/8026_Anime_Surprised.png" width="40px" /> Se o módulo $||u|| = 1$ dizemos que o vetor é unitário

</aside>

<aside>
<img src="Norma%20de%20um%20Vetor%20e%20Dista%CC%82ncia%20entre%20dois%20Vetores%2062e0965bc40d446d87d50f1fbfc1dcbc/sagiriBleh.png" alt="Norma%20de%20um%20Vetor%20e%20Dista%CC%82ncia%20entre%20dois%20Vetores%2062e0965bc40d446d87d50f1fbfc1dcbc/sagiriBleh.png" width="40px" /> Se um vetor não for unitário, podemos transforma-lo em um simplesmente multiplicando pelo inverso da norma: $\hat{u} = u (\frac{1}{||u||})$

</aside>

# Distância entre dois vetores

- A distância entre dois vetores nada mais é do que a norma de sua diferença:
    
    $$
    d(u,v) = ||u-v||
    $$
    

# Propriedades da Norma e da Distância

- $||0|| = 0 \rightarrow$  A norma do vetor nulo é zero;
- $||v|| = 0 \iff v = 0$;
- $||\alpha v|| = |\alpha| \cdot||v||, \forall \alpha \in \R$
- $d(u,v) = 0 \iff u=v$
- $d(u,v) \ge 0$
- $d(v,0) = ||v||$