productos = ["papa" , "manzana", "zanahoria"]

largo = 0
for i in productos:
    largo += 1

print(f"La lista tiene {largo} elementos")
print(f"El primer elemento es {productos[0]}")
print(f"El ultimo elemento es {productos[largo-1]}")