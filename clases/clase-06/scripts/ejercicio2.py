# nums = [1,100,300,1000]

# suma = 0
# for i in nums:
#     # suma += i
#     suma = suma + i

# canti = len(nums) # Cantidad de elementos de la lista
# print(f"La suma de todos es {suma}")
# print(f"Hay {canti} numeros")
# print(f"El promedio es {suma/canti}")

# Mi codigo
nums = [1,100,300,1000]

suma_total = 0

for numero in nums:
    suma_total  = suma_total + numero

print(suma_total)

cantidad_de_numeros = len(nums)

promedio = suma_total / cantidad_de_numeros

print(f" La suma total es de : {suma_total}, la cantidad de numeros son {cantidad_de_numeros} y el promedio de esto es{promedio} ")
