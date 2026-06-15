# Guía breve de repaso

La idea es que puedan usar estos ejercicios para revisar si entienden los temas principales y detectar qué necesitan volver a mirar.

Intenten pensar primero la solución sin ejecutar Python. Después, si quieren, pueden probar el código para verificar.

## Material útil para repasar

* [Clase 9 - Tuplas, conjuntos, diccionarios y estructuras combinadas](https://github.com/Ymil/unrn-programacion-1/tree/main/clases/clase-09)
* [Clase 10 - Archivos](https://github.com/Ymil/unrn-programacion-1/tree/main/clases/clase-10)
* [Clase 11 - Manipulación y validación de datos](https://github.com/Ymil/unrn-programacion-1/tree/main/clases/clase-11)
* [Clase 12 - Repaso e interpretación de consignas](https://github.com/Ymil/unrn-programacion-1/tree/main/clases/clase-12)

## Temas para mirar

Para el examen conviene repasar especialmente:

* diccionarios, tuplas y conjuntos;
* lectura y escritura de archivos;
* manipulación de strings con `split`, `strip`, `upper`, `lower`, `isnumeric`;
* validación de datos;
* recorridos con `for`;
* lectura de código.

---

## Ejercicio 1

Responder con sus palabras.

1. ¿Cuándo conviene usar una tupla?
2. ¿Cuándo conviene usar un conjunto?
3. ¿Cuándo conviene usar un diccionario?
4. ¿Por qué es importante validar un dato antes de convertirlo a número?
5. ¿Qué diferencia hay entre mostrar un resultado con `print` y devolverlo con `return`?

---

## Ejercicio 2

Sin ejecutar el código, explicar qué hace el programa.

```python
registros = [
    "sensor_a;18",
    "sensor_b;texto",
    "sensor_a;20",
    "sensor_c;15",
    "sensor_b;22"
]

mediciones = {}

for registro in registros:
    partes = registro.split(";")
    sensor = partes[0].strip()
    valor_texto = partes[1].strip()

    if valor_texto.isnumeric():
        valor = int(valor_texto)

        if sensor not in mediciones:
            mediciones[sensor] = []

        mediciones[sensor].append(valor)

print(mediciones)
```

Responder:

1. ¿Qué registros se cargan?
2. ¿Qué registro se ignora?
3. ¿Qué contiene el diccionario `mediciones` al finalizar?
4. ¿Qué imprime el programa?
5. ¿Para qué sirve el `isnumeric()` en este caso?

---

## Ejercicio 3

Tenemos la siguiente lista:

```python
eventos = [
    ("zona_a", "movimiento"),
    ("zona_b", "puerta"),
    ("zona_a", "puerta"),
    ("zona_c", "movimiento"),
    ("zona_b", "movimiento"),
    ("zona_a", "movimiento")
]
```

Cada tupla tiene el formato:

```text
(zona, tipo_evento)
```

2. Armar un diccionario donde la clave sea la zona y el valor sea la cantidad de eventos registrados en esa zona.
3. Armar un conjunto con los tipos de eventos que aparecieron.
4. Mostrar el diccionario final.
5. Mostrar el conjunto final.

---

## Ejercicio 4

A partir del siguiente archivo:

```text
homero;permitido
lisa;permitido
bart;denegado
maggie;permitido
flanders;error
```

Escribir un programa que:

1. Abra el archivo en modo lectura.
2. Lea las líneas del archivo.
3. Separe cada línea usando `split(";")`.
4. Cuente cuántos accesos fueron `permitido`.
5. Guarde en una lista los nombres con acceso permitido.
6. Ignore los estados que no sean `permitido` o `denegado`.
7. Muestre la cantidad de accesos permitidos y la lista final.
