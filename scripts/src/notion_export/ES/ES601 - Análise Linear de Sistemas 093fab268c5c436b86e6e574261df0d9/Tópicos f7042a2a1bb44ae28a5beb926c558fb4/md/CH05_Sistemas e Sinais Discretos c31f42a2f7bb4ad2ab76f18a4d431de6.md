# Sistemas e Sinais Discretos

Created: October 5, 2022 4:18 PM

[Anotações de Aula](Sistemas%20e%20Sinais%20Discretos%20c31f42a2f7bb4ad2ab76f18a4d431de6/Anotac%CC%A7o%CC%83es%20de%20Aula%20e5585af81899476781609c4216a9b8b4.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Basicamente tudo hoje em dia gira em torno de sistemas digitais.

$\hookrightarrow$ Tais sistemas, entretanto, não intrinsecamente discretos, pois trabalham, em seus níveis mais fundamentais, com valores discretos (bits).

$\hookrightarrow$ Por isso é de suma importância conseguirmos analizar sistemas que são descritos por dados discretos.

# Definição de Sinais Discretos

$\hookrightarrow$ É de suma importância saber que, no que tange sinais discretos, há majoritariamente dois tipos:

- Sinais Naturalmente Discretos
- Sinais contínuos Discretizados

**Sinais Naturalmente Discretos** 

$\hookrightarrow$ Um exemplo de algo naturalmente discreto é o número de recém-nascidos, valor diário de determinada bolsa de valores, etc.

**Sinais Contínuos Discretizados**

$\hookrightarrow$ Na maioria das vezes, entretanto, estamos tentando medir/representar um fenômeno que é naturalmente contínuo em sistemas digitais (e.g um computador) em que ter infinitos pontos/medições continuamente (i.e sem um intervalo) é inviável.

$\hookrightarrow$ Nesses casos, onde temos um sinal contínuo $x(t)$, teremos uma taxa de amostragem $t = KT$, onde $T$ é o tempo e $K$ é um número real. 

$\hookrightarrow$ Podemos, ainda, representar o sinal discreto como sendo $x(k)$, onde $k$ representa o número da amostra (ou seja do dado coletado).

## Principais Sinais

### Impulso Unitário

$$
\delta (k) = \begin{cases}
1 & ,se \ k =0 \\ 
0 & ,se \ k \ne0 \\ 
\end{cases}
$$

![Screen Shot 2022-10-05 at 4.33.13 PM.png](Sistemas%20e%20Sinais%20Discretos%20c31f42a2f7bb4ad2ab76f18a4d431de6/Screen_Shot_2022-10-05_at_4.33.13_PM.png)

### Degrau Unitário

$$
\mu (k) = \begin{cases}
1 & ,se \ k \ge0 \\ 
0 & ,se \ k <0 \\ 
\end{cases}
$$

![Screen Shot 2022-10-05 at 4.34.22 PM.png](Sistemas%20e%20Sinais%20Discretos%20c31f42a2f7bb4ad2ab76f18a4d431de6/Screen_Shot_2022-10-05_at_4.34.22_PM.png)

### Sequência Exponencial

$$
x(k) = a^k,  \ \ a\in \R
$$

![Screen Shot 2022-10-05 at 4.36.55 PM.png](Sistemas%20e%20Sinais%20Discretos%20c31f42a2f7bb4ad2ab76f18a4d431de6/Screen_Shot_2022-10-05_at_4.36.55_PM.png)

$\hookrightarrow$ É importante ressaltar duas coisas:

- Diferentemente de sistemas contínuos, a sequência exponencial tem por base qualquer valor $a$, e não somente $e$.
- Além disso, podemos ver que a sequência pode tanto convergir (como a em azul, para $a = 0.6$) como pode divergir (como a em vermelho, para $a = -1.1$). A partir disso podemos dizer que, para $**a<0$ a exponencial DIVERGE**.

### Sequência Periódica

$$
x(k) = x(k + P),  \ \ P\in \mathbb{Z}
$$

- Dos sinais supracitados, as sequências periódicas são as mais peculiares em sinais discretos. Isso se dá pois não necessariamente todos os sinais contínuos periódicos continuam periódicos após a discretização, a depender da frequência e da taxa de amostragem (que não é objetivo dos nosso estudos para essa matéria).

# Propriedades de Sinais Discretos

$\hookrightarrow$ Analogamente ao que foi visto durante os estudos de sinais contínuos, os sinais discretos também apresentam certas propriedades.

## Convolução

- A convolução entre dois sinais, $x(k)$ e $y(k)$ é dada por:

$$
y(k) *x(k) = \sum^{\infty}_{n = -\infty} y(k - n)x(n)=\sum^{\infty}_{n = -\infty} x(k - n)y(n)
$$

## Convolução com o Impulso

- A partir da definição de convolução acima, podemos dizer que um sinal $x(k)$ pode sempre ser reescrito como sendo sua convolução com o impulso, ou seja:

$$
x(k) = \sum^{\infty}_{n = -\infty} x(n) \delta(k-n)
$$

- Ao analisarmos o impulso, podemos ver que ele é $\delta (k - n) = 1 \iff  k = n \therefore x(k)*\delta(k) = x(k)$

## Energia de uma Sequência

- A energia de uma sequência é definida como sendo:

$$
E = \sum^{\infty}_{k=-\infty} x(k)x^* (k) = \sum^{\infty}_{k=-\infty} |x(k)|^2
$$

- Onde $x^*(k)$ é o complexo conjugado de $x(k)$