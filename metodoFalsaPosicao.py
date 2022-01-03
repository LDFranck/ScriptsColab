# Metodo Numerico para Equacoes Nao-Lineares
# Regula Falsi (Falsa Posicao)

# f = funcao para analise
# a = inicio do intervalo
# b = final do intervalo
# e = erro maximo
# i = numero maximo de iteracoes

def regulaFalsi(f, a, b, e, i):
    r = [f(a), f(b)]

    if r[0]*r[1] > 0:
        print('erro: intervalo invalido')
    elif r[0]*r[1] == 0:
        print(f'raiz: {a if r[0]==0 else b}')
    else:
        while True:
            xk = (r[1]*a-r[0]*b)/(r[1]-r[0])
            if min(map(abs, [xk-a, xk-b])) < e*max(1, abs(xk)):
                print(f'raiz: {xk}')
                break
            else:
                a, b = [b, xk] if f(xk)*r[0] < 0 else [a, xk]
                r = [f(a), f(b)]
                i -= 1
                if i == 0:
                    print('erro: maxiter')
                    break
