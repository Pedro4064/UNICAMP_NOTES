# Anotações de Aula

# Método de Newton

Queremos achar uma função $g(x)$ tal que:

$$
f(x) = 0 \Rightarrow g(x) = x
$$

Com isso, queremos achar um $g(x)$ tal que:

$$
|g'(\psi)| = 0, \ f(\psi) = 0
$$

Para isso temos:

$$
g(x) = x - \frac{f(x)}{f'(x)}
$$

Agora, para encontrar o ponto fixo de $g(x)$ temos:

$$
\boxed{x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}}
$$

Com isso teremos que o ponto fixo de $g(x)$ será o valor de $x$ para $f(x) = 0$, i.e o zero da nossa função.

- EXEMPLO
    
    $$
    f(x) = x^2 - 2 = 0
    $$
    
    1. Chute inicial $X_0$ (podemos usar outros métodos como o de bissecção para acharmos esse chute inicial). 
        
        $$
        x_0 = 1
        $$
        
    2. Aplicando a fórmula e o algoritmo recursivo para achar o ponto médio de $g(x)$.
        
        $$
        x_{n+1} = x_n - \frac{(x^2_n - 2)}{2x_n}
        $$
        

## Convergência

Para convergir precisamos que:

$$
f(x), f'(x) \ \ e \ \  f''(x) \rightarrow Cont. \ em \ torno \ de \ \psi \ e \ x_0
$$

$\hookrightarrow$ Isso significa que $x_0$ (i.e o chute inicial) precisa ser suficientemente próximo de $\psi$ (i.e o zero da função)

<aside>
<img src="Anotac%CC%A7o%CC%83es%20de%20Aula%203f14b35bd6804a18bccaee642e9060e1/Evangelion.gif" alt="Anotac%CC%A7o%CC%83es%20de%20Aula%203f14b35bd6804a18bccaee642e9060e1/Evangelion.gif" width="40px" /> OBS: Não diz o que "suficientemente próximo" é

</aside>

$\hookrightarrow$ Para algo mais exato temos que se:

$$
\frac{|f(x) \cdot f''(x)|}{|f'(x)^2|} < 1
$$

for válido para para um certo intervalo em torno de $\psi$, temos que irá convergir

## Velocidade de Convergência

- Falamos que é um algoritmo quadrático pois:

$$
|x_{n+1} - \psi| \le C|x_n - \psi|^2
$$

$\hookrightarrow$ $C$ é uma constante

---

### Representação Gráfica

- Começando de um ponto $x_0$, aproximar a curva $f(x)$ pela reta tangente:
    
    ![Screen Shot 2021-08-24 at 7.54.16 PM.png](Anotac%CC%A7o%CC%83es%20de%20Aula%203f14b35bd6804a18bccaee642e9060e1/Screen_Shot_2021-08-24_at_7.54.16_PM.png)
    

---

# Método da Secante

- Inspirada pela interpretação gráfica de Newton, mas sem a utilização da derivada:

$$
x_{n+1} = \frac{x_{n-1} f(x_n) - x_n f(x_{n-1})}{f(x_n) - f(x_{n-1})}
$$