entrada = input("Ingresar producto y precio separado por ';': ")

try:
    producto, precio = entrada.split(";")
except ValueError:
    print("Producto y precio invalido, ingresar con " \
    "el siguiente formato: 'Producto;1200'")

    exit(1)

# producto = datos[0]
# precio = datos[1]
try:
    precio_f = float(precio)
    print(f"{producto} cuesta {precio_f}$")
except ValueError:
    print("Se ingreso un precio invalido, " \
    "ingrese valores numericos")

