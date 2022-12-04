class Hash:

    def __init__(self, numeros: list):
        self.numeros = numeros  # Todos los números comienzan con 1  <- Patron

    @staticmethod
    def __print_listahash(lista_hash, numero_a_buscar):

        try:
            i = lista_hash.index(numero_a_buscar)
        except ValueError:

            return print(f'El número no existe dentro del array || {lista_hash}')
        else:
            return print(f'El número se encuentra en en la posición {i} \n {lista_hash}')

    def funcion_identidad(self, numero_a_buscar: int):
        """
        Almacena la clave k en una lista con index(k)
        Trabaja únicamente con números inferiores o iguales a 100.
        """
        lista_hash = []

        for n in self.numeros:
            if n > 100:
                return print("Números demasiado Grandes")
            lista_hash.insert(n,n)

        self.__print_listahash(lista_hash, numero_a_buscar)

    def funcion_resta(self, numero_a_buscar):
        """
        Dada una clave númerica k, se define un patron inicial, y el resto de los números representan
        el indice de la clave
        """
        mayor = str(max(self.numeros)+1)
        lista_hash = [0 for x in range(0, int(mayor[1:]))]

        for n in self.numeros:
            n = str(n)
            i = int(n[1:])
            lista_hash[i] = int(n)

        self.__print_listahash(lista_hash, numero_a_buscar)

    def funcion_modular(self, numero_a_buscar):
        """
        Esta función toma el residuo de la división la clave (k) sobre el número de elementos del arreglo (N - 1)
        Es decir:
        i = (k mod (N-1))
        Guarda el valor de una clave númerica k en un índice dado por i = (k mod (N-1))
        """
        mayor = str(max(self.numeros)+1)
        lista_hash = [0 for x in range(0, int(mayor[1:]))]

        for n in self.numeros:
            i = n % (len(lista_hash)-2)
            lista_hash[i] = n

        self.__print_listahash(lista_hash, numero_a_buscar)
