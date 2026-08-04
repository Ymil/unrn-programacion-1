---
marp: true
theme: unrn-programacion
size: 16:9
paginate: false
---

<!-- _class: title -->
<!-- _paginate: false -->

# 3.0 Condicionales e iterador FOR

## IF, ELSE, ELIF, AND, OR y FOR

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
  <img src="./logo.png" alt="Logo UNRN">
  <span>UNIVERSIDAD<br>NACIONAL</span>
</div>

---

<!-- _class: inverse -->

# Repaso express

- ¿Qué vimos la clase anterior?
- ¿Qué problema intentamos resolver?
- ¿Qué herramienta nueva aparece hoy?

---

# Objetivos de la clase

- Entender el concepto principal.
- Ver ejemplos cortos en Python.
- Practicar con consignas incrementales.

---

# Concepto clave

Las funciones nos permiten agrupar código para construir **bloques reutilizables** que encapsulan una tarea específica.

> Una buena función tiene un nombre claro, recibe datos si los necesita y devuelve un resultado cuando corresponde.

---

# Ejemplo en Python

```python
def saludar(nombre):
    return f"Hola {nombre}"

mensaje = saludar("Ana")
print(mensaje)
```

---

<!-- _class: compact -->

# Dos formas de pensarlo

<div class="columns">
<div>

## Sin función

```python
nombre = input("Nombre: ")
print(f"Hola {nombre}")
```

</div>
<div>

## Con función

```python
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Ana")
```

</div>
</div>

---

# Ejercicio

Escribir una función `es_par(numero)` que devuelva `True` si el número es par y `False` en caso contrario.

1. Resolverlo con `if`.
2. Probarlo con tres números.
3. Mejorarlo usando una expresión booleana directa.

---

<!-- _class: inverse -->

# Cierre

- ¿Qué parte quedó menos clara?
- ¿Qué ejemplo conviene practicar de nuevo?
- ¿Qué se llevan para resolver en casa?
