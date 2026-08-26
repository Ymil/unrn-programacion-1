import sys

# if len(sys.argv) == 3:
#     ruta_archivo = sys.argv[1]
#     if sys.argv[2].isdigit():
#         posicion = int(sys.argv[2])
#     else:
#         print("Posicion invalida")
# else:
#     print("Cantidad de argumentos no esperada")
# print(ruta_archivo, posicion)
# exit()

try:
    ruta_archivo = sys.argv[1]
    # ruta_archivo = input()
    posicion = int(sys.argv[2]) - 1
    # posicion = input()
except ValueError:
    print("[ERROR] Posicion ingresada invalida, se esperaba un numero")
except IndexError:
    print("[ERROR]Se esperaban dos parametros: archivo posicion")
