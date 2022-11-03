class Nodo:

    def __init__(self, dato: int):
        self.dato = dato
        self.hijoIzq = None
        self.hijoDer = None


class Arboles_Binarios:

    def __init__(self):
        self.raiz = None

    def __is_empty(self) -> bool:
        """Evalua si árbol esta vacío"""
        return self.raiz is None

    def search_node(self, raiz: Nodo, busqueda: int) -> None | Nodo:
        """Evalúa si un nodo se encuentra en el árbol"""
        if raiz is None:
            return None
        if raiz.dato == busqueda:
            return raiz
        if busqueda < raiz.dato:
            return self.search_node(raiz.hijoIzq, busqueda)
        else:
            return self.search_node(raiz.hijoDer, busqueda)

    def __add_node(self, nodo, dato: int):
        """Agrega un nuevo nodo al árbol de forma recursiva"""

        if nodo is None:
            self.raiz = Nodo(dato)
            return

        if dato < nodo.dato:
            if nodo.hijoIzq is None:
                nodo.hijoIzq = Nodo(dato)
            else:
                self.__add_node(nodo.hijoIzq, dato)
        else:
            if nodo.hijoDer is None:
                nodo.hijoDer = Nodo(dato)
            else:
                self.__add_node(nodo.hijoDer, dato)

    def add_node(self, dato: int):
        """Se encargad de añadir un nuevo nodo al árbol"""
        self.__add_node(self.raiz, dato)

    def count_sheets(self, raiz: Nodo) -> int:
        """Metodo para contar los nodos hijos dentro del árbol de forma recursiva
        """
        contador = 0
        if (raiz.hijoDer and raiz.hijoIzq) is None:
            return 1
        if raiz.hijoIzq is not None:
            contador += self.count_sheets(raiz.hijoIzq)
        if raiz.hijoDer is not None:
            contador += self.count_sheets(raiz.hijoDer)
        return contador


def recorrer_arbol(nodo: Nodo, level=0):
    print(f"{'-' * level} {nodo.dato}")

    if nodo.hijoIzq is not None:
        recorrer_arbol(nodo.hijoIzq, level + 1)

    if nodo.hijoDer is not None:
        recorrer_arbol(nodo.hijoDer, level + 1)
