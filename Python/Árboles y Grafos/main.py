from Arboles_Binarios import Arboles_Binarios, recorrer_arbol

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

# Imprimimos la cantidad e nodos hihos dentro del árbol
print(prueba.count_sheets(prueba.raiz))
