# Introduction to Heat Transfer

Created: August 18, 2022 10:45 AM

[Anotações de Aula](Introduction%20to%20Heat%20Transfer%2074d72b1cf92a416386960d21c89d4bb9/Anotac%CC%A7o%CC%83es%20de%20Aula%20fe274564a39a4efd816cdfc1da8a265d.md)

- SUMMARY
    
    

# Introduction

> Heat Transfer is thermal energy in transit due to spatial temperature difference
> 

$\hookrightarrow$ As the above quote describes, there is heat transfer whenever there is a temperature difference not only in a single medium, but also between media.

$\hookrightarrow$ From that we can have multiple ways/mechanisms for that thermal energy to transit, resulting in 3 main modes of heat transfer:

1. Conduction → Trough solid or stationary fluid.
2. Convection → From a surface to a moving fluid.
3. Radiation    → "Net radiation heat exchange between two surfaces” (i.e in electromagnetic waves).

$\hookrightarrow$ Because we have many different mode of heat transfer, we will first introduce each and their corresponding "rate equations”, so later on we can use them to model our systems.

# Modes of Heat Transfer

## Conduction

$\hookrightarrow$ The key concept to grasp conduction is molecular activity.

$\hookrightarrow$ Conduction is basically the transfer of energy from the impact of two molecules, moving the energy from the more energetic to the less energetic molecule.

$\hookrightarrow$ It is also important to remember that the energy of a particle is directly associated with higher temperatures, $\therefore$ heat transfer through conduction happens from the body of highest temperature to the body of less temperature. 

$\hookrightarrow$ We are able to quantify the amount of heat transfer in terms of rate equations. For one dimensional conduction we use Fourier's Law, that describes the heat flux (i.e the heat transfer rate in the $x$ direction per unit area perpendicular to the direction of transfer):

$$
\boxed{q^{''}_ x = k\frac{\Delta T}{L}  }\\ \Downarrow \\  \begin{cases}k & \rightarrow T. \ Conductivity \\ \Delta T & \rightarrow Diff. \ in\ Temp. \\ 
L &\rightarrow Thickness\end{cases}
$$

$\hookrightarrow$ As state above, such equation provides a heat flux, that is the rate of heat transfer per unit area, so if we want the heat rate we need to multiply by the area in contact:

$$
q_x = q_n^x \cdot A
$$

## Convection

$\hookrightarrow$ We saw that there was one mechanism responsible for conduction heat transfer. 

$\hookrightarrow$ For Convection, on the other hand, we have 2 distinct mechanisms:

1. Random molecular motion, called diffusion.
2. Bulk, macroscopic motion of the fluid.

$\hookrightarrow$ Therefore convection is the superposition of both mechanism of heat transfer.

$\hookrightarrow$ We will be studying especially the convection heat transfer that happens between a moving fluid and a bounding surface that have different temperatures.

$\hookrightarrow$ In such cases, as a consequence of the fluid-surface interaction there is the development of a region in the fluid through which the velocity varies from zero at the surface to a finite value $u_\infty$, associated with the flow, that is called the hydrodynamic boundary layer.

$\hookrightarrow$ Moreover, if the surface and flow temperatures differ, there will be a region which the temperature varies from $T_s$ at $y=0$ to $T_\infty$, in the outer flow. This region is called thermal boundary layer, and if $T_s > T_\infty$, convection heat transfer will occur from the surface to the outer flow.

$\hookrightarrow$ Further more, we can classify different types of convection heat transfer based on the nature of the flow:

- **Forced Convection** - When the flow is caused by an external force such as a pump, a fam, etc.
- **Natural (Free) Convection** - When the flow is due to natural phenomena.
- **Mixed (Combined) Convection** - When both of the above occur.

$\hookrightarrow$ Despite the type of flow, the rate equation for heat flux due to convection is called Newton's law of cooling:

$$
q'' = h(T_s - T_\infty)
$$

$\hookrightarrow$ Where:

- $T_s$  → Surface temperature
- $T_\infty$ → Fluid Temperature

## Radiation

$\hookrightarrow$ It is energy emitted by nonzero temperature matter, therefore it is not limited to solids, but also occur from liquids and gasses. Despite that, we will focus only on solids in this subject.

$\hookrightarrow$ The main difference between Radiation and the other modes of heat transfer is that it does not need a material medium, and occurs most effectively on vacuum.

$\hookrightarrow$ The rate at which energy is release/emitted from a surface is called the surface emissive power $(E)$,  and there is an upper limit to it, given by the *Stefan-Boltzmann law, that describes an ideal radiator (a.k.a Black Body)*:

$$
E_b = \sigma T^4_s
$$

$\hookrightarrow$ Where:

- $T_s$ → Absolute Surface Temperature $[K]$
- $\sigma$   → Constante $5.67 \times 10^{-8}W/m^2\cdot K^4$

