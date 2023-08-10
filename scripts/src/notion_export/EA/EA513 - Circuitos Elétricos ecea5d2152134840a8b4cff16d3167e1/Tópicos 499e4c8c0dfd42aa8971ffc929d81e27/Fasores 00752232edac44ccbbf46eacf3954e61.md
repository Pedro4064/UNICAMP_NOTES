# Fasores

Aula: Aula 13
Created: June 9, 2021 9:35 PM
Prova: P3

# O que são Fasores?

- Em Engenharia, um FASOR (Phasor) é um número complexo que representa uma função senoidal com amplitude, frequência angular e fase inicial, invariantes no tempo.

# Definição de Fasor

- É uma constante complexa oriunda da identidade de Euler que abstrai a dependência do tempo e a frequência dos sinal.

## Identidade de Euler

$$
e^{\pm j \theta} = \cos \theta  \pm j \sin \theta
$$

$\hookrightarrow$ $\cos \theta = \R \{e^{j \theta}\}$

$\hookrightarrow \sin \theta = Im\{e^{j \theta}\}$

## Representação Por Fasores

- Considerando uma fonte de tensão:

$$
v(t) = V \cos (\omega t + \phi)
$$

- Somos capazes de reescreve-la utilizando a identidade de Euler, que ficaria:

$$
\begin{aligned}
v(t) &= V \cdot \R \{e^{j(\omega t + \phi)}\}\\
&= V \cdot \R \{e^{j\omega t} e^{j\phi})\}

\end{aligned}
$$

- Agora, iremos representar o seu fasor $\hat{V}$:

$$
\boxed{\hat{V} = V e^{j \phi}}
$$