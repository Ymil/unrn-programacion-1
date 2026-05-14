# Ejercicio 1: Crear el archivo nombres.txt y escribir 5 nombres, uno en cada linea.
# Leer el archivo desde nuestro programa y crear una lista con los 5 nombres 
# e imprimir en pantalla mostrando su índice.

archivo = open("nombres.txt", "r")
lista_de_nombres = archivo.readlines()
archivo.close()

idx = 0
for nombre in lista_de_nombres:
    print(idx, nombre.strip())
    idx += 1

print("------")

for idx, nombre in enumerate(lista_de_nombres):
    print(idx, nombre.strip())
