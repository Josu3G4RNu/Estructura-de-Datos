class queue:

    def __init__(self,maxsize = 0):
        self.maxsize = maxsize
        self.__vacia = -1
        self.cola = []

    def is_empty(self) -> bool:
        """
        Evalua si la cola esta vacia

        :return: True o False
        """
        return self.__vacia == -1

    def is_full(self) -> bool:
        """
        Evalua si la cola esta llena

        :return: True o False
        """
        return self.__vacia == self.maxsize - 1

    def extract(self):
        """
        Extrae el primer elemento de la cola

        :return: Any
        """
        if not self.is_empty():
            return self.cola.pop(0)
        else:
            print("Cola Vacia! No hay elementos en cola")

    def add(self, dato):
        """
        Añade un elemento al final de la cola

        :param dato: Any
        :return: None
        """
        if not self.is_full():
            self.cola.append(dato)
        else:
            print("Cola Llena! No se pueden agregar más elementos")

    def length(self):
        """
        Devuelve la longitud de la cola

        :return: int
        """
        return len(self.cola)

    def front(self):
        """
        Devuelve el primer elemento de la cola

        :return: Any
        """
        return self.cola[0]