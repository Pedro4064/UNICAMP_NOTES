# Método de Variação dos Parâmetros

Aula: Aula 8
Created: April 18, 2021 9:12 AM
Prova: P1

# Formato da Equação

$$
y'' + p(x)y' + q(x) = f(x) , \ \ f(x)\ne0
$$

- Temos $y_1,y_2$ como sendo as soluções da equação homogênea associada.

# A solução da EDO

- É a soma da solução da homogênea associada e da não homogênea $y_p(x)$ dada por:

$$
y_p(x) = u_1(x)y_1(x) + u_2(x)y_2(x)
$$

- Onde temos:

$$
\boxed{u_1(x) = - \int \frac{y_2(x)f(x)}{W(x)}dx} \\ 

\boxed{u_2(x) = \int \frac{y_1(x)f(x)}{W(x)}dx} \\ 
$$

- $W(x)$ é o wronskiano de $y_1 \ e \ y_2$

<aside>
<img src="Me%CC%81todo%20de%20Variac%CC%A7a%CC%83o%20dos%20Para%CC%82metros%20b2351ada997d40428911d9d8da258a54/Evangelion.gif" alt="Me%CC%81todo%20de%20Variac%CC%A7a%CC%83o%20dos%20Para%CC%82metros%20b2351ada997d40428911d9d8da258a54/Evangelion.gif" width="40px" /> OBS: Nosso $f(x)$ é para a equação no formato padrão, isso é, nada multiplicando $y''$

</aside>