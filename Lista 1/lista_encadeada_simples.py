class No:
    def __init__(self, dado = None):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0

    def __str__(self):
        return str([self])

    def add(self, dado, posicao = None):
        novo_no = No(dado)
        if posicao is None:
            posicao = self._tamanho
        
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        
        if posicao == 0:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            no_atual = self.inicio
            for i in range(posicao - 1):
                no_atual = no_atual.proximo
            novo_no.proximo = no_atual.proximo
            no_atual.proximo = novo_no

        self._tamanho += 1

    def addAll(self, posicao, lista):
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        for i, elemento in enumerate(lista):
            self.add(elemento, posicao + i)

    def remove(self, elemento):
        no_atual = self.inicio
        no_anterior = None
        while no_atual is not None:
            if no_atual.dado == elemento:
                if no_anterior is None:
                    self.inicio = no_atual.proximo
                else:
                    no_anterior.proximo = no_atual.proximo
                self._tamanho -= 1
                return True
            no_anterior = no_atual
            no_atual = no_atual.proximo
        return print(f'O elemento {elemento} não pertence a esta lista.')
    
    def removeAt(self, posicao):
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        
        no_atual = self.inicio
        no_anterior = None
        for i in range(posicao):
            no_anterior = no_atual
            no_atual = no_atual.proximo

        if no_anterior is None:
            self.inicio = no_atual.proximo
        else:
            no_anterior.proximo = no_atual.proximo

        self._tamanho -= 1

    def getElement(self, posicao):
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        
        no_atual = self.inicio
        for i in range(posicao):
            no_atual = no_atual.proximo
        return no_atual.dado
    
    def isEmpty(self):
        return self.inicio is None
    
    def size(self):
        return self._tamanho
    
    def clear(self):
        self.inicio = None
        self._tamanho = 0
    
    def __str__(self):
        elementos = []
        no_atual = self.inicio
        while no_atual:
            elementos.append(no_atual.dado)
            no_atual = no_atual.proximo
        if len(elementos) > 0:
            return " -> ".join(map(str, elementos))
        raise ValueError('Lista vazia')
