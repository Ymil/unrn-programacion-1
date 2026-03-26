lista_de_comidas = ["pizza", "empanada", "hamburguesa"]

for indice in range(len(lista_de_comidas)):
    print(f"{indice+1}: {lista_de_comidas[indice]}")

indice = 0
while indice < len(lista_de_comidas):
    print(indice, lista_de_comidas[indice])
    indice += 1

while True:
    indice_seleccionado = int(input("Elegi la comida"))
    if indice_seleccionado < len(lista_de_comidas):
        comida = lista_de_comidas[indice_seleccionado]
        print(f"Elegiste el indice {indice_seleccionado}: {comida}")
    else:
        print("elegiste una comida invalida")