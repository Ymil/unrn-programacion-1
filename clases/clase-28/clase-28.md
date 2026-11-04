---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
math: mathjax
---

<!-- _class: title -->
<!-- _paginate: false -->

# 28. Recursividad

## Funciones que se llaman a sí mismas

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
  <img src="../../recursos/marp/logo.png" alt="Logo UNRN">
  <span>UNIVERSIDAD<br>NACIONAL</span>
</div>

---

<!-- _class: inverse -->

# Repaso express

1. ¿Qué hereda una clase hija de la clase base?
2. ¿Qué pasa cuando una clase hija sobrescribe un método?
3. ¿Que hace `super`?

---

# Funciones recursivas

> Una función recursiva es una función que se llama a sí misma para resolver una versión más pequeña del mismo problema.

Toda función recursiva tiene dos partes:

- **Caso base:** la situación en la que la función puede devolver un resultado sin volver a llamarse. Es la condición que corta las llamadas.
- **Caso recursivo:** la situación en la que la función resuelve una parte del problema y le pasa el resto a una nueva llamada a sí misma.

---

<!-- _class: compact -->

# Estructura de una función recursiva

<div class="columns">
<div>

```python
def funcion(problema):
    if caso_base:
        return resultado

    return funcion(problema_mas_pequeno)
```

> Cada llamada recursiva debe acercarse al caso base.

Si nunca llega, la función se sigue llamando hasta que Python la corta con un `RecursionError`.

</div>
<div>

- Primero se revisa el caso base: si se cumple, la función termina ahí.
- Si no, se llama con un problema más chico: un número menor, una lista más corta.
- Cada llamada es una ejecución nueva, con sus propios parámetros.
- La anterior queda en pausa hasta que la nueva termine.
- Al llegar al caso base, las llamadas terminan de la última a la primera.
- Puede haber más de un caso base y más de una llamada recursiva.

</div>
</div>

---

<!-- _class: compact -->

# Ejemplo practico: Cuenta regresiva

<div class="columns">
<div>

```python
def cuenta_regresiva(n):
    if n == 0:
        print("Fin")
        return

    print(n)
    cuenta_regresiva(n - 1)


cuenta_regresiva(4)
```

</div>
<div>

```text
4
3
2
1
Fin
```

`return` sin valor termina la función: cuando `n` llega a 0 no queda nada más para hacer.

</div>
</div>

> **Caso base:** `n == 0`.
>**Llamada recursiva:** `cuenta_regresiva(n - 1)`.
---

# Seguimiento de las llamadas

```text
cuenta_regresiva(4)                     imprime 4
    cuenta_regresiva(3)                 imprime 3
        cuenta_regresiva(2)             imprime 2
            cuenta_regresiva(1)         imprime 1
                cuenta_regresiva(0)     imprime Fin
```

- `n` baja de a uno en cada llamada; al llegar a 0 ya no se vuelve a llamar y se corta la cadena.

---

<!-- _class: compact -->

# Cuidado con la recursividad infinita

Sin caso base, la función se llama sin parar hasta que Python la corta, con unas 1000 llamadas abiertas.

<div class="columns">
<div>

```python
def cuenta_regresiva(n):
    print(n)
    cuenta_regresiva(n - 1)


cuenta_regresiva(2)
```

`n` sigue bajando y nada corta las llamadas.

</div>
<div>

```python
# OUTPUT
2
1
0
-1
-2
...
-996
```

</div>
</div>

```text
RecursionError: maximum recursion depth exceeded
```

También pasa si el caso base nunca se alcanza: `cuenta_regresiva(-1)` se aleja del 0.

---

<!-- _class: compact -->

# For VS Recursividad

<div class="columns">
<div>

## Con for

```python
def mostrar(lista):
    for numero in lista:
        print(numero)


numeros = [5, 8, 12]
mostrar(numeros)
```

</div>
<div>

## Con recursividad

```python
def mostrar(lista):
    if len(lista) == 0:
        return

    print(lista[0])
    mostrar(lista[1:])


numeros = [5, 8, 12]
mostrar(numeros)
```

</div>
</div>

Las dos imprimen 5, 8 y 12. La recursividad no reemplaza a los ciclos: para recorrer una lista como esta, el `for` es más claro.

---

<!-- _class: compact -->

# ¿Cuando utilizar la recursividad?

La recursividad no aplica para todo y en muchos casos puede complicar la lectura de nuestro codigo.

<div class="columns">
<div>

- Problemas que se definen con una versión más chica del mismo problema.
- Estructuras anidadas.
- Estructuras con una profundidad que no conocemos de antemano.

</div>
<div>

```text
caja
└── caja
    └── caja
```

```text
lista
└── lista
    └── lista
```

</div>
</div>

> Si un `for` o un `while` lo resuelve de forma clara, probablemente sea mejor. La recursividad sirve sobre todo cuando hay niveles anidados o el problema ya se define de forma recursiva.

---

# Caso práctico: Factorial

