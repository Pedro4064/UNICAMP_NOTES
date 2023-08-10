# Espaços Vetoriais

Semana: Semana 3

# O que é um Espaço Vetorial?

É basicamente um conjunto não vazio onde a soma e multiplicação por escalar está definida e é fechada. Formalizando:

1. Conjunto não vazio;
2. Uma soma: $u,v\in V \Rightarrow u+v\in V$.
    
    $\hookrightarrow$ É fechado na soma, isso é, a soma de dois de seus elementos também é seu elemento.
    
3. Uma multiplicação: $\alpha \in \R, u\in V \Rightarrow \alpha u \in V$
    
    $\hookrightarrow$ É fechado no prudto por um escalar, isso é, o produto pertence ao própio conjunto.
    

Além disso, para ser um espaço vetorial, precisaseguir os $8$ axiomas seguintes (4 sobre adiçao e 4 sobre produto por escalar):

1. A soma é comutativa;
2. A soma é associativa;
3. A soma existe um elemento neutro: $\exists 0_v \in V \: | \: \forall v\in V, v+0_V = v$
4. A soma possui um inverso aditivo tal que quando somado deve ser o elemento neutro da soma: $\forall v\in V, \exists w \in V | v+w=0_V$.
5. A multiplicação por escalar é associativa;
6. A multiplicação por escalar possui um elemento neutro;
7. A multiplicação por escalar possibilita a distribuituva: $\alpha(u+w) = \alpha v + \alpha w$
8. A multipliação por escalar possibilita distribuitividade com relação à soma vetorial: $(\alpha + \beta)v = \alpha v + \beta v$