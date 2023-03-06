# Equações Lineares de 2a Ordem e de Ordem Superiores e Homogêneas

Aula: Aula 5
Created: April 7, 2021 9:21 PM
Prova: P1

# Equações de Ordem 2

## Forma

- As equações de 2a ordem  homogêneas tem a seguinte construção:

$$
A(x)y''+ B(x)y' + C(x)y = \underbrace{F(x)}_{0}
$$

Com $F(x) = 0$  e $A(x) \ne 0$ para que possa ser, respectivamente, homogênea e de segundo grau.

<aside>
💡 Em um problema de valor inicial, uma EDO que possui $B(x), C(x), F(x)$ contínuos em um intervalo $I$ que contém o valor dado de $x_0$ admite uma única solução.

</aside>

## Resolução

### Equações Características

- Conseguimos resolver EDOs homogêneas de grau maior ou igual à dois através do que de equações auxiliares/características.
- Utilizaremos como exemplo EDO genérica $A(x)y''+ B(x)y' + C(x)y = F(x)$, que possui a seguinte equação auxiliar:

$$
ar^2 + br + c = 0
$$

- Como temos nossa equação característica, precisamos achar suas raizes (como é um polinômio de grau 2 teremos duas raizes). Para acha-las podemos utilizar Bhaskara:

$$
r = \frac{-b \pm\sqrt{b^2 - 4ac}}{2a}
$$

- Com isso iremos identificar as raizes da nossa equação característica, agora podemos utiliza-las para acharmos a solução da nossa $EDO$.

<aside>
<img src="Equac%CC%A7o%CC%83es%20Lineares%20de%202a%20Ordem%20e%20de%20Ordem%20Superio%209fe92ce83fd04b1da738a9ab9a24f645/Hifumi_Surprised.png" alt="Equac%CC%A7o%CC%83es%20Lineares%20de%202a%20Ordem%20e%20de%20Ordem%20Superio%209fe92ce83fd04b1da738a9ab9a24f645/Hifumi_Surprised.png" width="40px" /> Lembrando sempre que nossas raizes podem ser número imaginários!!!

</aside>

### Achando a solução da EDO a Partir das Raizes da Equação Característica

- Para isso precisamos transformar nossas raizes da equação característica em componentes da solução da nossa EDO (i.e a solução da EDO é a soma das raizes "tratadas" da nossa equação característica), e esse "tratamento" muda de acordo com o  caso:

**Raizes Reais**

- Para  $n$  raizes iguais, consideramos que  a componente que irá ser somada à solução da nossa $EDO$ (referente à todas essas $n$ raizes iguais) será:

$$
c_1e^{rx} + c_2xe^{rx} + c_3x^2e^{rx}
$$

- Basicamente nós sempre multiplicamos por $x$ a cada nova aparição da mesma raiz.
- Se a raiz for única, seria somente a soma de $c_ie^{r_ix}$

**Raizes Imaginárias**

- Nós sempre consideramos raizes imaginárias como um par conjugado ($\alpha \pm \beta i$), com isso a componente que devemos somar à solução da nossa EDO é:

$$
e^{ax}(c_1\cos(\beta x) + c_2\sin(\beta x))
$$

<aside>
💡 Se a raiz imaginária também se repetir, fazemos de modo análogo ao como fizemos com raizes reais que se reptem, nós multiplicamos a nova "componente" por x para cada vez que ela se repte, depois somamos todas.

E.G
$e^{ax}(c_1\cos(\beta x) + c_2\sin(\beta x)) + xe^{ax}(c_3\cos(\beta x) + c_4\sin(\beta x)) + ...$

</aside>

No final nós simplesmente somamos todas as componentes, e isso resultará na solução da nossa EDO, exemplo:

$$
y(x) = c_1e^{r_1x} + e^{\alpha x}(c_1\cos(\beta x) + c_2\sin(\beta x))
$$

# Equações de Ordem n>2

- A única coisa que mudaria seria a forma de obtermos nossas raizes da equação característica, pois teríamos que fatorar.