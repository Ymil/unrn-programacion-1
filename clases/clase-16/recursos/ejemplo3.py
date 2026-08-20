import json

with open("producto.json", "r") as archivo:
    datos = json.load(archivo)

datos["nombre"] = "Coca Cola"
print(datos)

# with open("nuevo_producto.json", "w") as archivo: 
archivo = open("nuevo_producto.json", "w")
json.dump(datos, archivo)
archivo.close()