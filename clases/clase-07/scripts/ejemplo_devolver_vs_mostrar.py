

def sumar_lista_devolver(lista_entrada): # DEVOLVER
    suma = 0
    for item in lista_entrada:
        suma += item
    return suma


def sumar_lista_mostrar(lista_entrada): # MOSTRAR
    suma = 0
    for item in lista_entrada:
        suma += item
    print(suma)

lista = [1, 2, 3]

resultado = sumar_lista_mostrar(lista)
print(resultado + 1) # FALLA