# Mini TP 4: Funciones y modulos

> Programacion 1  
> Universidad Nacional de Rio Negro  
> Tema: funciones, parametros, retorno e importacion de modulos

## Objetivo

Practicar la construccion de programas que usen:

- Funciones propias
- Parametros
- `return`
- Separacion del codigo en modulos
- Reutilizacion de logica

## Parte 1: Primeras funciones

### Ejercicio 1

Escribir una funcion llamada `saludar` que reciba un nombre y devuelva un mensaje de bienvenida.

Ejemplo:

```python
print(saludar("Ana"))
```

Salida esperada:

```text
Hola Ana
```

### Ejercicio 2

Escribir una funcion llamada `sumar` que reciba dos numeros y devuelva el resultado.

Luego:

1. Guardar el resultado en una variable.
2. Mostrarlo por pantalla.

### Ejercicio 3

Escribir una funcion llamada `es_par` que reciba un numero y devuelva `True` si es par o `False` si es impar.

Probarla con al menos 3 valores distintos.

## Parte 2: Funciones con decisiones

### Ejercicio 4

Escribir una funcion llamada `calcular_descuento` que reciba un precio.

Condiciones:

- Si el precio es mayor a 10000, devolver el precio con 10% de descuento.
- Si no, devolver el mismo precio.

Mostrar el resultado final con un mensaje descriptivo.

### Ejercicio 5

Escribir una funcion llamada `obtener_estado` que reciba una nota y devuelva:

- `"Promociona"` si la nota es 8 o mas
- `"Aprueba"` si la nota esta entre 6 y 7
- `"Desaprueba"` si es menor a 6

Probar la funcion con varias notas.

## Parte 3: Separar en modulos

### Ejercicio 6

Crear un archivo llamado `conversores.py` con estas funciones:

- `metros_a_centimetros(metros)`
- `centimetros_a_milimetros(centimetros)`
- `horas_a_minutos(horas)`

Luego crear otro archivo llamado `conversor.py` que:

1. Importe el modulo.
2. Llame a las tres funciones con valores de prueba.
3. Muestre los resultados por pantalla.

### Ejercicio 7

Crear un modulo llamado `mensajes.py` con una funcion `despedir(nombre)` que devuelva un saludo de despedida.

Luego, desde otro archivo:

1. Importar el modulo.
2. Pedir un nombre con `input()`.
3. Mostrar el mensaje devuelto por la funcion con print().

## Parte 4: Integracion

### Ejercicio 8

Armar un programa simple de pedidos de comida dividido en funciones.

El programa debe tener al menos:

- Una funcion para pedir una comida al usuario
- Una funcion para obtener el precio segun la comida

Opciones validas:

- `pizza`
- `hamburguesa`
- `milanesa`

Al final, mostrar:

- La comida elegida
- El precio correspondiente

## Sugerencia

- Usar nombres de funciones claros.
- Guardar cada ejercicio en un archivo diferente cuando corresponda.

Cuando un programa falle, revisar tres cosas:

1. Si la funcion esta siendo llamada correctamente.
2. Si recibe los parametros esperados.
3. Si realmente devuelve un valor con `return`.
4. Si no devuelve el valor esperado revisa si no estas usando simplemente `print()`.
