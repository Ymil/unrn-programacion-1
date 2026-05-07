# Mini TP 6 - Ejercicios intermedios e integradores

## Objetivo

Aplicar tuplas, conjuntos, diccionarios y estructuras combinadas en problemas más amplios.

## Regla general

Resolver toda la guía sin usar librerías externas.

## Parte 1 - Ejercicios intermedios

### Ejercicio 1 - Ranking de ciudades
Tenés una lista de tuplas con datos semanales de temperatura máxima por ciudad y fecha:

```python
registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]
```

Resolver:
1. Mostrar todas las ciudades sin repetir (usar set).
2. Mostrar todas las fechas disponibles sin repetir.
3. Calcular el promedio de temperatura por ciudad (usar diccionario).
4. Indicar qué ciudad tuvo el mayor promedio.

### Ejercicio 2 - Inventario con alertas
Modelar un inventario como diccionario donde la clave es el nombre del producto y el valor otro diccionario con `precio` y `stock`.

Ejemplo sugerido:

```python
inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}
```

Resolver:
1. Mostrar productos con stock bajo (`stock < 5`).
2. Calcular valor total del inventario (`precio * stock` por producto).
3. Generar un set con productos que requieren reposición urgente (`stock <= 2`).

### Ejercicio 3 - Catálogo de biblioteca
Tenés una lista de libros, donde cada libro está representado por una tupla:
`(titulo, autor, anio, genero)`.

```python
libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]
```

Resolver:
1. Mostrar todos los títulos publicados después de 2010.
2. Obtener un set con los géneros disponibles.
3. Crear un diccionario donde la clave sea el género y el valor la cantidad de libros de ese género.
4. Mostrar qué género tiene más libros.
5. Mostrar los géneros sin repetirse.

## Parte 2 - Ejercicios integradores

### Ejercicio 4 - Sistema de seguimiento académico
Se tiene una lista de diccionarios. Cada estudiante tiene:
- `nombre`
- `notas` (lista de enteros)
- `asistencias` (cantidad)
- `comision` (string)

#### Lista de estudiantes

```python
estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6], "asistencias": 9, "comision": "C1"},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencias": 6, "comision": "C1"},
    {"nombre": "Mora", "notas": [9, 8, 10], "asistencias": 10, "comision": "C2"},
    {"nombre": "Pedro", "notas": [2, 4, 3], "asistencias": 7, "comision": "C2"}
]
```

#### Consignas
Antes de empezar a escribir código, desarrollá una explicación completa de cómo resolverías el problema. Tomate el tiempo para pensar la estrategia, los pasos, las estructuras de datos y las decisiones lógicas. Escribí ese análisis al comienzo del archivo, antes de la implementación.

1. Mostrar promedio de cada estudiante.
2. Clasificar cada estudiante en:
- `Promociona` si promedio >= 8 y asistencias >= 8
- `Regulariza` si promedio >= 4 y asistencias >= 6
- `Recursa` en otro caso
3. Mostrar cuántos estudiantes hay en cada categoría.
4. Mostrar la comisión con mejor promedio general.
5. Generar un set con nombres de estudiantes en riesgo (`Recursa`).

### Ejercicio 5 - Buscador interactivo por género
Escribir un programa que permita al usuario elegir un género de libro y, a partir de esa elección, mostrar los libros disponibles.

#### Lista de libros
```python
libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("1984", "George Orwell", 1949, "Novela"),
    ("Rayuela", "Julio Cortázar", 1963, "Novela"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Armas, gérmenes y acero", "Jared Diamond", 1997, "Historia"),
    ("Historia mínima de América Latina", "Carlos Malamud", 2014, "Historia"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Cosmos", "Carl Sagan", 1980, "Ciencia"),
    ("Una breve historia del tiempo", "Stephen Hawking", 1988, "Ciencia"),
    ("El arte de la guerra", "Sun Tzu", -500, "Estrategia"),
    ("Pensar rápido, pensar despacio", "Daniel Kahneman", 2011, "Psicología")
]
```

#### Consignas
Antes de empezar a escribir código, desarrollá una explicación completa de cómo resolverías el problema. Tomate el tiempo para pensar la estrategia, los pasos, las estructuras de datos y las decisiones lógicas. Escribí ese análisis al comienzo del archivo, antes de la implementación.

1. Mostrar al inicio los géneros disponibles sin repetir.
2. Pedir al usuario un género por `input`.
3. Si el género existe, mostrar todos los títulos de ese género.
4. Si el género no existe, mostrar un mensaje de aviso.
5. Repetir el proceso hasta que el usuario escriba `salir`.
