def sumar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total
# def sumar_lista(lista):
#     if len(lista) == 0:
#         return 0

#     numero = lista[0]
#     numeros_por_sumar = lista[1:] 
#     # print(f"Sumando {numero} + {numeros_por_sumar}")
    
#     resultado = numero + sumar_lista(numeros_por_sumar)

#     # print(f"{resultado}")
#     print(f"Sumando {numero} + {numeros_por_sumar}: {resultado}")

#     return resultado
#     # -> 5 + sumar_lista([10, 15, 30])
#     # -> 10 + sumar_lista([15, 30])
#     # -> 15 + sumar_lista([30])
#     # -> 30 + sumar_lista([])
#     # -> 30 + 0
#     # -> 15 + 30
#     # -> 10 + 45
#     # -> 5 + 55
#     # -> 60

print(sumar_lista([5, 10, 15, 30, 100]))
print(sumar_lista([5, 10, 15, 30, 100]) == sum([5, 10, 15, 30, 100]))