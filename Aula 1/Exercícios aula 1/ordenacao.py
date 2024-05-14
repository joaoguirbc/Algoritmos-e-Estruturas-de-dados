array = [4, 7, 2, 10, 5, 0, 1, 9, 12, 6]

def ordenacao(vetor):
    n = len(vetor)
    
    for i in range(n):
        menor_valor = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[menor_valor]:
                menor_valor = j
        
        vetor[i], vetor[menor_valor] = vetor[menor_valor], vetor[i]
    
    return vetor

print(f'Array original: {array}')
print(f'Array ordenado: {ordenacao(array)}')