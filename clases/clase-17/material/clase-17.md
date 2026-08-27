---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 17. Manejo básico de excepciones

## `try`, `except` y errores esperables en Python

<div class="course">
Programación I<br>
Ingeniería Electrónica y Telecomunicaciones
</div>

<div class="meta">
Comisión 3<br>
Profesor: Lautaro Linquimán<br>
Universidad Nacional de Río Negro
</div>

<div class="unrn-logo">
  <img src="../../../recursos/marp/logo.png" alt="Logo UNRN">
  <span>UNIVERSIDAD<br>NACIONAL</span>
</div>

---

<!-- _class: inverse -->

# Repaso express <br>Clase anterior

1. ¿Para qué y porque se utilizan los archivos de tipo `.json`?
2. ¿Para qué usamos `json.dump()` y `json.load()`?
3. ¿Los archivos de tipo `.json` son iguales a un diccionario de Python?

---

# ¿Para que sirven las excepciones?

Los programas hablan con el mundo real:

- personas que escriben datos;
- archivos que pueden faltar;
- formatos que pueden venir mal;
- otros sistemas que a veces no no funcionan.

Las excepciones nos permiten responder a esos casos sin que el programa termine de golpe.

---

# ¿Qué es una excepción?

Una excepción es una señal de que algo salió mal **mientras el programa se estaba ejecutando**.

No siempre es un error de escritura del código.

También puede pasar porque:

- el usuario escribió un dato inesperado;
- falta un archivo;
- intentamos usar una posición que no existe;
- el contenido recibido desde afuera no tiene el formato esperado.


---

# ¿Qué hace Python cuando aparece?

Cuando Python encuentra una excepción:

1. corta la ejecución normal del programa;
2. muestra el traceback;
3. muestra la línea y el tipo de excepción;
4. termina el programa si nadie maneja ese caso.

Eso es útil para entender el problema, pero no siempre queremos que el programa se cierre de golpe.

---

# La mayoria de los lenguajes manejan excepciones

La idea aparece en muchos lenguajes modernos.

| Lenguaje | Forma habitual |
|---|---|
| Python | `try` / `except` |
| JavaScript | `try` / `catch` |
| Java / C# | `try` / `catch` |

Cambia la palabra, no la idea central: intentar una operación y manejar un error esperable.


---
# Rompiendo programas

<div class="columns">
<div>

## Calculador de edad 

```python
edad = input("Edad: ")
edad = int(edad)

print(f"El año que viene vas a tener {edad + 1}")
```
</div>
<div>

## Calculadora de división

```python
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

print(dividendo / divisor)
```
</div>
</div>



<!-- Probamos: `20`, `veinte` y vacío. -->

---

<!-- _class: compact -->
<!-- _footer: "[Python docs: `try` / `except`](https://docs.python.org/es/3/tutorial/errors.html)" -->

# Estructura básica de control de excepción

<div class="columns">
<div>

```python
try:
    # codigo que hay que cuidar
    operacion_que_puede_fallar()
except TipoDeError:
    # codigo de control de excepcion
    responder_al_error()
```

</div>
<div>

```python
try:
    # codigo que hay que cuidar
    operacion_que_puede_fallar()
except:
    # codigo de control de excepcion
    responder_al_error()
```

</div>
</div>

`try` contiene la operación riesgosa.

`except` indica qué tipo de excepción vamos a manejar.

---

<!-- _class: compact -->

# `try` / `except`

```python
texto = input("Cantidad: ")

try:
    cantidad = int(texto)
    print(cantidad)
except ValueError:
    print("ERROR")
```

1. Python intenta ejecutar el bloque `try`.
2. Si aparece `ValueError`, ejecuta ese `except`.
3. El programa puede seguir o terminar con un mensaje más claro.

Tenemos los siguientes datos: `20`, `veinte` y vacío.
En que caso entrariamos en el `except`?

---

<!-- _class: compact -->

# Ejercicio 1

Crear `producto_precio.py`.

El programa pide un producto y su precio separados por punto y coma:

```text
Producto y precio: Rosquillas;1200
```

Debe separar el texto, convertir el precio a `float` y mostrar:

```text
Rosquillas cuesta $1200.0
```

Probar primero sin `try` / `except`.

Después manejar las excepsiones.

Casos para probar: `Rosquillas;1200`, `Rosquillas;gratis`, `Rosquillas`.

---

<!-- _class: compact -->

# Validar y manejar excepciones

No son herramientas competidoras. Son dos estrategias que pueden solaparse.

Mismo caso: convertir texto a `int`.

<div class="columns">
<div>

**LBYL**: mirar antes de saltar / Look Before You Leap.

Verificar antes con `if`.

```python
if texto.isdigit():
    numero = int(texto)
else:
    print("No se pudo convertir.")
```

</div>
<div>

**EAFP**: pedir perdón antes que permiso / Easier to Ask for Forgiveness than Permission.

