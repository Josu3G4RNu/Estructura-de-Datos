import time
from Esqueleto_Estructuras.Stacks import Stack

class Pilas(Stack):
    """
    Clase creada para dar solución al problema 1 de pilas. Esta hereda de la clase Stack que almacena todas las
    operaciones de pilas.
    """
    def __init_(self, maxlenght):
        Stack.__init__(self, maxlenght)

    def is_full(self):
        if self._vacia == self.lenght - 1:
            print(self.stacklist)
            print("Upps... PILA LLENA! \nEspera el tamaño se esta ampliando")
            time.sleep(2)
            self.lenght = self.lenght * 2
            print("Hecho... Tamaño ampliado. Limite de almacenamiento nuevo: ", self.lenght)
            return False
        else:
            return self._vacia == self.lenght

def SolutionP1():
    x = Pilas(2)
    print("la capacidad máxima de la pila es de: ", x.lenght)
    x.push(23)
    x.push(46)
    x.push(89)