# Impedância

Aula: Aula 14
Created: June 22, 2021 10:20 AM
Prova: P3

# Relembrando

- Antes de falarmos sobre a impedância propriamente dito, vamos primeiro relembrar da relação de tensão e corrente no mundo fasorial para os principais bipolos com que trabalhamos:
    - **Resistências**
        
        $$
        \hat{V} = R\hat{I}
        $$
        
    - **Capacitâncias**
        
        $$
        \hat{V} = -j\frac{1}{\omega \cdot C} \hat{I}
        $$
        
    - **Indutância**
        
        $$
        \hat{V} = j \omega L \hat{I}
        $$
        

- Podemos observamos que sempre estamos encontrando a relação da tensão e corrente com um fator de proporcionalidade, sendo eles $R$ para resistências, $-j \frac{1}{\omega C}$ para capacitâncias e $j \omega L$ para a indutância. Tais constantes de proporcionalidade são chamadas de IMPEDÂNCIA ⇒ $Z$.

# Impedância

$$
\overbrace{\hat{V}}^{[V]} = \underbrace{Z}_{[\Omega]} \overbrace{\hat{I}}^{[A]}
$$

## Impedâncias em Série

- Temos que a impedância equivalente para um circuito em série é simplesmente a soma das impedâncias (de forma análoga a como era a associação de resistências em série)

$$
Z_{eq} = \sum^k_{n = 1} Z_n
$$

- Imaginando agora um circuito com uma resistência, capacitância e indutância em série (circuito $RLC$
), temos que a indutância equivalente vai ser constituída de uma parte real (das resitências) e uma parte imaginária (reatância do circuito) .

## Impedâncias em Paralelo

- Da mesma forma que circuito resistivo em paralelo, o inverso a impedância equivalente é igual a soma dos inversos das impedâncias do circuito.

## Reatância e suas Implicações

- Vimos que para um circuito $RLC$ temos que a parte imaginária da impedância resultante é chamada de reatância do circuito e que ela é influênciada pelas capacitâncias e indutâncias presentes no circuito.
- Levando isso com consideração, a relação das reatâncias oriundas de capacitores e das reatâncias oriundas dos indutores geram 3 possíveis caracterizações para o circuito, sendo elas:
    1. Puramente Indutivo ⇒ Reatância indutiva se sobrepõe a dos capacitores.
    2. Puramente Capacitivo ⇒ Reatância capacitiva se sobrepões à indutiva.
    3. Puramente Resistiva ⇒ Se anulam.
    

### Análise Fasorial Circuito Puramente Indutivo

$$
\hat{V} = \omega L I \phase{(\theta + 90º)}
$$

- Com isso podemos ver que para um  circuito puramente indutivo a corrente está atrasada em relação à tensão em $90º$.

### Análise Fasorial Circuito Puramente Capacitivo

 

$$
\hat{V} = \frac{I}{\omega C}\phase{(\theta - 90º)}
$$

- Com isso vemos que para um circuito puramente capacitivo a tensão está atrasada em $90º$ em relação à corrente.

### Análise Fasorial Circuito Puramente Resistivo

- Não ocorre atraso.

-