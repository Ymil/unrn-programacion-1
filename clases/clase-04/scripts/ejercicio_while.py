opcion = ""
total = 0
print("Seleccione la comida para llevar")

while opcion != "terminar pedido":
    opcion = input("Escribi la comida que quieras agregar al pedido: ").lower()

    if opcion == "pizza":
        total += 25 # Opcion 1
        # total = total + 25 # Opcion 2
        print("Excelente! Agregamos la pizza a tu pedido")
    elif opcion == "terminar pedido":
        print("Cerrando pedido")
    else:
        print(f"Lo siento, no tenemos {opcion}, prueba con otra cosa")

print(f"Pedido finalizado, el total es {total}$, gracias por confiar en nosotros")