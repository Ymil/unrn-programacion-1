# Mini TP 2: Decisiones, lógica y primeros `for`

> Programación 1  
> Universidad Nacional de Río Negro  
> Tema: condicionales, operadores lógicos e iteraciones simples

## Objetivo

Practicar la construcción de programas usando:

- Operadores de comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Operadores lógicos: `and`, `or`
- Estructuras condicionales: `if`, `elif`, `else`
- Iteraciones simples con `for`

## Parte 1: Pensar antes de programar

Antes de escribir código, resolver en prosa.

### Ejercicio 1

Diseñar un algoritmo que determine si una persona puede entrar a un evento.

Datos:

- edad
- tiene_documento (`True` o `False`)

Condición:

- Solo puede entrar si tiene 18 años o más y tiene documento.

Escribir los pasos en forma clara y ordenada.

### Ejercicio 2

Diseñar un algoritmo que indique qué ropa usar según la temperatura.

Dato:

- temperatura

Condiciones:

- Menor a 10: abrigo
- Entre 10 y 20: ropa media
- Mayor a 20: ropa liviana

Escribir los pasos en forma clara y ordenada.

## Parte 2: Pasar a código

### Ejercicio 3

Implementar en Python el algoritmo del ejercicio 1.

Ejemplo:

```python
edad = 20
tiene_documento = True
```

### Ejercicio 4

Implementar en Python el algoritmo del ejercicio 2.

Ejemplo:

```python
temperatura = 15
```

### Ejercicio 5

Escribir un programa que determine si un número es:

- Par o impar
- Mayor, menor o igual a 10

Ejemplo de salida esperada:

```text
El numero es par
El numero es mayor a 10
```

### Ejercicio 6

Sistema de acceso a un banco.

Datos:

- clave_almacenada
- clave_ingresada
- usa_token (`True` o `False`)

Condición:

- Permitir acceso si la clave es correcta o si se usa token.

Mostrar uno de estos mensajes:

- `Acceso permitido`
- `Acceso denegado`

## Parte 3: Leer y razonar código

### Ejercicio 7

Indicar qué imprime el siguiente código:

```python
monto = 900
es_cliente_vip = False
tiene_cupon = True

if monto > 1000 and es_cliente_vip or tiene_cupon:
    print("Se aplica descuento")
else:
    print("No hay descuento")
```

Explicar en palabras por qué ocurre ese resultado.

## Parte 4: Primeros ejercicios con `for`

### Ejercicio 8

Usar un `for` para imprimir los números del 1 al 5.

Salida esperada:

```text
1
2
3
4
5
```

### Ejercicio 9

Usar un `for` para imprimir una tabla simple de multiplicar del 2.

Ejemplo de salida:

```text
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
```

Completarla hasta `2 x 10`.

### Ejercicio 10

Imprimir mediante un `for` todos los días de la semana junto con su posición.

Usar esta referencia:

```text
0: Lunes
1: Martes
2: Miercoles
3: Jueves
4: Viernes
5: Sabado
6: Domingo
```

Nota: guardar cada programa en un archivo diferente.
