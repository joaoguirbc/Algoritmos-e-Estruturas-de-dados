class No:
    def __init__(self, dado = None):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class BaseListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def isEmpty(self):
        return self.inicio is None
    
    def size(self):
        return self._tamanho
    
    def clear(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def getElement(self, posicao):
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        
        no_atual = self.inicio
        for i in range(posicao):
            no_atual = no_atual.proximo
        return no_atual.dado
    

class ListaEncadeada(BaseListaEncadeada):
    def add(self, elemento, posicao = None):
        novo_no = No(elemento)
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

    def __str__(self):
        elementos = []
        no_atual = self.inicio
        while no_atual:
            elementos.append(no_atual.dado)
            no_atual = no_atual.proximo
        if len(elementos) > 0:
            return " -> ".join(map(str, elementos))
        raise ValueError('Lista vazia')
    

class ListaDuplamenteEncadeada(BaseListaEncadeada):
    def add(self, elemento, posicao = None):
        novo_no = No(elemento)
        if posicao is None:
            posicao = self._tamanho
        
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        
        if posicao == 0:
            if self.inicio is None:
                self.inicio = novo_no
                self.fim = novo_no
            else:
                novo_no.proximo = self.inicio
                self.inicio.anterior = novo_no
                self.inicio = novo_no
        elif posicao == self._tamanho:
            novo_no.anterior = self.fim
            if self.fim is not None:
                self.fim.proximo = novo_no
            self.fim = novo_no
            if self.inicio is None:
                self.inicio = novo_no
        else:
            no_atual = self.inicio
            for i in range(posicao):
                no_atual = no_atual.proximo
            novo_no.anterior = no_atual.anterior
            novo_no.proximo = no_atual
            no_atual.anterior.proximo = novo_no
            no_atual.anterior = novo_no
        
        self._tamanho += 1


    def addAll(self, posicao, lista):
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        for i, elemento in enumerate(lista):
            self.add(elemento, posicao + i)

    def remove(self, elemento):
        no_atual = self.inicio
        while no_atual is not None:
            if no_atual.dado == elemento:
                if no_atual.anterior is not None:
                    no_atual.anterior.proximo = no_atual.proximo
                else:
                    self.inicio = no_atual.proximo

                if no_atual.proximo is not None:
                    no_atual.proximo.anterior = no_atual.anterior
                else:
                    self.fim = no_atual.anterior
                
                self._tamanho -= 1
                return True
            no_atual = no_atual.proximo
        return print(f'O elemento {elemento} não pertence a esta lista.')
    
    def removeAt(self, posicao):
        if posicao < 0 or posicao > self._tamanho:
            raise ValueError('Posição inválida')
        
        no_atual = self.inicio
        for i in range(posicao):
            no_atual = no_atual.proximo

        if no_atual.anterior is not None:
            no_atual.anterior.proximo = no_atual.proximo
        else:
            self.inicio = no_atual.proximo
        
        if no_atual.proximo is not None:
            no_atual.proximo.anterior = no_atual.anterior
        else:
            self.fim = no_atual.anterior
        
        self._tamanho -= 1

    def __str__(self):
        elementos = []
        no_atual = self.inicio
        while no_atual:
            elementos.append(no_atual.dado)
            no_atual = no_atual.proximo
        if len(elementos) > 0:
            return ' <-> '.join(map(str, elementos))
        raise ValueError('Lista vazia')