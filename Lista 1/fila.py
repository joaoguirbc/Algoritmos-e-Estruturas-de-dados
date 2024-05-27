from lista_encadeada import ListaEncadeada

class Fila():
    def __init__(self):
        self.fila = ListaEncadeada()
        self._dados = []

    def enqueue(self, elemento):
        self.fila.add(elemento)
        self._dados.append(elemento)

    def dequeue(self):
        if self.fila.isEmpty():
            raise IndexError("Fila vazia")
        elemento = self.fila.getElement(0)
        self.fila.remove(elemento)
        self._dados.remove(elemento)
    
    def peek(self):
        if self.fila.isEmpty():
            raise IndexError("Fila vazia")
        return self.fila.getElement(0)
    
    def isEmpty(self):
        return self.fila.isEmpty()
    
    def size(self):
        return self.fila.size()
    
    def __str__(self):
        if len(self._dados) > 0:
            return ', '.join(map(str, self._dados))
        raise ValueError('Lista vazia')