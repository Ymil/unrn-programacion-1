---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 25. Testing básico con `pytest`

## Pruebas unitarias automaticas

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

# Conceptos: ¿Qué significa probar un programa?

Probar es ejecutar el código con una entrada conocida y comparar lo que devuelve con lo que **debería** devolver.

Por ejempo, queremos una función que nos ayude a calcular el vuelto.

```python
def calcular_vuelto(total, pagado):
    return total - pagado
```

```text
entrada:   total=1800, pagado=2000
esperado:  200   (cuenta a mano)
obtenido:  -200   no coincide
```

---

<!-- class: compact -->

# Conceptos: Pruebas manuales y automáticas

Podemos comprobar el funcionamiento de un programa de forma **manual** o **automática**.

| Prueba manual | Prueba automática |
|---|---|
| Una persona ejecuta el programa o una función. | La prueba ejecuta el código automáticamente. |
| La persona prepara o ingresa los datos. | Los datos de entrada quedan definidos en la prueba. |
| La persona observa el resultado. | La prueba compara el resultado obtenido con el esperado. |
| La persona decide si el comportamiento es correcto. | La herramienta informa si la prueba pasó o falló. |

Las pruebas manuales son útiles para explorar un programa o verificar comportamientos puntuales.
Las pruebas automáticas permiten repetir las mismas comprobaciones después de cada cambio. Esto se vuelve especialmente importante en sistemas grandes o críticos, donde un error puede tener consecuencias importantes y no alcanza con revisar todo “a ojo”.

---

# Conceptos: Pruebas unitarias

En esta clase nos vamos a centrar en las **pruebas unitarias**.

Las pruebas unitarias verifican pequeñas partes de un programa de forma independiente, por ejemplo una función.

Cada prueba ejecuta esa unidad con una entrada conocida y comprueba que produzca el resultado esperado.

Una misma función puede necesitar varias pruebas para comprobar sus distintos comportamientos.

---

<!-- _class: compact -->

# Conceptos: ¿Qué es un caso de prueba?

Un **caso de prueba** es una situación concreta que usamos para comprobar el comportamiento de una función o programa.

<div class="columns">
<div>

Normalmente define:

- una **entrada**;
- un **resultado esperado**;
- y qué comportamiento queremos verificar.

</div>
<div>
Por ejemplo:

```text
Función: puede_votar(edad)

Entrada: 18
Resultado esperado: True
```
</div></div>

Una función suele necesitar varios casos de prueba porque puede tener distintos comportamientos según los datos que recibe.

---

<!-- _class: compact -->

# Conceptos: Elegir casos de prueba

No existe una única lista de casos que sirva para todas las funciones.

Los casos se eligen según el **comportamiento esperado de la función**: sus condiciones, rangos válidos, entradas especiales y posibles errores.

Algunos criterios habituales para elegir entradas son:

| Criterio | Qué buscamos comprobar | Ejemplo: edad mínima de 18 |
|---|---|---|
| Caso normal | Un comportamiento habitual. | `25` |
| Caso límite | Un valor donde cambia el comportamiento. | `18` |
| Caso inválido | Una entrada que la función debería rechazar o manejar. | `-4` |

Estos criterios no son los únicos. Una función puede necesitar otros casos según lo que deba hacer.

---

# Construyendo casos de prueba

Antes de escribir una prueba necesitamos entender **qué comportamientos tiene la función** y elegir entradas que nos permitan comprobarlos.

<div class="columns">
<div>

## Función 1

```python
def normalizar_estado(estado):
    estado = estado.strip().lower()

    if estado == "activo" or estado == "inactivo":
        return estado

    raise ValueError("Estado inválido")
```


</div>
<div>

## Función 2

```python
def clasificar_velocidad(velocidad):
    if velocidad < 0:
        raise ValueError("Velocidad inválida")

    if velocidad <= 60:
        return "baja"

    return "alta"
```

</div>
<div>

---

<!-- _class: compact -->
<!-- _footer: "[Python: sentencia assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)" -->

# Nuestro primer test en python

Python nos da mecanismos nativos para verificar datos mediante la sentencia `assert`.

```python
def sumar(a, b):
    return a + b


assert sumar(2, 3) == 5
```

