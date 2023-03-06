# Anotações de Aula

- SUMÁRIO
    
    

# O que é?

- O método de eliminação de Gauss consiste na alteração (operações elementares) da sua matriz até triangularizar e chegar em uma matriz análoga à original mas "mais fácil" de se calcular.
- O método de Gauss para uma matriz $n \times n$ terá $n-1$ etapas, onde em cada uma irá zerar uma coluna abaixo da diagonal. Com isso, na etapa $k$ estaremos eliminando a variável $x_k$ das linhas $k+1, k+2, ..., n$.

<aside>
<img src="Anotac%CC%A7o%CC%83es%20de%20Aula%2057e4a2793e364d9d8a265f6302fa794a/Evangelion.gif" alt="Anotac%CC%A7o%CC%83es%20de%20Aula%2057e4a2793e364d9d8a265f6302fa794a/Evangelion.gif" width="40px" /> OBS: Para um sistema $Ax = b$, essas operações não são feitas somente sobre $A$, mas sim sobre a matriz aumentada $[A|b]$.

</aside>

# Pivoteamento Parcial

- Para evitar erros computacionais se o pivô for muito próximo de zero, trocaremos a ordem das linhas para que o maior elemento em magintude siga para o lugar do pivô.