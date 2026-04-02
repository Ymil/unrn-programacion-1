salir = True
i = 0
while salir:
    print(f"Estoy al principio de la iteración: {i}")
    i += 1
    if input("Ir a la proxima iteracion? [si/no]") == "si":
        # salir = False
        # break
        continue
    if input("Desea salir? [si/no]") == "si":
        # salir = False
        # break
        exit()
    print(f"Estoy al final de la iteración: {i-1}")
print("Adios")