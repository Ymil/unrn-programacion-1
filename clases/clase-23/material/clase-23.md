---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 23. Matplotlib desde cero

## Graficar datos con Python

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

1. ¿Alguien se acuerda que era pandas?
2. ¿Podemos trabajar con JSON en Pandas?

<center>
<img src="https://www.shutterstock.com/shutterstock/videos/1007107075/thumb/1.jpg?ip=x480">
</center>

---

# Matplotlib

**Matplotlib** es una librería de Python para crear y guardar gráficos.

Los gráficos nos permiten interpretar datos de forma visual.

## Qué podemos mirar con gráficos

- cambios a lo largo del tiempo;
- comparaciones entre categorías;
- relación entre dos valores;
- distribución de muchas mediciones.

Cada caso se puede representar con un tipo de gráfico distinto.

---

# Instalar e importar

Matplotlib no forma parte de la biblioteca estándar. Hay que instalarlo:

```bash
pip install matplotlib
```

En cada programa que genere gráficos:

```python
import matplotlib.pyplot as plt
```

`plt` es el nombre corto para usar `pyplot`.

---

<!-- _class: compact -->

# Primer gráfico

```python
import matplotlib.pyplot as plt

horas = [0, 1, 2, 3, 4, 5]
temperatura = [18.1, 18.4, 19.0, 20.2, 21.1, 21.5]

plt.plot(horas, temperatura)
plt.show()
```

`plot()` arma un gráfico de línea.

`show()` lo muestra en pantalla.

> En Jupyter el gráfico se ve directamente debajo de la celda. Fuera de Jupyter, se muestra en una ventana emergente.

---

# Cómo interpreta `plot()` los datos

```python
plt.plot(horas, temperatura)
```

Matplotlib toma los valores por posición:

| Posición | Eje X | Eje Y |
|---:|---:|---:|
| 0 | 0 | 18.1 |
| 1 | 1 | 18.4 |
| 2 | 2 | 19.0 |

Las dos listas deben tener la misma cantidad de elementos.

---

<!-- _class: compact -->

# Título y ejes

Matplotlib nos permite escribir un título y etiquetas para los ejes.

```python

horas = [0, 1, 2, 3, 4, 5]
temperatura = [18.1, 18.4, 19.0, 20.2, 21.1, 21.5]

plt.plot(horas, temperatura)
plt.title("Temperatura medida por un sensor")
plt.xlabel("Hora")
plt.ylabel("Temperatura (°C)")
plt.show()
```

- `title()` agrega un título al gráfico
- `xlabel()` y `ylabel()` agregan etiquetas a los ejes

---

# Gráfico de líneas

```python
plt.plot(x, y)
```

Cuando los datos tienen un orden, el gráfico de línea permite ver cómo cambian.

- temperatura medida cada hora;
- tensión de una batería durante una descarga;
- potencia generada a lo largo del día.


---

<!-- _class: compact -->

# Ejemplo: potencia solar

Tenemos una medición de potencia solar en distintos horarios.

```python

horas = [8, 10, 12, 14, 16, 18]
potencia = [120, 360, 680, 720, 410, 90]

plt.plot(horas, potencia)
plt.title("Potencia generada")
plt.xlabel("Hora")
plt.ylabel("Potencia (W)")
plt.show()
```

---

# Gráfico de barras

```python
plt.bar(categorias, valores)
```

Cuando los datos están separados por categorías, las barras ayudan a comparar cantidades.

- consumo electrico por sector;
- cantidad de mediciones por sensor;
- energía producida por panel;
- errores detectados por equipo.

---

<!-- _class: compact -->

# Ejemplo: consumo por sector

Tenemos consumo eléctrico por sector.

```python

sectores = ["Aula", "Lab", "Taller", "Servidor"]
consumo = [18, 32, 25, 41]

plt.bar(sectores, consumo)
plt.title("Consumo eléctrico por sector")
plt.xlabel("Sector")
plt.ylabel("Consumo (kWh)")
plt.show()
```

La altura de cada barra representa el valor de esa categoría.

---

# Gráfico de dispersión

```python
plt.scatter(x, y)
```

Cuando cada medición tiene dos valores, la dispersión permite ver cómo se relacionan.

- temperatura y consumo de gas;
- velocidad y corriente;
- tensión y potencia;
- presión y caudal.

Los puntos no se unen porque no muestran una secuencia temporal.

---

<!-- _class: compact -->

# Ejemplo: temperatura y consumo

Registramos temperatura exterior y consumo de gas.

```python
temperatura = [10, 12, 14, 16, 18, 20, 22]
consumo = [42, 39, 35, 31, 28, 26, 25]

plt.scatter(temperatura, consumo)
plt.title("Temperatura exterior y consumo")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Consumo (m³)")
plt.show()
```

Cada punto relaciona una temperatura con el consumo registrado.

---

# Histograma

```python
plt.hist(valores)
```

Cuando tenemos muchas mediciones numéricas, el histograma muestra dónde se concentran.

Casos típicos:

