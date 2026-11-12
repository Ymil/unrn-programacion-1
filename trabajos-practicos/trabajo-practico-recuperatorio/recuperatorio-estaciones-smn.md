# Recuperatorio de los Trabajos Integradores

## Estaciones del SMN

En este trabajo van a construir un programa de línea de comandos que lee las observaciones de un día de las estaciones del Servicio Meteorológico Nacional, representa cada observación con un objeto y resume las temperaturas de una estación.

El trabajo es individual.

**Entrega: miércoles 18/11/2026.**

## Organización requerida

```text
recuperatorio-smn/
├── README.md
├── requirements.txt        pytest
├── observacion.py          clase Observacion
├── consultar_clima.py      funciones de carga, filtrado y resumen
├── main.py                 programa principal
├── test_observacion.py     un caso válido y uno inválido
└── observaciones.json      provisto
```

El programa usa la biblioteca estándar de Python. Para las pruebas se usa `pytest`, que debe incluirse en `requirements.txt`.

## Formato de entrada

Se usa el archivo provisto [`observaciones.json`](./observaciones.json), que deben copiar en la raíz de su repositorio, junto a los archivos `.py`. Tiene las observaciones horarias del 24/08/2026 de 118 estaciones del SMN.

El archivo es una lista de diccionarios, uno por observación:

```json
{"estacion": "AEROPARQUE AERO", "fecha": "2026-08-24", "hora": 0, "temperatura": 8.0, "humedad": 70, "presion": 1027.7, "direccion_viento": 80, "velocidad_viento": 13}
```

| Campo | Contenido |
|---|---|
| `estacion` | nombre de la estación |
| `fecha` | fecha de la observación |
| `hora` | hora de la observación |
| `temperatura` | temperatura en °C |
| `humedad` | humedad relativa en % |
| `presion` | presión en hPa |
| `direccion_viento` | dirección del viento en grados |
| `velocidad_viento` | velocidad del viento en km/h |

Cuando una estación no informó un valor, el campo viene en `null`. El archivo tiene registros con errores que el programa tiene que descartar.

## Requerimientos

1. Diseñar una clase `Observacion` en `observacion.py`.
    1. La clase guarda la estación, la hora, la temperatura, la humedad y la velocidad del viento.
    2. La clase debe verificar que los datos sean correctos:
        1. La estación no puede estar vacía.
        2. La hora debe estar entre 0 y 23.
        3. La temperatura, la humedad y la velocidad del viento no pueden faltar.
        4. La humedad debe estar entre 0 y 100.
        5. La velocidad del viento no puede ser negativa.

        Si un dato no cumple estas reglas, la clase debe rechazarlo con `ValueError`.

    3. La clase debe tener métodos con los siguientes comportamientos:
        1. Recibir el nombre de una estación y devolver `True` si la observación es de esa estación y `False` si no.
        2. Devolver la intensidad del viento según su velocidad:

            | Intensidad | Velocidad |
            |---|---|
            | `calma` | menor a 2 km/h |
            | `leve` | desde 2 y menor a 20 km/h |
            | `moderado` | desde 20 y menor a 40 km/h |
            | `fuerte` | 40 km/h o más |

        3. Devolver una cadena con la estación, la hora, la temperatura con un decimal, la humedad, la velocidad del viento y su intensidad. Por ejemplo: `AEROPARQUE AERO | 22 h | 10.0 °C | 73 % | 20 km/h (moderado)`.
2. Crear en `consultar_clima.py` funciones con los siguientes comportamientos:
    - Recibir la ruta del archivo JSON, leerlo y devolver una lista de objetos `Observacion`. Si un registro no cumple las validaciones de la clase, se descarta y el programa sigue con el siguiente.
    - Una función que devuelva sólo las observaciones de una estación. Para decidir si una observación es de la estación, usar el método de la clase.
    - Una función que calcule y devuelva un diccionario con la cantidad de observaciones (`"cantidad"`), la observación con la temperatura mínima (`"minima"`), la observación con la temperatura máxima (`"maxima"`) y el promedio de temperatura (`"promedio"`). Devuelve observaciones y no sólo temperaturas, para poder mostrar a qué hora ocurrió cada una. Si la mínima o la máxima se repite, se toma la primera en el orden del archivo. No se pueden usar `max`, `min`, `sum` ni `sorted`.
3. Copiar el programa principal provisto en `main.py` y completarlo usando las funciones de `consultar_clima.py`, como se indica en esa sección. Pueden ajustar el formato de los mensajes, manteniendo la información que se muestra.
4. Escribir dos pruebas con `pytest` en `test_observacion.py`:
    - Un caso válido: crear una instancia de `Observacion` y comprobar que sus atributos conservan los datos recibidos.
    - Un caso inválido: elegir una regla de validación y comprobar que el constructor produce `ValueError` cuando no se cumple. Los demás datos del caso deben ser válidos.

    Las dos pruebas deben pasar. No se pide cobertura mínima ni pruebas de carga, filtrado, resumen o programa principal.
5. Escribir un `README.md` con su nombre y cómo preparar el entorno, ejecutar el programa y ejecutar las pruebas.

## Programa principal provisto

Este código va en `main.py`.  Hay que completar las llamadas a funciones y el acceso a los objetos:

- Cada comentario `# Función de ...` se reemplaza por la llamada a la función correspondiente de `consultar_clima` y la asignación de su resultado.
- Cada `REEMPLAZAME` se reemplaza por el atributo o el método de la clase que corresponde.

