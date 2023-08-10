# Anotações de Aula

# Zeros de Funções

## O que é?

- Achar um $\lambda$ tal que $f(\lambda) = 0$
- Para funções mais conhecidas, existem métodos analíticos (e.g funções de segundo grau) mas outras não.

## Método Bissecção

### 1º Passo → Isolar

- Isolar o intervalo no qual você quer encontrar seu resultado.
- Pode ser estabelecido olhando o gráfico, no qual podemos utilizar alguns teoremas para auxiliar, como:

TEOREMA DO VALOR INTERMEDIÁRIO

> Se uma função é contínua, e seus extremos alteram de sinal, podemos afirmar que há pelo menos uma raiz em seu intervalo.
> 

TEOREMA DE ROLLE

> Se, em uma função contínua, se sua derivada não altera de sinal entre dois pontos críticos com sinais alternados, há somente uma raiz no intervalo.
> 

<aside>
<img src="Anotac%CC%A7o%CC%83es%20de%20Aula%20f5a1f4d27ef149a685d8a4e3df4174ec/Evangelion.gif" alt="Anotac%CC%A7o%CC%83es%20de%20Aula%20f5a1f4d27ef149a685d8a4e3df4174ec/Evangelion.gif" width="40px" /> Esse teoremas satisfazem e podemos afirmar que há somente uma raiz, mas não necessariamente todas as raizes seguem essa regra (e.g funções de segundo grau.)

</aside>

### 2º Passo → Dividir a parte ao meio

- Pegamos o intervalo onde há uma única raiz, e dividimos esse intervalo ao meio (no ponto $x_n  = \frac{a_n + b_n}{2}$)
- Depois da divisão, pegamos a metade que apresenta o ponto de mudança de sinal.
- Depois de repetir isso várias vezes, o ponto $x$ será a aproximação

### Condições de Parada

- Diferença Absoluta
    
    $$
    |x_k - x_{k-1}| < \epsilon
    $$
    
- Quase zero
    
    $$
    |f(x_k)| < \epsilon
    $$
    
- Intervalo Pequeno
    
    $$
    |b_k - a_k| < \epsilon
    $$
    

### Erro Máximo

- O número de passos necessários para garantir um erro máximo é menor que $\epsilon$:

$$
k > \frac{\log (b_0 - a_0) - \log(\epsilon)}{\log 2}
$$

$\hookrightarrow b_0, a_0$: Intervalo inicial.

$\hookrightarrow k$: Número de passos (o próximo inteiro do valor da conta) .

$\hookrightarrow \epsilon$: Erro máximo.