---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 20. Rutas y pathlib

## `Path`, rutas multiplataforma y recorrido de carpetas

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

# Repaso express <br>Clase anterior

1. Cuando una fecha llega desde un archivo, ¿qué tipo de dato tiene antes de convertirla?
3. ¿Porque tiene sentido trabajar con las fechas en formato datetime?

---

<!-- _class: compact -->

# Trabajo previo con rutas

<div class="columns">
<div>

## Abrir un archivo

```python
open("datos/usuarios.csv", "r")
```

</div>
<div>

## Consultar una ruta

```python
import os

os.path.exists("datos/usuarios.csv")
```

</div>
</div>

En ambos casos, la ruta aparecía como un `str` necesario para llegar a un archivo.

Construirla, consultar sus partes o adaptarla a otro sistema operativo requiere manipular ese texto.

---

<!-- _class: compact -->

# Partes de una ruta

Una ruta describe cómo localizar un archivo o directorio dentro del sistema de archivos.

```text
proyecto/
├── main.py
└── datos/
    ├── usuarios.csv
    └── reportes/
        └── reporte_2026.csv
```

| Parte | Ejemplo |
|---|---|
| Directorio base | `proyecto` |
| Subdirectorios | `datos/reportes` |
| Archivo | `reporte_2026.csv` |
| Extensión | `.csv` |

La ruta completa es `proyecto/datos/reportes/reporte_2026.csv`.

---

<!-- _class: compact -->

# Rutas en Linux y Windows

Las rutas en Linux y Windows son diferentes.

<div class="columns">
<div>

## Linux

```text
/home/homero/proyecto/datos/usuarios.csv
```

- La raíz es `/`.
- El separador habitual es `/`.
- Una carpeta personal puede ser `/home/homero`.

</div>
<div>

## Windows

```text
C:\Users\homero\proyecto\datos\usuarios.csv
```

- Usa unidades como `C:`.
- El separador tradicional es `\`.
- Una carpeta personal puede ser `C:\Users\homero`.

</div>
</div>

---

<!-- _class: compact -->

# Rutas absolutas y relativas

<div class="columns">
<div>

## Absolutas

Indican la ubicación desde la raíz del sistema:

```text
/home/homero/proyecto/datos/usuarios.csv
```

```text
C:\Users\homero\proyecto\datos\usuarios.csv
```

</div>
<div>

## Relativas

Parten desde el directorio de trabajo actual:

```text
datos/usuarios.csv
```

</div>
</div>

La ruta se interpreta desde el directorio de trabajo actual.

---

<!-- _class: compact -->

# Librería `pathlib`

`pathlib` forma parte de Python y permite representar las rutas como objetos en lugar de manipularlas solamente como texto.

Su clase principal es `Path`. Con ella podemos:

- construir rutas que funcionen en distintos sistemas operativos;
- consultar sus partes y verificar si representan archivos o directorios;
- recorrer carpetas y usar las rutas directamente con `open()`.

---

<!-- _class: compact -->
<!-- _footer: "[DataCamp: guía de pathlib](https://www.datacamp.com/es/tutorial/comprehensive-tutorial-on-using-pathlib-in-python-for-file-system-manipulation)" -->

# Nuestro primer `Path`

<div class="columns">
<div>

## Como texto

```python
carpeta = "datos"
archivo = "usuarios.csv"

ruta = carpeta + "/" + archivo
print(ruta)
```

Tenemos que agregar el separador manualmente.

</div>
<div>

## Como ruta

```python
from pathlib import Path

ruta = Path("datos/usuarios.csv")

print(ruta)
print(type(ruta))
```

`Path` representa una ruta usando las reglas del sistema donde se ejecuta Python.

</div>
</div>

---

<!-- _class: compact -->

# De relativa a absoluta

```python
from pathlib import Path

actual = Path.cwd()  # Directorio de trabajo actual
ruta = Path("datos/usuarios.csv")

print(actual)
print(ruta)
print(ruta.resolve())
```

`resolve()` permite observar la ruta absoluta correspondiente.

---

<!-- _class: compact -->

# Construir rutas con `pathlib`

```python
from pathlib import Path

base = Path("datos")
archivo = base / "reportes" / "reporte_2026.csv"

desde_actual = Path.cwd() / archivo
desde_home = Path.home() / "proyecto" / archivo

print(archivo)
print(desde_actual)
print(desde_home)
```

El operador `/` combina las partes de una ruta.

- `Path.cwd()` representa el directorio desde donde trabaja el programa.
- `Path.home()` representa la carpeta personal del usuario.

---

<!-- _class: compact -->
<!-- _footer: "[Python docs: componentes de rutas](https://docs.python.org/es/3/library/pathlib.html)" -->

# Inspeccionar una ruta

<div class="columns">
<div>

```python
from pathlib import Path

archivo = Path(
    "datos/reportes/reporte_2026.csv"
)

print(archivo.name) # nombre completo del archivo
print(archivo.stem) # nombre del archivo sin extension
print(archivo.suffix) # extensión del archivo
print(archivo.parent) # rutas padre
```

</div>
<div>

| Atributo | Resultado |
|---|---|
| `name` | `reporte_2026.csv` |
| `stem` | `reporte_2026` |
| `suffix` | `.csv` |
| `parent` | `datos/reportes` |

</div>
</div>

Estos atributos describen la ruta sin abrir el archivo ni descomponer manualmente sus partes.

---

<!-- _class: compact -->

# Existencia y tipo

```python
from pathlib import Path

ruta = Path("datos")

print(ruta.exists())
print(ruta.is_file())
print(ruta.is_dir())
```

| Método | Verifica |
|---|---|
| `exists()` | La ruta existe actualmente |
| `is_file()` | La ruta existe y es un archivo |
| `is_dir()` | La ruta existe y es un directorio |

---

<!-- _class: compact -->

# Usar un `Path` con `open()`

```python
from pathlib import Path

ruta = Path("datos") / "usuarios.csv"

with open(ruta, "w") as archivo:
    archivo.write("nombre,puntaje\nLisa,95\nBart,70\n")

with open(ruta, "r") as archivo:
    contenido = archivo.read()

print(contenido)
```

`open()` acepta un objeto `Path`: no hace falta convertirlo a `str`.

---

<!-- _class: compact -->
<!-- _footer: "[Python docs: recorrido de directorios](https://docs.python.org/es/3/library/pathlib.html#pathlib.Path.iterdir)" -->

# Recorrer una carpeta

```python
from pathlib import Path

carpeta = Path("datos")

for elemento in carpeta.iterdir():
    print(elemento.name)
    print("  Archivo:", elemento.is_file())
    print("  Directorio:", elemento.is_dir())
```

`iterdir()` recorre el contenido directo de una carpeta.

Cada elemento obtenido también es un `Path`, por eso podemos consultar su nombre y su tipo.

---

<!-- _class: compact -->

# Ejercicio integrador

<div class="columns">
<div>

```text
archivos_simpsons/
├── personajes.txt
├── episodios.csv
├── configuracion.json
└── imagenes/
    └── homero
        └── imagen_1.png
        └── imagen_2.png
```

Crear un programa `main.py` que use `Path` para representar `archivos_simpsons`.

</div>
<div>

El programa debe:

1. mostrar la ruta absoluta con `resolve()`;
2. recorrer el contenido de la carpeta actual;
3. indicar el nombre y si cada elemento es archivo o directorio;
4. mostrar la extensión de cada archivo.
4. Si el elemento es un directorio, mostrar su contenido;

</div>
</div>