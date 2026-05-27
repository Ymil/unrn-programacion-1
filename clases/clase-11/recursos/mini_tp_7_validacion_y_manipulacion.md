# Mini TP 7 - Validacion y manipulacion de datos

El objetivo de esta guia es practicar como validar y manipular datos como vimos en la clase 11.

La entrega se debe realizar subiendo la resolución de los ejercicios en el repositorio de github y comentando la aquí: https://campusbimodal.unrn.edu.ar/mod/forum/discuss.php?d=241566.

- Es obligatoria.
- No usar inteligencia artificial para resolverla.
- Guardar cada ejercicio practico en un archivo separado.

## Ejercicio 1 - Algunas preguntas

Responder en un archivo de texto plano (.TXT), con sus palabras.

1. ¿Porque es importante validar los datos que ingresa un usuario?
2. ¿Que hace `strip` y en que se diferencia de `split`?
3. ¿Para que puede servir `count` cuando una linea tiene datos separados por comas o por punto y coma?
4. ¿Que problema pueden traer los espacios de mas al principio o al final de un dato?

## Ejercicio 2 - Leer codigo y explicarlo

Este ejercicio no es para programar. Lean el codigo y escriban una explicación de que hace.

```python
linea = " mara ; programacion ; 8 "

partes = linea.split(";")
nombre = partes[0].strip().capitalize()
materia = partes[1].strip().capitalize()
nota_texto = partes[2].strip()

if nota_texto.isnumeric():
    nota = int(nota_texto)
    print(f"{nombre} cursa {materia} y obtuvo {nota}")
else:
    print("La nota no es valida")
```

Para orientar la explicacion:

1. ¿Que queda guardado en `partes`?
2. ¿Por que se usa `strip` antes de `capitalize`?
3. ¿Que dato se esta validando antes de convertirlo?
4. ¿Que imprimiria el programa si en lugar de `8` viniera `ocho`?

## Ejercicio 3 - Acomodar nombres

Partiendo de esta lista:

```python
nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
```

Armar una nueva lista llamada `nombres_normalizados` donde cada nombre quede sin espacios sobrantes y con un formato prolijo.

Al final, mostrar la lista. Deberia quedar parecido a esto:

```text
["Mara", "Tomas", "Lucia", "Marcos", "Sofia"]
```

## Ejercicio 4 - Edad valida

Pedir una edad por teclado. Antes de usarla como numero, revisar que el dato tenga sentido.

El programa tiene que aceptar edades numericas entre 0 y 120. Si la persona escribe espacios de mas, el programa deberia poder limpiarlos antes de validar.

Si el dato sirve, mostrar algo como:

```text
Edad registrada: 25
```

Si no sirve, mostrar un mensaje de error claro. No alcanza con que el programa se rompa.

## Ejercicio 5 - Codigo de materia

Pedir al usuario un codigo de materia con este formato:

```text
PROG-101
```

El programa tiene que validar que:

- tenga un solo guion `-`;
- la parte de la izquierda tenga solo letras;
- la parte de la derecha tenga solo numeros.

Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo `upper`).

Ejemplo:

```text
Codigo valido: PROG-101
```

Si no es valido, mostrar un mensaje de error claro.
