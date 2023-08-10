# Anotações de Aula

# Aproximações

## Principais Tipos de Aproximações

### Truncamento (floor)

- Quando um número possui $n$ casa decimais amais do que o se é possível guardar.
- Quando isso ocorre, existe a possibilidade de simplesmente ignorarmos os números que passaram do armazenamento → chamamos isso de truncamento

### Arredondamento (ceil)

- No caso descrito acima, existe a possibilidade de arredondar o número ao invés de fazer o truncamento do mesmo.
- Arredondamento:
    
    $\hookrightarrow$ Se o último digito "válido" for menor que $5$ → o número arredondado para baixo;
    
    $\hookrightarrow$ Se o último digito válido for maior que $5$ → o número é arredondado para cima;
    
    $\hookrightarrow$ Se o último digito válido for igual a $5$ → o comportamento depende da implementação da linguagem em utilização.
    

## Erros de Aproximação

- Temos 2 tipos de erro:
    - **Erro Absoluto**
        
        $$
        E_A = |x - \bar{x}|
        $$
        
         $\hookrightarrow x$ → Valor Exato
        
        $\hookrightarrow \bar{x}$ → Valor com Erro 
        
    - **Erro Relativo**
        - Considera a ordem de grandeza do número, utilizamos quando queremos analizar se a ordem de grandeza do nosso erro é considerável.
        
        $$
        E_R = \frac{|x-\bar{x}|}{|\bar{x}|}
        $$
        
         $\hookrightarrow x$ → Valor Exato
        
        $\hookrightarrow \bar{x}$ → Valor com Erro 
        
    
- Além disso, temos uma fórmula do erro máximo, que depende se é feito o arredondamento ou truncamento.
    - Truncamento
        
        $$
        E_A < 10^{e - n}
        $$
        
        $\hookrightarrow n$ → Quantidade de dígitos
        
        $\hookrightarrow e$  → Ordem de grandeza
        
        $$
        E_R < 10^{-n+1}
        $$
        
    - Arredondamento
        
        $$
        E_A \le 0.5 \times 10^{e-n}
        $$
        
        $\hookrightarrow n$ → Quantidade de dígitos
        
        $\hookrightarrow e$  → Ordem de grandeza
        
        $$
        E_R < 0.5 \times 10^{-n + 1}
        $$
        

- Com isso, observamos que o erro do arredondamento é menor do que no truncamento, mas isso também implica em um custo computacional maior.

## Erros de Operações

### Erro de Cancelamento/Catastrófico

$\hookrightarrow$ Ocorre na subtração de $x - y$ quando $x \approx y$

$\hookrightarrow$ Considerando $x = 28.9$ e $y = 28$, calculando $x-y$ em uma máquina onde float tem 2 dígitos e utilizando arredondamento temos:

$$
\bar{x} = 0.29 \times 10^2 \ \ \\ \bar{y} = 0.28 \times 10^2
$$

$\hookrightarrow$ Nesse caso teremos:

$$
\begin{aligned}E_{R_x} &\approx 3 \times 10^{-3} \\ 
E_{R_y} &\approx 0\end{aligned}
$$

e 

$$
\bar{x} - \bar{y} = 0.1 \times 10^2 = 1\\
\Downarrow \\
E_{R_{x-y}} = \frac{|1 - 0.9|}{1} = 0.1 >>> E_R{_x},E_{R_y}
$$

$\hookrightarrow$ Observamos que a ordem da grandeza do erro é muito maior do que os erros dos números.