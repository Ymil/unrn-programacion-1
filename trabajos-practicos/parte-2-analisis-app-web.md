# Trabajo Practico Integrador 1 - Parte 2
## Analisis de datos y app web

## Proyecto completo

En la Parte 1 construyeron un conversor de TXT a JSON. En esta segunda parte van a usar ese JSON para construir una aplicacion que permita explorar los datos meteorologicos.

El recorrido completo del trabajo queda asi:

```text
TXT original -> JSON validado -> procesamiento -> app web
```

La app web no debe volver a leer ni interpretar el TXT original. El punto de partida de esta parte es el JSON generado en la Parte 1.

## Objetivo Parte 2

Construir una aplicacion que cargue el JSON, permita elegir una estacion y una medicion, calcule estadisticas simples y muestre una grafica de linea.

La aplicacion debe tener dos partes:

- una parte de procesamiento de datos, hecha con funciones propias.
- una app web en Streamlit, que use esas funciones para mostrar los resultados.

## Organizacion sugerida

```text
trabajo_integrador/
├── conversor/
│   ├── adaptar_datos.py
│   └── validaciones.py
├── app_web/
│   ├── app.py
│   ├── procesar_datos.py
│   ├── datos.py
│   ├── estadisticas.py
│   ├── graficos.py
│   ├── datos/
│   │   └── observaciones.json
│   └── salidas/
├── requirements.txt
└── README.md
```

No es obligatorio usar exactamente esta estructura, pero el proyecto debe estar ordenado. La Parte 1 debe quedar separada de la Parte 2, pero en el mismo repositorio, por ejemplo dejando el conversor TXT a JSON dentro de una carpeta `conversor/` y la aplicacion nueva dentro de `app_web/`.

## Etapa 1: procesamiento de datos

Entrega: miercoles 07/10/2026

En esta etapa deben resolver la parte de procesamiento de datos. No debe haber interfaz web: si entregan una app web para esta etapa, la entrega no cumple con lo pedido.

El codigo debe estar escrito con funciones. No alcanza con resolver todo en un unico bloque de instrucciones: tiene que haber funciones para cargar datos, filtrar, calcular estadisticas y generar salidas.

En esta etapa no se debe usar Pandas. El procesamiento debe resolverse con Python, recorriendo listas y diccionarios.

El programa debe recibir por argumentos la ruta del JSON, la estacion y la medicion a analizar:

```bash
python procesar_datos.py datos/observaciones.json "BARILOCHE AERO" temperatura
```

Una forma esperada de organizar `procesar_datos.py` es:

```python
import sys

from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica


def main():
    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    datos = cargar_json(ruta_json)
    filtrados = filtrar_datos(datos, estacion, medicion)
    estadisticas = calcular_estadisticas(filtrados)
    ruta_grafica = generar_grafica(filtrados, estacion, medicion)

    print(estadisticas)
    print(f"Grafica guardada en: {ruta_grafica}")


main()
```

La plantilla no es obligatoria pero es una guia de funciones y estructura a definir para que el programa pueda funcionar correctamente en la etapa 2.

Debe incluir:

- cargar el JSON generado en la Parte 1 usando el modulo `json`.
- recibir por `sys.argv` la ruta del JSON de entrada.
- recibir por `sys.argv` una estacion meteorologica.
- recibir por `sys.argv` una medicion disponible, por ejemplo temperatura, humedad, presion o viento.
- filtrar los datos segun la estacion y la medicion seleccionadas.
- calcular cantidad, minimo, maximo y promedio con una funcion propia.
- mostrar por consola las estadisticas y los primeros registros filtrados.
- generar un CSV con los datos filtrados, abriendo un archivo y escribiendo encabezado y filas.
- generar una grafica de linea con Matplotlib.
- guardar la grafica como imagen PNG.
- manejar errores simples con mensajes claros.
- incluir instrucciones basicas en el `README.md`.

Los archivos generados deben guardarse en `salidas/` con nombres claros. Por ejemplo:

```text
salidas/2026-10-07_bariloche_temperatura.csv
salidas/2026-10-07_bariloche_temperatura.png
```

La grafica debe mostrar como cambia una medicion a lo largo del tiempo para una estacion.

## Etapa 2: app web

Entrega: miercoles 14/10/2026

En esta etapa deben construir una app web con Streamlit.

Streamlit debe usar las funciones escritas en la etapa anterior. La app no debe duplicar la logica de carga, filtrado, estadisticas, CSV o graficos dentro de `app.py`.

`app.py` debe recibir por argumento la ruta del JSON de entrada:

```bash
streamlit run app.py -- datos/observaciones.json
```

La estacion y la medicion deben elegirse desde controles de Streamlit, por ejemplo con `selectbox`. Esos valores se usan para llamar a las mismas funciones de carga, filtrado, estadisticas y graficos de la Etapa 1.

En esta etapa se debe usar Pandas para armar o acomodar la tabla que se muestra en Streamlit. Pandas no debe reemplazar las funciones de calculo de estadisticas desarrolladas en la Etapa 1.

Debe incluir:

- app web ejecutable con Streamlit.
- ruta del JSON recibida por `sys.argv`.
- seleccion de estacion y medicion desde la interfaz.
- estadisticas visibles en la app.
- tabla de datos filtrados visible en la app, armada con Pandas.
- generacion de CSV y grafica desde la app, usando las funciones del proyecto.
- grafica de linea generada con Matplotlib, guardada como PNG y mostrada en la app.
- manejo de errores principales desde la interfaz.
- `requirements.txt`.
- `README.md` completo.

## Clases de interes

- [Clase 10 - Trabajo con archivos](../../clases/clase-10/): lectura y escritura de archivos, modos `r`, `w` y `a`, archivos CSV y organizacion de entradas y salidas.
- [Clase 12 - Interpretacion de consignas, diccionarios y archivos](../../clases/clase-12/): identificacion de entradas, salidas, estructuras y validaciones.
- [Clase 15 - Terminal y argumentos](../../clases/clase-15/): ejecucion de programas desde la terminal, uso de `sys.argv` y validacion de argumentos.
- [Clase 16 - JSON en Python](../../clases/clase-16/): lectura de JSON con `json.load()`, escritura con `json.dump()` y trabajo con listas de diccionarios.
- [Clase 21 - Introduccion a Pandas](../../clases/clase-21/): DataFrame, seleccion de columnas, inspeccion y filtrado de datos.
- [Clase 22 - Analisis y transformacion con Pandas](../../clases/clase-22/): ordenamiento, calculos sobre columnas, datos faltantes y escritura de resultados.
- [Clase 23 - Visualizacion de datos con Matplotlib](../../clases/clase-23/): graficos de linea, titulos, ejes, etiquetas y guardado de imagenes.
