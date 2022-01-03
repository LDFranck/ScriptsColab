import csv
import numpy

with open('nome_arquivo.txt', 'rt') as arquivo:
    # abre buffer de leitura como arquivo de dados separados por tab
    buffer = csv.reader(arquivo, delimiter='\t')
    # o buffer aponta para cada linha, e avanca por linha (ignora colunas) -> next(buffer) avanca uma linha

    # pega primeira linha do buffer e avanca -> separa cabecalho dos dados
    cabecalho = next(buffer)
    print(cabecalho)

    # funcao map aplica list() nos elementos do buffer -> cada linha vira um vetor com os dados nas colunas
    matriz = list(map(list, buffer))
    # a list(...) externa cria, por sua vez, um vetor com os vetores de cada linha -> gerando uma matriz de dados

    # aplica a funcao float(...) em todos elementos da matriz de dados (estava em string)
    dados = numpy.vectorize(float)(matriz).T
    # e pega a matriz transposta (.T) -> agrupa cada grandeza medida em um vetor linha (facilita para graficos)
