alumnos = [
    {"nombre": "Paula", "nota": 8},
    {"nombre": "Juan", "nota": 3},
    {"nombre": "Pedro", "nota": 6},
]


for alumno in alumnos:
    print(alumno["nombre"])


import json

print(json.dumps(alumnos, indent=2))