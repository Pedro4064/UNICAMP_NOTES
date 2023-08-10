# Sistema Linear - Triangular Superior

Aula: Aula 06
Created: September 27, 2021 12:34 PM

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ Esse tipo de algoritmo é usado em casos específicos onde o sistema linear, em sua representação matricial, resulta em uma matriz $A$ triangular (seja ela superior ou inferior, mas iremos abordar como exemplo a superior).

$\hookrightarrow$ Uma matriz é dita triangular quando acima ou abaixo da sua diagonal principal todos os elementos são nulos.

# Implementação do Algoritmo

$\hookrightarrow$ Nesse algoritmo nós resolvemos de baixo para cima, levando em consideração uma matriz triangular superior. Com isso temos, para uma matriz $A_{n, n}$:

```python
A = [...]
x = [...]
b = [...]

#! Acho que seria reversed(range(0,n)) pois index começa no zero
for k in reversed(range(1, n)):
	s = 0

	for j in range(k + 1, n):
		s+= A[k][j] * x[j]

	
	x[k] = (b[k] - s) / A[k][K]
		
```

- RESOLUÇÃO MATEMÁTICA
    
    ![Screen Shot 2021-09-27 at 12.57.24 PM.png](Sistema%20Linear%20-%20Triangular%20Superior%20285f929888214138a92085b4b4eb7248/Screen_Shot_2021-09-27_at_12.57.24_PM.png)
    

# Ordem de Complexidade

$\hookrightarrow$ No quesito de comparação de complexidade, temo e memória necessária para um algoritmo nós utilizamos a "Big - O" notation. 

$\hookrightarrow$ Nesse caso, ocorre um loop dentro de um loop, com isso temos que o big-o notation é:

$$
O(n^2)
$$