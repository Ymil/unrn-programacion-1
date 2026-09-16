---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 21. Introducción a Pandas

## Datos organizados en filas y columnas

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

1. ¿Para que usamos `PathLib`?
2. ¿Que hace la función `Path.cwd()`?

---

# Ambiente de trabajo: Jupyter Notebook

<!-- _class: compact -->

# ¿Qué es un notebook?

Un notebook es un documento interactivo formado por **celdas** que puede contener codigo python. Es muy utilizado en el ambito de la ciencia de datos dado que permite escribir codigo como documento y mostrar sus resultados.

- Las celdas de código contienen instrucciones de Python.
- Las celdas de texto, escritas en Markdown, permiten agregar títulos y explicaciones.

## Instanlando jupyter en VS Code.

1. Abrir **Extensiones** con `Ctrl + Shift + X`.
2. Buscar `ms-toolsai.jupyter`.
3. Elegir **Jupyter**, publicada por **Microsoft**, e instalarla.

---

<!-- _class: compact -->

# Creando nuestro primer notebook

1. Crear un archivo `primer_notebook.ipynb`.
2. Presionar **Seleccionar kernel** y elegir el entorno de Python del virtual environment.
3. Escribir el código en una celda y ejecutarla con `Shift + Enter`.

```python
temperaturas = [4, 7, 9]
promedio = sum(temperaturas) / len(temperaturas)
promedio
```

Jupyter muestra la última expresión debajo de la celda.

Las variables quedan disponibles mientras el notebook esté abierto.

---

# Hay que tener en cuenta el orden de ejecución

```python
# Celda 1
consumos = [120, 135, 128]
```

```python
# Celda 2
mayor_consumo = max(consumos)
mayor_consumo
```

La segunda celda usa una variable creada en la primera. Conviene ejecutar el notebook de arriba hacia abajo.

Al reiniciar el kernel se borran las variables y podemos volver a ejecutar todo desde el comienzo.

---

<!-- _class: inverse -->

# Arrancando con Pandas

## Explorar, filtrar y transformar datos desde Python

---

# ¿Qué es Pandas?

Pandas es una librería de Python orientada al trabajo con **datos estructurados**, especialmente datos organizados en filas y columnas.

Permite trabajar con una tabla desde Python sin dejar de usar los conceptos de variables, tipos, condiciones, archivos y funciones que ya conocemos.

> Es como un excel pero en Python.

---

# Operaciones habituales

Con Pandas podemos:

- leer y guardar archivos CSV;
- inspeccionar filas y columnas;
- seleccionar y filtrar datos;
- ordenar registros;
- calcular valores sobre columnas;
- agrupar información.

La libreria es enorme, vamos a trabajar sobre unas pocas funciones.



---

# Instalar e importar

La instalación se realiza una vez desde la terminal, con un virtual environment creado:

```bash
pip install pandas
```

En cada programa que use la librería:

```python
import pandas as pd
```

Pandas es una librería externa. `pd` es el alias usado habitualmente.


---

<!-- _class: compact -->

# Del CSV a una estructura de datos

<div class="columns">
<div>

## Lectura manual

Tendríamos que ocuparnos de:

- reconocer el encabezado;
- respetar las comas dentro de las descripciones;
- convertir números y fechas;
- representar los datos faltantes.

</div>
<div>

## Con Pandas

```python
import pandas as pd

simpsons = pd.read_csv("SimpsonsData.csv")
```

Pandas se ocupa de leer los episodios y organizar sus columnas.

</div>
</div>

---

<!-- _class: compact -->

# Dataset para los ejemplos

Para los ejemplos voy a usar `SimpsonsData.csv`.

| Columna | Información registrada |
|---|---|
| `Season` | temporada |
| `Title` | título del episodio |
| `Airdate` | fecha de emisión |
| `Rating` | calificación |
| `Vote_count` | cantidad de votos |
| `Description` | descripción del episodio |


> Una dataset es un conjunto de datos, se pueden encontrar muchos en paginas como kaggle.

---

# Leer el CSV

```python
import pandas as pd

simpsons = pd.read_csv("SimpsonsData.csv")
simpsons
```

`read_csv()` lee el archivo y devuelve un DataFrame. La variable `simpsons` contiene ahora la tabla completa.

---

# La estructura principal de pandas: DataFrame

Un `DataFrame` es la estructura principal de Pandas para datos tabulares.

| índice | Season | Title | Rating |
|---:|---:|---|---:|
| 0 | 1 | Simpsons Roasting on an Open Fire | 8.2 |
| 1 | 1 | Bart the Genius | 7.7 |

- Cada **fila** representa un registro.
- Cada **columna** reúne un tipo de información.
- El **índice** identifica las filas; por defecto comienza en `0`.

`type(simpsons)`

