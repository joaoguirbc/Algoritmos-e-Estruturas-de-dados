class ArrayList:
    def __init__(self, capacidade):
        self._capacidade = capacidade          # Inicializa um vetor com a capacidade passada na criação e sem nenhum dado
        self._tamanho = 0
        self._dados = [None] * self._capacidade
    
    def __str__(self):
        return str([self._dados[i] for i in range(self._tamanho)])     
    
    def add(self, elemento, posicao = None):
        if posicao is None:                           # Caso o usuário não especifique a posição, será adicionado no fim da lista
            posicao = self._tamanho
        if posicao < 0 or posicao > self._tamanho:    # Verifica se a posição inserida pelo usuário é válida
            raise ValueError('Posição inválida')

        if self._tamanho >= self._capacidade:         # Redimensiona o vetor
            self._resize()

        for i in range(self._tamanho, posicao, -1):
            self._dados[i] = self._dados[i - 1]       # Move os elementos à direita da posicao para abrir espaço para o novo elemento
        self._dados[posicao] = elemento
        self._tamanho += 1

    def addAll(self, posicao, lista):
        if posicao < 0 or posicao > self._tamanho:    # Verifica se a posição inserida pelo usuário é válida
            raise ValueError('Posição inválida')
        
        capacidade_necessaria = self._tamanho + len(lista)     # Essa variável representa o tamanho que a lista precisa ter para armazenar os elementos que já estão nela e a lista que será inserida
        if capacidade_necessaria > self._capacidade:
            self._resize(capacidade_necessaria)
        
        for i in range(len(lista)):
            self.add(lista[i], posicao)                    # Adiciona a lista na posição indicada pelo usuário

    def remove(self, elemento):
        encontrado = False
        for i in range(self._tamanho):
            if self._dados[i] == elemento:
                encontrado = True
            if encontrado and i < self._tamanho - 1:
                self._dados[i] = self._dados[i + 1]
        
        if encontrado:
            self._dados[self._tamanho - 1] = None
            self._tamanho -= 1
        return encontrado
    
    def removeAt(self, posicao):
        if posicao < 0 or posicao >= self._tamanho:
            raise ValueError('Posição inválida')
        
        for i in range(posicao, self._tamanho -  1):
            self._dados[i] = self._dados[i + 1]
        self._dados[self._tamanho - 1] = None
        self._tamanho -= 1

    def getElement(self, posicao):
        if posicao < 0 or posicao >= self._tamanho:
            raise ValueError('Posição inválida')
        return self._dados[posicao]
    
    def isEmpty(self):
        return self._tamanho == 0
    
    def size(self):
        return self._tamanho
    
    def clear(self):
        self._tamanho = 0
        self._dados = [None] * self._capacidade

    def _resize(self, nova_capacidade = None):
        if nova_capacidade is None:
            nova_capacidade = max(2 * self._capacidade, 1)
        
        novos_dados = [None] * nova_capacidade
        for i in range(self._tamanho):
            novos_dados[i] = self._dados[i]
        self._dados = novos_dados
        self._capacidade = nova_capacidade