- Si la condición es `True`, la ejecución continúa y no aparece ningún mensaje.
- Si la condición es `False`, Python detiene esa ejecución con `AssertionError`.

```python
assert sumar(2, 3) == 6
# AssertionError
```

`assert` expresa una condición que esperamos que sea verdadera.

---

<!-- _class: compact inverse -->

# Introducción a `pytest`

`pytest` es una herramienta para escribir y ejecutar pruebas automáticas en Python. Busca las pruebas del proyecto, las ejecuta y presenta un resumen de los resultados.

Cuando una comprobación falla, informa en qué prueba ocurrió y muestra los valores obtenidos para ayudar a encontrar la diferencia.

Si todavía no está instalado:

```bash
pip install pytest
```

Verificar la instalación:

```bash
pytest --version
```

---

<!-- _class: compact -->

# Primera prueba con `pytest`

```text
proyecto/
├── operaciones.py
└── test_operaciones.py
```

<div class="columns">
<div>

**operaciones.py**

```python
def sumar(a, b):
    return a + b
```

</div>
<div>

**test_operaciones.py**

```python
from operaciones import sumar


def test_sumar_dos_positivos():
    assert sumar(2, 3) == 5
```

</div>
</div>

---

## Ejecutar la prueba

Desde la carpeta `proyecto/`:

```bash
pytest
```

```text
collected 1 item

test_operaciones.py .                                    [100%]

========================= 1 passed =========================
```

El punto representa una prueba que pasó. El resumen informa cuántas se ejecutaron.


---

<!-- _footer: "[pytest: primeros pasos y descubrimiento de pruebas](https://docs.pytest.org/en/stable/getting-started.html)" -->

# Nombre archivos y funciones

PyTest busca de forma automatica las pruebas, pero para estó los archivos de prueba y sus funciones deben comenzar con el prefijo `test_`.

- el archivo comienza con `test_`;
- la función comienza con `test_`;


---

# Haciendo fallar nuestra prueba

Modificamos temporalmente la expectativa:

```python
def test_sumar_dos_positivos():
    assert sumar(2, 3) == 6
```

Ejecutamos otra vez:

```bash
pytest
```

La función sigue devolviendo `5`, pero la prueba espera `6`. Uno de los dos comportamientos debe corregirse.

Después de observar el fallo, restauramos el resultado esperado a `5`.

---

<!-- _class: compact -->
<!-- _footer: "[pytest: información de los assert fallidos](https://docs.pytest.org/en/stable/how-to/assert.html)" -->

# Leer el reporte de un fallo

```text
________________ test_sumar_dos_positivos _________________

    def test_sumar_dos_positivos():
>       assert sumar(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = sumar(2, 3)

test_operaciones.py:5: AssertionError
======================= short test summary info =======================
FAILED test_operaciones.py::test_sumar_dos_positivos - assert 5 == 6
============================ 1 failed ============================
```

El reporte ubica la prueba y muestra la comparación: se obtuvo `5` y se esperaba `6`.

---

<!-- _class: compact -->

# Implementado Prueba: Empresa logistica

<div class="columns">
<div>

Una empresa calcula el costo de envío según el peso:

| Peso | Costo |
|---|---:|
| Hasta 1000 g inclusive | $2500 |
| Más de 1000 g y hasta 5000 g | $4500 |
| Más de 5000 g | $7000 |

Un peso menor o igual que cero es inválido y produce `ValueError`.

</div>
<div>

```python
def calcular_costo_envio(peso_gramos):
    if peso_gramos <= 0:
        raise ValueError("El peso debe ser mayor que cero")
    if peso_gramos <= 1000:
        return 2500
    if peso_gramos <= 5000:
        return 4500
    return 7000
```

</div>
</div>

---

# Probando casos normales

```python
from operaciones import calcular_costo_envio


def test_costo_envio_paquete_liviano():
    assert calcular_costo_envio(500) == 2500


def test_costo_envio_paquete_pesado():
    assert calcular_costo_envio(6000) == 7000
```

Los dos valores representan caminos diferentes dentro de la la función.

El nombre de cada prueba anticipa qué situación comprueba.

---

