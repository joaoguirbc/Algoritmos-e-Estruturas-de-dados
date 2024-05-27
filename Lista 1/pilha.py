from lista_encadeada import ListaEncadeada

class Pilha:
    def __init__(self):
        self.pilha = ListaEncadeada()
        self._dados = []

    def push(self, elemento):
        self.pilha.add(elemento)
        self._dados.append(elemento)

    def pop(self):
        if self.pilha.isEmpty():
            raise IndexError('Pilha vazia')
        posicao = self.pilha.size() - 1
        elemento = self.pilha.getElement(posicao)
        self.pilha.remove(elemento)
        self._dados.remove(elemento)
    
    def peek(self):
        if self.pilha.isEmpty():
            raise IndexError('Pilha vazia')
        posicao = self.pilha.size() - 1
        return self.pilha.getElement(posicao)
    
    def isEmpty(self):
        return self.pilha.isEmpty()
    
    def size(self):
        return self.pilha.size()
    
    def __str__(self):
        if len(self._dados) > 0:
            return ', '.join(map(str, self._dados))
        raise ValueError('Lista vazia')