# Método de Frobenius - Ponto Singular Regular

Created: June 19, 2021 10:50 AM
Prova: P2

# O que é um Ponto Singular Regular?

Para uma $EDO$ do formato:

 

$$
P(x)y'' + Q(x)y' + R(x)y = 0
$$

Dizemos que um Ponto $x_0$ é singular $\iff P(x_0) = 0$.

Além disso, dizemos que um ponto $x_0$ é singular regular se:

$$
\lim_{x\rightarrow x_0}(x - x_0) \frac{Q(x)}{P(X)} \Rightarrow \exist
$$

$$
\lim_{x\rightarrow x_0}(x - x_0)^2 \frac{R(x)}{P(X)} \Rightarrow \exist
$$

# Como resolver ?

- 1- Verificar que o ponto $x_0$ é singular regular
    
    $$
    \lim_{x\rightarrow x_0}(x - x_0) \frac{Q(x)}{P(X)} \Rightarrow \exist
    $$
    
    $$
    \lim_{x\rightarrow x_0}(x - x_0)^2 \frac{R(x)}{P(X)} \Rightarrow \exist
    $$
    
    - Existem e são finitos
    
- 2- Definir $y$ e suas derivadas e substituir na $EDO$
    
    $$
    \begin{cases}
    y(x) = \sum^\infty_{n=0} a_nx^{n+r} \\ 
    
    y'(x) = \sum^{\infty}_{n=0}(n+r)a_nx^{n+r-1}
    \\
    y''(x) = \sum^{\infty}_{n=0}(n+r)(n+r-1)a_nx^{n+r-2}
    \end{cases}
    $$
    
    <aside>
    <img src="Me%CC%81todo%20de%20Frobenius%20-%20Ponto%20Singular%20Regular%202295247fa9334d0a86dc94bdb3c5f477/Hifumi_Surprised.png" alt="Me%CC%81todo%20de%20Frobenius%20-%20Ponto%20Singular%20Regular%202295247fa9334d0a86dc94bdb3c5f477/Hifumi_Surprised.png" width="40px" /> OBS: diferente de quando nós estamos calculando com ponto ordinário, os índices das derivadas não mudam!
    
    </aside>
    
- 3- Igualar as potências de $x$ por $x^{n+r}$
- 4- Caso não estejam, igualar os índices dos somatórios pelo maior.
- 5- Resolver a equação indicial, que é a parte da equação que sobre para fora do somatório. E observar o comportamento da subtração das raizes.
    - Se você subtrair a raiz menor da raiz maior e a diferença NÃO der um número inteiro positivo ou zero, temos então duas soluções linearmente independentes, caso contrário teremos somente uma solução.
- 6- Juntar os somatórios e botar $x^{n+r}$ em evidência, e igualar o que está dentro do parênteses a zero→ encontrando a relação de recorrência.
- Calcular alguns $a_n$'s caso haja mais de uma solução e expressar $a_n$ em função de $n$