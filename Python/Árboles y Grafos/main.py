from Arboles_Binarios import Arboles_Binarios, recorrer_arbol
from Grafos import Grafo

# Arboles
# Creación de un objeto del tipo arbol binario
prueba = Arboles_Binarios()

# Agregado de los diversos nodos
prueba.add_node(19)
prueba.add_node(78)
prueba.add_node(15)
prueba.add_node(18)
prueba.add_node(7)
prueba.add_node(89)
prueba.add_node(76)
prueba.add_node(2)
prueba.add_node(5)

# Recorremos e imprimimos el árbol
recorrer_arbol(prueba.raiz)

# Imprimimos la cantidad e nodos hijos dentro del árbol
print(prueba.count_sheets(prueba.raiz))


# Grafos
# Creamos un objeto de tipo Grafo
grafo = Grafo()

# Añadimos los vertices al grafo
grafo.add_vertice('A')
grafo.add_vertice('B')
grafo.add_vertice('C')
grafo.add_vertice('D')
grafo.add_vertice('E')
grafo.add_vertice('F')
grafo.add_vertice('G')
grafo.add_vertice('H')

# Añadimos los ejes correspondientes
grafo.add_arista('A', 'D', 7)
grafo.add_arista('A', 'G', 16)
grafo.add_arista('B', 'F', 21)
grafo.add_arista('C', 'B', 16)
grafo.add_arista('C', 'E', 12)
grafo.add_arista('C', 'H', 9)
grafo.add_arista('D', 'B', 8)
grafo.add_arista('E', 'D', 9)
grafo.add_arista('E', 'F', 6)
grafo.add_arista('F', 'G', 8)
grafo.add_arista('G', 'B', 13)
grafo.add_arista('G', 'C', 12)
grafo.add_arista('H', 'A', 8)
grafo.add_arista('H', 'D', 17)

print(grafo.dijkstra('B'))
grafo.imprimir_grafo()
