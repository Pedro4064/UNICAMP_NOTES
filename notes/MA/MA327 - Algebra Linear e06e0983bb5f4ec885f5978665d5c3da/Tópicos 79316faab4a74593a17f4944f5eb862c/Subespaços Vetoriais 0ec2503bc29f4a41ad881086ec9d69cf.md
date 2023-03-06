# Subespaços Vetoriais

Semana: Semana 4

# O Que é Um Subespaço?

Nada mais é do que um subconjunto de um espaço vetorial. Tal subconjunto também é um espaço vetorial e possui as mesmas operações do espaço que o contém.

# Condições de um Subespaço Vetorial

Para que um subconjunto de um espaço vetorial seja considerado um subconjunto ele precisa estar de acordo com somente 3 requisitos:

- Para que um subconjunto $W \subset V$ , onde $V$ é um espaço vetorial, temos que $W$ é um subespaço $\iff$
    
    
    1. $0_V \in W$
    2. $u,v \in W \Rightarrow u+v \in W$
    3. $\lambda \in \R, u\in W \Rightarrow \lambda u \in W$
    
- Explicando um pouco melhor:
    1. O zero (elemento neutro da soma) do espaço vetorial $V$ precisa estar contido no subespaço vetorial $W$, onde também será o elemento neutro.
    2. Ele é fechado no que tange a soma;
    3. Ele é fechado no que tange a multiplicação por escalar.
    

# Subespaço Afim

Um subespaço afim $H$ nada mais é do que a translação de um subespaço $W \subset V:$

$$
H = v_0 + W = \{w \in W\} |v_0 \in V
$$

Dizemos então que $H$ é um subespaço afim associado ao subespaço $W$.

<aside>
<img src="Subespac%CC%A7os%20Vetoriais%200ec2503bc29f4a41ad881086ec9d69cf/a6ada7178c8b6b762e47f8ff1f841cfa.gif" alt="Subespac%CC%A7os%20Vetoriais%200ec2503bc29f4a41ad881086ec9d69cf/a6ada7178c8b6b762e47f8ff1f841cfa.gif" width="40px" /> Um subespaço Afim **NUCA** vai ser um subespaço vetorial, tendo em vista houve uma translação $\therefore$ o zero do sistema original não faz mais parte de subespaço afim $\therefore 0_V \notin H \therefore$ não é um subespaço.

</aside>