Se evaluará con el archivo provisto y estaciones que tengan observaciones válidas. No hace falta resolver el caso de una consulta sin observaciones.

```python
import sys
import consultar_clima


def main():
    ruta = sys.argv[1]
    estacion = sys.argv[2]

    # Función de carga de observaciones.
    print(f"Observaciones válidas: {len(observaciones)}")
    print()

    # Función de filtrado por estación.
    # Función de resumen de temperaturas.
    minima = resumen["minima"]
    maxima = resumen["maxima"]

    print(estacion)
    print(f"Observaciones: {resumen['cantidad']}")
    # REEMPLAZAME: temperatura y hora de la observación mínima y de la máxima.
    print(f"Temperatura mínima: {REEMPLAZAME} °C a las {REEMPLAZAME} h")
    print(f"Temperatura máxima: {REEMPLAZAME} °C a las {REEMPLAZAME} h")
    print(f"Temperatura promedio: {resumen['promedio']} °C")
    print()
    for observacion in de_la_estacion:
        # REEMPLAZAME: descripción de la observación.
        print(REEMPLAZAME)


main()
```

## Salida esperada

Con la estación `AEROPARQUE AERO`:

```bash
python main.py observaciones.json "AEROPARQUE AERO"
```

```text
Observaciones válidas: 1812

AEROPARQUE AERO
Observaciones: 24
Temperatura mínima: 7.6 °C a las 7 h
Temperatura máxima: 10.7 °C a las 11 h
Temperatura promedio: 9.399999999999999 °C

AEROPARQUE AERO | 0 h | 8.0 °C | 70 % | 13 km/h (leve)
AEROPARQUE AERO | 1 h | 8.6 °C | 66 % | 11 km/h (leve)
AEROPARQUE AERO | 2 h | 8.0 °C | 69 % | 13 km/h (leve)
AEROPARQUE AERO | 3 h | 8.2 °C | 68 % | 13 km/h (leve)
AEROPARQUE AERO | 4 h | 8.1 °C | 69 % | 9 km/h (leve)
AEROPARQUE AERO | 5 h | 8.7 °C | 64 % | 7 km/h (leve)
AEROPARQUE AERO | 6 h | 8.3 °C | 69 % | 7 km/h (leve)
AEROPARQUE AERO | 7 h | 7.6 °C | 75 % | 9 km/h (leve)
AEROPARQUE AERO | 8 h | 8.0 °C | 73 % | 9 km/h (leve)
AEROPARQUE AERO | 9 h | 9.3 °C | 66 % | 9 km/h (leve)
AEROPARQUE AERO | 10 h | 9.7 °C | 67 % | 9 km/h (leve)
AEROPARQUE AERO | 11 h | 10.7 °C | 65 % | 13 km/h (leve)
AEROPARQUE AERO | 12 h | 10.6 °C | 64 % | 11 km/h (leve)
AEROPARQUE AERO | 13 h | 10.4 °C | 66 % | 9 km/h (leve)
AEROPARQUE AERO | 14 h | 10.6 °C | 62 % | 11 km/h (leve)
AEROPARQUE AERO | 15 h | 10.5 °C | 62 % | 11 km/h (leve)
AEROPARQUE AERO | 16 h | 10.6 °C | 64 % | 15 km/h (leve)
AEROPARQUE AERO | 17 h | 10.5 °C | 64 % | 17 km/h (leve)
AEROPARQUE AERO | 18 h | 10.1 °C | 68 % | 15 km/h (leve)
AEROPARQUE AERO | 19 h | 9.7 °C | 68 % | 15 km/h (leve)
AEROPARQUE AERO | 20 h | 9.8 °C | 70 % | 17 km/h (leve)
AEROPARQUE AERO | 21 h | 9.9 °C | 72 % | 19 km/h (leve)
AEROPARQUE AERO | 22 h | 10.0 °C | 73 % | 20 km/h (moderado)
AEROPARQUE AERO | 23 h | 9.7 °C | 74 % | 22 km/h (moderado)
```

Los resultados deben coincidir con los del ejemplo. El formato de los mensajes puede variar.

## Prolijidad de la entrega

La entrega debe estar ordenada: archivos con nombres claros, sin archivos duplicados o que no se usen. El repositorio no incluye `.venv/`, `__pycache__/` ni `.pytest_cache/`.

## Clases relevantes

- [Clase 6 - Ejercicios de repaso](../../clases/clase-06/): máximos, mínimos y promedios sin funciones de Python.
- [Clase 9 - Archivos, tuplas y diccionarios](../../clases/clase-09/): recorrido de listas de diccionarios.
- [Clase 15 - Terminal y argumentos](../../clases/clase-15/): uso y validación de `sys.argv`.
- [Clase 16 - JSON en Python](../../clases/clase-16/): lectura del archivo de entrada.
- [Clase 17 - Manejo básico de excepciones](../../clases/clase-17/): descartar registros inválidos sin detener el programa.
- [Clase 25 - Testing básico con `pytest`](../../clases/clase-25/material/clase-25.md): pruebas con datos válidos e inválidos.
- [Clase 26 - Introducción a la POO](../../clases/clase-26/material/clase-26.md): clases, instancias, atributos y métodos.
- [Clase 29 - Debugging en VS Code](../../clases/clase-29/material/clase-29.md): seguir la ejecución cuando un valor no coincide.
