# TP 8 - Diccionarios y archivos

El objetivo de esta guia es practicar estructuras de datos, diccionarios y archivos como repaso de Programacion 1.

La entrega se debe realizar subiendo la resolucion de los ejercicios en el repositorio de github y entregando el link aqui: [https://campusbimodal.unrn.edu.ar/mod/assign/view.php?id=1181502](https://campusbimodal.unrn.edu.ar/mod/assign/view.php?id=1181502).

- Es obligatoria.
- No usar inteligencia artificial para resolverla.
- Guardar cada ejercicio practico en un archivo separado.

Antes de arrancar con ejercicios, tomense su tiempo de leer las consignas y traten de hacer algun mapa mental de como encarar la solución.

Luego a escribir codigo!

### Ejercicio 1 — Estructuras de datos

Explicá con tus palabras la diferencia entre:

- Lista
- Tupla
- Conjunto
- Diccionario

Para cada estructura, indicá un ejemplo de situación donde podría resultar útil.

### Ejercicio 2 — Registro de sensores

Dada la siguiente lista de tuplas:

```python
mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]
```

Cada tupla tiene el formato:

```python
(tipo_medicion, valor, ubicacion)
```

Escribí un programa que:

1. Cree un diccionario donde la clave sea la ubicación.
2. Cada ubicación debe guardar una lista con sus mediciones.
3. Cree un conjunto con todos los tipos de medición sin repetir.
4. Muestre el diccionario final.
5. Muestre el conjunto de tipos encontrados.

---

### Ejercicio 3 — Base de datos de alumnos

Escribí un programa que:

1. Pida al usuario el nombre de 4 alumnos.
2. Valide que el nombre no esté vacío.
3. Guarde los nombres válidos en una lista.
4. Escriba los nombres en un archivo llamado `alumnos.txt`, un nombre por línea.
5. Cierre el archivo.

---

### Ejercicio 4 — Lectura de archivo

Se tiene un archivo llamado `temperaturas.txt` con el siguiente contenido:

```text
Bariloche;12
Viedma;20
Roca;18
Bariloche;15
```

Escribí un programa que:

1. Lea el archivo línea por línea.
2. Separe cada línea usando `split(";")`.
3. Genere un diccionario donde:
   - la clave sea la ciudad;
   - el valor sea una lista de temperaturas registradas.
4. Muestre el diccionario final.

---

### Ejercicio 5 — Interpretación de código

Leer el siguiente código **sin ejecutarlo**:

```python
def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)
```

Responder:

1. ¿Qué hace el programa?
2. ¿Qué hace la función `limpiar`?
3. ¿Qué hace la función `es_valido`?
4. ¿Qué nombres quedan almacenados en `validos`?
5. ¿Qué imprime el programa al finalizar?

---
