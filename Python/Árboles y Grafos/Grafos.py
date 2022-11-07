import networkx as nx
import matplotlib.pyplot as plt


class Grafo:

    def __init__(self):
        self.G = nx.DiGraph()
        self.vertices = []

    def add_vertice(self, v):
        """Agrega un nuevo vertice al nodo"""
        if v in self.vertices:
            print(f"El vertice {v} ya se encuentra dentro del nodo")
            return self.add_vertice(input("Ingresa un nuevo nodo"))

        self.vertices.append(v)
        self.G.add_node(v)

    def add_arista(self, a, b, p):
        """Agrega una arista ponderada en p entre dos ejes a, b"""
        if (a and b) not in self.vertices:
            return "Uno o ambos nodos no existen en el grafo"

        self.G.add_edge(a, b, weight=p)

    def dijkstra(self, salida):
        """Realiza el recorrido de dijkstra hacia todos los otros vertices desde la el vertice(salida)"""
        if salida not in self.vertices:
            return False
        list(self.G)
        for i in list(self.G):
            if i == salida:
                continue
            print(f"Desde el vertice {salida} hacia el vertice {i}")
            camino = nx.dijkstra_path(self.G, source=salida, target=i, weight=True)
            print(camino)

    def imprimir_grafo(self):
        """Imprime el grafo"""
        # Se coloca el orden que llevarán los nodos del grafo
        pos = nx.layout.spectral_layout(self.G)

        # Llamamos al metodo de dibujo del grafo para agregar el valor de los nodos
        nx.draw_networkx(self.G, pos)

        # Le damos la propiedad a los ejes para mostrar su peso
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

        # Mostramos el grafo
        plt.title("Grafo Creado con Networkx")
        plt.show()
