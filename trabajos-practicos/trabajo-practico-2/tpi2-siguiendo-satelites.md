# Trabajo Práctico Integrador 2

## Proyecto completo

En este trabajo van a construir un programa de línea de comandos que lee un archivo con los satélites activos, obtiene la posición de cada uno, lo representa con un objeto y permite filtrar, ordenar y consultar esos satélites.

Para realizar este trabajo utilizaremos datos obtenidos del sitio CelesTrak el cual publica las órbitas de todos los satélites activos.

El trabajo es individual. Cada estudiante crea un repositorio nuevo en GitHub, e informa el enlace al docente antes de la primera entrega. El historial de commits tiene que mostrar el avance a lo largo de las dos etapas.

## Organización requerida

```text
tpi2-satelites/
├── README.md
├── requirements.txt
├── .gitignore
├── funciones_base.py          provisto
├── consultar_satelites.py     programa principal
├── satelite.py                clase Satelite
├── catalogo.py                carga del catálogo, resúmenes y zona
├── datos/
│   └── satelites.json         provisto
└── test_*.py                  pruebas de satelite.py y catalogo.py
```


## Etapa 1

Entrega: Viernes 30/10/2026

1. Diseñar una clase `Satelite` e implementarla en el archivo `satelite.py`.
    1. La misma debe guardar:
        - nombre
        - número de catálogo
        - latitud
        - longitud
        - altitud
    2. La clase debe verificar que los datos sean correctos.
        1. La latitud debe estar entre -90 y 90.
        2. La longitud debe estar entre -180 y 180.
        3. La altitud debe ser de al menos 100 km.
        4. El nombre no debe estar vacío.
        5. El número de catálogo debe ser un entero.
    3. La clase debe implementar métodos con los siguientes comportamientos:
        1. Devolver un texto con el tipo de órbita según la altitud:
            - `LEO` (órbita baja): Menor a 2.000 km
            - `MEO` (órbita media): Desde 2.000 km y menor a 34.000 km
            - `GEO` (geoestacionaria): Desde 34.000 km hasta 37.000 km inclusive
            - `HEO` (órbita alta): Mayor a 37.000 km
        2. Devolver una cadena con el nombre, el número de catálogo, el tipo de órbita y la altitud. Por ejemplo: `ISS (ZARYA) | 25544 | LEO | 419.7 km`.
        3. Devolver `True` si el satélite se encuentra dentro de una zona y `False` si no. La zona se define con cuatro argumentos, en este orden: longitud mínima, latitud mínima, longitud máxima y latitud máxima. El borde cuenta como adentro.
2. Crear funciones con los siguientes comportamientos en `catalogo.py`:
    - Leer el archivo JSON y devolver la lista de registros (diccionarios) tal como vienen en el archivo.
    - Crear el catálogo: recibir una lista de registros y devolver una lista de objetos `Satelite`. Para obtener la posición de cada satélite, usar `obtener_posicion` de `funciones_base.py`.
    - Resumir los satélites por tipo de órbita: cuántos hay de cada uno y el mínimo, máximo y promedio de altitud. La función devuelve los datos, por ejemplo un diccionario por tipo de órbita; el texto que se muestra lo arma `consultar_satelites.py`.
    - Obtener todos los satélites dentro de una zona, definida con los mismos cuatro argumentos y en el mismo orden que en la clase.
3. Reutilizando `catalogo.py` y `satelite.py`, implementar el CLI de nuestro programa en `consultar_satelites.py`:
    1. Recibir con `sys.argv` la ruta del archivo JSON como primer parámetro y la consulta como segundo. Se deben poder ejecutar las consultas `resumen` y `zona`:
        - `python consultar_satelites.py datos/satelites.json resumen` muestra, para cada tipo de órbita, la cantidad de satélites y el mínimo, máximo y promedio de altitud.
        - `python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13` muestra la cantidad de satélites en la zona y la descripción de cada uno. Los argumentos son longitud mínima, latitud mínima, longitud máxima y latitud máxima. En ese cuadro, centrado en Bariloche, hay 41 satélites. 

> Para armar otras zonas pueden dibujar un rectángulo sobre el mapa en [bboxfinder](https://bboxfinder.com/#-41.245805,-71.806641,-40.938415,-70.942841). El campo "Box" muestra los cuatro límites en el mismo orden que usa el programa: alcanza con copiarlos y reemplazar las comas por espacios.

Implementar pruebas unitarias en `test_catalogo.py` y `test_satelite.py`, la cobertura de las pruebas debe ser del 80% o superior.

Otras consideraciones:
- Crear e instalar `requirements.txt` con `skyfield==1.55`, `pytest` y `pytest-cov`.
- Se debe crear un `.gitignore` que contenga `.venv/`, `__pycache__/`, `.pytest_cache/`, `htmlcov/` y `.coverage`.
- Se debe crear un `README.md` inicial con el nombre del estudiante, una descripción breve y cómo ejecutar las consultas y las pruebas.

## Etapa 2

Pendiente: la consigna de la Etapa 2 se publica después de la entrega de la Etapa 1.

## Prolijidad de la entrega

La entrega debe estar ordenada: archivos con nombres claros, sin archivos duplicados o que no se usen, y con instrucciones suficientes para ejecutar el proyecto desde cero. El repositorio no incluye `.venv/`, `__pycache__/`, `.pytest_cache/`, `htmlcov/` ni `.coverage`.

## Clases relevantes

- [Clase 5 - Funciones y módulos](../../clases/clase-05/): división del programa en funciones y módulos.
- [Clase 9 - Archivos, tuplas y diccionarios](../../clases/clase-09/): conteos y resúmenes con diccionarios.
- [Clase 14 - Ambientes virtuales](../../clases/clase-14/): ambiente virtual y `requirements.txt`.
- [Clase 15 - Terminal y argumentos](../../clases/clase-15/): uso y validación de `sys.argv`.
- [Clase 16 - JSON en Python](../../clases/clase-16/): lectura del archivo de entrada.
- [Clase 17 - Manejo básico de excepciones](../../clases/clase-17/): `try`/`except` al cargar el catálogo y en el programa principal.
- [Clase 25 - Testing básico con `pytest`](../../clases/clase-25/material/clase-25.md): casos normales, límites e inválidos, `pytest.raises` y cobertura.
- [Clase 26 - Introducción a la POO](../../clases/clase-26/material/clase-26.md): clases, instancias, atributos y métodos.

## Anexo: formato de entrada

El sitio CelesTrak (<https://celestrak.org/NORAD/elements/>) publica las órbitas de todos los satélites activos. Se usa el archivo provisto [`satelites.json`](./satelites.json), con 16.710 satélites, que deben copiar en la carpeta `datos/` de su repositorio.

El archivo es una lista de diccionarios, uno por satélite. Por ejemplo, el de la Estación Espacial Internacional:

```json
{
    "OBJECT_NAME": "ISS (ZARYA)",
    "OBJECT_ID": "1998-067A",
    "EPOCH": "2026-10-14T08:06:39.057984",
    "MEAN_MOTION": 15.48861773,
    "ECCENTRICITY": 0.00067245,
    "INCLINATION": 51.6325,
    ...
    "NORAD_CAT_ID": 25544,
    ...
}
```

> Adaptación del trabajo práctico de la Comisión 2, a cargo de Tomás Manuel Guozden: <https://github.com/tguozden/programacion_2026/tree/main/proyesat>