- lecturas de un sensor;
- tiempos de respuesta;
- errores de medición;
- consumos diarios.

Agrupa valores cercanos en intervalos.

---

<!-- _class: compact -->

# Ejemplo: lecturas de sensor

Tomamos varias lecturas de tensión.

```python

lecturas = [4.9, 5.1, 5.0, 5.2, 4.8, 5.1, 5.3, 4.9, 5.0]

plt.hist(lecturas)
plt.title("Lecturas de tensión")
plt.xlabel("Tensión (V)")
plt.ylabel("Cantidad de mediciones")
plt.show()
```

El eje Y indica cuántos valores caen en cada intervalo.

> Se puede usar el parámetro `bins` en `hist` para determinar el número de intervalos del histograma.
> Por defecto su valor es 10.

---

<!-- _class: compact -->

# Ejercicio 1: elegir el gráfico

<div class="columns">

<div class="column">

Para cada caso:

- elegir un tipo de gráfico;
- construirlo con Matplotlib;
- agregar título y nombres de ejes;
- justificar la elección en una frase.

</div>

<div class="column">

```python
# Nivel de tanque
minutos = [0, 10, 20, 30, 40, 50]
nivel = [82, 76, 69, 63, 58, 51]

# Intensidad de señal
distancia = [1, 2, 3, 4, 5, 6, 7]
senal = [-31, -35, -42, -48, -57, -65, -72]

# Errores por módulo
modulos = ["Carga", "Filtro", "Reporte", "Exportacion"]
errores = [4, 9, 3, 6]

# Notas de examen
notas_examen = [4, 6, 7, 8, 5, 6, 9, 7, 8, 6, 10, 5]
```

</div>

</div>

---


<!-- _class: compact -->

# Dos series en el mismo gráfico

La herramienta nos permite poner más de una serie en el mismo gráfico.

```python
horas = [8, 10, 12, 14, 16, 18]
panel_norte = [120, 360, 680, 720, 410, 90]
panel_sur = [80, 240, 510, 540, 300, 70]

plt.plot(horas, panel_norte, label="Panel norte")
plt.plot(horas, panel_sur, label="Panel sur")
plt.title("Potencia por panel")
plt.xlabel("Hora")
plt.ylabel("Potencia (W)")
plt.legend()
plt.show()
```

`label` nombra cada serie y `legend()` muestra la leyenda.

---

<!-- _class: compact -->

# Guardar un gráfico

```python

horas = [8, 10, 12, 14, 16, 18]
potencia = [120, 360, 680, 720, 410, 90]

plt.plot(horas, potencia)
plt.title("Potencia generada")
plt.xlabel("Hora")
plt.ylabel("Potencia (W)")

plt.savefig("potencia.png")
plt.show()
```

`savefig()` crea un archivo con el gráfico.

---

<!-- _class: inverse -->

# Pandas + Matplotlib

Podemos utilizar Pandas para leer CSV, manipular la información y graficarla después.

---

<!-- _class: compact -->

# Cargar un CSV

```python
import pandas as pd

df = pd.read_csv("paneles_solares.csv")

print(df.head())
```

El archivo contiene mediciones de potencia de paneles solares.

---

<!-- _class: compact -->

# Usar columnas como datos

Podemos utilizar las columnas de pandas como fuente de información para gráficos.

```python
import matplotlib.pyplot as plt

inv_1 = df[df["inversor"] == "INV_1"]

plt.plot(inv_1["fecha_hora"], inv_1["potencia_ac"])
plt.title("Potencia generada")
plt.xlabel("Fecha y hora")
plt.ylabel("Potencia AC")
plt.xticks(rotation=90)
plt.show()
```

> Hack: podemos rotar las etiquetas con `plt.xticks(rotation=90)` para que se vean más claras.

---

<!-- _class: inverse -->

# Ejercicio integrador

Leer `telemetria_ambiental.csv` con Pandas y realizar los siguientes pasos:

1. Construir un histograma de temperatura por dispositivo.
Analizar qué valores parecen más atípicos y escribirlo textualmente en Jupyter.

2. Construir un gráfico que muestre cómo cambia la temperatura de todos los dispositivos. 
El gráfico debe incluir título, nombres de ejes y leyenda.

3. Guardar el gráfico de líneas y cada histograma como archivos `.png`.

---

# Matplotlib ofrece una gran variedad de gráficos

En los siguientes links están los ejemplos oficiales de Matplotlib.

<div class="columns">

<div class="column">

- [Galería general de ejemplos](https://matplotlib.org/stable/gallery/)
- [Líneas, barras y marcadores](https://matplotlib.org/stable/gallery/lines_bars_and_markers/index.html)
- [Gráfico de línea básico](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)
- [Gráfico de barras](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)
- [Histogramas](https://matplotlib.org/stable/gallery/statistics/hist.html)
- [Scatter plot](https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html)
- [Gráfico de torta / Pie chart](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html)
- [Boxplot](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

</div>

<div class="column">

![](https://matplotlib.org/stable/_images/sphx_glr_pie_features_002.png)

</div>

</div>
