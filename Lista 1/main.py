from lista_encadeada import ListaDuplamenteEncadeada

lde_1 = ListaDuplamenteEncadeada()

lde_1.add('Davi')

print(lde_1)

lde_1.add('Cabeça', 0)

print(lde_1)

lde_1.removeAt(0)

print(lde_1)

lde_1.addAll(1, ['João', 'Henrique', 'Lucas'])

lde_1.clear()

print(lde_1.isEmpty())