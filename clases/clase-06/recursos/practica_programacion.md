# Práctica - Programación 1

**REGLA:** No utilizar Python para realizar estos ejercicios. El parcial será en papel y no habrá ayuda del intérprete.  
Responder en este mismo documento.

---

## Ejercicio 1 - Tipos de datos

Indicar qué tipo de dato devuelve cada expresión:

```
8 < 2: __________  
"perro" != "gato": __________  
"Hola" * 2: __________  
9 / 2: __________  
9 // 2: __________  
```

---

## Ejercicio 2 - Lectura de código

Explicar con tus palabras qué hace el siguiente código:

```
numeros = [2, 4, 6, 8]
contador = 0

for numero in numeros:
    if numero > 4:
        contador = contador + 1

print(contador)
```

Explicar el comportamiento general, no línea por línea.

---

## Ejercicio 3 - Análisis

¿El siguiente código funciona correctamente?  
En caso de que no funcione, explicar por qué.

```
valores = [10, 20, 30]
print(valores[2])
print(valores[3])
```

---

## Ejercicio 4 - Desarrollo

Se pide desarrollar un sistema de registro de números:

1. Pedir números al usuario hasta que ingrese 0.  
2. Guardarlos en una lista.

Luego, crear una función que:

- Reciba la lista.  
- Muestre:
  - Cantidad total de números ingresados (sin usar `len`).
