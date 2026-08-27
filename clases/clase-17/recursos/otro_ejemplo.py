texto = input("Temperatura: ")
temperatura = None

try:
    temperatura = float(texto)
    print("Temperatura registrada:", temperatura)
except ValueError as error:
    print("ERROR", error)
    if str("not convert" in str(error)):
        print("Valor ingresado no es FLOAT")
    exit(1)

print("El programa sigue", temperatura * 10)