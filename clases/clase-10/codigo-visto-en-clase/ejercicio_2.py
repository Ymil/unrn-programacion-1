# Ejercicio 2: Crear el archivo productos.csv y escribir 5 lineas
# el siguiente formato: nombre_producto; precio_producto; stock;
# Leer el archivo desde nuestro programa y crear un diccionario con todos los productos.
# Mostrar en pantalla ordenadamente.
import json
archivo = open("productos.csv", "r")

productos = {}

for linea in archivo.readlines():
    nombre_producto, precio_producto, stock = linea.strip().split(";")
    productos[nombre_producto] = {
        "precio_producto": precio_producto,
        "stock": stock
    }

for producto, datos in productos.items():
    # print(producto)
    # print(datos)
    print(f"{producto} - Precio: {datos["precio_producto"]} - Stock: {datos["stock"]}")

archivo.close()

print(json.dumps(productos, indent=2))