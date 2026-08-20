import json

producto = {
    "nombre": "Coca",
    "precio": 950,
    "stock": 9,
    "ventas": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "tipo": "Bebida",
    "tamano": "chico"
}

with open("producto.json", "w") as archivo:
    json.dump(producto, archivo, indent=4)