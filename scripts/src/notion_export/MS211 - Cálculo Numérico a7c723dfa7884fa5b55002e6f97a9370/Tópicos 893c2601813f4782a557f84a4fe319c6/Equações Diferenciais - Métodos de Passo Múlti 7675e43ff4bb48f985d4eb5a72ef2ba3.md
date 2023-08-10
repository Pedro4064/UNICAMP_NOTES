# Equações Diferenciais - Métodos de Passo Múltiplo e Equações de Ordem Superior

Aula: Aula 18
Created: November 10, 2021 9:50 PM
Prova: P2

- SUMÁRIO
    
    

# Introdução - Métodos de Passo Múltiplo

$\hookrightarrow$ Como dito no início do capitulo de métodos numéricos para resolução de EDOs, os métodos podem ser caracterizados como métodos simples, i.e dependem somente do passo anterior $y_k$ para encontrar o valor $y_{k+1}$, e em métodos de passo múltiplo, que depende de mais iterações do que somente a da diretamente anterior.

$\hookrightarrow$ Tais métodos de passo múltiplo muitas das vezes usam as estratégia de tornar uma equação diferencial em integrais:

 

$$
\begin{aligned}
y'(x) &= f(x, y(x)) \\ 
\int^{x_{k+1}}_{x_k} y'(x) &= \int^{x_{k+1}}_{x_k}f(x, y(x)) \\ 
y(x_{k+1}) - y(x_{k}) &= \int^{x_{k+1}}_{x_k}f(x, y(x)) \\ 
\end{aligned}
$$

Que podemos reescrever como:

$$
y(x_{k+1})=y(x_{k}) +  \int^{x_{k+1}}_{x_k}f(x, y(x)) \\ 
$$

Onde iremos realizar a integração  numérica de $f(x, y(x))$, que necessita de valores além do diretamente anterior → Por isso é um método de passos múltiplos.

# Métodos Explícitos e Implícitos

$\hookrightarrow$ Os métodos numéricos de EDO podem ser dividido em dois tipos, sendo eles:

- Métodos Explícitos → Que dependem somente de iterações anteriores.
- Métodos Implícitos → Que dependem, além das iterações anteriores, da iteração atual.

## Métodos Explícitos

### Adams-Bashforth 4 ordem

$$
y_{k+1} = y_k + \frac{h}{24} [55 \cdot f(x_k, y_k) - 59 \cdot f(x_{k-1}, y_{k-1}) + 37 \cdot f(x_{k-2}, y_{k-2}) - 9 \cdot f(x_{k-3}, y_{k-3})]
$$

$\hookrightarrow$ Levando em consideração que esse método necessita de 3 valores anteriores, ele só pode ser aplicado a partir do 4 ponto. O que implica na necessidade de aproximações para os 3 primeiros pontos (seja por outros métodos ou sejam eles dados)

## Métodos Implícitos

### Adams-Moulton

$\hookrightarrow$ Nesse tipo de método, nós precisamos de uma previsão de $y_{k+1}$ para calcular $y_{k+1}$.

$\hookrightarrow$ Esse tipo de método é chamado de previsão-correção, onde utilizamos um método explícito para fazer a primeira aproximação (nesse caso utilizaremos o método Adams-Bashforth de quarta ordem)  para então calcularmos o valor pelo método implícito.

$$
y_{k+1} = y_k + \frac{h}{24}[9 \cdot f(x_{k+1}, y_{k+1}) + 19 \cdot f(x_k, y_k) - 5 \cdot f(x_{k-1}, y_{k-1}) + f(x_{k-2}, y_{k-2})]
$$