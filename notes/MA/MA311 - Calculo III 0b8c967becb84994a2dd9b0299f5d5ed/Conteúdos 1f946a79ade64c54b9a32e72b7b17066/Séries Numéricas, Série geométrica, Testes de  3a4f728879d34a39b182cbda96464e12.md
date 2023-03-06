# Séries Numéricas, Série geométrica, Testes de Convergência

Aula: Aula 15
Created: May 23, 2021 1:26 PM
Prova: P2

# Séries Numéricas

Dada uma sequência infinita $\{a_n\}_{n=1}^\infty$, a soma dos seus termos: 

$$
a_1 + a_2 + a_3+...+a_n = \sum_{n=1}^{\infty}a_n
$$

é denominada uma série infinita, ou simplesmente série.

## Soma Parcial

A soma dos $n$ primeiros termos da sequência, denotada por:

$$
s_n = a_1 + ... + a_n = \sum_{i=1}^n a_i
$$

é chamada de n-ésima somar parcial da série. 

<aside>
<img src="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/mugi.gif" alt="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/mugi.gif" width="40px" /> Teste de divergência através do limite do termo geral (expressão dentro da somatória) quando $n \rightarrow \infty$, se o limite for diferente de 0 ou não existirtemos que ela não é convergente !

</aside>

<aside>
<img src="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Hifumi_Surprised.png" alt="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Hifumi_Surprised.png" width="40px" /> Se a sequência de somas parciais for convergente, dizemos que que a série é convergente, já se a sequência de somas parciais for divergente, dizemos que a série é divergente.

</aside>

# Série Geométrica

- A série geométrica é a soma dos elementos de uma $PG$:

$$
\sum_{n=1}^{\infty} a(r)^{n-1} = \frac{a}{1-r}
$$

<aside>
<img src="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Hifumi_Surprised%201.png" alt="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Hifumi_Surprised%201.png" width="40px" /> OBS: Se começar com $n=1$ temos o expoente como sendo $n-1$, caso comece com $n=0$ temos expoente como sendo $n$.

OBS$^2$: Caso tenhamos $n=1$ mas o expoente $n$, devemos subtrair $a$, pois não podemos contar com o primeiro elemento →  [LINK](https://app.respondeai.com.br/materias/solucionario/livro/2/edicao/20/exercicio/1538) para questão do responde Aí

</aside>

<aside>
<img src="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Amazon_com__animal_shirt_women.jpeg" alt="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Amazon_com__animal_shirt_women.jpeg" width="40px" /> Normalmente precisaremos fazer algumas manipulações algébricas para que fique da forma acima, isso é, uma constante $a$ e um $r$ elevado a $n-1$ ou $n$ → Devemos elevar para o menor dos dois que já houver na fórmula: 

e.g $\sum \frac{(\pi)^{n}}{3^{n+1}}$ → devemos manipular para botar o denominador também em $n$

já  $\sum \frac{(-3)^{n-1}}{4^{n}}$ → devemos manipular para botar o denominador também em $n-1$

</aside>

- Teremos os seguintes comportamentos para os valores de $r$:
    
    a) $-1 < r < 1 \Rightarrow$ Convergente para $\frac{a_1}{1-r}$
    
    b)$r = 1 \Rightarrow$ Divergente
    
    c)$r = -1 \Rightarrow$ Nunca converge
    

# Testes de Convergência

## Teste de Divergência

- Temos que se:

$$
\lim_{n\rightarrow \infty} a_n \nexists
$$

ou 

$$
\lim_{n\rightarrow \infty} a_n \ne 0
$$

Então é uma série divergente

## Teste da Integral

- Considerando $a_n = f(n)$, temos que, se ela for DECRESCENTE, isso é, $f'(n) < 0$, positiva e contínua :
1. Se $\int_1^{\infty}f(x)dx$ for convergente, então a série é convergente;
2. Se $\int_1^{\infty}f(x)dx$ for divergente, então a série é divergente.

## Teste da Razão

- Aplicando:

$$
\lim_{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_n} \right| = L
$$

Teremos:

$$
\begin{cases}
0 \le L < 1 \Rightarrow & Convergente \\ 
L > 1 \Rightarrow & Divergente\\
L = 1 \Rightarrow & Não \ Podemos\ afirmar \ nada
\end{cases}
$$

## Teste da Raiz

- Usado quando nossa série está elevada a $n$
- Aplicando:

$$
\lim _{n\rightarrow \infty}\sqrt[n]{|a_n|} = L
$$

Teremos então: 

$$
\begin{cases}
0 \le L < 1 \Rightarrow & Convergente \\ 
L > 1 \ ou\ L\rightarrow \infty \Rightarrow & Divergente\\
L = 1 \Rightarrow & Não \ Podemos\ afirmar \ nada
\end{cases}
$$

## Teste da Comparação

- Utilizando uma série a qual sabemos o comportamento (geométrica ou p-série e Harmônica), comparamos ela com a nossa série, se:
    - Nossa série conhecida converge e for maior, a nova série também converge.
    - Nossa série conhecida diverge e for menor, a nova série também diverge
    
    <aside>
    <img src="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Hifumi_Surprised%202.png" alt="Se%CC%81ries%20Nume%CC%81ricas,%20Se%CC%81rie%20geome%CC%81trica,%20Testes%20de%20%203a4f728879d34a39b182cbda96464e12/Hifumi_Surprised%202.png" width="40px" /> OBS: Para escolher nossa série conhecida (se for uma p-série) precisamos escolher o expoente como sendo a subtração entre o expoente dominante(i.e maior) do numerador pelo expoente dominante(i.e maior) no denominador.
    
    [EXEMPLO](https://www.respondeai.com.br/aprender/118/topico/35/663/exercicio/2397)
    
    </aside>
    

## Limite da Comparação

- Tiramos o limite da divisão entre a série que queremos e a série que sabemos, se for maior que $0$ temos que a nova série em análise possui o mesmo comportamento da série conhecida.
- OBS do teste da comparação ainda se aplica