---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 26. Introducción a la programación orientada a objetos

## Clases, instancias, atributos y métodos en Python

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

# Repaso express

1. ¿Qué se busca hacer con las pruebas unitarias?
2. ¿Qué pasa si una condición de `assert` resulta falsa?

---

# Formas de organizar un programa

Hasta ahora usamos variables, listas y diccionarios para guardar datos, y funciones para trabajar con ellos.

Los mismos datos y operaciones se pueden organizar de distintas maneras. A cada forma general de organización la llamamos **paradigma de programación**.

La **programación orientada a objetos** (POO, u OOP por sus siglas en inglés: *Object-Oriented Programming*) es una de esas formas: reúne datos relacionados y las operaciones que trabajan con ellos.

---

# POO y Python

La POO se desarrolló durante los años 60. Hoy es central en lenguajes como Java y C#, y también está presente en C++ y Python.

Python es **multiparadigma**: podemos organizar programas con funciones y también definir clases.

> Notita de color: En Python **todo es un objeto**: números `int`, textos `str`, listas `list`, diccionarios `dict` e incluso funciones.

---

# Clase e instancia

Una **clase** define cómo serán los objetos de un tipo: qué información guardan y qué operaciones pueden realizar.

Una **instancia** u **objeto** es un elemento concreto creado a partir de esa clase. Podemos crear varios objetos con la misma clase, y cada uno puede tener valores diferentes.

Por ejemplo, podríamos representar varios televisores. Cada uno puede estar en un canal distinto y tener su propio volumen.

---

# Nuestra primera clase

```python
class Televisor:
    pass


televisor_a = Televisor()
televisor_b = Televisor()
```

`class` define un tipo nuevo. Por ahora, `pass` deja la clase sin contenido.

`Televisor()` crea una instancia. `televisor_a` y `televisor_b` hacen referencia a dos objetos distintos de la misma clase.

---

# Observando los tipos

```python
print(type(televisor_a))  # <class '__main__.Televisor'>
print(type(televisor_b))  # <class '__main__.Televisor'>

print(type(3))          # <class 'int'>
print(type("hola"))     # <class 'str'>
```

`Televisor` es una clase definida por nosotros. `int` y `str` son tipos que Python ya ofrece.

---

# Inicializando los televisores

<!-- _class: compact -->

Ampliamos `Televisor` con `__init__`, el método de inicialización que en POO suele llamarse **constructor**. Recibe los datos al crear cada objeto y los guarda como parte de su estado.

```python
class Televisor:
    def __init__(self, ubicacion, canal, volumen):
        self.ubicacion = ubicacion
        self.canal = canal
        self.volumen = volumen


sala = Televisor("Sala", 4, 3)
cocina = Televisor("Cocina", 12, 7)
```

Python ejecuta `__init__` en cada llamada a `Televisor(...)`. `sala` y `cocina` quedan con valores diferentes.


---

# ¿Qué representa `self`?

`self` hace referencia a la instancia concreta con la que se está trabajando. Es el primer parámetro de los métodos de instancia.

```python
def __init__(self, ubicacion, canal, volumen):
    self.ubicacion = ubicacion
    self.canal = canal
    self.volumen = volumen
```

Al crear `sala`, esas asignaciones guardan sus valores en `sala`. Al crear `cocina`, los guardan en `cocina`. Al invocar el método desde un objeto, escribimos los valores que siguen a `self`.

---

# Atributos de cada instancia

Un **atributo** es un dato asociado a un objeto. Normalmente lo definimos en `__init__` con `self.nombre_del_atributo`.

```python
print(sala.ubicacion)  # Sala
print(sala.canal)      # 4
print(cocina.canal)    # 12

sala.volumen = 5
print(sala.volumen)    # 5
print(cocina.volumen)  # 7
```

Cambiar un atributo de `sala` no cambia el de `cocina`.

---

<!-- _class: inverse -->

# Ejercicio 1: libros

Creá una clase `Libro` que represente **título, autor y cantidad de páginas**.

- Creá dos libros con valores diferentes.
- Mostrá el título y la cantidad de páginas de cada uno.
- Cambiá la cantidad de páginas de uno y comprobá qué pasa con el otro.

Decidí qué datos recibe la clase al crear cada objeto y cómo quedan guardados.

---

# Atributos vs Métodos

Los **atributos** guardan datos del objeto. Los **métodos** son funciones definidas dentro de la clase que pueden consultar o modificar esos datos mediante `self`.

Una función independiente recibe los datos que necesita; un objeto conserva los suyos y sus métodos trabajan con ellos. Ambas formas pueden convivir en un programa.

---

# Agregando métodos

Un método se define **dentro de la clase**, con la misma indentación que `__init__`. Los métodos de instancia siempre reciben `self` como primer parámetro.

```python
class Televisor:
    def __init__(self, ubicacion, canal, volumen):
        self.ubicacion = ubicacion
        self.canal = canal
        self.volumen = volumen

    def volumen_porcentaje(self):
        return self.volumen * 10
```

Como una función, el método puede devolver un valor con `return` y recibir argumentos.

---

# Probando nuestro metodo `volumen_porcentaje`

`volumen_porcentaje()` lee el volumen de cada objeto y lo expresa como porcentaje.

```python
print(sala.volumen_porcentaje())    # 50
print(cocina.volumen_porcentaje())  # 70
```

> El método usa el atributo de la instancia desde la que lo invocamos.

---

# Modificando un atributo dentro de un método

Un metodo puede cambiar el valor de un atributo haciendo una operación de asignación.

```python
    def cambiar_canal(self, nuevo_canal):
        self.canal = nuevo_canal
```

```python
sala.cambiar_canal(9)

print(sala.canal)    # 9
print(cocina.canal)  # 12
```

---

# Ejercicio 2: métodos para `Libro`

Retomá la clase del ejercicio 1 y agregá estos métodos:

- `es_extenso()`: devuelve `True` si el libro tiene más de 300 páginas; en otro caso devuelve `False`.
- `ficha()`: devuelve un texto con el título y el autor.

Invocalos desde los dos libros. Probá al menos un libro de más de 300 páginas y otro de 300 o menos.

---

# Modelando una clase

Cuando pensamos en POO, solemos partir de algo del mundo real, como un auto. La forma de representarlo depende del programa.

En un programa de mantenimiento nos interesan los kilómetros recorridos y el registro de servicios. En uno de alquileres, la disponibilidad y las reservas.

Eso determina qué datos serán atributos y qué operaciones serán métodos.

---

<!-- _class: compact inverse -->

# Ejercicio integrador

Un almacén exportó su inventario a [productos.json](../recursos/productos.json). Cada producto tiene `nombre`, `precio`, `stock` y `stock_minimo`. Hay que reponer cuando el stock queda por debajo del mínimo.

Crear un programa que:

1. Lea el archivo y defina una clase `Producto`.
2. Cree una instancia por registro y guarde las instancias en una lista.
3. Incluya métodos para calcular el valor en stock e indicar si hay que reponer.
4. Recorra la lista de objetos para mostrar el valor en stock de cada producto, listar los que hay que reponer y calcular el valor total del inventario.

