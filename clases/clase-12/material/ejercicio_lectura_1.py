# Solicitar al usuario su nombre
# Verificar su que el nombre tiene más de 3 caracteres, 
#   si no verifica, finalizar el programa.
# Solicitar al usuario tres numeros
# Verificar que cada dato ingreso es numerico
#   Si no verifica finalizar el programa
# Sumar todos los numeros e imprimir

nombre = input("").strip()

if len(nombre) < 4:
    print("ERROR FATAL: el nombre tiene que tener más de 3 caracteres")
    print(f"Se ingresaron solo {len(nombre)} caracteres")
    exit(1)

total_ingresado = 0
for n in range(0,3):
    numero = input("").strip()
    if numero.isnumeric() == False:
        print(f"ERROR FATAL: '{numero}' no es un numero")
        exit(1)

    total_ingresado += int(numero)
        
print(f"Suma total de ingresados: {total_ingresado}")