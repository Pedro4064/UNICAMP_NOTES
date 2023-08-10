# Transformada de Laplace da Função Degrau

Aula: Aula 11
Created: April 28, 2021 11:28 AM
Prova: P1

# Transformada da Função Degrau

$$
\boxed{\mathcal{L}\{u_c(t)\} = \frac{e^{-sc}}{s}}
$$

# Transformada de uma Função Multiplicada por um Degrau

$$
\boxed{\mathcal{L}\{u_c(t)f(t-c)\} = e^{-cs}\mathcal{L}\{f(t)\}}
$$

## Exemplo

- Considerando o seguinte degrau:

$$
g(t) = u_0 \sin t
$$

- Temos que:

$$
\mathcal{L}\{u_0\sin t\} = \mathcal{L}\{u_0 \sin(t-0)\} = e^{-0s}\mathcal{L}\{\sin t\} = \frac{1}{s^2 + 1}
$$