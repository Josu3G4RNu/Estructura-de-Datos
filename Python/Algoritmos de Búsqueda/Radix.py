# Radix sort in Python


# Esta función es la encargada de ordenar la lista en base a la cantidad de unidades, decenas, etc.
def countingsort(array, place):
    size = len(array) # Almacena la longitud del arreglo de números
    output = [0] * size # Se crea una lista para el ordenar los números sin afectar a la original
    count = [0] * 10 # Almacena la cantidad de unidades, decenas, centenas, etc.

    # Se utiliza para contar las unidades, decenas, centenas, etc.
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Suma acumulativa de unidades, decenas, centenas, etc.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Ordenación de los elementos
    i = size - 1 # Comenzando por el último digito
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    # Reorganiza la lista original
    for i in range(0, size):
        array[i] = output[i]


# Función principal para implementar el método Radix
def radixsort(array):
    # Obtiene el valor máximo dentro de la lista
    max_element = max(array)

    # Comenzamos evaluando desde las unidades, por ello place vale 1.
    place = 1

    # Nota: // significa división entera.

    while max_element // place > 0:
        countingsort(array, place)
        place *= 10  # Esto permite la evaluación a decenas, centenas, etc.


if __name__ == "__main__":

    data = [121, 432, 564, 23, 1, 45, 788]
    radixsort(data)
    print(data)
