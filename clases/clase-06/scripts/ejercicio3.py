# A partir de una lista de numeros
# Obtener el maximo y el minimo
# Utilizando el bucle FOR
# y NO UTILIZAR MAX y MIN.

# nums = [1, 2, 3]
# maximo = 0
# minimo = 0

# for num in nums:
#     if : # Verificar si el numero de 
#         # entrada es mayor que maximo
#         maximo = num
#     elif : # Verificar si el numero de 
#         # entrada es menor que el minimo
#         minimo = num
#     print(num)

# x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]

# max = 0
# min = 0
# for i in x :
#     if i > max :
#         max = i
#     elif i < min :
#         min = i

# print(f'El numero maximo es: {max}')
# print(f'El numero minimo es: {min}')


x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10, 100, -100]
maximo = 0
minimo = 0
for num in x:
    if num > maximo:
       maximo = num
    # else:
    #    maximo = maximo
 
print(maximo)
for num in x:
    if num < minimo:
        minimo = num
    # else:
    #     minimo = minimo

print(minimo)