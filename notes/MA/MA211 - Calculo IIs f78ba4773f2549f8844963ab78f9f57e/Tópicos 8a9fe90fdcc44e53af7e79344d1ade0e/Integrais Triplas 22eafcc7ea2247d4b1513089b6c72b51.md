# Integrais Triplas

# Integrais Triplas do Tipo $I$

- $Z$ Varia entre $f_1(x,y)$ e $f_2(x,y)$;
- Tem uma projeção $D$ no plano $xy$ e é limitado em cima e embaixo por duas superfícies.
- Esses sólidos podem ser escritos da seguinte forma:

$$
W = \{(x,y,z)|(x,y) \in D; f_1(x,y) \leq z \leq f_2(x,y)\}
$$

- As integrais do tipo $I$ são montadas da seguinte forma:

$$
\iiint_W f(x,y,z)dV = \iint \left[\int^{f_2(x,y)}_{f_1(x,y)} f(x,y,z)dz\right]dA
$$

 

- Onde $dA$ pode ser tanto uma integral dupla do tipo $1$ quanto do tipo $2$, logo pode ser substituído ou por $dxdy$ ou $dydx$.

![Integrais%20Triplas%2022eafcc7ea2247d4b1513089b6c72b51/Screen_Shot_2020-11-16_at_8.30.24_PM.png](Integrais%20Triplas%2022eafcc7ea2247d4b1513089b6c72b51/Screen_Shot_2020-11-16_at_8.30.24_PM.png)

# Integrais Triplas do Tipo $II$

- $y$  varia entre duas funções: $g_1(x,z)$ e $g_2(x,z)$;
- É limitada no plano $xz$ por uma área $D$

![Integrais%20Triplas%2022eafcc7ea2247d4b1513089b6c72b51/Screen_Shot_2020-11-16_at_8.30.55_PM.png](Integrais%20Triplas%2022eafcc7ea2247d4b1513089b6c72b51/Screen_Shot_2020-11-16_at_8.30.55_PM.png)

- Matematicamente esses sólidos podem ser escritos da seguinte forma:

$$
W = \{(x,y,x)|(x,z)\in D; g_1(x,y)\leq y \leq g_2(x,y)\}
$$

- As integrais podem ser escritas da seguinte forma:

$$
\iiint_W f(x,y,z)dV = \iint \left[\int^{g_2(x,z)}_{g_1(x,z)} f(x,y,z)dy\right]dA
$$

# Integrais Triplas do Tipo $III$

- $x$ varia entre duas funções $h_1(y,z)$ e $h_2(y,z)$;
- São limitas no plano $yz$ por uma área $D$;

![Integrais%20Triplas%2022eafcc7ea2247d4b1513089b6c72b51/Screen_Shot_2020-11-16_at_8.36.02_PM.png](Integrais%20Triplas%2022eafcc7ea2247d4b1513089b6c72b51/Screen_Shot_2020-11-16_at_8.36.02_PM.png)

- Esses sólidos podem ser escritos da seguinte forma:

$$
W = \{(x,y,x)|(y,z)\in D; h_1(y,z)\leq x \leq h_2(y,z)\}
$$

- E as integrais sobre essas regiões serão:

$$
\iiint_W f(x,y,z)dV = \iint \left[\int^{h_2(y,z)}_{h_1(y,z)} f(x,y,z)dx\right]dA
$$