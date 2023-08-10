# Análise Estrutural - Treliças [Métodos de nós]

Capítulo: Cap. 6
Created: December 1, 2021 7:39 PM
Prova: P2

- SUMÁRIO

# Introdução

$\hookrightarrow$ Treliça é o nome dado a uma estrutura de elementos relativamente delgados ligados entre si pelas extremidades, normalmente por uma placa de reforço ou um pino.

![Screen Shot 2021-12-01 at 7.43.33 PM.png](Ana%CC%81lise%20Estrutural%20-%20Trelic%CC%A7as%20%5BMe%CC%81todos%20de%20no%CC%81s%5D%201641ff02eb3d4a6c9041e2762b8ffe42/Screen_Shot_2021-12-01_at_7.43.33_PM.png)

# Principais Hipóteses

$\hookrightarrow$ Para projetar elementos e conexões de uma treliça, é necessário determinar as forças desenvolvidas em cada elemento quando submetido a um determinado carregamento. Tendo isso em mente, as duas seguintes hipóteses são consideradas:

1. Todas as cargas são aplicadas aos nós: Na maioria das situações essa suposição é verdadeira. Além disso, na maioria dos casos, o peso dos elementos é desprezado, mas quando for necessário levar em consideração podemos dizer que sua força é dividida igualmente para cada nó que está em contato.
2. Os elementos são ligados entre si por pinos lisos: Principalmente nos casos quando conexões são feitas por parafusos ou soldas, essa hipóteses é satisfatória.

$\hookrightarrow$ Devido a essas hipóteses, cada elemento de uma treliça atua como um elemento de duas forças e, consequentemente, as forças devem ser direcionadas ao longo do seu próprio eixo.

$\hookrightarrow$ Levando isso em consideração, é de suma importância a identificação do tipo de cada força, sendo eles:

- Força de Tração $(T)$: Que tende a alongar o elemento.
- Força de Compressão $(C)$: Que tende a comprimir o elemento.

# Treliça Simples

$\hookrightarrow$ Uma treliça simples deve ser suficientemente rígida $\therefore$ a estrutura básica de uma treliça é o triangulo, que é a forma geométrica mais rígida e simples.

$\hookrightarrow$ Levando isso em consideração, uma treliça simples é composta de uma série de elementos triangulares, como mostrado na figura ao lado:

![Screen Shot 2021-12-01 at 8.00.55 PM.png](Ana%CC%81lise%20Estrutural%20-%20Trelic%CC%A7as%20%5BMe%CC%81todos%20de%20no%CC%81s%5D%201641ff02eb3d4a6c9041e2762b8ffe42/Screen_Shot_2021-12-01_at_8.00.55_PM.png)

# Método de Nós

$\hookrightarrow$ Para analisarmos uma treliça precisamos identificar todas as forças que atuam em seus nós, mas se considerarmos o corpo como sendo a treliça como um todo essas forças serão consideradas forças internas e não serão estudadas no DCL. 

$\hookrightarrow$ Por esse motivo nós estudamos os equilíbrio (e a análise de forças) de cada nós, dando a base para o método de nós.

$\hookrightarrow$ Além disso, devido ao fato dos elementos de uma treliça serem todos retilíneos, coplanares e com duas forças atuando sobre eles temos que o sistema de forças para cada nós é coplanar e concorrente. e, por conseguinte, o equilíbrio de momentos é automaticamente satisfeito sendo necessariamente somente garantir $\sum F_x = \sum F_y = 0$ para termos equilíbrio.

## Análise e Desenvolvimento

- Devemos sempre começar a análise por um nó no qual temos pelo menos uma força conhecida e não mais de duas forças desconhecidas. Aplicando então o diagrama de corpo livre para aquele pontoe fazendo a análise para:
    
    $$
    \sum F_x = \sum F_y = 0
    $$
    
- Para tal, precisamos primeiramente determinar o sentido das forças atuando no nó, e para isso temos duas possibilidades:
    1. Considerar todas as forças incógnitas como forças de tração (i.e puxando o pino): isso é uma suposição válida e que, após a análise numérica, saberemos se está correta (isso é as forças com valores positivos) ou se está incorreta (que resultará nos sinais negativos para as forças que tiverem sentido contrário).
    2. Determinar por inspeção o esquemático, isso é, imaginar a situação e identificar se a força está comprimindo ou tensionando o elemento (mas que no final das contas se a suposição feita for errada o sinal indicará, assim como na forma 1).
    

- De modo geral temos:
    
    ![Screen Shot 2021-12-01 at 8.20.01 PM.png](Ana%CC%81lise%20Estrutural%20-%20Trelic%CC%A7as%20%5BMe%CC%81todos%20de%20no%CC%81s%5D%201641ff02eb3d4a6c9041e2762b8ffe42/Screen_Shot_2021-12-01_at_8.20.01_PM.png)
    

<aside>
<img src="Ana%CC%81lise%20Estrutural%20-%20Trelic%CC%A7as%20%5BMe%CC%81todos%20de%20no%CC%81s%5D%201641ff02eb3d4a6c9041e2762b8ffe42/Evangelion.gif" alt="Ana%CC%81lise%20Estrutural%20-%20Trelic%CC%A7as%20%5BMe%CC%81todos%20de%20no%CC%81s%5D%201641ff02eb3d4a6c9041e2762b8ffe42/Evangelion.gif" width="40px" /> Algumas vezes todos os nós terão mais de duas forças desconhecidas. Quando isso acontecer precisaremos fazer análise da treliça como um todo (para balanço de forças e momentos).

</aside>