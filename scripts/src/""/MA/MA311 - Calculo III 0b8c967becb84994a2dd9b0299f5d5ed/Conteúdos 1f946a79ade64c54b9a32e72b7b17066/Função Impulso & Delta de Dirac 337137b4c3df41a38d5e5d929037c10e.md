# Função Impulso & Delta de Dirac

Aula: Aula 12
Created: April 28, 2021 9:26 PM
Prova: P1

# Função Impulso

Em algumas aplicações modeladas por equações diferenciais da forma:

$$
ay'' + by' + cy = g(t)
$$

a função de entrada $g(t)$ pode ser impulsiva, isso é, assumir um valor grande em um intervalo pequeno e ser nula fora desse intervalo.

# Delta de Dirac

A "função" dental de Dirac, no ponto $t_0$ é definida como o limite de $g_{t_0,\epsilon}(t)$ quando $\epsilon \rightarrow 0$ é denota por: 

$$
\delta(t-t_0)
$$

## Transformada da Delta de Dirac

$$
\mathcal{L}\{\delta(t-t_0)\} = \lim_{\epsilon\rightarrow 0}\mathcal{L}\{g_{t_0,\epsilon}(t)\}  = \boxed{e^{-t_0s}}
$$

## Integral

Sabemos ainda que:

$$
\int^c_b f(x) \delta(x-a) dx = f(a)
$$

<aside>
💡 Útil para se precisarmos calcular laplace da multiplicação de uma delta de dirac por uma função qualquer através da definição de transformada.

</aside>