# Segunda Lei da Termodinâmica

Aula: Aula13, Aula14, Aula15, Aula16
Cap.: Cap. 5
Created: September 27, 2021 9:27 AM

[Anotações de Aula](Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/Anotac%CC%A7o%CC%83es%20de%20Aula%20cbe707db853d40c5a7587f0eb7e9992b.md)

- SUMÁRIO
    
    

# Enunciados da Segunda Lei

- Enunciado de Clausius
    
    > É impossível para qualquer sistema operar de tal maneira que o único resultado seja a transferência de energia sob a forma de calor de um corpo mais frio para um corpo mais quente.
    > 
    - Basicamente para que ocorra transferência de calor de um corpo frio para um corpo mais quente precisa da entra de energia, não ocorrerá espontaneamente.
    
- Enunciado de Kelvin-Planck
    
    > É impossível para qualquer sistema operar em um ciclo termodinâmico e fornecer uma quantidade líquida de trabalho para sua vizinhança enquanto receber energia por transferência de calor de um único reservatório térmico.
    > 
    
- Enunciado de Entropia da Sgunda Lei
    
    > É impossível para qualquer sistema operar de uma maneira que a entropia seja destruída.
    > 
    - Ao contrário da massa e da energia, que se conservam, a entropia é produzida (gerada) no interior de um sistema sempre que estão presentes condições não ideais, chamadas de irreversibilidades, como o atrito.
    

# Processos Reversíveis e Irreversíveis

## Processos Irreversíveis

$\hookrightarrow$ Um processo é chamado de irreversível se o sistema e todas as partes que compões a vizinhança não puderem ser restabelecidos exatamente aos seus respectivos estados iniciais após o processo ter ocorrido.

$\hookrightarrow$ Um sistema que passou por um processo irreversível não está impedido de voltar para seu estado original, mas se isso ocorrer é impossível que a vizinhança também retorne.

<aside>
<img src="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/Screen_Shot_2021-09-23_at_10.18.50_PM.png" alt="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/Screen_Shot_2021-09-23_at_10.18.50_PM.png" width="40px" /> Temos através da segunda lei que processos espontâneos, como transferência de calor, expansão não resistida, etc. São processos irreversíveis.

</aside>

### Irreversibilidades Internas e Externas

$\hookrightarrow$ As irreversibilidades internas são aquelas que ocorrem dentro do sistema, já as irreversibilidades externas ocorrem na vizinhança, frequentemente a vizinhança imediata.

# Ciclos Termodinâmicos

## Eficiência

### Ciclos de Potência

$\hookrightarrow$ Somos capazes de calcular a eficiência de um ciclo termodinâmico que está em contato com dois reservatórios termicos pela seguinte equação:

$$
\eta = \frac{W_{ciclo}}{Q_H} = 1-\frac{Q_C}{Q_H}
$$

$\hookrightarrow$ Onde $Q_H$ é a quantidade de energia recebida pelo sistema do reservatório quente por transferência de calor, e $Q_C$ é a quantidade de energia descarregada do sistema para o reservatório frio por transferência de calor.

<aside>
<img src="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/kawasegaua.png" alt="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/kawasegaua.png" width="40px" /> Observamos que se $Q_c = 0$ teríamos que a eficiência seria $100\%$, mas isso é impossível e violaria o enunciado de Kelvin-Planck.

</aside>

## Desempenho

### Ciclo de Refrigeração

$$
\beta = \frac{Q_c}{W_{ciclo}} = \frac{Q_C}{Q_H - Q_C}
$$

$\hookrightarrow$ Que tem como função remover energia $Q_C$ do reservatório frio.

$\hookrightarrow$ Onde $Q_c$ é o calor que entra na máquina

### Bomba de Calor

$$
\gamma = \frac{Q_H}{W_{ciclo}} = \frac{Q_H}{Q_H - Q_C}
$$

$\hookrightarrow$ Que tem como função fornecer energia $Q_H$ para o reservatório quente.

$\hookrightarrow$ Onde $Q_H$ é o calor que sai da máquina.

<aside>
<img src="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/Evangelion.gif" alt="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/Evangelion.gif" width="40px" /> Estamos tratando de módulo!!!! Pois O trabalho do ciclo é a diferença entre o calor que entra ($Q_H$) e o calor que é "perdido"/sai ($Q_c$).

</aside>

## Eficiência Teórica Máxima

### Ciclos de Potência

$\hookrightarrow$ Para ciclos de potência, temos a seguinte fórmula para a eficiência de um ciclo de potência, onde as temperaturas são dadas em $K$ ou Rankine $R$:

 

$$
\eta_{max} = 1 - \frac{T_C}{T_H}
$$

$\hookrightarrow$ Chamada de eficiência de Carnot.

<aside>
<img src="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/mugi.gif" alt="Segunda%20Lei%20da%20Termodina%CC%82mica%2043de3305016f46e986c1efde744c7b73/mugi.gif" width="40px" /> Através da eficiência Máxima de Carnot, somos capazes de determinar se um ciclo opera reversivelmente (se $\eta = \eta_{max}$), irreversivelmente (se $\eta < \eta_{max}$) ou se é impossível ($\eta > \eta_{max}$)

</aside>

## Desempenho Teórico Máximo

### Ciclos de Refrigeração

$$
\beta_{max} = \frac{T_C}{T_H - T_C}
$$

$\hookrightarrow$ Onde, de forma análoga aos ciclos de potência, sabemos que um ciclo irreversível terá um desempenho menor do que o max teórico.

### Bomba da Calor

$$
\gamma_{max} = \frac{T_H}{T_H - T_C}
$$

$\hookrightarrow$ Onde, de forma análoga aos ciclos de potência, sabemos que um ciclo irreversível terá um desempenho menor do que o max teórico.