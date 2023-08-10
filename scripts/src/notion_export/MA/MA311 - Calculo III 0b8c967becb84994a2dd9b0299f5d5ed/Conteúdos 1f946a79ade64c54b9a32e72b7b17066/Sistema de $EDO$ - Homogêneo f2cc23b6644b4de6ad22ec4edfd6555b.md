# Sistema de $EDO$ - Homogêneo

Created: June 19, 2021 6:53 PM
Prova: P2

# Método Matricial para o sistema $2 X 2$

- **FORMATO MATRICIAL**
    - Primeiramente devemos escrever a equação no formato:
    
    $$
    X'(t) = AX(t)
    $$
    
- **ACHAR OS AUTOVALORES**
    - Agora precisamos achar os autovalores $[\lambda_1, \lambda_2]$, pelo método da algebra linear de determinante:
    
    $$
    \det(A - \lambda I) = 0
    $$
    
    - Agora podemos ter $3$ possibilidades para os autovalores.
    
- **ACHAR OS AUTOVETORES & SOLUÇÕES**
    - Os autovetores  e as soluções dependem da relação dos autovalores:
    
    - $\lambda_1 \ne \lambda_2$
        - Para quando eles são diferentes, podemos achar os autovetores pelas fórmulas:
        
        $$
        (A - \lambda_1 I)v_1 = 0 \\ 
        (A - \lambda_2 I)v_2 = 0
        $$
        
        - Que vai ter como soluções:
        
        $$
        x^{(1)} = v_1 e^{\lambda_1 t} \\
        x^{(2)} = v_2 e^{\lambda_2 t}
        $$
        
        - Além disso, temos a MATRIZ FUNDAMENTAL:
        
        $$
        \Phi = \begin{pmatrix}
        | & | \\ 
        x^{(1)} & x^{(2)} \\
        | & | \\ 
        \end{pmatrix}
        $$
        
        - E o Vetor $C$:
        
        $$
        C = \begin{pmatrix}
        C_1 \\ C_2
        \end{pmatrix}
        $$
        
        - Com a solução Geral sendo:
        
        $$
        X = C_1 x^{(1)} + C_2 x^{(2)}
        $$
        
    - $\lambda_1 = \lambda_2$
        - Para encontrar os autovetores temos:
        
        $$
        (A - \lambda_1 I)v_1 = 0 \\ 
        (A - \lambda_2 I)v_2 = v_1
        $$
        
        - Com as soluções sendo:
        
        $$
        x^{(1)} = v_1 e^{\lambda_1 t} \\
        x^{(2)} = v_1 t e^{\lambda_2 t} + v_2 e^{\lambda_2 t}
        $$
        
    - Autovalores Complexos
        - Os autovalores Complexos tem a forma:
        
        $$
        \lambda_1 = a + bi\\
        \lambda_2 = a - bi
        $$
        
        - Com isso são associados a autovetores complexos $\vec{v_1}$ e $\vec{v_2}$:
        
        $$
        \vec{v_1} = \vec{\alpha} + \vec{\beta}i \\
        \vec{v_2} = \vec{\alpha} - \vec{\beta}i
        $$
        
        - Com as soluções:
        
        $$
        x^{(1)} =  e^{at} \left(\vec{\alpha} \cos bt - \vec{\beta} \sin bt\right ) \\ 
        
        x^{(2)} =  e^{at} \left(\vec{\alpha} \sin bt - \vec{\beta} \cos bt\right )
        $$
        
        <aside>
        <img src="Sistema%20de%20$EDO$%20-%20Homoge%CC%82neo%20f2cc23b6644b4de6ad22ec4edfd6555b/Evangelion.gif" alt="Sistema%20de%20$EDO$%20-%20Homoge%CC%82neo%20f2cc23b6644b4de6ad22ec4edfd6555b/Evangelion.gif" width="40px" /> OBS: o expoente do $e$ é a (do autovalor), e não $\alpha$ do autovetor!!!!!
        Mas dentro do parênteses é o $\alpha$  mesmo.
        
        </aside>