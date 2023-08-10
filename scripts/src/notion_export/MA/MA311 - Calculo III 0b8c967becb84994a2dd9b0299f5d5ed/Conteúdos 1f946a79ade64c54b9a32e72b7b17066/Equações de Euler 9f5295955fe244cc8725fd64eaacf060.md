# Equações de Euler

Aula: Aula 6
Created: April 12, 2021 7:38 PM
Prova: P1

# Equação Modelo

$$
ax^2y'' + bxy' + cy = 0
$$

- Observe que as potencias da variável $x$ coincidem com a ordem da derivada de $y$, isso é uma equação de Euler.
- Observe, também, que até o momento nós vimos somente equações de grau igual ou maior que dois com coeficientes constantes, mas agora temos em função de $x$.

# Equação Característica e Solução

- Assim como nas outras equações de grau 2, precisamos da equação característica para acharmos as soluções da EDO.
- No caso específico da equação de Euler, temos a equação característica como sendo:

$$
ar^2 + (b-a)r + c = 0
$$

- A partir disso temos 4 Casos:

$\boxed{\Delta = (b-a)^2 - 4ac}$

1. Raizes reais distintas ($\Delta > 0$): 
    
    $y(x) = c_1x^{r_1} + c_2x^{r_2}$
    
2. Raizes complexas (do tipo $r = \alpha + i\beta$) conjugadas ($\Delta < 0$) :
    
    $y(x) = c_1x^\alpha \cos(\beta \ln x) + c_2x^\alpha \sin(\beta \ln x)$
    
3. Raizes repetidas ($\Delta = 0$):
    
    $y(x) = c_1x^{r_1} + c_2x^{r_1}\ln x$