from Esqueleto_Estructuras.Queue import *
from Esqueleto_Estructuras.Linked_List import *

class lista_enlazada(LinkedList):

    def __init__(self):
        LinkedList.__init__(self)

    def insert(self, NSS):
        """
        Metodo que se encarga de agregar un nuevo trabajador manteniendo un orden ascendente en los numeros de seguro
        social de los trabajadores.

        :param NSS: int
        :return: None
        """
        nodo = Node([NSS, input("Nombre: "), int(input("Dias Trabajados: "))])
        if self.head is None:
            self.head = nodo
            return

        if self.head.data[0] > nodo.data[0]:
            nodo.next = self.head
            self.head = nodo
            return

        while self.head.data[0] < nodo.data[0]:
            if self.head.next is None:
                self.head.next = nodo
                return
            self.head = self.head.next
        self.head.next = nodo

    def search(self, NSS):
        """
        Metodo que evalua si el numero de seguro social existe dentro de la lista

        :param NSS: int
        :return: True o False
        """
        n = self.head
        if n is None:
            return False

        while n.next is not None:
            if n.data[0] == NSS:
                return True
            n = n.next
        return False


class Colas(queue):

    def add(self, dato):
        self.cola.append(dato)

    def extract(self):
        return self.cola.pop(0)[0]

    def front(self):
        return self.cola[0][0]

    def print_cola(self):
        """
        Metodo para imprimir la Cola en consola

        :return: None
        """
        for i in range(0, self.length()):
            print(self.cola[i], end= " ")
        print()


class SolutionP2:
    lista = lista_enlazada()
    cola = Colas()
    cola.add([12, "AT&T"])
    cola.add([15, "Telcel"])
    cola.add([7, "Movistar"])
    cola.print_cola()

    def actualizar_Cola(self):
        """
        Metodo encaragdo de analizar si el trabajador esta en la lista enlazada, en caso de estarlo no hará nada,
        de no estarlo agregará al trabajador. Evaluando si el Número de Seguridad Social que esta dentro de la cola
        se encuentra tambien en la lista enlazada.

        :return: None
        """
        #Evaluación de Existencia
        for i in range(0, self.cola.length()):
            if self.lista.search(self.cola.front()):
               return

            self.lista.insert(self.cola.extract())
            self.lista.display()
