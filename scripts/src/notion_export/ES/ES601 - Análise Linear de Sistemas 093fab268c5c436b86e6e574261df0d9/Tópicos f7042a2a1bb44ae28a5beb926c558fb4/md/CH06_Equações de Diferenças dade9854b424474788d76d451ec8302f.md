# Equações de Diferenças

Created: October 6, 2022 3:55 PM

[Anotações de Aula](Equac%CC%A7o%CC%83es%20de%20Diferenc%CC%A7as%20dade9854b424474788d76d451ec8302f/Anotac%CC%A7o%CC%83es%20de%20Aula%20ce10f190576744fca8e314d3558b930f.md)

- SUMMARY
    
    

# Introdução

$\hookrightarrow$ Analogamente aos sistemas contínuos, os quais podiam ser modelados matematicamente por equações diferenciais, os sistemas discretos também podem ser modelados, mas pelas chamadas equações de diferenças, que possuem o seguinte formato.

$$
\begin{align}y(k + 1) = f(k, y(k)), \ \ \ y(0) = y_0,  \ \ \ k = 0, 1, 2, ...
\end{align}
$$

# Classificação de equações de Diferença

$\hookrightarrow$ Assim como as equações diferenciais (para os sistemas discretos) eram classificadas de acordo com o grau da derivada presente (e.g primeiro grau, segundo grau, etc) as equações de diferença também tem essa classificação. Elas, entretanto, são caracterizadas não pela ordem da derivada (já que não possuem derivada por ser discreto, e não contínua), mas sim pelo maior $\alpha$ presente em $y(k+\lambda)$.

$\hookrightarrow$ Na equação de número $1$ podemos ver que $\lambda = 1$ logo dizemos que ela é uma equação de diferença de primeira ordem.

$\hookrightarrow$ Além disso, um problema de valor inicial necessita, para uma equação de ordem $n$, $n$ valores iniciais.

$\hookrightarrow$ Podemos, ainda, classificar uma equação de diferença a partir do fato dela ser igual, ou não, a zero, isso é, se há ou não um termo forçante (análogo ao caso contínuo).

# Equações de Diferença de Primeira Ordem

## Equações Homogêneas

$\hookrightarrow$ Considerando a seguinte equação:

$$
y(k+1) = a y(k), \ \ y(0) = y_0
$$

$\hookrightarrow$ **Primeiramente** nós re-arranjamos a equação acima para igualar a zero, resultando em:

$$
\begin{align}
y(k+1) - ay(k) = 0
\end{align}
$$

$\hookrightarrow$ Em **seguindo lugar**, supomos que a solução é dada por:

$$
\begin{align}
y(k) = C a^k
\end{align}
$$

$\hookrightarrow$ Onde $C$ é uma constante arbitrária a ser determinada, no **terceiro passo**, ao substituir os valores iniciais na solução proposta.

$\hookrightarrow$ Podemos ainda analizar a equação de diferença no que tange sua característica de convergência, que depende de $a$, como mostrado abaixo:

$$
\lim_{k \rightarrow \infty} y(k) = \begin{cases}
0 & , se \ |a| < 1  \\ 
y_0 &, se \ \ a \ = 1 \\ 
\nexists & , se \ |a| > 1 \ ou \ a=-1
\end{cases}
$$

$\hookrightarrow$ A partir disso vemos que é assintoticamente estável $\iff$ $|a| < 0$.

$\hookrightarrow$ Podemos ver também que para $a = -1$ a solução dará $y(k) = \{y_0, -y_0, y_0, -y_0, ...\}$, que possui duas subsequências convergentes, uma para $y_0$ e outra para $-y_0$ (a depender da taxa de amostragem).

## Equações Não Homogêneas

$\hookrightarrow$ Considerando a seguinte equação não homogênea de primeira ordem:

$$
\begin{align}
y(k+1) = ay(k) + x(k),  \ \ y(0)=y_0,  \ \ k \ge 0
\end{align}
$$

$\hookrightarrow$ E supondo que temos como o termo forçante (i.e a entrada) um degrau:

$$
\begin{align}
x(k) = \begin{cases}
b,& k \ge 0 \\ 
0, & k<0
\end{cases}
\end{align}
$$

$\hookrightarrow$ Temos, análogo aos sistemas contínuos, que a solução final $y(k)$ será composta por duas partes:

$$
\begin{align}
y(k) = y_h + y_p
\end{align}
$$

$\hookrightarrow$ Onde:

- $y_h$ → Solução no mesmo **formato** da homogênea associada
- $y_p$ → Solução particular

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> IMPORTANTE Ressaltar que $y_h$ tem o mesmo formato, mas não podemos substituir os valores das condições iniciais para achar $C$, é somente o formato $Ca^k$.

</aside>

$\hookrightarrow$ Como já temos o formato da homogênea, o **primeiro passo** é achar um formato da particular. Como temos que a entrada, para $k \ge 0$  é uma constate, iremos supor que nossa resposta forçada $y_p$  também é uma constante $\beta$, que precisamos achar:

 

$$
y_p = \beta
$$

$\hookrightarrow$ O **segundo passo**, então, é substituir na EDO para achar o $\beta$, resultando em:

$$
\begin{aligned}
y(k+1) &= ay(k) + x(k) \\ 
\beta &= a \beta + b  \\ 
\beta - a \beta &= b \\ 
\beta(1 - a) &= b \\ 
\end{aligned}
$$

$$
\begin{align}
\beta&= \frac{b}{1-a}
\end{align}
$$

$\hookrightarrow$ Se observarmos, entretanto, tal valor de $\beta$ não é valido para $a = 1$. Para tais casos precisamos supor que um formato diferente para a resposta forçada:

$$
\begin{align}
y_p(k) = k\beta
\end{align}
$$

$\hookrightarrow$ Substituindo na EDO, então, $y_p$ tendo o formato acima para os casos em que $a = 1$ temos:

$$
y_p(k) = kb
$$

$\hookrightarrow$ Sendo o $b$ da entrada degrau.

$\hookrightarrow$ A partir disso o **terceiro passo** é montar a equação de $y$ completa (tanto parte homogênea quanto parte forçada) e substituir os valores iniciais, a fim de achar os coeficientes restante (nesse caso específico o único que falta é $C$ da parte homogênea, o que bate com o fato de termos somente uma condição inicial)