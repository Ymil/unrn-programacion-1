---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 22. Pandas: analizar y transformar

## Resumir datos y producir nuevos resultados

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

https://github.com/Ymil/unrn-programacion-1/tree/main/clases/clase-22

---

<!-- _class: inverse -->

# Repaso express <br>Clase anterior

1. ¿Cuándo podemos usar Jupyter Notebook?
2. ¿Qué es Pandas?
3. ¿Qué produce una comparación como `df["Rating"] > 8.5`?

---

# Retomar los datos

Crear el notebook de la clase y cargar el dataset de Los Simpson:

```python
import pandas as pd

df = pd.read_csv("SimpsonsData_es.csv")
```

---

# Ordenar los datos

Pandas nos permite ordenar la información de los DataFrames:

```python
por_rating = df.sort_values("Rating")
por_rating[["Title", "Season", "Rating"]].head()
```

El orden descendente se indica con `ascending=False`:

```python
por_rating = df.sort_values(
    "Rating",
    ascending=False
)
por_rating[["Title", "Season", "Rating"]].head()
```

El DataFrame original no se modifica: `sort_values()` genera un nuevo DataFrame ordenado.

---

# Cálculos sobre una columna

```python
promedio = df["Rating"].mean()
menor = df["Rating"].min()
mayor = df["Rating"].max()
suma = df["Rating"].sum()

print(promedio)
print(menor)
print(mayor)
print(suma)
```

La operación se realiza sobre todos los valores de la columna seleccionada.

---

# Contar valores

```python
episodios_por_temporada = df["Season"].value_counts()
episodios_por_temporada.head()
```

`value_counts()` indica cuántas veces aparece cada valor.

En este caso permite conocer cuántos episodios contiene cada temporada.

---

<!-- _class: compact -->

# Ejercicio 3 — Preparar un resumen

En un nuevo notebook, leyendo el archivo `data.csv`, preparar un resumen de `actividades` que contenga:

- los cinco registros con mayor `Maxpulse`, mostrando `Date`, `Pulse`, `Maxpulse` y `Calories`;
    - Guardar en nuevo dataframe
- el promedio, el mínimo, el máximo y el total de `Calories` de todos los registros;
    - Guardar cada uno en una variable
- el valor de `Pulse` que más veces aparece.

Presentar la tabla y escribir una conclusión breve basada en los resultados obtenidos.

> La conclusión debe explicar qué muestran los valores, no enumerar los pasos técnicos realizados.

---

<!-- _class: compact -->

# Operaciones sobre los datos

Podes aplicar operaciones sobre los datos de a las columnas (serie) de un DataFrame:

<!-- Add columns div -->

<div class="columns">
  <div class="column">
Es posible realizar operaciones sobre una columna

```python
df["Vote_count"] / 1000
```
</div>

<div class="column">
Y tambien es posible realizar operaciones entre columnas:

```python
df["Vote_count"] / df["Rating"]
```

</div>
</div>

> Las salidas de estas operaciones son series

Y podriamos lograr algo equivalente mediante un for de forma más artesanal.

```python
data = []
for x in df["Vote_count"]:
    data.append(x / 1000)
```
---

# Creando columnas

Podemos calcular un valor nuevo a partir de columnas existentes:

```python
df["Votes_mils"] = df["Vote_count"] / 1000

df["Impact"] = df["Rating"] * df["Votes_mils"]

df.head()
```

---

# Agrupar y calcular

```python
rating_por_temporada = (
    df.groupby("Season")["Rating"].mean()
)

rating_por_temporada.head()
```

`groupby()` reúne los episodios de la misma temporada; después `mean()` calcula el promedio de sus calificaciones.

---

<!-- _class: inverse -->
# ¿Cómo resolvemos agrupaciónes sin no tuvieramos `groupby()`?

---
<!-- _class: compact -->

# ¿Cómo resolvemos agrupaciónes sin no tuvieramos `groupby()`? - RESP

Para calcular el rating promedio de cada temporada tendríamos que:

1. recorrer todos los episodios;
2. separar sus ratings según la temporada;
3. acumular la suma y la cantidad de cada grupo;
4. calcular un promedio por temporada.

```text
episodios → grupos por temporada → suma y cantidad → promedio por grupo
```

`value_counts()` resuelve solamente el conteo. `groupby()` forma los grupos y permite calcular un resumen sobre cada uno.

---

<!-- _class: compact -->

# Ejercicio 4 — Analizar actividades

A partir del DataFrame actividades, determinar qué duraciones parecen representar los entrenamientos de mayor intensidad.

- agrupar los registros según Duration;
    - obtener para cada grupo el promedio de Pulse, Maxpulse y Calories;
- obtener también cuántos registros hay en cada duración;
- ordenar el resultado a partir de la metrica calculada `calories / duration`

---

# Guardado de datos

Pandas nos permite leer y guardar los DataFrames en diferentes formatos:
- CSV
- JSON

Y muchos otros.

> Toda la info: https://pandas.pydata.org/docs/reference/io.html

---

# Guardando un CSV

```python
destacados = df[df["Rating"] > 8.5]

destacados.to_csv(
    "episodios_destacados.csv",
    index=False
)

destacados.head()
```

`to_csv()` escribe el DataFrame en un archivo nuevo.

`index=False` evita agregar el índice del DataFrame como otra columna del CSV.

---

# Guardando un JSON

Podemos guardar el mismo DataFrame en formato JSON:

```python
destacados.to_json(
    "episodios_destacados.json",
    orient="records",
    force_ascii=False,
    indent=4
)
```

`orient="records"` guarda cada fila como un objeto dentro de una lista.

`force_ascii=False` conserva letras como tildes y la `ñ`.

---

<!-- _class: inverse -->

# Ejercicio integrador

## Reporte configurable de partidos

---

<!-- _class: compact -->

# Preparar los datos

En un nuevo notebook, leer `afa_2015_2022_eng.csv` con pandas.

> Dataset: [Argentinian Football Results 2015–2022](https://www.kaggle.com/datasets/camussonif/argentinian-football-results-20152022), publicado en Kaggle.

El usuario debe poder ingresar una cantidad mínima de goles totales y convertirla a un número entero.

El reporte debe:

- incluir una columna `total_goals`, calculada a partir de `goals_home` y `goals_away`;
- conservar los partidos que alcancen la cantidad mínima ingresada;
- mostrar `tournament`, `week`, `team_home`, `team_away`, `goals_home`, `goals_away`, `total_goals` y `result`;
- quedar ordenado de mayor a menor por `total_goals`.

---

# Exportar e interpretar

Solicitar al usuario la extensión de salida: `csv` o `json`.

Guardar el reporte como `partidos_destacados.csv` o `partidos_destacados.json`, según la extensión elegida.

Antes de exportarlo, informar la cantidad de partidos encontrados, el promedio de `total_goals` y el resultado que aparece con mayor frecuencia.
