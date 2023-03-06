# Transformada de Laplace e Problemas de Valores Iniciais

Aula: Aula 10
Created: April 26, 2021 8:21 PM
Prova: P1

# Introdução

- Considerando a EDO de segundo grau:

$$
ay''(t) + by' + cy(t) = f(t), \ \ y(0)=y_0 \ e \  y'(0) = y_1
$$

- Através da propriedade de linearidade de Laplace temos que:

$$
a\mathcal{L}\{y''(t)\} + b\mathcal{L}\{y'(t)\} + c\mathcal{L}\{y(t)\} = \mathcal{L}\{f(t)\}
$$

- Iremos ver que existe relação entre as transformadas das derivadas de $y$, como $y''$ e $y'$ e a transformada do próprio $y$. E iremos explorar essa relação para facilitar na hora da conta.

# Transformada da Derivada $y'$

$$
\boxed{\mathcal{L}\{y'(t)\} = s\mathcal{L}\{y(t)\} - y(0)}
$$

# Transformada da Derivada $y''$

$$
\boxed{\mathcal{L}\{y''(t)\} = s^2\mathcal{L}\{y(t)\} - sy(0) - y'(0)}
$$

# Transformada das Derivadas de Ordem maior igual a 2

$$
\mathcal{L}\{y^{(n)}(t)\} = s^n\mathcal{L}\{y(t)\} - s^{n-1}y(0) - s^{n-2}y'(0) -...-y^{(n-1)}(0)
$$

# Exemplos

## Exemplo 1

- Use a transformada de Laplace para determinar a solução do $PVI$:

$$
y'' - y' - 6y = 0, \ \ y(0)=2 \ e \ y'(0) = -1
$$

- Primeiramente iremos aplicar a propriedade de linearidade da transformada:

$$
\mathcal{L}\{y''\} - \mathcal{L}\{y'\} - 6\mathcal{L}\{y\} = 0
$$

- Iremos usar $Y(s) = \mathcal{L}\{y(t)\}$ para facilitar no momento da conta.
- Agora podemos achar as transformadas das derivadas por meio da transformada da função original $y(t)$:

$$
s^2Y(s) - sy(0) - y'(0) - (sY(s) - y(0)) - 6Y(s) = 0
$$

- Sabemos, entretanto, os valores de $y(0)$ e $y'(0)$ pelos valores iniciais, com isso teremos:

$$
s^2Y(s) - 2s + 1 - sY(s) + 2 - 6Y(s) = 0 \Rightarrow Y(s) = \frac{2s - 3}{s^2 - s - 6}
$$

- Precisamos rearrumar a equação de $Y(s)$ (achando as frações parciais) para que possamos aplicar a transformada inversa.

$$
Y(s) = \frac{2s - 3}{(s-3)(s+2)}
$$

- Com isso podemos separar em duas partes a transformada:

$$
\frac{A}{s-3} + \frac{B}{s+2}, \ tal \ que: \\
A(s+2) + B(s-3) = 2s-3
$$

Com essa última expressão somos capazes de achar os valores de $A = \frac{3}{5}$ e $B=\frac{7}{5}$. Temos, então:

$$
Y(s) = \frac{3}{5}\frac{1}{s-3} + \frac{7}{5}\frac{1}{s+2}
$$

- Aplicando a transformação inversa, juntamente com sua propriedade de linearidade temos:

$$
\mathcal{L}^{-1}\{Y(s)\} = \frac{3}{5}\mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\} + \frac{7}{5}\mathcal{L}\left\{\frac{1}{s+2}\right\}
$$

- Através da tabela ade transformadas temos que:

$$
\mathcal{L}^{-1}\left\{\frac{1}{s-a}\right\} = e^{+at}
$$

- Logo temos:

$$
y(t) = \frac{3}{5}e^{3t} + \frac{7}{5}e^{-2t}
$$

# Frações Parciais

- Pode ocorrer de que:

$$
Y(s) = \frac{P(s)}{Q(s)}
$$

tal que $P(s)$ e $Q(s)$ sejam polinômios de grau $m, n$ respectivamente com $m<n$. Para isso temos o método de frações parciais.

## Exemplo

- Use a transformada de Laplace para determinar a solução do $PVI$:

$$
y'' + 4y = \sin(3t),\ \ y(0) = 0 \ e \ y'(0) = 0
$$

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.21.52_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.21.52_AM.png)

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.22.00_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.22.00_AM.png)

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.22.08_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.22.08_AM.png)

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.22.59_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.22.59_AM.png)

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.23.08_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.23.08_AM.png)

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.23.28_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.23.28_AM.png)

# Translação em S

![Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.43.54_AM.png](Transformada%20de%20Laplace%20e%20Problemas%20de%20Valores%20Ini%20e6464c1b5bca4ee5b768724a722e5c91/Screen_Shot_2021-04-27_at_10.43.54_AM.png)