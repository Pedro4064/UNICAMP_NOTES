# Núcleo e Imagem

Semana: Semana 9

# Núcleo

## O que é um núcleo de uma Transformação Linear ?

- O núcleo de uma $TL$ é o conjunto elementos que zeram ela.

> Tendo uma Transformação Linear $T:U\rightarrow V$, temos que seu núcleo $nuc(T)=\{u \in U | T(u)=0_v\}$
> 

<aside>
<img src="Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/a6ada7178c8b6b762e47f8ff1f841cfa.gif" alt="Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/a6ada7178c8b6b762e47f8ff1f841cfa.gif" width="40px" /> Os elementos do núcleo pertencem ao DOMÍNIO da transformação linear

</aside>

<aside>
<img src="Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/a6ada7178c8b6b762e47f8ff1f841cfa.gif" alt="Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/a6ada7178c8b6b762e47f8ff1f841cfa.gif" width="40px" /> O núcleo normalmente é chamado de KERNEL

</aside>

## Exemplo:

Tendo a $T$: $\R^3\rightarrow \R^2$  sendo:

$$
T(x,y,z) = (x-2y+z,2x+y+z)
$$

encontre o seu núcelo. 

- Para conseguirmos encontrar o núcleo, basta encontrarmos o **elemento neutro do contra domínio.**
- Sabemos que o elemento neutro do $\R^2$ é o $(0,0)$, então temos o seguinte sistema linear:

$$
\begin{cases}
x-2y+z = 0 \\
2x+y+z = 0
\end{cases}
$$

- Ao resolvermos esse sistema, vemos que:

$$
(x,y,z) = (-3y, y, 5y) = y(-3,1,5) \\ \therefore \\ Nuc(T) = span\{(-3,1,5)\} \ \ ou \ \ Nuc(T) = <(-3,1,5)>
$$

Pontos Importantes que devem ser ressaltados:

1. O $Nuc(T)$ pertence ao domínio (tanto que é $\R^3$) ;
2. Todo $Nuc$ é subespaço do seu domínio;
3. A **NULIDADE** é a dimensão do núcleo de uma transformação linear (no nosso caso foi $1$ -já que o núcleo foi formado por apenas um elemento).

# Imagem

## O que é a imagem de uma transformação linear?

- A imagem são todos os elementos transformados a partir do domínio da transformação linear.
    
    ![Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/Screen_Shot_2020-11-10_at_9.11.02_AM.png](Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/Screen_Shot_2020-11-10_at_9.11.02_AM.png)
    
    <aside>
    <img src="Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/8026_Anime_Surprised.png" alt="Nu%CC%81cleo%20e%20Imagem%203ab98c0a080a40efab62a59d2ca789dd/8026_Anime_Surprised.png" width="40px" /> Os elementos da Imagem de uma transformação linear pertencem ao CONTRA DOMÍNIO
    
    </aside>
    
    ## Exemplo
    
    Tendo uma transformação linear $T:\R^2 \rightarrow \R^3$ :
    
    $$
    T(x,y) = (x+y,x-y,2x)
    $$
    
    encontre a imagem dessa $TL$.
    
    - Primeiramente devemos desmembrar essa transformação:
    
    $$
    (x+y,x-y,2x) = x(1,1,2)+y(1,-1,0)
    $$
    
    - Assim temos:
    
    $$
    Im(T) = span\{(1,1,2),(1,-1,0)\} = <(1,1,2),(1,-1,0)>
    $$
    
    Coisas importantes de serem lembradas:
    
    1. Os elementos da Imagem pertencem ao **CONTRA DOMÍNIO: $Im(t) \sub V$**
    2. O **POSTO** é a dimensão da imagem $dim(Im(T))$
    

# Teorema Núcleo-Imagem

$$
\boxed{dim(Ker(T)) + dim(Img(T)) = dim(U)}
$$

- Onde $U$ é a domínio da transformação linear.