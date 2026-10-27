---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 27. Herencia y polimorfismo

## Programación Orientada a Objetos en Python

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

1. ¿Qué diferencia hay entre una clase y una instancia?
2. ¿Cuándo se ejecuta `__init__`?
3. ¿Qué representa `self` dentro de un método?

---

# Modelando sensores

Pensemos en los **sensores de una chacra**:

- Todos tienen una **ubicación** y el **último valor medido**. Esas características serán los **atributos**; cada sensor tendrá sus propios valores.
- Todos pueden **actualizar** ese valor y **mostrarlo**. Esas acciones serán sus **métodos**.

Cada sensor instalado en la chacra va a ser una instancia. Lo que cambia entre los tres tipos es la unidad y algo que solo ese sensor sabe hacer, avisar si hay heladas o vientos fuertes.

---

<!-- _class: inverse -->

# Herencia

La **herencia** permite crear una clase a partir de otra. La clase nueva tiene los atributos y métodos de la primera y puede agregar los suyos.

---

<!-- _class: compact -->

# Un sensor de temperatura y uno de viento

<div class="columns">
<div>

```python
class SensorTemperatura:
    def __init__(self, ubicacion, valor):
        self.ubicacion = ubicacion
        self.valor = valor

    def actualizar(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"{self.ubicacion}: {self.valor}")
```

</div>
<div>

```python
class SensorViento:
    def __init__(self, ubicacion, valor):
        self.ubicacion = ubicacion
        self.valor = valor

    def actualizar(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"{self.ubicacion}: {self.valor}")
```

</div>
</div>

`__init__`, `actualizar()` y `mostrar()` están escritos dos veces. Si cambia la forma de mostrar un sensor, hay que corregirlo en cada clase, y con un tercer tipo serían tres.

---

<!-- _class: compact -->
<!-- _footer: "[Python: herencia](https://docs.python.org/es/3/tutorial/classes.html#inheritance)" -->

# Clase base y clase derivada

<div class="columns">
<div>

- **Clase base** (o clase padre): la que ya existe, con lo común.
- **Clase derivada** (o clase hija): hereda de la base y agrega lo propio.

```python
class ClaseHija(ClasePadre):
    ...
```

</div>
<div>

```text
Sensor
├── SensorTemperatura
└── SensorViento
```

Lo común se escribe una sola vez en `Sensor`. Cada clase hija suma lo que le es propio.

</div>
</div>

---

<!-- _class: compact -->

# Creando nuestras primeras clases hijas

Una clase hija hereda todo lo de la clase base, aunque no escriba nada.

<div class="columns">
<div>

```python
class Sensor:
    def __init__(self, ubicacion, valor):
        self.ubicacion = ubicacion
        self.valor = valor

    def actualizar(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"{self.ubicacion}: {self.valor}")
```

- Las clases hijas están vacías y aun así tienen `__init__`, atributos y métodos.
- Python busca cada método en la clase del objeto. Si no está, lo busca en `Sensor`.

</div>
<div>

```python
class SensorTemperatura(Sensor):
    pass


class SensorViento(Sensor):
    pass


chacra = SensorTemperatura("Chacra norte", 3)
molino = SensorViento("Molino", 45)

molino.actualizar(72)
chacra.mostrar()    # Chacra norte: 3
molino.mostrar()    # Molino: 72
```

</div>
</div>

---

<!-- _class: compact -->

# Agregando métodos a las clases hijas

Una clase hija puede agregar métodos propios, que la clase base no tiene.

<div class="columns">
<div>

```python
class SensorTemperatura(Sensor):
    def hay_helada(self):
        return self.valor < 0


class SensorViento(Sensor):
    def hay_viento_fuerte(self):
        return self.valor > 60
```

- Usan `self.valor`, un atributo que viene de `Sensor`.
- La herencia va de la base a la hija: `SensorViento` no tiene `hay_helada()`.

</div>
<div>

```python
chacra.actualizar(-2)
molino.actualizar(72)

print(chacra.hay_helada())
print(molino.hay_viento_fuerte())
print(molino.hay_helada())
```

