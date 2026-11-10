def total_compra(compra):
    total = 0
    descuento = 0
    for nombre in compra:
        precio, cantidad = compra[nombre]
        if cantidad >= 6:
            descuento = 0.15
        elif cantidad >= 3:
            descuento = 0.10
        subtotal = precio * cantidad
        total += subtotal * (1 - descuento)
    return total


compra = {
    "Yerba": (4200, 1),
    "Alfajores": (900, 6),
    "Leche": (1500, 2),
    "Galletitas": (1100, 3),
    "Queso cremoso": (6000, 1),
}
print(total_compra(compra))
