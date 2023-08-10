# Sistemas de Potência a Vapor

Cap.: Cap. 8
Created: October 8, 2021 9:09 PM

[Anotações de Aula](Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/Anotac%CC%A7o%CC%83es%20de%20Aula%205c2ab3a27b864b8eb1f41fd5ce4ad7e5.md)

- SUMÁRIO
    
    

# Ciclo de Rankine

## Modelagem do Ciclo de Rankine

$\hookrightarrow$ O ciclo de Rankine é um ciclo de vapor de água, composto pelas seguintes máquinas:

1. Turbina
2. Condensador
3. Bomba
4. Caldeira

$\hookrightarrow$ Durante a modelagem de um ciclo de Rankine, podemos considerar as variações nas energias cinéticas e potenciais como sendo desprezíveis.

### Processos

![Screen Shot 2021-11-03 at 10.15.57 AM.png](Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/Screen_Shot_2021-11-03_at_10.15.57_AM.png)

- Turbina
    - A partir da caldeira no estágio $1$, o vapor tem sua pressão e temperatura elevados. Depois disso, entram na turbina e se expande produzindo trabalho.
    - Como podemos desconsiderar as variações nas velocidades e energias potenciais, assim como a perda de calor da turbina para o lado de fora temos o balanço de energia como:
    
    $$
    \frac{\dot{W_t}}{\dot m} = h_1 - h_2
    $$
    
- Condensador
    - No condensador ocorre a troca de calor para com a água de resfriamento em um sistema separado.
    - Com isso temos que não ha trabalho mas somente troca de calor, resultando no seguinte balanço de energia:
    
    $$
    \frac{\dot Q_c}{\dot m} = h_2 - h_3
    $$
    
- bomba
    - Desconsiderando novamente a perda de energia para a vizinhança temos:
    
    $$
    \frac{\dot{W_b}}{\dot m} = h_4 - h_3
    $$
    
- Caldeira
    - Água é aquecido até a saturação e evaporação.
    - Com isso não há trabalho mas somente transferência de calor:
    
    $$
    \frac{\dot Q_{entrada}}{\dot m} = h_1 - h_4
    $$
    

### Ciclo Ideal

- Processo $1-2:$ Expansão Isentrópica até a pressão do condensador.
- Processo $2-3:$ Pressão constante até líquido saturado.

![Screen Shot 2021-11-03 at 10.30.29 AM.png](Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/Screen_Shot_2021-11-03_at_10.30.29_AM.png)

- Processo $3-4$$:$ Compressão isentrópica até o estágio  4 na região de líquido comprimido.
- Processo $4-1:$ Transferência de calor para o fluido de trabalho a Pressão Constante.

<aside>
<img src="Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/sagiriBleh.png" alt="Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/sagiriBleh.png" width="40px" /> OBS: O estado 1 pode ser ou vap. saturado ou vapor superaquecido !!!!

</aside>

### Eficiência

$\hookrightarrow$ Sabemos que a eficiência é "o que nós conseguimos sobre o que demos".

$\hookrightarrow$ Levando isso em consideração, para analisarmos a eficiência de um ciclo de rankine temos:

$$
\eta = \frac{\dot W_{net}}{\dot Q_{entrada}} = 1-\frac{h_2 - h_3}{h_1 - h_4}
$$

<aside>
<img src="Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/yuru_camp.png" alt="Sistemas%20de%20Pote%CC%82ncia%20a%20Vapor%20ca4f114de3f341d4a1c5113991410ea7/yuru_camp.png" width="40px" /> Para o estado de Liquido Comprimido, podemos achar a entalpia podemos fazer $h_{liq. \ comp} = h_l - cp(T_{sat} - T)$

</aside>