datos = [
    10,
    20,
    [
        30,
        40,
        [50, 60, 70]
    ]
]

for elemento in datos:
    if isinstance(elemento, list):
        for valor in elemento:
            if isinstance(valor, list):
                for valor_2 in valor:
                    print(valor_2)
            else:
                print(valor)
    else:
        print(elemento)