from lista_encadeada_dupla import ListaEncadeadaDupla

led_1 = ListaEncadeadaDupla()

led_1.add('Guilherme')

led_1.add('Carol', 1)

print(led_1)

led_1.addAll(2, ['João', 'Pedro', 'Marcelo'])

led_1.remove('Pedro')

led_1.remove('Luc')

led_1.removeAt(2)

print(led_1)

print(led_1.getElement(2))

print(led_1.isEmpty())

print(led_1.size())

led_1.clear()

print(led_1.isEmpty())

print(led_1.size())