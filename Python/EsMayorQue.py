"""
Desarrollar un metodo recursivo que calcule el producto de los elementos del array v
mayores que el entero b

v = Lista de Datos Enteros
b = entero

El metodo creado habra de devolver un valor entero.

for x in range(0, len(v):
    if v[x] > b:


"""
def ProductodeMayores(v, b):
    resultado = 1
    for x in v:
        if x > b:
            resultado = resultado * x
    return resultado

def MetodoRecursivo(v, b):
    if len(v) == 0:
        return 1
    else:
        if v[0] > b:
            return v[0]*MetodoRecursivo(v[1:],b)
        else:
            return MetodoRecursivo(v[1:],b)
if __name__ == "__main__":
    print(ProductodeMayores([3,18,15,32,9,7,12],2))
    print(MetodoRecursivo([3,18,15,32,9,7,12],2))