# Sistema Linear - Eliminação de Gauss

Aula: Aula 07
Created: August 31, 2021 7:01 PM
Prova: P1

[Anotações de Aula](Sistema%20Linear%20-%20Eliminac%CC%A7a%CC%83o%20de%20Gauss%209043207448ff4c2388705d3c3919062b/Anotac%CC%A7o%CC%83es%20de%20Aula%2057e4a2793e364d9d8a265f6302fa794a.md)

- SUMÁRIO
    
    

# Introdução

$\hookrightarrow$ O método de eliminação de Gauss nada mais é do que uma série de operações, chamadas de operações elementares, a fim de tornar a matriz em questão triangular.

# Operações Elementares

$\hookrightarrow$ Podemos fazer uma série de operações com nosso sistema linear sem altera-lo. Sendo elas:

- Permuta de Linhas
- Multiplicação Escalar
- Soma/Subtração de uma Equação pela outra

# Eliminação de Gauss

$\hookrightarrow$ Fazemos operações elementares visando triangularizar o sistema.

$\hookrightarrow$ Essa estratégia é a mais conhecido, levando em consideração que vemos ela em AlgeLin.

$\hookrightarrow$ De forma resumida ela consiste em utilizar uma linha de cada vez como pivô, e através dele irmos zerando aquela coluna específica para todas as linhas abaixo do pivô.

$\hookrightarrow$ Lembrando sempre de utilizar a matriz aumentada.

<aside>
<img src="Sistema%20Linear%20-%20Eliminac%CC%A7a%CC%83o%20de%20Gauss%209043207448ff4c2388705d3c3919062b/Screen_Shot_2021-09-23_at_11.49.01_PM.png" alt="Sistema%20Linear%20-%20Eliminac%CC%A7a%CC%83o%20de%20Gauss%209043207448ff4c2388705d3c3919062b/Screen_Shot_2021-09-23_at_11.49.01_PM.png" width="40px" /> Para triangularizarmos uma matriz $A_{m, \ n}$ iremos precisar de $n-1$ etapas. Onde a etapa $k$ elimina $x_k$ das linhas $k+1, k+2, ..., m$, isso é, elimina todos os $x_k$ das linhas abaixo.

</aside>

## Algoritmo Matemático

$\hookrightarrow$ Basicamente multiplicamos a linha pivô pelo multiplicador $m_{ik}$ e a subtraímos da linha alvo, zerando-a.

$$
m_{ik} = \frac{a_{ik}^{(k-1)}}{a_{kk}^{(k-1)}}
$$

## Algoritmo Computacional

```python
A = [...]
b = [...]
x = [...]

n = len(A)

# Passamos por cada linha como pivô
for k in range(n):
	# Se necessário, acho que iriamos fazer o pivoteamento parcial nessa etapa

	# Passamos por cada linha abaixo do Pivô 
	for i in range(k + 1, n):
		
		# Calcular o Multiplicador
		m = A[i][k] / A[k][k]
		A[i][k] = 0

		# Aplicamos a Operação para o restante da linha
		for j in range(k + 1, n):
			A[i][j] -= A[k][j] * m

		# Aplicamos para o vetor b (como aplicamos as operações na matriz aumentada)
		b[i] -= m * b[k]
		
```

### Big-O Notation

$\hookrightarrow$ Levando em consideração as instruções mais pesadas (i.e multiplicações e divisões) juntamente com os nestted loops temos :

$$
O(n^3)
$$

## Pivoteamento Parcial

$\hookrightarrow$ Ao analisarmos de perto o multiplicador, vemos que se o elemento pivô for zero ou muito próximo de zero, teremos um problema.

$\hookrightarrow$ A fim de evitar isso, podemos permutar (i.e trocar) as linhas entre as equações para que o pivô seja o maior possível em módulo.

## Pivoteamento Total

$\hookrightarrow$ Podemos alterar não somente as linhas, mas também coluna, resultando em um custo computacional muito grande com pouco retorno no que tange evitar propagação de erros. 

$\hookrightarrow$ Por isso não usamos o pivoteamento total.