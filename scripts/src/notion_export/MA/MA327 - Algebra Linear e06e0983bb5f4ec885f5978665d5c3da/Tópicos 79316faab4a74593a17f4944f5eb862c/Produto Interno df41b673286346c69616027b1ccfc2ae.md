# Produto Interno

Semana: Semana 11

# Denotação de Produto Interno entre dois vetores:

- $\langle u,v \rangle$;
- $\langle u|v\rangle$;
- $u \cdot v$

<aside>
<img src="Produto%20Interno%20df41b673286346c69616027b1ccfc2ae/a6ada7178c8b6b762e47f8ff1f841cfa.gif" alt="Produto%20Interno%20df41b673286346c69616027b1ccfc2ae/a6ada7178c8b6b762e47f8ff1f841cfa.gif" width="40px" /> CUIDADO: nós também usamos a denotação $\langle u,v\rangle$ para representar espaço gerado, mas não confunda, depende do contexto em que está. Usarmos essa denotação.

</aside>

# Cálculo do Produto Interno

## Produto Interno Usual

- Também conhecido como produto escalar;
    
    $$
    \lang (1,2,3),(4,5,6) \rang = 1(4) +2(5) +3(6) = 32
    $$
    
    ## Produtos Internos Não Usuais
    
    - Podemos criar produtos internos, desde que eles obedeçam certos axiomas,  chamados de **axiomas de produto interno**:
    
    ### Axiomas do Produto Interno
    
    - Simetria / Simetria Hermitiana: $\langle u,v\rangle = \langle v,u\rangle$;
    - Homogeneidade: $\langle \lambda u,v\rangle = \lambda \langle u,v\rangle$;
    - Aditividade / Distribuitividade: $\langle u+w,v\rangle = \langle u,v\rangle + \langle w,v\rangle$;
    - Positividade: $\langle u,v\rangle \ge 0, \forall u\neq 0$;
    - $\langle u,v\rangle = 0 \iff u = 0$
    
    ### Exemplos
    
    - Sendo $u = (x_1,y_1)$ e $v = (x_2 , y_2)$ vetores do $\R^{2}$, verifique se $\langle u,v\rangle = 2x_1x_2 - y_1y_2$ é um produto escalar sobre $\R^{2}$:
        
        
        Simetria:
        
        $$
        \langle u,v\rangle = \langle v,u\rangle \\
        \boxed{2x_1x_2 - y_1y_2 = 2x_2x_1 - y_2y_1} \checkmark
        $$
        
        Homogeneidade:
        
        $$
        \langle \lambda u,v\rangle =  \lambda \langle u,v\rangle \\ 
        
        \boxed{2\lambda x_1x_2 - \lambda y_1y_2 = \lambda(2x_1x_2 - y_1y_2)}\checkmark
        $$
        
        Aditividade:
        
        $$
        \langle u+w,v\rangle = \langle u,v\rangle + \langle w,v\rangle\\
        
        w = (x_3,y_3)\\
        
        \boxed{2(x_1+x_3)x_2 - (y_1+y_3)y_2 = 2x_1x_2 - y_1y_2 + 2x_3x_2 - y_3y_2 } \checkmark
        $$
        
        Positividade:
        
        - Podemos testar a positividade fazendo o produto interno entre dois vetores iguais (para facilitar);
            
            $$
            \lang u, u\rang \gt 0 \\
            \boxed{2x_1x_1 - y_1y_1 \gt 0 } \times
            $$
            
        - Não necessariamente isso sempre será verdade, logo existe a possibilidade de ser menor que zero, o que implica que essa operação não é um produto interno.
        
        <aside>
        <img src="Produto%20Interno%20df41b673286346c69616027b1ccfc2ae/sagiriBleh.png" alt="Produto%20Interno%20df41b673286346c69616027b1ccfc2ae/sagiriBleh.png" width="40px" /> Um espaço vetorial real que apresenta produto interno é denominado **ESPAÇO EUCLIDIANO**. ****
        
        </aside>
        
        <aside>
        <img src="Produto%20Interno%20df41b673286346c69616027b1ccfc2ae/LewdMegumin.png" alt="Produto%20Interno%20df41b673286346c69616027b1ccfc2ae/LewdMegumin.png" width="40px" /> Um espaço vetorial complexo que apresenta produto interno é denominado de **ESOAÇO UNITÁRIO**.
        
        </aside>