# Séries Alternadas

Aula: Aula 16
Created: June 1, 2021 9:28 AM
Prova: P2

# O que é uma Série Alternada ?

- Um série alternada é uma séria na qual seus elementos alteram de sinal a cada termo.

# Principal Forma

$$
\sum_{n=1}^{\infty} (-1)^n
$$

$\hookrightarrow$ Basicamente quando temos $-1$ elevado a $n$ é uma boa indicação de que nossa série é alternada.

$\hookrightarrow$ Outro sinal interessante é se for $\cos n\pi$ ou $\sin n\pi$.

# Teste das Séries Alternadas

Dada uma série alternada:

$$
\sum_{n=1}^\infty (-1)^n b_n
$$

Se ela satisfaz essas duas condições:

$$
\begin{cases}
b_{n+1} \le b_n, \forall n \rightarrow f(n) = b_n\ tal\ que\ f'(n) < 0 \\ 
\lim_{n\rightarrow \infty}b_n = 0
\end{cases}
$$

Então ela é convergente.

<aside>
<img src="Se%CC%81ries%20Alternadas%20cf820afd463e464ba57ea86eb9ec99fb/Evangelion.gif" alt="Se%CC%81ries%20Alternadas%20cf820afd463e464ba57ea86eb9ec99fb/Evangelion.gif" width="40px" /> OBS: Se ela não se enquadrar, NÃO podemos dizer que ela é divergente automaticamente, precisamos mostrar por outro método (muito provavelmente pelo Teste da Divergência)

</aside>

# Convergência Absoluta

$\hookrightarrow$ Quando temos alguns termos de uma série sendo negativos, é uma boa ideia verificar se a série é absolutamente convergente.

$\hookrightarrow$ Uma série é absolutamente convergente se:

$$
\sum |a_n|
$$

for convergente.

## Exemplo

- Verifique a convergência da série:

$$
\sum_{n=1}^{\infty}  \  \frac{\cos n}{n^2}
$$

$\hookrightarrow$  Sabemos que por ter o $\cos n$ que alguns valores serão negativos, logo suspeitamos que seja absolutamente convergente, para isso temos que:

$$
\sum_{n=1}^{\infty} \left| \  \frac{\cos n}{n^2} \ \ \right|
$$

precisa ser convergente.

$$
\sum_{n=1}^{\infty} \left| \  \frac{\cos n}{n^2} \ \ \right| = \sum_{n=1}^{\infty}\frac{|\cos n|}{n^2}
$$

$\hookrightarrow$ Levando em consideração que:

$$
0 \le |\cos n|  \le 1
$$

$\hookrightarrow$ Podemos considerar que:

$$
\frac{|\cos n|}{n^2} \le \frac{1}{n^2}
$$

$\hookrightarrow$ pelo teste de [convergência por comparação](https://www.respondeai.com.br/aprender/118/topico/35/662/teoria/643) (com uma p-série com expoente maior que 1 $\therefore converge$) temos que nossa série também converge.

<aside>
<img src="Se%CC%81ries%20Alternadas%20cf820afd463e464ba57ea86eb9ec99fb/LewdMegumin.png" alt="Se%CC%81ries%20Alternadas%20cf820afd463e464ba57ea86eb9ec99fb/LewdMegumin.png" width="40px" /> TODA série absolutamente convergente é convergente!

</aside>