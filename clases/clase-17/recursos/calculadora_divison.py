import modulo_division
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

# modulo_division.division(dividendo, divisor)
try:
    resultado = dividendo / divisor
    resultado * 10
except ZeroDivisionError:
    print("No se puede dividir por 0")
    exit(1)