# Probando límite y valor cercano

```python
def test_costo_envio_en_el_primer_limite():
    assert calcular_costo_envio(1000) == 2500


def test_costo_envio_despues_del_primer_limite():
    assert calcular_costo_envio(1001) == 4500
```

Estos casos permiten revisar el significado de “hasta 1000 g inclusive”.

| Entrada | Qué comprueba |
|---:|---|
| 1000 | El límite todavía pertenece al primer precio. |
| 1001 | El siguiente valor pertenece al segundo precio. |

---

<!-- _class: compact -->
<!-- _footer: "[pytest: comprobar excepciones esperadas](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions)" -->

# Probando un caso inválido

```python
import pytest

from operaciones import calcular_costo_envio


def test_costo_envio_con_peso_invalido():
    with pytest.raises(ValueError):
        calcular_costo_envio(0)
```

La prueba pasa solamente si la llamada produce `ValueError`.

No estamos “evitando” el error: estamos comprobando que la función rechace una entrada inválida de la manera acordada.

---

<!-- _class: inverse compact -->

# Ejercicio 1: nivel de batería

<div class="columns">
<div>
Escriban la función `clasificar_nivel_bateria(porcentaje)` en `bateria.py`. Debe recibir un porcentaje entero y devolver:

- `"baja"` entre 0 y 20 inclusive;
- `"media"` entre 21 y 80 inclusive;
- `"alta"` entre 81 y 100 inclusive;
- produce `ValueError` fuera del rango de 0 a 100.
    - `raise ValueError("El porcentaje debe estar entre 0 y 100")`

</div>
<div>
Antes de escribir las pruebas, escriban los tipos de casos que cubran los distintos comportamientos, por ejemplo:

- Normal para bajo, medio y alto
- Límites para bajo, medio y alto
- Inválido

Luego crear `test_bateria.py` implementando los casos.

Ejecuten `pytest` y usen el reporte para corregir el código o la expectativa que no coincida con el comportamiento acordado.
</div>
</div>

---

<!-- _class: compact -->
<!-- _footer: "[pytest-cov: instalación y uso](https://pytest-cov.readthedocs.io/en/latest/readme.html)" -->

# Cobertura de las pruebas

La **cobertura** indica qué parte del código fue ejecutada mientras corrían las pruebas. Puede ayudar a encontrar líneas que todavía no fueron probadas.

Instalar el complemento `pytest-cov`:

```bash
pip install pytest-cov
```

Ejecutar las pruebas y generar un reporte HTML:

```bash
pytest --cov=. --cov-report=html
```

- `--cov=.` mide los archivos Python de la carpeta actual.
- `--cov-report=html` crea el reporte visual dentro de `htmlcov/`.

---

<!-- _class: compact -->
<!-- _footer: "[pytest-cov: formatos de reporte](https://pytest-cov.readthedocs.io/en/latest/reporting.html)" -->

# Reporte visual de cobertura

![w:1000 Captura del reporte HTML de cobertura generado para los recursos de la clase.](../recursos/cobertura-html.png)

Abrimos `htmlcov/index.html` en el navegador. El reporte muestra cuántas sentencias se ejecutaron, cuántas faltaron y el porcentaje de cobertura de cada archivo.

> **Dato de color:** **80 %** suele ser el umbral nominal de cobertura esperado, aunque esto no garantiza la calidad de las mismas.

---

<!-- _class: inverse compact -->

# Ejercicio integrador

<div class="columns">
<div>

El objetivo es incorporar pruebas automáticas al Proyecto Integrador para verificar funciones existentes que transforman o validan datos.

**Funciones posibles:**

- Filtrar datos.
- Calcular estadísticas.
- Validar un dato.
- Construir un nombre de archivo.

</div>
<div>

1. Elijan al menos dos funciones existentes.
2. Para cada una escriban un caso normal, uno límite y, cuando corresponda, uno inválido.
3. Guarden las pruebas en uno o más archivos `test_*.py`.
4. Agreguen `pytest` al `requirements.txt` y ejecuten `pytest`.

Usen datos pequeños y resultados esperados fáciles de revisar.

</div>
</div>

> Subir las pruebas al repositorio git.
