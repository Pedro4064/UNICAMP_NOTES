# Operações com Subespaço

Semana: Semana 5

# União de Subespaços Vetoriais

Relembrando União de conjuntos:

$$
A \cup B = \{x |x\in A \:\:ou\:\: x\in B \}
$$

A pergunta que fica é: Se tivermos dois subespaços $H,W$, a união deles ainda será um subespaço?

Para responder essa pergunta devemos lembrar que para ser um subespaço, deve ser fechado por soma. Quando  $W \nsubseteq H$ ou $H \nsubseteq W$, temos que um elemento $w \in W$, $h\in H$ e por conseguinte $w,h \in (H\cup W)$ se somados não pertencem à união (o que torna a afirmação de fechado na multipicação falsa).  Isso é muito fácil de vizualizar se considerarmos $H$ um plano e $W$ uma reta da seguinte forma:

Onde temos que $W$ não pertence a $H$ e nem vice-versa.

![Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Screen_Shot_2020-10-20_at_2.56.41_PM.png](Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Screen_Shot_2020-10-20_at_2.56.41_PM.png)

Se pegarmos um vetor $w \in W \:\:e \:\: h\in H$:

![Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled.png](Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled.png)

Assim que analisarmos a soma desses dois vetores (que pertencem ao conjunto $(H\cup W)$ teremos um vetor que não pertence a tal conjunto. Com isso, vemos que quando ocorre a união de dois subespaços que não contém um ao outro resulta em um conjunto que não é um subespaço vetorial.

![Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled%201.png](Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled%201.png)

Entretanto, se observarmos um cenário conde a reta $W$ faz parte do plano $H \Rightarrow W \sub H$ a resultante seria sim fechada na soma e por conseguinte um subespaço vetorial.

# Soma de Subespaços

A soma de dois subespaços vetoriais nada mais é do que a soma de todos os elementos do primeiro subespaço com todos os elementos do outro:

$$
W+H = \{y \:\: | \:\: y = x_1+x_2, x_1 \in H,x_2\in W\}
$$

Em outras palavras, os elementos de $W+H$ são combinação linear de todos os elementos desses subespaços.

 

<aside>
💡 A soma de dois conjuntos pode ser escrita como o **conjunto gerado pela junção dos geradores** de dois conjuntos.

</aside>

<aside>
<img src="Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/a6ada7178c8b6b762e47f8ff1f841cfa.gif" alt="Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/a6ada7178c8b6b762e47f8ff1f841cfa.gif" width="40px" /> A soma de dois subespaços **SEMPRE** será um subespaço.

</aside>

## Base da Soma de Subespaços

Se $H$  tem como gerador $(v_1,v_2)$ e $W$ tem como gerador $(v_3)$, então $H+W$ terá como gerador $(v_1,v_2,v_3)$. Para acharmos a base, basta tirarmos quaisquer elementos $LD$  do gerador acima.

# Interseção de Subespaço Vetorial

A interseção são todos os elementos que conseguem satisfazer a condição de existência de ambos os subespaços simultaneamente.

![Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled%202.png](Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled%202.png)

# Soma de Dimensões de Subespaços

## Soma Direta

Dizemos que a soma entre dois subespaços $H,W$ é direta quando:

$$
H \cap W = \{0\}
$$

Isso é, a única interseção entre os dois subespaços é o zero.

E possui a seguinte notação:

$$
H \oplus W
$$

## Dimensões de Subespaços

![Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled%203.png](Operac%CC%A7o%CC%83es%20com%20Subespac%CC%A7o%2097c12ff93ab247668e5b4ff00a45c7eb/Untitled%203.png)