# Mecânica Analítica: Princípio de D’Alembert, Forças Generalizadas e Equações de Lagrange

Created: July 3, 2022 2:57 PM
Prova: P3

[Anotações de Aula](Meca%CC%82nica%20Anali%CC%81tica%20Princi%CC%81pio%20de%20D%E2%80%99Alembert,%20For%202b488e2857e64bfa92d13a6f38990ef9/Anotac%CC%A7o%CC%83es%20de%20Aula%202a9428d0347e4bf89c81efb25f04c5db.md)

- SUMMARY
    
    

# Princípio de D'Alembert

$\hookrightarrow$ A partir da segunda Lei de Newton, dada por:

$$
F = m\cdot a
$$

$\hookrightarrow$ D'Alembert chamou o termo $m\cdot a$ de "Força de Inércia”, uma força fictícia.

$\hookrightarrow$ Juntando isso com o conceito de quantidade de movimento linear $G$ e trabalho virtual (utilizado para problemas de estática) temos:

$$
\delta W = \sum (F_i - \dot G_i)\delta r_i
$$

$\hookrightarrow$ Chamado de princípio de D'Alembert, usado para problemas de dinâmica pois:

- Não exige a inclusão das forças de vínculo
- Exige somente o número de coordenadas mínio que descreve o movimento $\therefore$ nº de variáveis = nº de graus de liberdade

# Forças Generalizadas

$\hookrightarrow$ Podemos representar o princípio de D'Alembert como sendo:

$$
\delta W = \sum Q_i \delta q_i
$$

$\hookrightarrow$ Onde o termo $Q_i$ é chamado de força generalizada, que representa a soma das componentes na coordenada generalizada $q_i$ de todas as forças presentes no sistema, e é dada por:

$$
Q_i = \sum F_j \frac{\partial x_j}{\partial q_i}
$$

$\hookrightarrow$ Análogo a como foi feito para trabalho virtual para problemas de estática na aula passada.

# Equações de Lagrange

$\hookrightarrow$ A partir do princípio de d'Alembert, Lagrange escreveu as equações de Legrange, que utilizam somente quantidades escalares:

$$
\frac{d}{dt}\left [ \frac{\partial L}{\partial \dot q_i}\right ]- \frac{\partial L}{\partial q_i} = Q'_i
$$

$\hookrightarrow$ Onde:

- $L = T - V$ → Chamado de função Lagrangiana
- $Q'_i$ → São as forças generalizadas que não são derivadas de uma função potencial

# Função de Dissipação de Rayleigh

$\hookrightarrow$ Uma extensão de Lagrange para incluir forças dissipativas viscosas (muito utilizado em problemas de vibrações e controle):

$$
\frac{d}{dt}\left [ \frac{\partial L}{\partial \dot q_i}\right ]- \frac{\partial L}{\partial q_i} + \frac{\partial R}{\partial \dot q_i} = Q^{NC}
$$

$\hookrightarrow$ Onde:

- $R = \sum \frac{1}{2}(c_j\dot x_j^2)$