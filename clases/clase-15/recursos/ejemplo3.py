import sys
import os

archivo = sys.argv[1]
if os.path.exists(archivo) == False:
    print("Error no existe el archivo ingresado ")
    exit(1)
with open(archivo, "r") as datos:
    contenido = datos.read()
print(contenido)