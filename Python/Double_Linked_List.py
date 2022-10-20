class Nodo:

    def __init__(self, dato):
        '''
        Metodo Constructor

        :param dato: String
        '''
        self.dato = str(dato)
        self.before = None
        self.next = None

class Double_LList:
    def __init__(self):
        """
        Metodo Constructor
        """
        self.head = None
        self.lenght = 0

    def is_empty(self):
        """
        Evalua si la lista esta vacia

        :return: True o False
        """
        return self.head is None

    def search(self, dato):
        """
        Evalua si el nodo se encuentra dentro dela lista

        :param dato: Nodo
        :return: True o False
        """
        n = self.head
        while n is not None:
            if dato == n.dato:
                return n
            n = n.next
        return None

    def add_head(self, dato):
        """
        Agrega un nodo al inicio de la lista

        :param dato: Nodo
        :return: Void
        """
        if self.is_empty():
            nodo = Nodo(dato)
            self.head = nodo
            self.lenght += 1
            self.traverse_list()
            return
        nodo = Nodo(dato)
        nodo.next = self.head
        self.head.before = nodo
        self.head = nodo
        self.lenght += 1
        self.traverse_list()

    def add_back(self, dato):
        """
        Añade al final de la lista

        :param dato: Nodo
        :return: Void
        """
        if self.is_empty():
            self.add_head(dato)
        n = self.head
        while n.next is not None:
            n = n.next
        nodo = Nodo(dato)
        n.next = nodo
        nodo.before = n
        self.lenght += 1
        self.traverse_list()

    def add_after(self, despuesde, dato):
        """
        Añade un Nodo depsués despuesde otro

        :param despuesde: Nodo
        :param dato: Nodo
        :return: Void
        """
        x = self.search(despuesde)
        if x is not None:
            nodo = Nodo(dato)
            nodo.before = x
            nodo.next = x.next
            if x.next is not None:
                x.next.before = nodo
            x.next = nodo
            self.lenght += 1
            self.traverse_list()
        else:
            print("El elemento no se encuentra dentro de la lista")

    def add_before(self, antesde, dato):
        """
        Añade un Nodo anted de otro

        :param antesde: Nodo
        :param dato: Nodo
        :return: Void
        """
        x = self.search(antesde)
        if x is not None:
            nodo = Nodo(dato)
            nodo.before = x.before
            nodo.next = x
            if x.before is not None:
                x.before.next = nodo
            x.before = nodo
            self.lenght += 1
            self.traverse_list()
        else:
            print("El elemento no se encuentra dentro de la lista")

    def delate_head(self):
        """
        Elimina el primer Nodo de la lista

        :return: Void
        """
        if not self.is_empty():
            if self.head.next is None:
                self.head = None
                return
            self.head = self.head.next
            self.head.before = None
            self.lenght -= 1
            self.traverse_list()
            return
        print("\n No hay elementos a eliminar")

    def delate_back(self):
        """
        Elimina el ultimo Nodo de la lista

        :return: Void
        """
        if not self.is_empty():
            if self.head.next is None:
                self.head = None
                return
            n = self.head
            while n.next is not None:
                n = n.next
            n.before.next = None
            self.lenght -= 1
            self.traverse_list()
            return
        print("\n No hay elementos a eliminar")

    def delate_value(self, dato):
        """
        Elimina un Nodo en específico

        :param dato: Nodo
        :return: Void
        """
        x = self.search(dato)
        if x is not None:
            if self.head == dato:
                self.delate_head()
                self.lenght -= 1
            n = self.head
            while n.next is not None:
                if n.dato == dato:
                    break
                n = n.next
            if n.next is not None:
                n.before.next = n.next
                n.next.before = n.before
                self.lenght -= 1
                self.traverse_list()
            return
        print("El elemento no existe dentro de la lista")

    def get_lenght(self):
        """
        Regresa la longitud de la lista

        :return: length
        """
        return self.lenght

    def traverse_list(self):
        """
        Imprime en Consola todos los elementos de la lista

        :return: Void
        """
        n = self.head
        while n is not None:
            print(n.dato, end=" <=> ")
            n = n.next
        print("Null")