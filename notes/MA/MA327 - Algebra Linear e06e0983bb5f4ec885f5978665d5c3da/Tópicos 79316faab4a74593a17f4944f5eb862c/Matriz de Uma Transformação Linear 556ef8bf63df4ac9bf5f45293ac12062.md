# Matriz de Uma Transformação Linear

Semana: Semana 10

<aside>
<img src="Matriz%20de%20Uma%20Transformac%CC%A7a%CC%83o%20Linear%20556ef8bf63df4ac9bf5f45293ac12062/8026_Anime_Surprised.png" alt="Matriz%20de%20Uma%20Transformac%CC%A7a%CC%83o%20Linear%20556ef8bf63df4ac9bf5f45293ac12062/8026_Anime_Surprised.png" width="40px" /> Toda $TL$ é uma matriz, e toda matriz é uma $TL$

</aside>

# Matrizes que representam $TL's$ (Base Canônica)

- Para transformarmos uma Transformação Linear em uma matriz precisamos de uma base, no momento iremos usar a base canônica.
- Passos para encontrarmos a matriz da $TL$:
    
    $$
    T:\R^{2} \rightarrow \R^{3} \\ 
    T(x,y) = (2x-y, x-2y, x+2y)
    $$
    
    1. Aplicamos a $TL$ nos vetores da base canônica $\{(1,0),(0,1)\}$ do domínio $\R^{2}$:
        
        $$
        T(1,0) = (2,1,1) \\ 
        T(0,1) = (-1,-2,2)
        $$
        
    2. Jogamos esses novos vetores nas colunas de uma matriz, **RESPEITANDO A ORDEM DA BASE:**
        
        $$
        \begin{bmatrix}
         2 & -1 \\
         1 & -2 \\
         1 &  2
        \end{bmatrix}
        $$
        

# Matrizes que representam $TL's$ (Base Arbitrária)

- Sendo a transformação Linear:
    
    $$
    T:\R^{2} \rightarrow \R^{3} \\ 
    T(x,y) = (2x-y, x-2y, x+2y)
    $$
    
    1. **Identificar as bases do domínio e do contra domínio**: Com o domínio na base $\alpha = \{(1,0),(1,1)\}$ e o contra domínio na base $\beta = \{(1,0,0),(0,1,1),(0,0,1)\}$ dados pelo enunciado. 
    2. **Aplicar a transformação linear na base do domínio:**
        
        $$
        T(1,0) = (2,1,1) \\ 
        T(1,1) = (1,-1,3)
        $$
        
    3. **Transformamos esses vetores para a base $\beta$ do contra domínio:**
        
        $$
        \begin{aligned}
         T(1,0) &= a_1(1,0,0)+b_1(0,1,1)+c_1(0,0,1) \\
        (2,1,1) &= a_1(1,0,0)+b_1(0,1,1)+c_1(0,0,1) \\ 
        (2,1,1) &= (a_1,b_1,b_1+c_1)
        \end{aligned}
        $$
        
        $$
        \begin{cases}
        \boxed{a_1  = 2} \\
        \boxed{b_1 = 1} \\
        b_1+c_1 = 1 \Rightarrow \boxed{c_1 = 0}
        \end{cases}
        $$
        
        Repetindo o mesmo procedimento para o outro vetor teremos os 2 vetores que representarão as duas colunas da matriz $TL$.
        
    4. **Jogar os vetores encontrados como as colunas matriz :**
        
        $$
        \begin{bmatrix}
        2 & 1 \\ 
        1 & -1 \\
        0 & 4
        \end{bmatrix}
        $$
        
        <aside>
        <img src="Matriz%20de%20Uma%20Transformac%CC%A7a%CC%83o%20Linear%20556ef8bf63df4ac9bf5f45293ac12062/LewdMegumin.png" alt="Matriz%20de%20Uma%20Transformac%CC%A7a%CC%83o%20Linear%20556ef8bf63df4ac9bf5f45293ac12062/LewdMegumin.png" width="40px" /> **DICA:** Tendo uma transformação linear $T:U\rightarrow V$, sabemos que a matriz $[T]_{\beta \leftarrow \alpha}$ terá sempre as dimensões $dim(V) \times dim(U) \therefore$ $nº Colunas = dim(Dom(T))$ e $nº Linhas = dim(C.Dom(T))$
        
        </aside>