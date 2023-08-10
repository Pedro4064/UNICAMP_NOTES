# Sistema de $EDO$ - Não Homogêneo

Created: June 20, 2021 9:40 AM
Prova: P2

# Método Matricial

## Resolução

1. Resolver a $EDO$ homogênea associada como [demonstrado anteriormente](Sistema%20de%20$EDO$%20-%20Homoge%CC%82neo%20f2cc23b6644b4de6ad22ec4edfd6555b.md), resultando na solução homogênea $X_h(t)$.
2. Encontrar a solução particular $X_p(t)$ que depende exclusivamente de $g(t)$.
3. Encontrar a solução geral fazendo a soma das duas anteriores: $X(t) = X_h(t) + X_p(t)$

## Solução Particular

- Existem dois métodos, sendo eles:

1. Método dos Coeficientes Indeterminados → A função $g(t)$ deve ter funções que sejam:
    - Funções Exponenciais: $e^{nt}$
    - Funções polinomiais: $t^n$
    - Funções trigonométricas: $\cos nt, \ \sin nt$
2.  Método de Variação dos Parâmetros → ...

### Método dos Coeficientes Indeterminados

- **Solução Particular - Polinomial**
    - Quando $g(t)$ tiver um polinômio, supomos que $X_p(t)$ é também um polinômio, de mesmo grau que o maior de $g(t)$, eg:
    
    $$
    g(t) = \begin{pmatrix}
    t^2 + 1 \\ t^3 + t
    \end{pmatrix} \therefore X_p(t) = \begin{pmatrix}
    At^3 + Bt^2 + Ct + D \\ Et^3 + Ft^2 + Gt + H
    \end{pmatrix}
    $$
    
- **Solução Particular - Exponencial**
    - Quando a matriz $g(t)$ tiver uma exponencial ou soma de exponenciais, supomos que $X_p(t)$ é também uma exponencial de mesmo expoente, e.g:
    
    $$
    g(t) = \begin{pmatrix}
    3e^{3t} \\ 3e^{t} 
    \end{pmatrix} \therefore X_p(t) = \begin{pmatrix}
    Ae^{3t} + Be^t \\ Ce^{3t} + De^t
    \end{pmatrix}
    $$
    
- **Solução Particular - Trigonométricas**
    - Quando a matriz $g(t)$ tiver uma função trigonométrica (senos e cossenos), supomos que $X_p(t)$ é também uma soma de seno e cosseno.
    
    $$
    g(t) = \begin{pmatrix} 
    \sin 2t \\ 3\cos 2t\end{pmatrix} \therefore 
    
    X_p(t) = \begin{pmatrix} 
    A\cdot \sin (2t) + B \cdot \cos (2t) \\ C\cdot \sin (2t) + D \cdot \cos (2t) \\  \end{pmatrix} 
    $$
    
    - Para cada valor diferente dentro do seno e do cosseno devemos ter a soma de sin e cos.

<aside>
💡 OBS: Se a solução já apareceu na solução homogênea, devemos adicionar mais um termo só que multiplicado por $t^{n + 1}$, onde $n$ é o valor do expoente de $t$ que aparece na resposta da homogênea.

</aside>

### Método de Variação dos Parâmetros

- Para o Método de Variação de Parâmetros, nós primeiramente achamos as resposta da homogênea associada e, com isso, a matriz fundamental:

$$
\psi(t) = \left( x^{(1)} \ \ \ x^{(2)}\right)
$$

- Com isso temos que:

$$
X(t) = \psi(t) \cdot u(t)
$$

- Onde:

$$
u(t) = \begin{pmatrix}u_1(t) \\ u_2(t) \end{pmatrix}
$$

- Que somos capazes de calcular por:

$$
u'(t) = (\psi(t))^{-1} \cdot g(t)
$$

- Lembrando que para matrizes $2\times 2$ temos que sua inversa é:

$$
\begin{bmatrix}a & b\\ c& d\end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d & -b \\ -c & a\end{bmatrix}
$$

- Com isso teremos a derivada de $u(t)$, logo precisamos integrar todos os elementos para termos $u(t)$ propriamente dito. Depois disso simplesmente multiplicamos  $\psi$  por $u$ e teremos nosso $X(t)$