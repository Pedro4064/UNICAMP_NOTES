# Introdução às  Equações Diferenciais e Suas Classificações

Aula: Aula 1
Created: March 15, 2021 7:04 PM
Prova: P1

# Classificações

## Número de Variáveis Independentes

Quanto ao número de variáveis independentes, podemos classificar equações diferenciais em duas categorias:

### Equações Diferenciais Ordinárias

- Dependem somente de uma variável independente.

### Equações Diferenciais Parciais

- Dependem de duas ou mais variáveis independentes.

## Ordem

A ordem de uma equação diferencial se refere à ordem da derivada de maior ordem que aparece na equação.

e.g: $\boxed{y'''}+ 2e^t + yy' = t^4$  é uma equação diferencial de terceira ordem. 

## Linearidade

### Linear

- Uma equação diferencial é dita linear quando:
    1. A variável dependente e suas derivadas estiverem elevadas somente à $1$;
    2. Os coeficientes que multiplicam a variável dependente e suas derivadas dependem apenas da variável independente.
    
    eg:
    
    $$
    x^5 \frac{d^5 y}{dx^5} + x^3 \frac{d^3 y}{dx^3}  \rightarrow É \ Linear
    $$
    
    $$
    \boxed{y\frac{dy}{dx}} + \frac{dy}{dx} \rightarrow Não \ é \ Linear
    $$
    
    $$
    \frac{d^2 \theta}{dt^2} + \frac{g}{L} \boxed{\sin \theta} = 0 \rightarrow Não \ é \ Linear
    $$
    

### Não Linear

- Se não satisfazer o que foi apresentado acima, ela é considerada não linear.

## Homogênea e Não Homogênea

As EDOs de primeira ordem possui a seguinte estrutura:

$$
q(x)\frac{dy}{dx} + r(x)y = g(x)
$$

Exemplos:

$$
-6x\frac{dy}{dx} + 4y = 0 \ \  \ \ \ \ \  \ \ (1)
$$

$$
-2x^3 \frac{dy}{dx} + y = 10x \ \ \ \ \ \  (2)
$$

### Homogênea

EDOs de primeiro grau são ditas homogêneas quando $g(x) = 0$, como no exemplo $1$.

### Não Homogênea

Quando $g(x) \neq 0$ , como no exemplo $2$