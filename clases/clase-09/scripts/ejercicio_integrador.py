
alumnos = [
    {
        "nombre": "Joaquin",
        "notas": [8, 5, 7],
        "materias": { "Programación", "Matemática"}
    },
    {
        "nombre": "Juan",
        "notas": [4, 3, 2],
        "materias": { "Programación" }
    },
    {
        "nombre": "Lucia",
        "notas": [6, 8, 9],
        "materias": {"Programación", "Inglés"}
    }
]
print("-"*25)

alumnos[0]["materias"].add("Laboratorio")
print(alumnos[0])

print("-"*25)

for alumno in alumnos:
    if "Matemática" in alumno["materias"]:
        print(alumno["nombre"], " cursa matematica")

print("-"*25)

for alumno in alumnos:
    print(alumno["nombre"])

print("-"*25)


for alumno in alumnos:
    suma_notas = sum(alumno["notas"])
    cantidad_notas = len(alumno["notas"])
    promedio = suma_notas / cantidad_notas

    if promedio >= 4:
        print(alumno["nombre"], " Aprobo ", promedio)

# for alumno in alumnos:
#     suma_notas = 0
#     cantidad_notas = 0

#     for nota in alumno["notas"]:
#         suma_notas += nota
#         cantidad_notas += 1
    
#     promedio = suma_notas / cantidad_notas

#     if promedio >= 4:
#         print(alumno["nombre"], " Aprobo ", promedio)