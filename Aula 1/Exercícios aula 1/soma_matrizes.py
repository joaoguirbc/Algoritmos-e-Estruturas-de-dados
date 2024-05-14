def soma_matrizes(m1, m2):
    n = 0
    if len(m1) != len(m2):
        return 'Essas matrizes não podem ser somadas.'
    else:
        for l in m1:
            if len(l) != len(m2[n]):
                return 'Essas matrizes não podem ser somadas.'
            else:
                n += 1
    
    i = 0
    
    soma = []
    for l in m1:
        j = 0
        linha = []
        for e in l:
            elemento_m2 = m2[i][j]
            e = e + elemento_m2
            linha.append(e)
            j += 1
        soma.append(linha)
        i += 1

    return soma

matriz_1 = [[1, 2], [0, 1]]
matriz_2 = [[3, 0], [1, 1]]

print(soma_matrizes(matriz_1, matriz_2))