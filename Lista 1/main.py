from list_of_array import ArrayList
from lista_encadeada_simples import ListaEncadeada

lista_1 = ArrayList(2)

lista_1.add('Guilherme')

lista_1.addAll(0, ['João', 'Pedro', 'Marcelo'])

#print(lista_1)

lista_encadeada_1 = ListaEncadeada()

lista_encadeada_1.add('Argentina')
lista_encadeada_1.add('Brasil')
lista_encadeada_1.add('Uruguai')
lista_encadeada_1.add('USA')

lista_encadeada_1.addAll(2, ['Espanha', 'França'])

print(lista_encadeada_1)

lista_encadeada_1.remove('China')

lista_encadeada_1.remove('USA')
lista_encadeada_1.remove('Brasil')

print(lista_encadeada_1)

lista_encadeada_1.removeAt(2)

print(lista_encadeada_1)

print(lista_encadeada_1.getElement(0))
print(lista_encadeada_1.getElement(1))
print(lista_encadeada_1.getElement(2))

print(lista_encadeada_1.isEmpty())

print(lista_encadeada_1.size())

lista_encadeada_1.clear()

print(lista_encadeada_1.isEmpty())

print(lista_encadeada_1.size())

#print(lista_encadeada_1)