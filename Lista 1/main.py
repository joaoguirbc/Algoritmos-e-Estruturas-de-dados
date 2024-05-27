from lista_de_vetor import ArrayList
from lista_encadeada import ListaEncadeada, ListaDuplamenteEncadeada
from fila import Fila
from pilha import Pilha

def teste_array_list():
    print('Teste ArrayList:')
    array_list = ArrayList(3)
    array_list.add('João')
    array_list.addAll(1, ['Pedro', 'Marcelo'])
    print('ArrayList:', array_list)
    array_list.remove('Pedro')
    array_list.removeAt(0)
    print('ArrayList:', array_list)
    array_list._resize(5)
    array_list.add('Carol')
    array_list.add('Guilherme')
    array_list.add('André')
    array_list.add('Luc', 2)
    print('ArrayList:', array_list)
    array_list.add('Ângela')
    print('ArrayList:', array_list)
    print('Elemento na posição 2:', array_list.getElement(2))
    print('Tamanho da lista:', array_list.size())
    print('Lista vazia?', array_list.isEmpty())
    array_list.clear()
    print('Lista vazia?', array_list.isEmpty())


def teste_lista_encadeada():
    print('Teste Lista encadeada:')
    lista_encadeada = ListaEncadeada()
    lista_encadeada.add('Sport')
    lista_encadeada.addAll(1, ['Náutico', 'Retrô', 'Santa Cruz'])
    print('Lista encadeada:', lista_encadeada)
    lista_encadeada.remove('Santa Cruz')
    lista_encadeada.removeAt(1)
    print('Lista encadeada:', lista_encadeada)
    print('Elemento na posição 1:', lista_encadeada.getElement(1))
    print('Tamanho da lista:', lista_encadeada.size())
    print('Lista vazia?', lista_encadeada.isEmpty())
    lista_encadeada.clear()
    print('Lista vazia?', lista_encadeada.isEmpty())


def teste_lista_encadeada_dupla():
    print('Teste lista duplamente encadeada:')
    lde = ListaDuplamenteEncadeada()
    lde.add(1)
    lde.addAll(1, [2, 3, 4, 5])
    print('Lista duplamente encadeada:', lde)
    lde.remove(3)
    lde.removeAt(0)
    print('Lista duplamente encadeada', lde)
    print('Elemento na posição 1:', lde.getElement(1))
    print('Tamanho da lista:', lde.size())
    print('Lista vazia?', lde.isEmpty())
    lde.clear()
    print('Lista vazia?', lde.isEmpty())


def teste_fila():
    print('Teste fila:')
    fila = Fila()
    fila.enqueue('Brasil')
    fila.enqueue('Espanha')
    fila.enqueue('França')
    print('Fila:', fila)
    fila.dequeue()
    print('Fila:', fila)
    print('Início da fila:', fila.peek())
    print('Tamanho da lista:', fila.size())
    print('Fila vazia?', fila.isEmpty())


def teste_pilha():
    print('Teste pilha:')
    pilha = Pilha()
    pilha.push('Audi')
    pilha.push('BMW')
    pilha.push('Mercedes')
    pilha.push('Porshe')
    print('Pilha:', pilha)
    pilha.pop()
    print('Pilha:', pilha)
    print('Topo da pilha:', pilha.peek())
    print('Tamanho da pilha:', pilha.size())
    print('Pilha vazia?', pilha.isEmpty())


if __name__ == '__main__':
    teste_array_list()
    teste_lista_encadeada()
    teste_lista_encadeada_dupla()
    teste_fila()
    teste_pilha()