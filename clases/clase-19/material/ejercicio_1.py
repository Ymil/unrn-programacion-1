from datetime import datetime

fechas = [
    "21-08-2026 18:45:20",
    "2026/08/21 07:30",
    "21.08.26",
]

print(datetime.strptime(fechas[0], "%d-%m-%Y %H:%M:%S"))
print(datetime.strptime(fechas[1], "%Y/%m/%d %H:%M"))
print(datetime.strptime(fechas[2], "%d.%m.%y"))