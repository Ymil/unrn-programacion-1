# A partir de la siguiente lista:
# numeros = [-1, 1, -2, -3, 7, 10]

# Mostrar:

#     Cuántos números son positivos
#     Cuántos son negativos
#     La suma total

numeros = [-1, 1, -2, -3, 7, 10]

numeros_positivos = []
numeros_negativos = []
suma_total = 0

for n in numeros:
    suma_total += n
    
    if n > 0:
        numeros_positivos.append(n)
    elif n < 0:
        numeros_negativos.append(n)

print("Positivos:", len(numeros_positivos))
print("Negativos:", len(numeros_negativos))
print("Suma total:", suma_total)
