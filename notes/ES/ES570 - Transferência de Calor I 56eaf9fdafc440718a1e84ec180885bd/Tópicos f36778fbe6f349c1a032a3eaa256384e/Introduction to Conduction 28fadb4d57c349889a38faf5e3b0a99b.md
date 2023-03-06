# Introduction to Conduction

Created: August 30, 2022 2:50 PM

[Anotações de Aula](Introduction%20to%20Conduction%2028fadb4d57c349889a38faf5e3b0a99b/Anotac%CC%A7o%CC%83es%20de%20Aula%2075d7adf5b51643528a9f396ce0518d4a.md)

- SUMMARY
    
    

# Introduction

$\hookrightarrow$ In the previous section we got an overview of conduction, including the main mechanism through which it happens and the rate equation for one dimensional conduction trough a linear wall, given by Fourier's Law.

$\hookrightarrow$ In this section we are going deeper, trying to:

1. Develop a deeper understanding of Fourier's law
2. Derive Fourier's law for general case regarding temperature gradient direction

# Fourier's Rate Equation

## Introduction to the Rate Equation

$\hookrightarrow$ It is important to note that the Fourier's Rate equation is phenomenological (i.e it was derived after experimentation and observation, and not derived from first principles).

$\hookrightarrow$ With that being said, in the rod experiment (where there is a rod isolated from the surroundings with a differences in temperature in both ends) Fourier noticed that the heat transfer is proportional to the cross-sectional area of the rod, its length, its size and the temperature difference.

$$
q_x \propto A\frac{\Delta T}{\Delta x}
$$

$\hookrightarrow$ Furthermore, it is proportional to the intrinsic characteristics of the material, resulting in what we know as the **Onde Dimensional Rate Equation for Conduction**:

$$
\begin{align}q_x = -kA\frac{dT}{dx}
\end{align}
$$

$\hookrightarrow$ And the heat flux (which is the heat transfer by unit area):

$$
\begin{align}
q''_x = \frac{q_x}{A} = -k\frac{dT}{dx}
\end{align}
$$

$\hookrightarrow$ Where the minus sign is due to the fact that heat transfer always happens from the body with greater temperature to the one with least temperature, and $\Delta T = T_{Colder} - T_{Hotter}$. So it is minus so the heat transfer from the Hottest body to the Colder body is positive.

$\hookrightarrow$ Moreover, if we analise the equation for Rate equation described above we can see that it implies that the heat transfer through conduction is dependent on orientation, more specifically it describes the heat transfer in the direction normal to the temperature difference. Which means that for a more general rate equation we need extra formulation.

## Generalization of the Rate Equation: Multi-Directional Conduction

$\hookrightarrow$ For cases where the temperature difference it is not one-dimensional, we have an extended formulation, using the Gradient-Vector of the Temperature Difference in all directions:

$$
\begin{align}
q'' = -k \nabla T = -k(i\frac{\partial T}{\partial x} + j\frac{\partial T}{\partial y} + k\frac{\partial T}{\partial z}) \ \ \ \ \ \ \ 
\end{align}
$$

$\hookrightarrow$ Which gives us a heat flux vector.

$\hookrightarrow$ If we look closely, the one-dimension version is just a particular case where $T(x, y, z) = T(x)$, i.e there is a temperature difference only in one direction.