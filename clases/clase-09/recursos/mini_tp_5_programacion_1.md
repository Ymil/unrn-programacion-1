# Mini TP 5 - Teoría y ejercicios básicos

## Objetivo

Reforzar los conceptos base de tuplas, conjuntos y diccionarios con ejercicios cortos y directos.

## Parte 1 - Teoría

Responder en un archivo de texto plano, con tus palabras, en no más de 4 líneas por punto:

1. ¿Qué es una **tupla** y en qué se diferencia de una lista?
2. ¿Qué es un **conjunto (set)** y qué problema resuelve mejor que una lista?
3. ¿Qué es un **diccionario** y cuándo conviene usar clave-valor?
4. ¿Qué significa combinar estructuras de datos? Dar un ejemplo simple.

## Parte 2 - Ejercicios básicos

### Ejercicio 1 - Tuplas: datos fijos
Crear una tupla `materia = ("Programación 1", 3, "Miércoles")` y resolver:
1. Mostrar el nombre de la materia.
2. Mostrar el número de comisión.
3. Mostrar el día de cursada.
4. Desempaquetar la tupla en tres variables e imprimirlas.

### Ejercicio 2 - Tuplas: operaciones simples
Dada la tupla:

```python
numeros = (4, 7, 2, 9, 7)
```

Resolver:
1. Mostrar el primer y el último valor.
2. Contar cuántas veces aparece el número `7`.
3. Mostrar el largo de la tupla.

### Ejercicio 3 - Sets: básicos
Dado:

```python
valores = [3, 3, 5, 7, 5, 8, 8, 8, 10]
```

Resolver:
1. Convertir la lista a set.
2. Mostrar el set resultante.
3. Mostrar cuántos elementos únicos hay.

### Ejercicio 4 - Sets: pertenencia y altas
Crear un set de materias:

```python
materias = {"Matemática", "Programación"}
```

Resolver:
1. Agregar `"Física"`.
2. Verificar si `"Química"` está en el set.
3. Mostrar el set final.

### Ejercicio 5 - Diccionarios: ficha simple
Crear un diccionario `alumno` con:
- nombre
- apellido
- edad

Resolver:
1. Mostrar nombre y apellido en una sola línea.
2. Aumentar la edad en 1.
3. Agregar la clave `activo` con valor `True`.
4. Mostrar el diccionario completo.

### Ejercicio 6 - Diccionarios: recorridos
Dado:

```python
producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}
```

Resolver:
1. Recorrer e imprimir claves.
2. Recorrer e imprimir valores.
3. Recorrer e imprimir `clave: valor`.
