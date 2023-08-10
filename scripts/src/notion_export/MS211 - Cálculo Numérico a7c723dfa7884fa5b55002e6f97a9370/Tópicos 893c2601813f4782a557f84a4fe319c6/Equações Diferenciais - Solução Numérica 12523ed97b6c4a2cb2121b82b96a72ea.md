# Equações Diferenciais - Solução Numérica

Aula: Aula 16
Created: October 5, 2021 5:49 PM
Prova: P2

[Anotações de Aula](Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Soluc%CC%A7a%CC%83o%20Nume%CC%81rica%2012523ed97b6c4a2cb2121b82b96a72ea/Anotac%CC%A7o%CC%83es%20de%20Aula%20293f26252991409ca448338435f9d465.md)

- SUMÁRIO

# Introdução

$\hookrightarrow$  Uma equação diferencial é uma equação que possui derivadas, e que nossas incógnitas são funções, e não valores.

$\hookrightarrow$  É de suma importância ter métodos de solução numérica pois a grande maioria de equações diferenciais que são úteis para a engenharia e na vida real não tem solução analítica, mas somente numérica.

$\hookrightarrow$  Exemplo: Equação do Pêndulo, uma equação não linear.

$$
\frac{d^2 \theta}{dt^2} + \frac{g}{L}\sin \theta = 0
$$

$\hookrightarrow$  Para esse tipo de equação (i.e não linear) podemos fazer duas coisas:

1. Simplificar: considerando $\theta \approx 0 \therefore \sin \theta = \theta$ e logo se torna linear, mas esse tipo de aproximação pode distorcer a realidade.
2. Solução Numérica: Através de calculo numérico nós achamos uma solução numérica.

# Solução Numérica

$\hookrightarrow$  Para a análise numérica de EDOs precisamos import algumas restrições, pois por natureza equações diferenciais tem infinitas soluções, mas como estamos tratando de uma solução numérica pode haver somente uma. 

<aside>
<img src="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Soluc%CC%A7a%CC%83o%20Nume%CC%81rica%2012523ed97b6c4a2cb2121b82b96a72ea/kawasegaua.png" alt="Equac%CC%A7o%CC%83es%20Diferenciais%20-%20Soluc%CC%A7a%CC%83o%20Nume%CC%81rica%2012523ed97b6c4a2cb2121b82b96a72ea/kawasegaua.png" width="40px" /> Para uma equação diferencial e ordem $n$ precisamos import restrições até a derivada $n-1$  para que seja possível soluciona-la numericamente.

</aside>

$\hookrightarrow$  Temos então dois tipos de problemas de equações diferenciais, sendo eles:

- PVI - Problemas de valor inicial
- PVC - Problemas de valor de contorno

## Problemas de Valor Inicial [PVI]

$\hookrightarrow$  Que é composto de uma equação de primeiro ordem e sua respectiva restrição de valor inicial:

$$
\begin{cases}
\frac{dy}{dx} = f(x, y) \\ 
y(x_0) = y_0
\end{cases}
$$

$\hookrightarrow$  Tendo como exemplo o problema do crescimento populacional:

$$
\begin{cases}
\frac{dN(t)}{dt} = \overbrace{\lambda}^{t. \ crescimento} N(T) \\ 
N(0) = N_0
\end{cases}
$$

$\hookrightarrow$  Que teria como  pergunta: Qual a população $N(10)$? Que estaria perguntando $y_k$ que é uma aproximação numérica para $y(x_k)$ onde $x_k = 10$. 

$\hookrightarrow$  Ou ainda pediria para você traçar o gráfico de $t_0$ até $t_n$, com um tamanho de passo de $h$, que se refere o "espaço" entre cada número (como o `step` no `np.arange(start, stop, step)`).

```python
>>> np.arange(0,10,0.1)
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. , 2.1, 2.2, 2.3, 2.4, 2.5,
       2.6, 2.7, 2.8, 2.9, 3. , 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8,
       3.9, 4. , 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5. , 5.1,
       5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6. , 6.1, 6.2, 6.3, 6.4,
       6.5, 6.6, 6.7, 6.8, 6.9, 7. , 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7,
       7.8, 7.9, 8. , 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9. ,
       9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9])
```

## Métodos Numéricos para PVI

$\hookrightarrow$  Podemos dividir os diferentes métodos numéricos para resolver problemas de valores iniciais em:

- Métodos de Passo Simples: Onde calculamos $y_k$ a partir de somente $y_{k -1}$.
- Métodos de Passo Múltiplo: Onde calculamos $y_k$ com outros valores de $y$ além do diretamente anterior.