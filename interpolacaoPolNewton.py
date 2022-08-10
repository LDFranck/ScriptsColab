import numpy

## DADOS DE ENTRADA
x = [-1, -0.5, 0, 0.5, 1]
y = [-1, 4, 5, 5, 7]
# resposta do exemplo: 4x^3 - 2x^2 + 5

## INICIO BLOCO: Diferencas Divididas
dd_mat = numpy.zeros([len(x), len(x)])
# preenche primeira coluna com os valores da funcao fornecidos
dd_mat[0][:] = y
dd_mat = dd_mat.T

# calcula as diferencas divididas de cada ordem
for i in range(0, len(x)):
    for j in range(0, len(x)-i-1):
        dd_mat[j][i+1] = (dd_mat[j+1][i]-dd_mat[j][i])/(x[j+i+1]-x[j])

dd_coef = dd_mat[0]
## FIM BLOCO: Diferencas Divididas

## INICIO BLOCO: Multiplicacao de Binomios + Coeficientes do Polinomio de Newton
# realiza a multiplicacao de (x-x1)*(x-x2)*(x-x3)... -> fornece lista com os coef
# a2*x^2 + a1*x + a0 -> resultado: [a2, a1, a0]
pol = numpy.zeros([len(x), len(x)])
pol[0][0] = 1
pol[1][0:2] = [-x[0], 1]

# computa as multiplicacoes dos binomios
for i in range(2, len(x)):
    pol[i][0] = pol[i-1][0]*(-x[i-1])
    for j in range(1, len(x)):
        pol[i][j] = pol[i-1][j]*(-x[i-1])+pol[i-1][j-1]
    pol[i][i] = 1

# multiplica cada 'sub-polinomio' por seu coeficiente das diferencas divididas
for i in range(0, len(x)):
    pol[i] = numpy.multiply(pol[i], dd_coef[i])

# soma termos de mesma ordem
coef = numpy.zeros(len(x))
for i in range(0, len(x)):
    for j in range(0, len(x)):
        coef[i] += pol[j][i]

# inverte coeficientes para ficar compativel com polyval (maior->menor grau)
print(list(reversed(coef)))
## FIM BLOCO: Multiplicacao de Binomios + Coeficientes do Polinomio de Newton