---

<!-- _class: compact -->

# Métodos `head()` y `tail()`

```python
simpsons.head(3)
```

```python
simpsons.tail(3)
```

`head()` muestra las primeras filas y `tail()` las últimas. El número entre paréntesis indica cuántas queremos ver.

Por defecto devuelven cinco filas.

---

# Tamaño, nombres y tipos

```python
print(simpsons.shape)
print(simpsons.columns)
print(simpsons.dtypes)
```

| Expresión | Aporta |
|---|---|
| `simpsons.shape` | cantidad de filas y columnas |
| `simpsons.columns` | nombres de las columnas |
| `simpsons.dtypes` | tipo de dato de cada columna |

En este archivo, `simpsons.shape` devuelve `(684, 6)`.

---

# Resumen con `info()`

```python
simpsons.info()
```

`info()` reúne en una salida breve:

- cantidad de filas;
- nombres de columnas;
- valores no nulos por columna;
- tipos de datos;
- memoria utilizada.

En `Rating` y `Vote_count` hay 683 valores no nulos: falta un dato en cada columna.

---

<!-- _class: compact -->

# Ejercicio 1 — Recibir un dataset nuevo

En un nuevo jupyter notebook, leer con pandas el archivo `data.csv`.

Mostrar los primeros y los últimos cinco registros.

Después, registrar en una celda Markdown:

- qué información registra cada fila, a partir de los datos observados;
- cuántos registros y columnas contiene el archivo;
- qué columnas son numéricas;
- si alguna columna tiene datos faltantes.

---

# Seleccionar una columna

```python
calificaciones = simpsons["Rating"]
calificaciones
```

El nombre debe coincidir con el encabezado del CSV.

`simpsons["Rating"]` devuelve una Series con el rating de cada episodio.

---

<!-- _class: compact -->

# Seleccionar varias columnas

```python
episodios = simpsons[["Title", "Season", "Rating"]]
episodios.head()
```

Con está seleccion ahora el dataframe tiene solo las columnas que nos interesan.

```python
simpsons["Rating"]     # Series
simpsons[["Rating"]]   # DataFrame con una columna
```

Los dobles corchetes aparecen porque estamos pasando una lista de columnas.

---

# Filtrando los datos: Condiciones

Pandas nos permite filtrar el dataframe con condiciones.

```python
condicion = simpsons["Rating"] > 7.5
condicion.head()
```

```text
0     True
1     True
2    False
3     True
4     True
```

Pandas compara el valor de cada fila y produce una Series de booleanos.

---

# Filtrar filas

```python
condicion = simpsons["Rating"] > 7.5
bien_calificados = simpsons[condicion]
bien_calificados
```

Como salida observamos solamente las filas donde la condición vale `True`.

También podemos escribir la condición dentro de los corchetes:

```python
bien_calificados = simpsons[simpsons["Rating"] > 7.5]
```


---

<!-- _class: compact -->

# Filtrar con dos condiciones

```python
condicion = (
    (simpsons["Season"] == 5) &
    (simpsons["Rating"] > 8.5)
)

resultado = simpsons[condicion]
resultado
```

- `&` exige que se cumplan ambas condiciones.
- Cada comparación debe estar entre paréntesis.

En el dataset, siete episodios cumplen estas dos condiciones.

---

<!-- _class: compact -->

# Ejercicio 2 — Filtrar mediciones

Continuar con el DataFrame `actividades` del ejercicio anterior y construir dos resultados:

- actividades con más de `350` calorías, mostrando `Date`, `Duration` y `Calories`;
- actividades de `45` minutos cuyo `Maxpulse` supere `130`, mostrando `Date`, `Pulse` y `Maxpulse`.

Comparar la cantidad de registros obtenidos y explicar en una celda Markdown cuál de los dos criterios fue más restrictivo.

---

<!-- _class: compact -->

# Ejercicio integrador - Filtrado de datos con Pandas

Crear un programa en Python que utilice **uno** de los siguientes datasets: `Pokemon.csv`, `vgsales.csv` o `StudentsPerformance.csv`.
El programa debe:
1. Cargar el dataset utilizando Pandas.
2. Pedir al usuario, mediante la función `input()`, un valor que será utilizado para filtrar los datos.
3. Elegir una columna del dataset y aplicar un filtro utilizando el valor ingresado.
4. Guardar el resultado del filtro en un nuevo DataFrame.
5. Mostrar en pantalla:
   - Las filas que cumplen con la condición.
   - La cantidad de filas resultantes.
   - La información del DataFrame filtrado utilizando `info()`.

La columna y la condición utilizada para realizar el filtro quedan a elección de cada estudiante.

Para mostrar el contenido completo del DataFrame filtrado en consola pueden utilizar:

```python
print(resultado.to_string())
```