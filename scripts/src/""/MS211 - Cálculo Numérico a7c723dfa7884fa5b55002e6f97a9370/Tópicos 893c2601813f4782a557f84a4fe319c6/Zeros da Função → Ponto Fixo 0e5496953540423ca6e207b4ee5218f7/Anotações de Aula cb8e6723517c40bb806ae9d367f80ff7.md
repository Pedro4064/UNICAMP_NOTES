# Anotações de Aula

# Ponto Fixo

## Primeiro Passo → Transformar em Problema de ponto fixo

- Transformamos em um problema de ponto fixo
- e.g: Queremos achar a raiz para essa função
    
    $$
    f(x) = x^2 - x - 2 = 0 \\ \Downarrow
    $$
    
    $$
    g(x) = \sqrt{2 + x}
    $$
    

## Segundo Passo → partindo de um $x_0$ Inicial, aplicamos recursivamente

$$
x_{n+1} = g(x_n)
$$

## Teorema de convergência do ponto fixo

- A derivada do valor absoluto de $|g(x) |$  precisa ser menor que zero:

$$
\frac{d|g(x)|}{dx} < 1
$$