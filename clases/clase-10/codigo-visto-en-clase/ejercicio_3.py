# Ejercicio 3: Crear un programa que solicite 5 nombres al usuario.
# Luego escribir los 5 nombres en un archivo de texto, cada nombre en una línea.

# lista_de_nombre = []
# for num in range(5):
#     nombre = input(f"Ingresar el nombre N{num}: ")
#     lista_de_nombre.append(nombre)

# archivo = open("ej3_archivo.txt", "w")
# archivo.write("\n".join(lista_de_nombre))
# archivo.close()

archivo = open("ej3_archivo.txt", "w")
for num in range(5):
    nombre = input(f"Ingresar el nombre N{num}: ")
    archivo.write(f"{nombre}\n")
    # if num != 4:
    #     archivo.write("\n")