`4!` significa `4 * 3 * 2 * 1 = 24`. Por definición, `0! = 1`.

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(4))
```

El caso base devuelve 1. En los demás casos, `n` multiplica el resultado de `factorial(n - 1)`.

---

<!-- _class: compact -->

# Las llamadas de factorial(4)

<div class="columns">
<div>

## Al llamar

```text
factorial(4) espera 4 * factorial(3)
factorial(3) espera 3 * factorial(2)
factorial(2) espera 2 * factorial(1)
factorial(1) espera 1 * factorial(0)
factorial(0) devuelve 1
```

</div>
<div>

## Al volver

```text
factorial(1) devuelve 1 * 1 = 1
factorial(2) devuelve 2 * 1 = 2
factorial(3) devuelve 3 * 2 = 6
factorial(4) devuelve 4 * 6 = 24
```

</div>
</div>

Cada llamada espera a la siguiente. Cuando `factorial(0)` devuelve 1, las multiplicaciones se resuelven de la última a la primera.

---

# Ejercicio 1: sumar una lista

Crear una función recursiva que reciba una lista de números y devuelva la suma de sus elementos.

```python
mediciones = [12, 8, 15, 5]
```

Con `mediciones` tiene que devolver 40. Con `[]`, 0.

---

<!-- _class: inverse -->

# Complejizando la recursividad

---

<!-- _class: compact -->

# Listas dentro de listas

<div class="columns">
<div>

```python
datos = [
    10,
    20,
    [
        30,
        40
    ]
]
```

</div>
<div>

```python
datos = [
    10,
    [
        20,
        [
            30,
            [
                40
            ]
        ]
    ]
]
```

</div>
</div>

---

<!-- _class: compact -->

# Un for por nivel

<div class="columns">
<div>

```python
for elemento in datos:
    if isinstance(elemento, list):
        for valor in elemento:
            print(valor)
    else:
        print(elemento)
```

</div>
<div>

Con el segundo `datos`:

```text
10
20
[30, [40]]
```

</div>
</div>

`isinstance(elemento, list)` devuelve `True` si `elemento` es una lista.

Con el primer `datos` funciona. Con el segundo, `valor` también puede ser una lista: habría que repetir el `if` y el `for` en cada nivel, y no sabemos cuántos niveles hay.

---

<!-- _class: compact -->

# Una función para cualquier profundidad

```python
def mostrar_valores(dato):
    if not isinstance(dato, list):
        print(dato)
        return

    for elemento in dato:
        mostrar_valores(elemento)


mostrar_valores(datos)
```

- **Caso base:** si recibe un número, lo imprime y termina.
- **Caso recursivo:** si recibe una lista, se llama con cada elemento.
- Con `[]`, el `for` no se ejecuta y la función termina sin imprimir.

---

# Seguimiento de mostrar_valores

```text
mostrar_valores([10, [20, [30, [40]]]])
    mostrar_valores(10): imprime 10 y termina
    mostrar_valores([20, [30, [40]]])
        mostrar_valores(20): imprime 20 y termina
        mostrar_valores([30, [40]])
            mostrar_valores(30): imprime 30 y termina
            mostrar_valores([40])
                mostrar_valores(40): imprime 40 y termina

mostrar_valores([]): termina sin entrar al for
```

Cada elemento genera una llamada. Los números llegan al caso base sin volver a llamar a la función.

---

# Ejercicio 2: sumar una lista anidada

Crear una función recursiva que reciba una lista anidada de números y devuelva la suma de todos sus valores, sin importar cuántos niveles tenga.

```python
consumos = [12, [7, 3], [[5], 8], []]
```

Con `consumos` tiene que devolver 35. Con `[]`, 0.

---

<!-- _class: inverse -->

# Ejercicio integrador

Una empresa de logística necesita saber cuánto stock real de **jugo** tiene en un depósito.

El inventario se exportó a un JSON: `deposito_sur.json`.

---

<!-- _class: compact -->

# Cómo se organiza un depósito

<div class="columns">
<div>

```text
Depósito
├── productos
├── cajas
│   ├── productos
│   └── cajas
│       └── productos
└── contenedores
    ├── productos
    ├── cajas
    └── otros contenedores
```

</div>
<div>

- Una caja puede estar dentro de otra caja.
- Un contenedor puede tener productos, cajas u otros contenedores.
- No hay una cantidad fija de niveles.
- Un producto es el caso base: la llamada termina ahí. Una caja vacía tampoco genera nuevas llamadas.

</div>
</div>

---

<!-- _class: compact -->

# Formato de los archivos

<div class="columns">
<div>

**Un producto**

```json
{
    "tipo": "producto",
    "producto": "jugo",
    "cantidad": 12
}
```

</div>
<div>

**Una caja o un contenedor**

```json
{
    "tipo": "caja",
    "nombre": "Caja A",
    "contenido": [
        ...
    ]
}
```

</div>
</div>

El archivo tiene el nombre del depósito en `deposito` y la lista de elementos en `contenido`. `tipo` puede ser `"producto"`, `"caja"` o `"contenedor"`.

---

<!-- _class: compact -->

# Consigna

Crear un programa que:

1. Lea el archivo `deposito_sur.json` de [recursos/](./recursos/).
2. Recorra el campo `contenido` con una función recursiva, sin importar cuántas cajas o contenedores haya anidados.
3. Sume las cantidades de los productos `"jugo"`, sin incluir otros productos.
4. Informe el nombre del depósito y el total de unidades de jugo.

---

# Salida esperada

```text
Puhelche Sur
Unidades de jugo: 41
```

**Desafío opcional:** que el producto a buscar se ingrese con `input()`, para que el mismo programa pueda buscar jugo, agua, gaseosa u otro producto.
