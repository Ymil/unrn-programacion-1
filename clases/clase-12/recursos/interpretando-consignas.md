# Interpretando consignas

## Verificaciones

1. Se pide verificar que un dato es un número?

**RESPUESTA:** 

```python
if data.isnumeric():
    # Codigo
```

> NOTA: **IsNumeric** no soporta numeros negativos.

2. Se pide verificar que tiene N cantidad de caracteres?

**RESPUESTA:** 
```python
if len(dato) == 10:
    # Se valida que el dato tenga 10 caracteres.

if len(dato) > 4:
    # Se valida que tiene más de 4 caracteres.
```

3. Se pide verificar que no sea un dato vacío?

**RESPUESTA:** 

```python
if len(dato) == 0:
    # El dato esta vacio

if dato == "":
    # El dato esta vacio
```

4. Se pide verificar que un elemento más exista más de N veces?


**RESPUESTA:** 

```python
datos = "nombre,edad,genero"
if datos.count(",") == 2:
    # mi codigo
```

5. Si tenemos que verificar que un texto contenga otro texto?

**RESPUESTA:** 

```python
# Ejemplo para textos
dato = "Hola Mundo"
if "Hola" in dato:
    # El dato contiene hola

# Ejemplo para listas 
dato = ["minipimer"]
if "minipimer" in dato:
    # la lista contiene minipimer

# Ejemplo diccionarios
dato = {"minipimer": {...}}
if "minipimer" in dato:
    # La clave existe en el dicionario

# Ejemplo para set
dato = {"minipimer"}
if "minipimer" in dato:
    # La valor existe en el conjunto

# Aplica para tuplas
```

> Si tenemos que buscar que una cosa exista dentro de otra todas las estructuras que vimos hasta ahora soporta el operador "in"

## Repeticiones

1. Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?

**RESPUESTA:**

**VEMOS UNA LISTA Y LA ITERAMOS**

```python
datos = ["1", "2", "3"]

for dato in datos:
    if dato.isnumeric():
        # Validamos que es dato
        int(dato)
```

2. Hay que pedirle 5 nombres al usuario. ¿Que hacemos?

**RESPUESTA:** 

```python
datos = []
while len(datos) < 5:
    datos.append(input("Ingresar nombre"))

for idx in range(5):
    datos.append(input("Ingresar nombre"))
```

3. Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?

**RESPUESTA:** 

```python
# Opcion trucha

while True:
    IN = input("")
    if IN == "fin":
        break

# Opcion buena

IN = ""
while IN != "fin":
    IN = input("")
```
## Archivos

1. Hay que leer un archivo: 

**RESPUESTA:** 

```python
f = open("archivo.txt", "r")

# Extraigo el texto
contenido = f.read()

# Extraigo el texto separado por salto de lineas
contenido_l = f.readlines()
```

2. Hay que escribir un archivo:

**RESPUESTA:** 

```python
f = open("archivo.txt", "w")
f.write("Hola Mundo")
f.close()
```

3. ¿Hay que cerrar un archivo?

**RESPUESTA:** 

`f.close()` SIEMPRE tiene que estar si no podemos perder datos.

## Otros
1. ...

1.1 Tenemos que solicitarle al usuario que ingrese 25 nombres, apellidos y año de nacimientos ¿Que hacemos?

```python
datos = []

for idx in range(2):
    nombre = input("Ingresar nombre")
    apellido = input("Ingresar apellido")
    anio_nacimiento = input("Año de nacimiento")
    datos.append({ 
        "nombre": nombre,
        "apellido": apellido,
        "anio_nacimiento": anio_nacimiento
    })
```

2. Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible.









