# Mini TP 3: While y listas

> Programacion 1  
> Universidad Nacional de Rio Negro  
> Tema: repeticiones con `while` y trabajo con listas

## Objetivo

Practicar la construccion de programas que usen:

- El iterador `while`
- Listas
- Carga de datos con `input()`
- Validaciones simples

### Ejercicio 1

Crear una lista con al menos 4 elementos. Pueden ser comidas, nombres, materias o cualquier otro conjunto de datos simples.

Luego:

1. Mostrar la lista completa.
2. Mostrar el primer elemento.
3. Mostrar el ultimo elemento.
4. Mostrar cuantos elementos tiene la lista.

### Ejercicio 2

Dada la siguiente lista:

```python
lista_de_compras = ["pan", "leche", "huevos"]
```

Indicar que devuelve cada una de estas expresiones:

1. `lista_de_compras[0]`
2. `lista_de_compras[-1]`
3. `len(lista_de_compras)`

Explicar en palabras por que devuelve ese resultado.

### Ejercicio 3

Escribir un programa que:

1. Cree una lista vacia.
2. Pida al usuario que ingrese un elemento.
3. Agregue ese elemento a la lista.
4. Repita el proceso hasta que el usuario escriba `"fin"`.

Al finalizar, mostrar:

- La lista completa.
- La cantidad de elementos ingresados.

### Ejercicio 4

En base al ejercicio anterior, crear un nuevo programa donde la lista pueda tener un maximo de 5 elementos.

Condiciones:

- Si el usuario escribe `"fin"`, el programa termina.
- Si la lista llega a 5 elementos, el programa ya no debe seguir agregando datos.
- Al finalizar, mostrar la lista y su cantidad de elementos.

## Parte 3: Recorrer y consultar listas

### Ejercicio 5

Dada una lista, mostrar todos sus elementos usando `while`.

Ejemplo:

```python
lista = ["pizza", "empanadas", "hamburguesa"]
```

Salida esperada:

```text
1. pizza
2. empanadas
3. hamburguesa
```

### Ejercicio 6

Escribir un programa que:

1. Tenga una lista ya cargada.
2. Pida al usuario un elemento.
3. Indique si ese elemento esta en la lista.
4. Si esta, mostrar en que posicion aparece.

### Ejercicio 7

Armar un sistema simple de pedidos.

El programa debe:

1. Permitir agregar comidas a una lista.
2. Aceptar solo estas opciones:
   - `pizza`
   - `empanadas`
   - `hamburguesa`
3. Si el usuario escribe otra opcion, mostrar un mensaje de error.
4. Terminar cuando el usuario escriba `"terminar"`.

Al final:

- Mostrar el pedido completo.
- Mostrar cuantos elementos tiene el pedido.

## Reglas

- Usar `while` en los ejercicios donde corresponda.
- Usar listas.
- No usar `for`.
- No usar herramientas o estructuras que no vimos en clase.
- Guardar cada ejercicio en un archivo diferente.

## Sugerencia

Si un programa con `while` no termina, revisar que variable cambia dentro del ciclo y cual es la condicion de salida.

> No te olvides de usar CTRL + C para salir de los programas en ejecucion.