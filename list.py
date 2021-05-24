from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self._size = 0

    # Inserir elementos no final da lista.
    def append(self, element):
        # Caso exista um elemento já na lista.
        if self.head:
            # Inserção quando a lista já possui elementos
            pointer = self.head
            ls = None
            # Pegar a posição da memória onde não exista nada no próximo next
            while(pointer.next):
                ls = pointer
                pointer = pointer.next
            pointer.next = Node(element)
            pointer.next.ls = pointer
            pointer.ls = ls
            if self.last:
                self.last = pointer.next

        # Se não insira o primeiro elemento na lista.
        else:
            # Primeira inserção
            self.head = Node(element)
            self.last = Node(element)
        self._size = self._size + 1

    def __len__(self):
        # Retorna o tamanho da lista.
        return self._size

    def _get_node(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def set(self, index, element):
        pass

    def __getitem__(self, index):
        # Recuperar o valor a partir de []
        # a = lista[6]
        pointer = self._get_node(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")


    def __setitem__(self, index, element):
        # lista[5] = 9
        pointer = self._get_node(index)
        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")

    def index(self, element):
        # Retorna o índice do element na lista
        pointer = self.head
        i = 0
        # for diferente de None
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError(f'{element} is not in list')

    def insert(self, index, element):
        node = Node(element)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._get_node(index-1)
            node = Node(element)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def dell(self):
        pass

    # Imprimir a lista.
    def get_lista(self):
        if self.head == None:
            raise IndexError("Empty list")
        else:
            print("Ordem normal, conforme foi inserido os elementos")
            pointer = self.head
            while(pointer):
                print(f'{pointer.data}, ', end="")
                pointer = pointer.next
            print(f'\nTamanho da lista: {self._size}')
            print("--------------------------")

    # Imprimir a lista (inversalmente)
    def get_lista_inversa(self):
        pointer = self.last
        print("Ordem inversa dos elementos inseridos")
        while(pointer):
            print(f'{pointer.data}, ', end="")
            pointer = pointer.ls
        print(f'\nTamanho da lista: {self._size}')
        print("--------------------------")