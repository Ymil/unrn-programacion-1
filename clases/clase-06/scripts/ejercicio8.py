suma_t = 0
canti = 0
while True:
    numero = input("Escribe un numero o ingrese 0 para terminar: ")
    if int(numero) != 0:
        suma_t = suma_t + int(numero)
        canti += 1
    else:
        break
print(suma_t)
print(canti)
print(suma_t/canti)

# ejercicio 12
pedido = ["banana"]
print(pedido)
producto = input("Ingresar producto> ")

if producto in pedido:
    print("Producto ya se encuentra en la lista")
else:
    pedido.append(producto)
print(pedido)


