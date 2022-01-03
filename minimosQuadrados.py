# MMQ Generico:
# F_aprox(x) = k0*g0(x) + k1*g1(x) + k2*g2(x) + ...
# onde ki = coeficientes, e gi(x) = funcoes de x (base do espaço)
# encontrar k0, k1, k2, ... para minimizar erro = |f(x)-Faprox(x)|^2

# Resolver o sistema:
#
#   | (g0,g0)  (g1,g0)  ...  (gm,g0) | | k0 |   | (f,g0) |
#   | (g0,g1)  (g1,g1)  ...  (gm,g1) | | k1 | = | (f,g1) |
#   |   ...      ...    ...    ...   | | .. |   |   ..   |
#   | (g0,gm)  (g1,gm)  ...  (gm,gm) | | km |   | (f,gm) |
#
# para o caso discreto temos o produto escalar (r,s) = Somatorio r(xi)*s(xi)
#                                                      (i=0 a n_pontos)
#
# onde: xi sao as abscissas dos pontos, e f as ordenadas (yi = f(xi))

import numpy

## DADOS DE ENTRADA
x = [numpy.pi/2, numpy.pi, 3*numpy.pi/2, 2*numpy.pi]
y = [159, 178, 179, 149]
# resposta do exemplo: F_aprox(x) = 166.25 - 14.5*sin(x) - 10*cos(x)

## FUNCAO APROXIMADORA
# F_aprox(x) = k0*1 + k1*cos(x) + k2*sin(x)
g0 = lambda x: 1
g1 = lambda x: numpy.cos(x)
g2 = lambda x: numpy.sin(x)

vetor_g = [g0, g1, g2]

# computa as funcoes da base nos pontos x de entrada (necessario para produto escalar)
# resulta em: [[g0(x0), g0(x1), ...], [g1(x0), g1(x1), ...], ...]
res_g = [list(map(g, x)) for g in vetor_g]
# transforma em objeto array para permitir manipulacao como matriz
arr = numpy.array(res_g)

# calcula o produto escalar de cada termo e gera as matrizes
mat_esq = numpy.dot(arr, arr.T)
mat_dir = numpy.dot(arr, y)

# resolve sistema linear e encontra vetor com os coeficientes ki
vetor_k = numpy.linalg.solve(mat_esq, mat_dir)
print(vetor_k)