Intentar y capturar si falla.

```python
try:
    numero = int(texto)
except ValueError:
    print("No se pudo convertir.")
```

</div>
</div>

---

<!-- _class: compact -->

# ¿Cuándo uso cada una?

<div class="columns">
<div>

`if` para reglas del problema:

- rangos;
- opciones permitidas;
- estados válidos.

</div>
<div>

`try` / `except` para operaciones que pueden fallar:

- conversiones;
- apertura de archivos;
- acceso a recursos.

</div>

Dentro de un programa van a convivir.


---

<!-- _class: compact -->

# Excepción `FileNotFoundError`

La excepción `FileNotFoundError` se lanza cuando no se encuentra un archivo.

Implementemos el siguiente codigo:

```python
nombre_archivo = input("Archivo: ")

with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

print(contenido)
```

Probamos:

```text
Archivo: datos.txt
Archivo: no_existe.txt
```

---

<!-- _class: compact -->

# Manejando la apertura de un archivo

```python
nombre_archivo = input("Archivo: ")

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()

    print(contenido)
except FileNotFoundError:
    print("No se encontro el archivo indicado.")
```


---

# Ejercicio 2

Crear `palabra_por_posicion.py`.

Usen el archivo [frases.txt](../recursos/frases.txt).

El programa pide una ruta de archivo y una posición:

```text
Archivo: frases.txt
Posición: 3
```

Debe abrir el archivo, separar las palabras y mostrar la palabra pedida.

Usamos numeración humana: `1` significa la primera palabra.

Agregar el control de excepciones necesarios para que el programa no falle.

---

<!-- _class: compact -->
<!-- 
# Excepción `IndexError`

Guardamos este ejemplo como `repetir.py`.

```python
import sys

nombre = sys.argv[1]
cantidad = int(sys.argv[2])
for i in range(cantidad):
    print(f"Hola, {nombre}")
```

Probamos:

```bash
python repetir.py Pedro 3
python repetir.py Pedro
python repetir.py
```

--- -->

<!-- _class: compact -->

<!-- # Manejar argumentos faltantes

```python
import sys

try:
    nombre = sys.argv[1]
    cantidad = int(sys.argv[2])

    for i in range(cantidad):
        print(f"Hola, {nombre}")
except IndexError:
    print("Uso: python repetir.py NOMBRE CANTIDAD")
except ValueError:
    print("La cantidad tiene que ser un numero entero.")
```

Cada `except` responde a un problema distinto. -->

---

<!-- _class: compact -->

<!-- # Ejercicio 3

Crear `linea_por_numero.py`.

Usen el archivo [frases.txt](../recursos/frases.txt).

El programa recibe por argumentos:

```bash
python linea_por_numero.py frases.txt 2
```

Debe abrir el archivo, leer sus líneas y mostrar la línea pedida:

```text
Segunda frase
```

Usamos numeración humana: `1` significa la primera línea.

Pista: si el usuario pide la línea `2`, en la lista hay que usar la posición `1`. -->

---

<!-- _class: compact -->

<!-- # Pista para el ejercicio 3

Casos para probar:

```bash
python linea_por_numero.py frases.txt 2
python linea_por_numero.py frases.txt dos
python linea_por_numero.py no_existe.txt 2
python linea_por_numero.py frases.txt 999
python linea_por_numero.py
```

Excepciones posibles:

- `IndexError`
- `ValueError`
- `FileNotFoundError`

Identificar primero cuál rompe cada caso. Después agregar mensajes claros. -->

---

# Extrayendo mensajes de excepciones

Podemos extraer el mensaje de la excepcion de la siguiente manera:

```python
try:
    float("hola")
except ValueError as error:
    print(error)
    print("could not convert string to float" in str(error))
```

---

# Lanzando excepciones

Es posible que lancemos nuestras propias excepciones utilizando la palabra reservada `raise + TipoExcepción`.

Por ejemplo:

```python
def sumador(anterior, siguiente):
    if siguiente < anterior:
        raise ValueError(f"El numero siguiente no puede ser más chico que el anterior")
    else:
        return siguiente + anterior
```

---

<!-- _class: compact -->
<!-- _footer: "[Python docs: excepciones incorporadas](https://docs.python.org/es/3/library/exceptions.html)" -->


# Tipos comunes de excepción

| Excepción | Suele aparecer cuando... |
|---|---|
| `ValueError` | el valor no sirve para una operación |
| `TypeError` | usamos un tipo de dato inadecuado |
| `NameError` | usamos un nombre que no existe |
| `IndexError` | pedimos una posición inexistente |
| `KeyError` | pedimos una clave inexistente |
| `FileNotFoundError` | intentamos abrir un archivo que no está |
| `ZeroDivisionError` | dividimos por cero |

No hace falta memorizarlas: hay que leer el nombre en el mensaje de error.
