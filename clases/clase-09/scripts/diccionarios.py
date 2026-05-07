## Ejercicio 03

producto = {
    "nombre": "Birome",
    "precio": 1500,
    "stock": 100
}

# print(producto)

producto["precio"] *= 1.1
# producto["precio"] = producto["precio"] * 1.1
# print(producto)

# producto["stock"] = producto["stock"] - 1
producto["stock"] -= 1
# print(producto)

# print("Producto: ", producto["nombre"]," - Precio actualizado: ", producto["precio"] ," - Stock: ",producto["stock"])
print(f"Producto: {producto["nombre"]} - Precio actualizado: {producto["precio"]} - Stock: {producto["stock"]}")

## Ejercicio 04


cuenta = {
    "usuario": "LautaroLinquiman",
    "email": "LautaroLinquiman@unrn.com.ar",
    "activo": True 
}

print(cuenta["email"])
print(cuenta)
cuenta["activo"] = False
print(cuenta)
cuenta["ultimo_login"] = (6, 5, 2026)
cuenta["ultimo_login"]
print(cuenta)