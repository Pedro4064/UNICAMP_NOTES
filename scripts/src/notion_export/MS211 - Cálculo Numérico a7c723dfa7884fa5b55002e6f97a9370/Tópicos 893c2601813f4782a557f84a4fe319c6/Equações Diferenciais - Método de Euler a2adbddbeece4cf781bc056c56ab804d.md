# Equações Diferenciais - Método de Euler

Aula: Aula 16
Created: November 9, 2021 9:34 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ Como dito anteriormente, podemos dividir os métodos numéricos para EDOs em métodos de passo simples e métodos de passos múltiplos.

$\hookrightarrow$ O Método de Euler se encaixa na categoria de método de passo simples, para resolver problemas de valor inicial do tipo:

$$
\begin{cases}
\frac{dy}{dx} = f(x, y) \\ 
y(x_0) =  y_0
\end{cases}
$$

# Estratégia

$\hookrightarrow$ Temos como objetivo achar a função $y(x)$, levando em consideração que temos a expressão da sua derivada $\frac{dy}{dx}$.

$\hookrightarrow$ Fazemos isso através da aproximação de $y(x_k)$ pela reta $r$ tangente a $y(x_{k-1})$ em $(x_{k-1}, y_{k-1})$, ou seja, $r$ passa pelo ponto $(x_{k-1}, y_{k-1})$ e tem coeficiente angular $y'(x_{k-1}) = f(x_{k-1}, y_{k-1})$, i.e:

$$
r_0(x) = y_0 + f(x_0, y_0) (x-x_0)
$$

$\hookrightarrow$ E aproximamos:

$$
y(x_1) \approx y_1 = r_0(x_1) = y_0 + f(x_0, y_0) (x_1-x_0) = y_0 + f(x_0, y_0) h
$$

$\hookrightarrow$ Onde $h$ é o passo.

$\hookrightarrow$ No geral temos:

$$
\boxed{y_k = y_{k-1} + f(x_{k-1}, y_{k-1}) h}
$$

<aside>
<img src="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/yuru_camp.png" alt="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/yuru_camp.png" width="40px" /> Basicamente é um método iterativo onde nós aproximamos $y_k$ do valor em $x_k$ da reta tangete ao ponto anterior $(y_{k-1}, x_{k-1})$. Isso é, traçamos uma reta tangente ao ponto calculado anteriormente (sendo que o primeiro ponto é dado pelo problema) e vemos o valor de $y$ nessa reta em $x_k$.

</aside>

# Interpretação Geométrica

![Screen Shot 2021-11-10 at 11.33.19 AM.png](Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/Screen_Shot_2021-11-10_at_11.33.19_AM.png)

![Screen Shot 2021-11-09 at 9.54.47 PM.png](Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/Screen_Shot_2021-11-09_at_9.54.47_PM.png)

# Interpretação de Taylor e Erro Local

$\hookrightarrow$ Além da interpretação geométrica mostrada acima, o método de Euler também tem uma interpretação pelo somatório de Tylor.

$\hookrightarrow$ Esse nova interpretação nos permite calcular o erro local, isso é, o erro $e$ de cada iteração:

 

$$
e(x_{k+1}) = |y(x_{k+1})  - y_{k+1}| = \frac{1}{2}|y''(\varepsilon)| h^2 \le \frac{M_2}{2} h^2
$$

- Onde $M_2$ é o máximo da segunda derivada $y''$
- $h$ é o passo.

$\hookrightarrow$ Normalmente nós temos $M_2$ e temos um erro $e$ máximo que queremos ter na nossa solução numérica. 

$\hookrightarrow$ Com isso somos capazes de determinar nosso passo $h$ para que estejamos dentro do erro esperado.

# Exemplos

## Ex. 1

$$
\begin{cases}
y' = (y) \\ 
y(0) = 1
\end{cases}
$$

- Obtenha $y(0.04)$ com uma tolerância $\varepsilon \le 5 \times 10^{-4}$ em 4 casa decimais.

- 1º Passo - Isolar a derivada na EDO
    - Precisamos isolar na nossa EDO $y'$ de um lado.
    - Com isso teremos do outro lado da equação nosso $f(x,y)$.
    
    $$
    f(x,y) = y
    $$
    
- 2º Passo - Identificar os Pontos
    - Temos no nosso caso:
    
    $$
    y_0 =  1, x_0 = 0
    $$
    
- 3º Passo - Determinar $h$
    - Precisamos aplicar a formula do erro de Euler para encontrarmos o passo.
    
    $$
    e(x_{k+1}) \le \frac{M_2}{2} h^2
    $$
    
    - Onde $M_2$ é o máximo valor da segunda derivada de $y$ entre o intervalo de análise, que no nosso caso seria $x = [0, 0.04]$.
    - Somos capazes de determinar isso pois sabemos a solução exata da nossa EDO, sendo $y = e^x \therefore M_2 = e^{0.04}$. Logo temos:
    
    $$
    \begin{aligned}
    e(x_{k+1}) &\le \frac{e^{0.04}}{2} h^2 \\ 
    h^2 &\le \frac{10^{-3} }{1.0408} \therefore h \le 0.0310
    \end{aligned}
    $$
    
    - Temos ainda que $h$ precisa ser um divisor do $x$ que queremos, que no nosso caso é $x=0.04$. Logo teremos $h = 0.02$
    
- 4º Passo - Aplicar o método de Euler
    - Podemos determinar quantos passos deveremos dar dividindo o $x$ alvo pelo nosso passo:
    
    $$
    nº \ passos = \frac{x}{h} = \frac{0.04}{0.02} = 2
    $$
    
    - Agora podemos achar $y_2$, e para isso achar $y_1$:
    
    $$
    y_1 = y_0 + f(x_0, y_0)h \\ 
    y_2 = y_1 + f(x_1, y_1)h
    $$
    
    <aside>
    <img src="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/mugi.gif" alt="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/mugi.gif" width="40px" /> Temos que $x_1 = x_0 + h$
    
    </aside>
    

# Taylor de Ordem P

$\hookrightarrow$ Para uma EDO de Ordem $p$ temos o seguinte erro:

$$
e(x_{k+1}) \le \frac{M_{p+1}}{(p+1)!} h^{p+1}
$$

$\hookrightarrow$ Para esse método numérico (onde o erro é um número vezes $h^{p+1}$) dizemos que é um método de ordem de convergência $p$.

<aside>
<img src="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/Hifumi_Surprised.png" alt="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Me%CC%81todo%20de%20Euler%20a2adbddbeece4cf781bc056c56ab804d/Hifumi_Surprised.png" width="40px" /> Com isso, temos que métodos para PVI com maior ordem de convergência $p$ converge em menores passos.

</aside>