```text
True
True
AttributeError: 'SensorViento' object has no
attribute 'hay_helada'
```

</div>
</div>

---

<!-- _class: compact -->

# Agregando atributos a una clase hija

Una clase hija puede tener su propio constructor, `__init__`, para agregar atributos.

<div class="columns">
<div>

```python
class SensorViento(Sensor):
    def __init__(self, ubicacion, valor, limite):
        super().__init__(ubicacion, valor)
        self.limite = limite

    def hay_viento_fuerte(self):
        return self.valor > self.limite
```

- `super().__init__(ubicacion, valor)` reutiliza el `__init__` de `Sensor`, sin repetir sus asignaciones.
- La hija solo escribe lo propio: `limite`.

</div>
<div>

```python
molino = SensorViento("Molino", 72, 60)
antena = SensorViento("Antena", 72, 90)

print(molino.hay_viento_fuerte())
print(antena.hay_viento_fuerte())
print(molino.ubicacion)
```

```text
True
False
Molino
```

</div>
</div>

---

<!-- _class: compact -->

# Ejercicio 1: bombas y calefactores

Una chacra tiene distintos actuadores: bombas para regar los cultivos, calefactores para proteger los frutales de las heladas. Todos se encienden y se apagan.

1. Escribir una clase base (o padre) `Actuador` con un nombre y un atributo `encendido`, que arranca en `False`.
    - Debe tener los metodos `encender()` y `apagar()` lo cambian y muestran el estado junto a la ubicación. 
    - Debe tener un método `estado()` que devuelve `"encendido"` o `"apagado"`.
2. Escribir las clases hijas `Bomba` y `Calefactor`, a partir de `Actuador`.

<div class="columns">
<div>

3. Crear `"Bomba 1"` y `"Calefactor 3"`. 
    - Encender las dos, apagar la bomba y mostrar con `estado()` cómo quedó cada una.

</div>
<div>


```text
# Salida esperada
Bomba 1: encendido
Calefactor 3: encendido
Bomba 1: apagado
apagado
encendido
```

</div>
</div>

---

<!-- _class: compact -->

# Sobrescribiendo un método

Una clase hija puede cambiar un método heredado escribiendolo de nuevo con el mismo nombre.

<div class="columns">
<div>

```python
class SensorTemperatura(Sensor):
    def mostrar(self):
        print(f"{self.ubicacion}: {self.valor} °C")


class SensorViento(Sensor):
    pass
```

</div>
<div>

```python
chacra = SensorTemperatura("Chacra norte", -2)
molino = SensorViento("Molino", 72)

chacra.mostrar()    # Chacra norte: -2 °C
molino.mostrar()    # Molino: 72
```

</div>
</div>

`SensorTemperatura` **sobrescribe** `mostrar()`: para sus objetos, la versión de la hija reemplaza a la de `Sensor`. `SensorViento` sigue heredando la suya.

> `__init__` de `SensorViento` también es una sobrescritura. La hija definió el suyo y, con `super()`, reutilizó el `__init__` de `Sensor`.

---

<!-- _class: compact -->

# Reutilizando el método de la base

Una clase hija puede sobrescribir un método y, aun así, usar el de la clase base llamándolo con `super()`.

<div class="columns">
<div>

```python
class Sensor:
    # __init__ y actualizar igual que antes
    def mostrar(self):
        print(f"{self.ubicacion}: {self.valor}")


class SensorTemperatura(Sensor):
    def mostrar(self):
        super().mostrar()
        if self.valor < 0:
            print("Hay helada")
```

</div>
<div>

```python
chacra = SensorTemperatura("Chacra norte", -2)
chacra.mostrar()
# Chacra norte: -2
# Hay helada

chacra.actualizar(5)
chacra.mostrar()
# Chacra norte: 5
```

</div>
</div>

`super().mostrar()` ejecuta la versión de `Sensor`, y la hija agrega lo suyo. Es la misma idea que con `__init__`.

---

<!-- _class: compact -->

# Ejercicio 2: regando

Retomar las clases del ejercicio 1: ahora las bombas llevan la cuenta de sus riegos.

