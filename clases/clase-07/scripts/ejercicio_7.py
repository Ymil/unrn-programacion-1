
# EJERCICIO 7:

# Crear una función que:
#     Reciba una lista de números
#     Devuelva una lista con el número mayor y cuántas veces aparece.
#         Ejemplo: [NumeroMayor, Repeticion] = [6, 10]
#     No usar max() ni count()

# Llamar a la función con la siguiente lista:
# numeros = [4, 9, 1, 9, 3]

# Pistas:

#     Usar for
#     Usar IFs
#     Crear variables contadoras

def obtener_numero_mayor_con_repeticion(lista_entrada):
    numero_mayor = lista_entrada[0]
    repeticion = 0
    
    for numero in lista_entrada:
        if numero_mayor < numero:
            numero_mayor = numero
    
    for numero in lista_entrada:
        if numero == numero_mayor:
            repeticion += 1
    
    return [numero_mayor, repeticion]

numeros = [4, 9, 1, 9, 3, 10, 10, 10, 100]

print(obtener_numero_mayor_con_repeticion(numeros))