$\hookrightarrow$ As said before, the above equation describes the ideal blackbody $\therefore$  it does not describe the real heat flux of a surface, that is given by:

$$
E = \varepsilon \sigma T^4_s
$$

$\hookrightarrow$ Where:

- $\varepsilon$ → radiative property of the surface, called emissivity, between $0$ and $1$.

$\hookrightarrow$ Part of that radiation, however, may be absorbed into materials, increasing its thermal energy, given by:

$$
G_{abs} = \alpha G
$$

$\hookrightarrow$ Where:

- $\alpha$ → Absorptivity $0<\alpha < 1$
- $G$ → Rate of the source's radiation that hits the surface.

$\hookrightarrow$ A case that occurs a lot is radiation exchange between a small surface at $T_s$ and a much larger surface that completely surrounds it, at $T_{sur}$, where $T_s \ne T_{sur}$. Is such occasion the net rate of radiation **heat transfer from the surface** is: 

$$
q_{rad}'' = \varepsilon \sigma(T^4_s - T^4_{sur})
$$

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> In many problems we can assume that $\alpha = \varepsilon$, i.e that the emissivity is equal to the rate of absorption.

</aside>

<aside>
<img src="Introduction%20to%20Heat%20Transfer%2074d72b1cf92a416386960d21c89d4bb9/Evangelion.gif" alt="Introduction%20to%20Heat%20Transfer%2074d72b1cf92a416386960d21c89d4bb9/Evangelion.gif" width="40px" /> IMPORTANT: When solving heat transfer problems by radiation it is NECESSARY to convert all temperatures to Kelvin

</aside>

$\hookrightarrow$ Furthermore, a surface might simultaneously transfer heat by convection and radiation to an adjoining gas. The resulting rate of heat transfer **FROM THE SURFACE** will be:

$$
q = q_{conv} + q_{rad} = hA(T_s - T_\infty)+ \varepsilon A\sigma (T^4_s - T^4_{sur})
$$

$\hookrightarrow$ In a nutshell we saw the rate equation for absorption through radiation by a surface $(G_{abs})$ and the rate equation for heat emission from the surface through radiation $(q_{rad})$. It is important to differentiate the two different radiations (the one being absorbed and the one being emitted) for latter, where we'll be drawing diagrams and using energy balance for our problem solving.

# Conservation of Energy Requirement

$\hookrightarrow$ Up until this point we've only seen the rate equations for the various modes of heat transfer in different occasions, now we will combine that with the knowledge on thermodynamics to solve engineering problems that relay on heat transfer. 

$\hookrightarrow$ As we have seen in thermodynamics, we can study both a Closed System (where energy can transit in the form of heat transfer and work done, but mass may not leave its boundaries) and Control Volumes (where energy can transit in the form of heat, work + kinetic energy, since mass can enter and leave).

$\hookrightarrow$ From this point on, we can stipulate the first law of Thermodynamics:

> The increase in the amount of energy stored in a control volume must equal the amount of energy that enters the control volume, minus the amount of energy that leaves the control volume.
> 

$\hookrightarrow$ The above definition involves all the possible forms of energy generation and transfer, but for this course we want to focus primarily on thermal and mechanical, so we can derive a more suitable equation:

$$
\boxed{\dot E_{in} + \dot E_g - \dot E_{out} = \dot E_{st}}
$$

$\hookrightarrow$ Where:

- $\dot E_g$    → Energy Generation (can be due to electrical resistance, chemical reaction, …)
- $\dot E_{out}$ → Energy transfer out of the control volume, and can be expressed as a combination of the different rate equations.
- $\dot E_{st}$   → Energy stored as thermal and mechanical energy

$\hookrightarrow$ More often than note we are really interested just in the surface of a body, and for such occasions we have the Surface Energy Balance equation, which is a simplification of the above eq:

$$
\dot E_{in} - \dot E_{out} = 0
$$

![Screen Shot 2022-08-19 at 3.51.12 PM.png](Introduction%20to%20Heat%20Transfer%2074d72b1cf92a416386960d21c89d4bb9/Screen_Shot_2022-08-19_at_3.51.12_PM.png)

<aside>
<img src="https://www.notion.so/icons/alert_purple.svg" alt="https://www.notion.so/icons/alert_purple.svg" width="40px" /> If we use the Steady State Hypothesis, we can say that $\dot E_{st} = 0$

</aside>

# Summary

$\hookrightarrow$ In this chapter we first saw the different modes of heat transfer and the mathematical model for each, called the rate equations. 

$\hookrightarrow$ From that we use the Steady-State analysis on Control Volumes to analyze all the different forms of heat transfer in and out of our target volume, so we can check the final temperature, or how long it took, etc.