1. Darle a `Bomba` su propio constructor, con un contador de riegos que arranque en cero. Reutilizar el de `Actuador` con `super()`.
2. Hacer que, al encenderse, muestre `Bomba 1: regando` en lugar de `Bomba 1: encendido` y sume un riego.
3. Agregar el método `total_riegos()`, que devuelve cuántos riegos hizo.
4. Hacer que `estado()` devuelva `"regando"` si la bomba está encendida y, si no, lo mismo que cualquier actuador. Reutilizar el `estado()` de `Actuador` con `super()`.
5. Crear `"Bomba 1"`, encenderla, apagarla y volver a encenderla. Mostrar el estado de la bomba después de cada paso y, al final, el total de riegos.

---

# Salida esperada

```text
Bomba 1: regando
regando
Bomba 1: apagado
apagado
Bomba 1: regando
regando
2
```

---

<!-- _class: inverse -->

# Polimorfismo

Permitir que objetos de diferentes clases respondan al mismo mensaje o método, pero cada uno ejecutando su propia versión o comportamiento

---

<!-- _class: compact -->

# Los sensores de la chacra

Sumamos el sensor de humedad. Cada objeto usa el `mostrar()` que le corresponde según su clase.

<div class="columns">
<div>

```python
class SensorHumedad(Sensor):
    def mostrar(self):
        print(f"{self.ubicacion}: {self.valor} %")


chacra = SensorTemperatura("Chacra norte", -2)
molino = SensorViento("Molino", 72, 60)
invernadero = SensorHumedad("Invernadero", 65)
```

</div>
<div>

| Objeto | `mostrar()` que se ejecuta |
|---|---|
| `chacra` | el de `SensorTemperatura`, que reutiliza el de `Sensor` con `super()` |
| `molino` | el que heredó de `Sensor` |
| `invernadero` | el de `SensorHumedad` |

</div>
</div>

---

<!-- _class: compact -->

# Una función para cualquier sensor

Una función puede recibir objetos de distintas clases y usarlos con la misma operación.

<div class="columns">
<div>

```python
def mostrar_sensor(sensor):
    sensor.mostrar()


mostrar_sensor(chacra)
# Chacra norte: -2
# Hay helada
mostrar_sensor(molino)
# Molino: 72
mostrar_sensor(invernadero)
# Invernadero: 65 %
```

</div>
<div>

- Recibe objetos de tres clases diferentes.
- Siempre ejecuta la misma instrucción: `sensor.mostrar()`.
- No pregunta si recibió un sensor de temperatura, de viento o de humedad.
- Cada objeto determina qué versión de `mostrar()` se ejecuta, propia o heredada.

</div>
</div>

Lo mismo pasa si los sensores están en una lista: un `for` puede pasarle cada uno a `mostrar_sensor()`.

---

<!-- _class: compact -->

# Sin polimorfismo

<div class="columns">
<div>

**Preguntando la clase**

```python
def mostrar_sensor(sensor):
    if type(sensor) == SensorTemperatura:
        ...  # valor y aviso de helada
    elif type(sensor) == SensorViento:
        ...  # valor
    elif type(sensor) == SensorHumedad:
        ...  # valor con %
```

</div>
<div>

**Llamando al método**

```python
def mostrar_sensor(sensor):
    sensor.mostrar()
```

</div>
</div>

- La primera tiene que conocer cada clase concreta: un sensor nuevo obliga a sumar otro `elif`.

> Con polimorfismo, el código que usa al objeto no necesita decidir qué versión del método ejecutar.

---

<!-- _class: inverse -->

# Ejercicio integrador

1. Definir una clase `Animal` con un nombre y un método `hablar()`.
2. Definir `Perro`, `Gato` y `Vaca`, que hereden de `Animal` y sobrescriban `hablar()` con el sonido de cada uno.
3. Crear un animal de cada tipo y hacer que todos hablen, sin preguntar de qué clase es cada uno.
4. Incorporar un `Pato` y hacerlo hablar junto con los demás, sin cambiar la forma en que se hace hablar a los animales.

---

# Salida esperada

```text
Firulais: Guau
Michi: Miau
Lola: Muuu
Donald: Cuac
```
