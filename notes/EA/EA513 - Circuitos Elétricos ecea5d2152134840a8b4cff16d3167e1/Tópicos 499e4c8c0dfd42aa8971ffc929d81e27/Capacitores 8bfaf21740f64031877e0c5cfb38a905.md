# Capacitores

Aula: Aula 7
Created: May 18, 2021 10:26 AM
Prova: P2

# O que é um capacitor?

Um capacitor é um componente construído com duas superfícies condutores separadas por uma camada de material isolante (dielétrico) que possui uma alta resistência elétrica, que tem capacidade de polarização por campo elétrico.

No modelo do capacitor ideal, consideramos que a resistência entre as placas é infinita e as cargas armazenadas nas placas condutoras nunca se recombinam.

# Capacitância

Característica do capacitor referente a quanta carga um ele é capaz de armazenar. 

Temos ainda que a carga armazenada é diretamente proporcional à tensão aplicada aos terminais:

$$
Q = C \cdot V
$$

## Características da capacitância

- Certas características físicas do capacitor influência na sua capacidade de armazenamento de cargas (i.e capacitância), tais como:
    1. Área das placas: $\uparrow A \uparrow C$
    2. Distância das placas: $\downarrow d \uparrow C$
    3. Tipo de dielétrico.
    

# Associação de Capacitores

## Paralelo

$$
C_T = C_1 + C_2 + ...+C_n
$$

## Série

$$
\frac{1}{C_T} = \frac{1}{C_1} + \frac{1}{C_2} + ...+\frac{1}{C_n}
$$

# Relação Tensão x Corrente capacitor

No momento em que o capacitor é ligado, ele age de forma análoga a um curto (com um pico de corrente) para carrega-lo, e vai caindo exponencialmente, até estar completamente carregado e não haver corrente.

$$
i = C\cdot \frac{dv}{dt}
$$

$$
v(t) = \frac{1}{C}\int idt + v_0
$$