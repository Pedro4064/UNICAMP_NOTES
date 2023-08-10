# Análise Nodal e de Malhas Modificadas

Aula: Aula 4
Created: April 13, 2021 9:17 AM
Prova: P1

# Análise Nodal Modificada

## Super Nós

- Idealmente, resistências internas de fontes de tensão são nulas. $\therefore$ Podemos considerar como um "Curto circuito", somente um nó.
- Levamos em consideração a equação da fonte sendo: $D.D.P = \Delta V$

### Exemplo

![Ana%CC%81lise%20Nodal%20e%20de%20Malhas%20Modificadas%20a949679177674f2196429a53fa519c60/circuit.png](Ana%CC%81lise%20Nodal%20e%20de%20Malhas%20Modificadas%20a949679177674f2196429a53fa519c60/circuit.png)

Considerando o ramo contendo a fonte de tensão como sendo um super nó, de número 2, o nó mais embaixo como sendo nosso nós de referência e a convenção de correntes que entram como sendo negativas e que saem como positivas, temos: 

$$
\begin{cases}
Nó \ 1: -(-3A) + \frac{v_1 - v_2}{3} - (-8A) + \frac{v_1 - v_3}{4} = 0 \\ 
Super\ Nó: -\frac{v_1 - v_2}{3} + \frac{v_2}{1} + \frac{v_3}{5} + (-25A) - \frac{v_1 - v_3}{4} + (-3A) = 0 \\ 
Fonte: v_3 - v_2 = 22V
\end{cases}
$$

- Com isso temos:

$$
\begin{cases}
v_1 = 32.86V \\ 
v_2 = -14.43 \\ 
V_3 = 7.57V 
\end{cases}
$$

# Análise de Malhas Modificadas

- Quando há uma fonte de corrente.

## Super Malhas

- Em uma fonte de corrente ideal a resistência interna é infinita $\therefore$ o circuito é aberto.