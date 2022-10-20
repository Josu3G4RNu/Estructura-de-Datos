from Esqueleto_Estructuras.Double_Linked_List import Double_LList


class ListasDE(Double_LList):
    """
    Clase creada para dar solución al problema número 3 de listas doblemente enlazadas. Esta clase hereda de la clase
    Double_LList que contiene todas las operaciones de las listas doblemente enlazadas.
    """
    def __init__(self):
        Double_LList.__init__(self)

    def add_close_middle(self, dato):
        """
        Añade un nuevo nodo después de aquel que esta en medio, de ser que la lista es vacia lo agrega en la
        cabeza de la lista

        :param dato: Nodo
        :return: Void
        """

        nodo = dato
        long = self.get_lenght()
        if self.is_empty():
            self.add_head(nodo)
            self.lenght += 1
        else:
            n = self.head
            if long % 2 == 0:
                for i in range(0, int(long / 2) -1):
                    n = n.next
                self.add_after(n.dato,nodo)
            else:
                for i in range(0, int(long / 2)):
                    n = n.next
                self.add_after(n.dato, nodo)

    @staticmethod
    def SolutionP3():
        z = ListasDE()
        z.add_close_middle(input())
        z.add_close_middle(input())
        z.add_close_middle(input())
        z.add_close_middle(input())
        z.add_close_middle(input())
