VACIO = "-"
JUGADOR_1 = "X"
JUGADOR_2 = "O"

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

turno_jugador = JUGADOR_1

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("----------")

def obtener_posicion():
    # Logica para solicitar datos al usuario (del 1 al 3)
    # Consejo: restar 1 aquí adentro para trabajar con índices 0, 1, 2
    fila = int(input("Ingresa la fila [1-3]: ")) - 1
    columna = int(input("Ingresa la columna [1-3]: ")) - 1
    return fila, columna

def validar_posicion_invalida(tablero, fila, columna):
    if (0 <= fila < 3) == False:
        return True
    
    if (0 <= columna < 3) == False:
        return True
    
    if tablero[fila][columna] != VACIO:
        return True
    return False

def asignar_posicion(tablero, fila, columna, jugador):
    # Logica para asignar un jugador a una posición
    tablero[fila][columna] = jugador

def cambiar_turno(turno_jugador):
    # Logica para cambiar de turno
    if turno_jugador == JUGADOR_1:
        return JUGADOR_2
    return JUGADOR_1

def buscar_ganador(tablero):
    # Devuelve True si un jugador completó una línea, False si no
    for idx in range(3):
        if tablero[idx][0] == tablero[idx][1] == tablero[idx][2] != VACIO:
            return True
        elif tablero[0][idx] == tablero[1][idx] == tablero[2][idx] != VACIO:
            return True
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != VACIO:
        return True
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != VACIO:
        return True

    
imprimir_tablero(tablero) # Mostrar tablero vacío al principio

while True:
    fila, columna = obtener_posicion()

    if validar_posicion_invalida(tablero, fila, columna):
        print("Posición inválida o ya ocupada. Vuelva a elegir.")
        continue
    
    asignar_posicion(tablero, fila, columna, turno_jugador)
    imprimir_tablero(tablero)

    if buscar_ganador(tablero):
        print(f"¡Ganó el JUGADOR {turno_jugador}!")
        break
        
    turno_jugador = cambiar_turno(turno_jugador)