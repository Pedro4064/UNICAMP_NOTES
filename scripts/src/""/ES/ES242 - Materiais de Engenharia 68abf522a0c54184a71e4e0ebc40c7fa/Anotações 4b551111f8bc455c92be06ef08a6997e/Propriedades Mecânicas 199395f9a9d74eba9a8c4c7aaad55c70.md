# Propriedades Mecânicas

Aula: Aula 8
Capitulo: Cap. 6
Created: June 10, 2021 8:07 PM

# Introdução

- Propriedades mecânicas são importantes para responder perguntas do tipo:
    
    $\hookrightarrow$ Qual material resiste a este esforço?
    
    $\hookrightarrow$ Quanto flexível deve ser o componente (qual rigidez é desejada)?
    
    $\hookrightarrow$ Esse metal pode ser conformado por forjamento?
    

# Tensão $V.S$ Deformação

## Ensaio de Tração

- Ensaio de tração: a carga necessária para alongar a barra é monitorada enquanto a tração é aplicada a taxa constante.
- Ensaio normatizado, ex: $ASTM \ E8/E8m-16a$
- A partir desse ensaio, os dados são normalizados considerando a geometria inicial dos corpos de prova:

### Tensão de Engenharia

$$
\sigma = \frac{P}{A_0}
$$

$\hookrightarrow$ $P:$ Carga aplicada

$\hookrightarrow A_0:$ Área inicial

### Deformação de Engenharia

$$
\epsilon = \frac{I - I_0}{I_0}
$$

$\hookrightarrow I:$ Comprimento

$\hookrightarrow I_0:$  Comprimento Inicial

## Gráfico

![Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_8.56.57_PM.png](Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_8.56.57_PM.png)

- A curva possui duas regiões características, sendo elas:
1. Região Elástica: Deformação recuperável com descarregamento.
2. Região Plástico: Deformação permanente (não linear).

- Há ainda um ponto importante, quando a curva deixa de ser linear e a deformação plástica permanente ocorre. Esse ponto é chamado de Limite de escoamento, que é definido como uma intersecção da curva $\sigma - \epsilon$ e  uma reta paralela à região elástica, porém com um deslocamento de $0.2\%$

![Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_9.02.48_PM.png](Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_9.02.48_PM.png)

# Propriedades Mecânicas do Ensaio de Tração

- Certas propriedades Mecânicas podem ser observadas/ressaltadas do ensaio anteriormente descrito, sendo elas:

1. Módulo de Elasticidade (Módulo de Young [$E$]) → obtido pela inclinação da curva de deformação Elástica.
2. Limite de Escoamento ($\sigma_{YS}$)
3. Limite de resistência de tração ($\sigma_{TS} \ ou \ \sigma_{UTS}$) → representa o início da queda da Tensão
4. Ductilidade → Alongamento ou redução da área
5. Tenacidade → área abaixo da curva, que representa a energia absorvida durante a deformação

![Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_9.09.55_PM.png](Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_9.09.55_PM.png)

- Outra propriedade importante de ser destacada é o chamado Encruamento, que é o aumenta da resistência por conta da deformação inicial.

## Tensão e Deformação Real

- Após $\sigma_{UTS}$, aparentemente o materia amolece, porém isso é artificial e ocorre pois são consideradas as dimensões originais do corpo de prova na tensão de engenharia.
- A tensão real cresce até a  fratura:

$$
\sigma_{real} = \frac{P}{A_{atual}}
$$

![Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_9.23.14_PM.png](Propriedades%20Meca%CC%82nicas%20199395f9a9d74eba9a8c4c7aaad55c70/Screen_Shot_2021-06-10_at_9.23.14_PM.png)

## Diferentes Comportamentos no Ensaio de Tração

- Resistência → Capacidade de suportar tensões elevados com pouco deformação
- Ductilidade → Indica a habilidade do material de se deformar
- Tenacidade → Combinação de resistência e ductilidade

# Deformação Elástica

- A deformação elástica está relacionada ao alongamento das ligações atômicas, os átomos são movidos de sua posição de equilíbrio.
- A deformação do tipo Elástica é totalmente recuperada no descarregamento.
- É regida pela Lei de Hook (até certo ponto eu acho).

# Deformação Plástica

- As deformações do tipo plástica requerem o deslizamento de planos atômicos, que são facilitados pela existência de [defeitos lineares](Imperfeic%CC%A7o%CC%83es%20em%20so%CC%81lidos%2003fa09e40aaa475ab0869b05f34af087.md) (chamadas de discordâncias).

# Dureza

- Resistência a indentação ou risco por outro objeto mais duro (diamante, por ex) → indicação da resistência mecânica.
- Medição qualitativa da resistência mecânica
- Amplamente utilizado na indústria
    - Controle de matéria prima
    - Durante estágios de fabricação
- Existem vários métodos de medição e também escalas