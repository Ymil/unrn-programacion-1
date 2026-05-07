# def operaciones(a, b):
#     return (a + b, a - b)

# suma, resta = operaciones(1, 2)
# print(suma)
# print(resta)

# resultado = operaciones(1, 2)
# suma = resultado[0]
# resta = resultado[1]
# print(suma)
# print(resta)

# print("________________")

# def operacion_b(a, b):
#     return ( a + b, a - b, a / b)

# suma, resta, division = operacion_b(1, 2)
# print(suma)
# print(resta)
# print(division)

# resultado = operacion_b(1, 2)
# print(resultado)

def datos_persona(nombre, edad):
    mayor_edad = False
    if edad >= 18:
        mayor_edad = True
    return (nombre, edad, mayor_edad)

resultado = datos_persona("Eustacio", 17)
print(resultado)
nombre, edad, es_mayor_edad = datos_persona("Eustacio", 18)
print(nombre, edad, es_mayor_edad)