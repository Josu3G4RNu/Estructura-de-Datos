class Stack:
    _vacia = -1
    stacklist = []

    def __init__(self, lenght):
        """
        Metodo Constructor

        :param lenght: Int
        """
        self.lenght = lenght

    def is_empty(self)-> bool:
        """
        Evalua si la pila esta vacía

        :return: True o False
        """
        return self._vacia == -1

    def is_full(self):
        """
        Evalua si la pila esta llena

        :return: True o False
        """
        return self._vacia == self.lenght -1


    def push(self, dato):
        """
        Agrega un elemento a la pila

        :param dato: Any
        :return: Void
        """
        if not self.is_full():
            self.stacklist.insert(0, dato)
            self._vacia += 1

    def pop(self):
        """
        Elimina el elemento top de la pila

        :return: void
        """
        if self.is_empty():
            print("Pila Vacia; no se puede eliminar algo dentro de un Nada")
        else:
            self.stacklist.pop(0)
            self._vacia -= 1
            print("Elemento eliminado correctamente. PILA resultante: ",self.stacklist)

    def clean_stack(self):
        """
        Elimina todos los elementos de la pila

        :return: Void
        """
        return self.stacklist.clear()

    def top(self):
        """
        Muestra el elemento top de la pila

        :return: Any
        """
        return self.stacklist[0]
