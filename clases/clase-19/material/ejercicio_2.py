from datetime import datetime

fecha_str = "2026-09-15T18:25:30"
print(type(fecha_str))
# fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S")
fecha = datetime(2026, 9, 15, 18, 25, 30)
print(type(fecha))
print(fecha)
fecha_salida = fecha.strftime("%d/%m/%Y %H:%M")
print(type(fecha_salida))
print(fecha_salida)