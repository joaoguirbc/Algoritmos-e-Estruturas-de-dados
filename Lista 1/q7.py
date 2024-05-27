while True:
    try:
        entrada = int(input())
    except:
        break

    num_elementos = 0                          # Variável para auxiliar na verificação da pilha
    vetor_fila = []
    vetor_pilha = []
    vetor_fila_de_prioridade = []

    fila = True
    pilha = True
    fila_de_prioridade = True

    for i in range(entrada):
        comando, elemento = input().split()

        if int(comando) == 1:
            vetor_pilha.append(int(elemento))
            num_elementos += 1

            vetor_fila.append(int(elemento))

            vetor_fila_de_prioridade.append(int(elemento))
            vetor_fila_de_prioridade.sort(reverse = True)
        else:
            if vetor_pilha[num_elementos-1] == int(elemento) and pilha:
                num_elementos -= 1
                del vetor_pilha[num_elementos]
            else:
                pilha = False

            if vetor_fila[0] == int(elemento) and fila:
                del vetor_fila[0]
            else:
                fila = False

            if vetor_fila_de_prioridade[0] == int(elemento) and fila_de_prioridade:
                del vetor_fila_de_prioridade[0]
            else:
                fila_de_prioridade = False

    if (pilha == True and fila == True) or (pilha == True and fila_de_prioridade == True) or (fila == True and fila_de_prioridade == True):
        print('not sure')
    elif fila:
        print('queue')
    elif pilha:
        print('stack')
    elif fila_de_prioridade:
        print('priority queue')
    else:
        print('impossible')