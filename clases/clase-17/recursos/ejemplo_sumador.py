def sumador(anterior, siguiente):
    if siguiente < anterior:
        raise ValueError(f"El numero siguiente no puede ser más chico que el anterior")
    else:
        return siguiente + anterior

anterior_n = 0
while True:
    print(f"El numero anterior es {anterior_n}")
    try:
        siguiente_n = int(input("Ingrese el siguiente numero> "))
    except:
        pass

    try:
        sumador(anterior_n, siguiente_n)
        anterior_n = siguiente_n
    # ValueError: invalid literal for int() with base 10
    # ValueError: El numero siguiente no puede ser más chico que el anterior
    except ValueError as error:
        if "invalid literal" in str(error):
            print("Int invalido")
        elif "El numero siguiente" in str(error):
            print("numero invalido")
        print(f"[ERROR] '{error}', reintentar")