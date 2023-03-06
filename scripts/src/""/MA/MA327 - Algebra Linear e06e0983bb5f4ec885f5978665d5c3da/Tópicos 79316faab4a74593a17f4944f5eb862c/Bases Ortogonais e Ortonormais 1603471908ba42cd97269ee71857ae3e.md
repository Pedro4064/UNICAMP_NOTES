# Bases Ortogonais e Ortonormais

Semana: Semana 12

# Bases Ortogonais

- Uma base é ortogonal se o produto interno de um vetor com cada um dos outros vetores da base for zero.
    
    $$
    Uma \ base \ \beta = \{u_1,...,u_n\} \ é \ ortogonal \ se \ \lang u_i, u_j \rang = 0 \ para \ i\neq j
    $$
    
- Exemplo:
    
    $$
    \alpha = \{(1,1,1),(-2,1,1),(0,-1,1)\}
    $$
    
    Podemos ver que se se fizermos a multiplicação interna entre todos os vetores dessa base $\alpha$, o resultado sempre será  $0 \therefore \alpha$ é uma base ortogonal.  
    

# Bases Ortonormais

- Para ser uma base ortonormal, ela precisa:
    1. Ser uma base ortogonal;
    2. O produto interno de um vetor da base com ele mesmo deve ser $1$.

$$
Uma \ base \ \beta = \{u_1,...,u_n\} \ é \ ortogonal \ se \ \lang u_i, u_j \rang = 0 \ para \ i\neq j \ e \ \lang u_i, u_i \rang = 1
$$

- Para que a multipliccão interna entre um vetor e ele mesmo seja $1$, ele precisa ser um vetor unitário, então podemos simplismente normaliza-lo  para transformar em uma base ortonormal.

## Normalização

$$
\frac{v}{||v||} = \frac{v}{\sqrt{\lang v,v \rang}}
$$

# Matriz Ortogonal

- Uma matriz quadrada é dita ortogonal quando sua transposta coincide com sua inversa.
    
    $$
    A^T = A^{-1}
    $$
    
    ![Bases%20Ortogonais%20e%20Ortonormais%201603471908ba42cd97269ee71857ae3e/Screen_Shot_2020-11-20_at_11.20.08_AM.png](Bases%20Ortogonais%20e%20Ortonormais%201603471908ba42cd97269ee71857ae3e/Screen_Shot_2020-11-20_at_11.20.08_AM.png)