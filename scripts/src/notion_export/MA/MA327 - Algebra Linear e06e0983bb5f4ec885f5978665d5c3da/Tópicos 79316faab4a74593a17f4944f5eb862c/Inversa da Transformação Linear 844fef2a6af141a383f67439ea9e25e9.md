# Inversa da Transformação Linear

Semana: Semana 9

# Quando que uma $TL$  é Invertível ?

- Uma transformação Linear é invertível $\iff$ for [bijetora](Espac%CC%A7o%20Vetorial%20Isomorfo%209910d71efd02487e80999315162817cb.md)

# O que é uma $TL$ inversa ?

- Basicamente é uma transformação linear $T^{-1}$ que recebe o resultado de uma transformação linear $T$ e "devolve" o valor do domínio correspondente.

# Exemplos:

Tendo a transformação linear $T: \R^3 \rightarrow \R^{3}$:

$$
T(x,y,z) = (z,x-2,x+2y)
$$

Defina se ela é invertível, e ache sua Transformação Linear inversa $T^{-1}$

- Para vermos se ela é invertível, precisamos determinar se ela é bijetiva, isso é, subjetiva e injetiva ao mesmo tempo.
- Para vermos se ela é **injetiva** precisamos ver se o $dim(Ker(T)) = 0$:

$$
T(x,y,z) = (z,x-2y,x+2y) = 0 \\ 
\begin{cases}
x-2y = 0 \Rightarrow x=2y\Rightarrow\boxed{x=0} \\ 
x+2y = 0 \Rightarrow 4y = 0 \Rightarrow \boxed{y=0}
\end{cases}
$$

Podemos ver então que o $Ker(T) = <0,0> \therefore dim(Ker(T)) = 0 \therefore \ \ Injetora$ 

- Podemos utilizar a propriedade Núcleo Imagem que fala que: $dim(Ker(T)) + dim(Img(T)) = dim(U)$ e achamos que posto ($dim(Img(T))$) é igual à $3$. Além disso a dimenção do domínio e do contra-domínio são iguais a $3$, com isso temos que eá também é subjetiva $\therefore$ é **bijeiva**
- Como provamos que ela é bijetiva, podemos então achar sua inversa:
1. Primeiramente precisamso achar uma base para o seu domínio $\R^3$:
    
    $$
    \varepsilon = \{(1,0,0),(0,1,0),(0,0,1)\}
    $$
    
2. Agora iremos calcular a imagem desses vetores:
    
    $$
    T(1,0,0) = (0,1,1) \\
    T(0,1,0) = (0,-2,2) \\
    T(0,0,1) = (1,0,0)
    $$
    
3. Sabemos então que esses vetores compões a base do domínio de $T^{-1}$: 
    
    $$
    \{(0,1,1),(0,-2,2),(1,0,0)\}
    $$
    
4. Agora temos a base de $T^{-1}$ e a imagem de cada um desses vetores da sua base, então podemos achar a expressão que caracteriza $T^{-1}$:
    
    $$
    (x,y,z) = a(0,1,1) + b(0,-2,2) + c(1,0,0) 
    $$
    
    Aplicando $T^{-1 }$ de ambos os lados temos:
    
    $$
    T^{-1}(x,y,z) = aT^{-1}(0,1,1) + bT^{-1}(0,-2,2) + cT^{-1}(1,0,0) \Rightarrow \\
    T^{-1}(x,y,z) = a(1,0,0) + b(0,1,0)+c(0,0,1) \Rightarrow \\ 
    T^{-1}(x,y,z) = (a,b,c)
    $$
    
5. Agora acharemos os valores de $a,b,c$ pela $eq:1$ e substituiremos na que acabamos de encontrar acima:
    
    $$
    (x,y,z) = a(0,1,1) + b(0,-2,2) + c(1,0,0) \Rightarrow \\ 
    (x,y,z) = (c,a-2b,a+2b) \Rightarrow \\ 
    \begin{cases}
    \boxed{c=x} \\
    y = a-2b \Rightarrow a = y+2b \Rightarrow \boxed{a = \frac{y+z}{2}} \\ 
    z = a+2b \Rightarrow z = y+4b \Rightarrow \boxed{b=\frac{z-y}{4}}
    \end{cases}
    $$
    
6. Substituimos na definição de $T^{-1}$ em função de $(a,b,c)$ e temos:
    
    $$
    T^{-1} = \left(\frac{y+z}{2}, \frac{z-y}{4}, x\right)
    $$