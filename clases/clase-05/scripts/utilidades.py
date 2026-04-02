def pedir_comida():
    comida = ""
    while comida == "":
        comida = input("Ingresa tu comida> ").lower()
    return comida

def obtener_precio(comida):
    precio = 0
    if comida == "hamburguesa":
        precio = 100
    elif comida == "milanesa":
        precio = 125
    elif comida == "pizza":
        precio = 150
    
    if precio > 0:
        print(f"Comida {comida} - Precio: {precio}$")
    else:
        print("No hay buscar en otro lado")
    
    return precio