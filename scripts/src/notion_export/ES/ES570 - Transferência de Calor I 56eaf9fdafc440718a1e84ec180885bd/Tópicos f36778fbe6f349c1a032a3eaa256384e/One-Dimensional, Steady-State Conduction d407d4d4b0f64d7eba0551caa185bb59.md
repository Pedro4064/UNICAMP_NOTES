# One-Dimensional, Steady-State Conduction

Created: August 30, 2022 4:22 PM

[Anotações de Aula](One-Dimensional,%20Steady-State%20Conduction%20d407d4d4b0f64d7eba0551caa185bb59/Anotac%CC%A7o%CC%83es%20de%20Aula%206eeeba9e4f784dd284148f35671c4194.md)

- SUMMARY
    
    

# Introduction

$\hookrightarrow$ In this section we'll be analyzing systems with the following characteristics:

1. **One-Dimensional** → Refers to the fact that only one coordinate is needed to describe the spatial variation of the difference in temperature.
2. **Steady-State** →  Refers to the fact that the temperature at each point is independent of time.

$\hookrightarrow$ Moreover, we will introduce the concept of thermal resistance, which is an interpretation of thermal energy transfer based on electrical circuits and resistances. 

# Temperature Distribution in Steady State

$\hookrightarrow$ In some problems it is of interest to us to analyze the temperature distribution within a body (in this case a plane wall) through the process of conduction, in steady state.

$\hookrightarrow$ The key information for this problem is that we are in **steady state**, that is, there is no change in temperature over time, therefore the heat flux is constant over all sections of the body. This must be true, otherwise some places would get hotter and others would get colder **over time**, which would violate the fact that it is in steady state (i.e theres is no temperature variance over time).

$\hookrightarrow$ This fact can be more closely understood by dividing the body being studied in an infinite number of smaller partes (as show in the image), and applying the law of conservation of Energy on them, given by:

![Screen Shot 2022-09-06 at 3.20.14 PM.png](One-Dimensional,%20Steady-State%20Conduction%20d407d4d4b0f64d7eba0551caa185bb59/Screen_Shot_2022-09-06_at_3.20.14_PM.png)

$$
\begin{align}
\dot E_{in} - \dot E_{out} + \dot E_{generated} - \dot E_{stored} = 0
\end{align}
$$

$\hookrightarrow$ Where, since we don't have generation of heat inside the wall and there is no change in temperature over time (steady state), we have, respectively:

$$
\begin{align}
\dot E_{generated} = \dot E_{stored} = 0 
\end{align}
$$

$\hookrightarrow$ Resulting in:

$$
\begin{align}
\dot E_{in} = \dot E_{out}
\end{align}
$$

## Plane Wall

$\hookrightarrow$ The above expression is for the first infinitely small part of the wall, but if we repeat for all the pieces of the wall we will find that, throughout the wall, the heat transfer is the same, therefore:

$$
\begin{align}
\frac{d}{dx}\left( -kA \frac{dT}{dx}\right) = 0
\end{align}
$$

$\hookrightarrow$ From that point on we can solve the above differential equation to find the temperature distribution on the wall in function of $x$:

$$
\begin{aligned}

\frac{d}{dx}\left( -kA \frac{dT}{dx}\right) &= 0  \\

-kA\left[\int \frac{d}{dx}\left( \frac{dT}{dx}\right) dx \right] &= \int0 dx \\

 -kA \left [\frac{dT}{dx} + c_1 \right ] &= 0 \\ 

-kA \left [\int  \frac{dT}{dx} dx+ \int c_1 dx \right ] &= \int0dx \\ 

-ka \left [ T(x) + c_1 x + c_2\right ] &= 0 \\ 

T(x) &= C_1x  + C_2 

\end{aligned}
$$

$\hookrightarrow$ Where $C_1 = -c_1$ and $C_2 = -c_2$.

$\hookrightarrow$ From this point on, we can substitute the boundary conditions to find the values for $C_1$ and $C_2$:

$$
\begin{align}
T(0) = T_{s_1} &\iff C_2 = T_{s_1} \\ 
T(L) \Rightarrow T_{s_2} = C_1L + T_{s_1} &\iff C_1 = \frac{T_{s_2} - T_{s_1}}{L}
\end{align}
$$

$\hookrightarrow$ Where:

- $T_{s_2}$ → Is the temperature at the other side of the wall, at $x = L$
- $T_{s_1}$ → Is the temperature of the "reference” side of the wall, at $x= 0$

$\hookrightarrow$ Resulting in:

$$
\begin{align}
T(x) = T_0- \frac{T_L - T_0}{L}x
\end{align}
$$

# Thermal Resistance

## Introduction

$\hookrightarrow$ If we look closely at Fourier's Equation for one-dimensional, steady state conduction we can draw a parallel between heat transfer and electrical circuits. This parallel will facilitate both the understanding and the analysis of heat transfer.

$\hookrightarrow$ Basically we have the concept of resistance for the different modes of heat transfer:

$$
\begin{align}
R_{cond} &= \frac{L}{kA} \\ 
R_{conv} &= \frac{1}{hA} \\ 
R_{radi} &= \frac{1}{h_rA}
\end{align}
$$

$\hookrightarrow$ Where the heat trasnfer is given by:

$$
\begin{align}
q = \frac{\Delta T}{R}
\end{align}
$$

$\hookrightarrow$ Or even, if we don't consider the area in the formulation of our resistances we can represent the heat flux on a simple plane wall through conduction as:

$$
\begin{align}
q'' = \frac{\Delta T}{R}, \ \ R = \frac{L}{K}
\end{align}
$$

$\hookrightarrow$ And in the same way that we can have different topologies and arrangements with resistors in series and parallel in circuits, we can also have it in heat transfer analysis:

![Screen Shot 2022-09-06 at 5.10.23 PM.png](One-Dimensional,%20Steady-State%20Conduction%20d407d4d4b0f64d7eba0551caa185bb59/Screen_Shot_2022-09-06_at_5.10.23_PM.png)

![Screen Shot 2022-09-06 at 5.10.56 PM.png](One-Dimensional,%20Steady-State%20Conduction%20d407d4d4b0f64d7eba0551caa185bb59/Screen_Shot_2022-09-06_at_5.10.56_PM.png)

$\hookrightarrow$ Furthermore, we can characterize the whole process of heat transfer through the global heat transfer coefficient, given by:

$$
\begin{align}
U = \frac{1}{R_{total} A}
\end{align}
$$

## Problem Solving

$\hookrightarrow$ The main advantage to this approach is that, once we  build our thermal-resistant model (model made up of the resistors representing the thermal resistance of each part), we can use the properties of conservation of energy on the circuit (pretty similar to kurchoff's law of current on a node) and the fact that the heat transfer is given by $q = \frac{\Delta T}{R_{total}}$ to analyze as if it was an electrical circuit.

![Screen Shot 2022-09-06 at 5.41.29 PM.png](One-Dimensional,%20Steady-State%20Conduction%20d407d4d4b0f64d7eba0551caa185bb59/Screen_Shot_2022-09-06_at_5.41.29_PM.png)

![Screen Shot 2022-09-06 at 5.42.50 PM.png](One-Dimensional,%20Steady-State%20Conduction%20d407d4d4b0f64d7eba0551caa185bb59/Screen_Shot_2022-09-06_at_5.42.50_PM.png)