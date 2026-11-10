def limpiar(lecturas):
    for i, valor in enumerate(lecturas):
        if valor == -999:
            lecturas.pop(i)
    return lecturas


def promedio(lecturas):
    validas = limpiar(lecturas)
    suma = 0
    for valor in validas:
        suma += valor
    return suma / len(validas)


temperaturas = [18.5, -999, -999,
                21.0, 19.5, 23.0]
print(promedio(temperaturas))
