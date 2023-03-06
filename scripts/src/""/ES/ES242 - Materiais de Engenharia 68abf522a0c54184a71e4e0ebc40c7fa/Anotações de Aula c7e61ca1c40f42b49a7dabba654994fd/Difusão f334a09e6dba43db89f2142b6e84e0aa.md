# Difusão

Aula: Aula 5
Created: April 14, 2021 7:01 PM

# Introdução

- Movimento de átomos $\rightarrow$  difusão no estado sólido;
- Defeitos pontuais dependentes da temperatura
    - Concentração aumenta exponencialmente
- Equações de difusão $\rightarrow$ cálculo da variação da composição química

# Processos Termicamente ativados

- Muitos processos tem dependência exponencial com a temperatura;
    - ex: Difusividade, fluência, condutividade elétrica em semicondutores, etc.
- Equação de Arrhenius

$$
taxa = Ce^{\frac{-Q}{RT}}
$$

Onde temos: 

$C:$ constante pré-exponencial

$Q:$ energia de ativação $\rightarrow$ barreira energética que necessita ser vencida com ativação térmica

$R:$ Constante universal dos gases

$T:$ Temperatura Absoluta

# Defeitos Pontuais

- Oriundos de vibrações térmicas
- Maior temperatura = Maior incidência de defeitos pontuais
- Concentração de defeitos pontuais aumenta exponencialmente com a temperatura:

# Difusão no estado sólido

- Movimento de átomos
- Mais concentrados para menos concentrados
- Ocorre entre materiais diferentes ($Cu$ e $Ni$) ou no mesmo material (autodifusão)
- Para a difusão no estado sólido é necessário que existam defeitos pontuais
- Fluxo de átomos é oposto ao da vacância
- Natureza aleatória dos movimentos atômicos $\rightarrow$ "random-walk"
- Migração resultante não é o somatório da distância de saltos.

- Átomos do sólido $A$ se fundem em direção ao sólido $B \rightarrow$ interdifusão;
    - Átomos de $B$ também se difundem em direção a $A$, por isso o nome inter-difusão
    

# Difusão no estado Sólido em Regime Estacionário

## Primeira Lei de Fick

$$
J_x = -D \frac{\partial C}{\partial x}
$$

- Calculo do fluxo.

- Difusão em estado estacionário ocorre quando a concentração inicial $(C_h)$ e $C_l$ são mantidos constantes;
- Após um centro tempo $(t_3)$ o perfil de:

$$
\frac{\partial C}{\partial x} = \frac{\Delta C}{\Delta X}= \frac{C_h - C_l}{0 - x_0} = -\frac{C_h - C_l}{x_0}
$$

# Difusão no estado Sólido  no Regime Transiente

## Segunda Lei de Fick

$$
\frac{\partial C_x}{\partial t} = \frac{\partial}{\partial}\left(D\frac{\partial C_X}{\partial X}\right)
$$

- Se $D$  for independente de $C$ temos:

$$
\frac{\partial C_x}{\partial t} = \frac{\partial}{\partial}\left(D\frac{\partial^2 C_X}{\partial X^2}\right)
$$

- Quando for uma peça semi-infinita:
    
    ![Difusa%CC%83o%20f334a09e6dba43db89f2142b6e84e0aa/Screen_Shot_2021-04-14_at_8.00.47_PM.png](Difusa%CC%83o%20f334a09e6dba43db89f2142b6e84e0aa/Screen_Shot_2021-04-14_at_8.00.47_PM.png)
    
    $C_x:$  Concentração desejada
    
    $C_s:$ Concentração na superfície
    
    $C_0:$  Concentração original
    
    $erf:$ Função Erro de Gauss
    

# Caminhos alternativos de difusão