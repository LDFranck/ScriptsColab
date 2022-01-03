# Importar dados de resposta em frequencia (Bode Plot) do LTSpice
# File -> Export data as text -> Format: cartesian (re, im) -> OK = nome_arquivo.txt
# adaptado de importarDados.py para suportar os dados complexos

# SEMPRE EXPORTAR EM FORMATO CARTESIANO

import csv
import numpy

with open('nome_arquivo.txt', 'rt') as arquivo:
    buffer = csv.reader(arquivo, delimiter='\t')

    cabecalho = next(buffer)
    print(cabecalho)

    matriz = list(map(list, buffer))
    freq = numpy.vectorize(float)([linha[0] for linha in matriz])
    cplx = numpy.vectorize(float)([linha[1].split(',') for linha in matriz])

    magnitude = numpy.linalg.norm(cplx, axis=1)
    fase = numpy.arctan([num[1]/num[0] for num in cplx])
