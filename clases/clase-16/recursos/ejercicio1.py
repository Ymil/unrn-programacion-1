import json

archivo = open("guardia_house.json", "r")
datos = json.load(archivo)
archivo.close()

# print(datos)
print(f"Guardia: {datos["guardia"]}")

# print(datos["pacientes"])
# print(type(datos["pacientes"]))

for paciente in datos["pacientes"]:
    # print(paciente)
    # print(type(paciente))
    # print(paciente.keys())
    # print(paciente["prioridad"])
    if paciente["prioridad"] == "alta":
        print(f"Paciente: {paciente["nombre"]}")
