# Projeção em Base Ortogonal

Semana: Semana 12

# Como projetar

- Considere um vetor $v = (1,2,1)$ e o plano em $\R^{3}$ formado pelos vetores $(1,0,1) \ e  \ (-1,4,1)$, calcule a projeção de $v$  nesse plano;';.
    - Se observarmos bem, os vetores formam uma base ortogonal $\lang (1,0,1),(-1,4,1)\rang = 0$ , com isso podemos fazer:
        
        $$
        P_H = \frac{\lang(1,2,1);(1,0,1)\rang}{\lang(1,0,1);(1,0,1)\rang} (1,0,1) + \frac{\lang(1,2,1);(-1,4,1)\rang}{\lang(-1,4,1);(-1,4,1)\rang}(-1,4,1)
        $$