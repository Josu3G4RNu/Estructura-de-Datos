class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        # Se crea el nodo head
        self.head = None

    def insert(self, new_node):
        """
        Inserta un nuevo nodo

        :param new_node: Nodo
        :return: None
        """
        if self.head:
            # obteniendo el nodo head
            n= self.head
            while n.next is not None:
                n = n.next

            # Asignando el nuevo nodo al apuntador del último nodo
            n.next = new_node

        else:
            # Si el nodo head es vacio asignará el nuevo nodo como el nodo head
            self.head = new_node

    def display(self):
        """
        Metodo para imprimir la lista

        :return: None
        """
        # Variable para iterar la lista
        n = self.head

        # Iteración de la lista
        while n is not None:
            # impresión de la lista
            print(n.data, end=' -> ')
            n = n.next
        print('Null')
