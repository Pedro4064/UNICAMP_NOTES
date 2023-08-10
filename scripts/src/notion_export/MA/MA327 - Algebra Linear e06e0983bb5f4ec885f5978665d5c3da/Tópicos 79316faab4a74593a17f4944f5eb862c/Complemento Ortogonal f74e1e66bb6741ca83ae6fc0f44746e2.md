# Complemento Ortogonal

Semana: Semana 12

# O que é um Complemento Ortognal?

- Nada mais é do que outro conjunto de vetores (um outro subespaço vetorial) que sejam ortogonais a todos os elementos de um espaço vetorial.
- Seja $V \sub R^{n}$ um subespaço vetorial. O complemento ortogonal de $V$ é o conjunto:
    
    $$
    V^{\perp} = \{w \in R^{n} \ | \ \lang w,v\rang = 0\}
    $$
    

# Como calcular o complemento Ortogonal?

- Considere o espaço vetorial gerado por:
    
    $$
    H = span\{(1,2,3,4),(-1,2,-3,4)\}
    $$
    
    Ache o  seu complemento ortogonal $H^{\perp}$:
    
    - Devemos sempre lembrar que o complemento ortogonal é o conjunto de vetores os quais terão a multiplicação interna com os elementos dos geradores de $H$ igual a $0$. Com isso podemos cirar um sitema linear, levando em consideração o vetor genério $(x,y,z,w)$:
        
        $$
        \begin{cases}
        \lang (1,2,3,4),(x,y,z,w) \rang = 0 \\
        \lang (-1,2,-3,4) , (x,y,z,w) \rang = 0
        \end{cases}
        $$
        
        Só resolver o sistema e batata.
        

# Teorema

![Complemento%20Ortogonal%20f74e1e66bb6741ca83ae6fc0f44746e2/Screen_Shot_2020-11-24_at_11.59.37_AM.png](Complemento%20Ortogonal%20f74e1e66bb6741ca83ae6fc0f44746e2/Screen_Shot_2020-11-24_at_11.59.37_AM.png)