# Funções Degrau

Aula: Aula 11
Created: April 28, 2021 10:24 AM
Prova: P1

# O que é uma função degrau ?

- É uma função que é definida por partes
- Exemplo:

$$
g(t) =  \begin{cases}
0 \ se \ 0 \le t \le 5 \\ 
\frac{t-5}{5} \ se\ 5\le t\le 10 \\
1 \ se r \ge 10
\end{cases}
$$

# Formas de representação

- Podemos representar pela forma explicita (utilizando cada caso, como demonstrado acima);
- Podemos ainda representar a função degrau como sendo uma única função formada pela soma (ou subtração) cada  "degrau".

## Forma de cada degrau

- Cada degrau de uma função de degraus pode ser representada como sendo:

$$
u_n \cdot f(x)
$$

- Onde $u_n$ é a representação que é uma função que começa no ponto $x = n$;
- $f(x)$ é a função que representa a para o degrau em específico.

<aside>
💡 OBS: A função $f(x)$  é "acumulativa" com o degrau diretamente anterior, isso é, se ela, no degrau anterior, fosse $f(x) = \cos x$, mas para esse degrau precisa ter o valor de $y=t^2$, precisamos "compensar" pelo comportamento anterior e falar que: $f(x) = (t^2 - \cos x)$ para que o degrau tenha então valor de $t^2$

</aside>

## Exemplo

$$
f(t) = \begin{cases}
\cos t, \ \ 0 \le t < \pi/2\\
t^2, \ \ \pi/2 \le t < 6\\
t, \ \ t\ge 6
\end{cases}
$$

- Precisamos achar o primeiro degrau:

$$
u_0(\cos t)
$$

- A partir disso, iremos obter o segundo degrau, lembrando que $f(x)$ junto ao degrau, quando não constante, é acumulativo com o diretamente anterior, logo precisa compensar o $f(x)$ anterior:

 

$$
u_{\frac{\pi}{2}}(t^2 - \cos t)
$$

- Podemos encontrar o último degrau:

$$
u_6(t - t^2)
$$

por fim temos:

$$
\boxed{f(t) = (\cos t) \cdot u_0 + (t^2 - \cos t)\cdot u_{\frac{\pi}{2}} + (t - t^2)u_6}
$$

- Se não compensarmos pela função do degrau anterior teríamos:
    
    ![Func%CC%A7o%CC%83es%20Degrau%209f2828f333dd47eb9d2bbc0bd347bc3e/Screen_Shot_2021-04-28_at_11.00.23_AM.png](Func%CC%A7o%CC%83es%20Degrau%209f2828f333dd47eb9d2bbc0bd347bc3e/Screen_Shot_2021-04-28_at_11.00.23_AM.png)
    

- Enquanto queríamos:

![Func%CC%A7o%CC%83es%20Degrau%209f2828f333dd47eb9d2bbc0bd347bc3e/Screen_Shot_2021-04-28_at_11.00.47_AM.png](Func%CC%A7o%CC%83es%20Degrau%209f2828f333dd47eb9d2bbc0bd347bc3e/Screen_Shot_2021-04-28_at_11.00.47_AM.png)