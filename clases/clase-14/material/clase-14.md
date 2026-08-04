---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 14. Volviendo a clases

## Breve recapitulación + Gestión de Ambientes + Chat Grupal

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

# Repaso express <br />¿Que herramienta usamos?

1. Pedir datos hasta escribir “salir”.
2. Recorrer una lista de datos fijos.
3. Una función debe producir un resultado manipulable.
4. Una función debe recibir datos si los necesita.
5. Tenemos que guardar datos que no se repiten.
6. Tenemos que guardar datos que no se pueden modificar.

---

# Analizando un poco de codigo

<div class="columns">
<div>

```python
registros_temperatura = [
    "FREY;12",
    "OTTO;8°C",
    "CATEDRAL;8",
    "FREY;5"
]

total = 0

for registro in registros:
    nombre, cantidad = registro.split(";")
    total += int(cantidad)

print(total)
```

</div>
<div>

## Analizar antes de ejecutar

- ¿Qué intenta calcular?
- ¿Qué línea puede fallar?
- ¿Qué registro lo rompe?
- ¿Por qué no conviene convertir directo?
- ¿Qué dato debería validarse antes?

> Arrancamos sin ejecutar el codigo

</div>
</div>

---

<!-- _class: inverse -->

# Gestión de ambientes e instación de paquetes

---

<!-- _class: compact -->

# Ambientes virtuales

Un ambiente virtual es una carpeta del proyecto que usa una versión de Python y guarda allí los paquetes instalados para ese proyecto. Así evitamos modificar Python global o mezclar versiones entre proyectos.

1. Para crearlo: `python -m venv .venv`
2. Para activarlo:
   - Windows: `.venv\Scripts\activate`
   - Linux/macOS: `source .venv/bin/activate`
4. Para desactivarlo: `deactivate`

> Se crea una sola vez por proyecto. Si abrimos otra terminal, hay que activarlo de nuevo.

---

# Instalación de paquetes

Dentro de nuesto ambiente virtual podemos instalar paquetes con: `pip install <paquete>`

## Archivo requirements.txt
Los archivos requirements permiten definir listas de dependencias de paquetes.

Para instalar el contenido de estos archivos usamos: `pip install -r requirements.txt`

---

# Instalando nuestro primer paquete

<div class="columns">


1. Ejecutamos `pip install cowsay`
2. Ejecutamos `python`
3. Escribimos el siguiente codigo:

<div>

```python
import cowsay

cowsay.cow("Hola mundo")
```
</div>
</div>

> Ejecutemos este codigo antes y despues de instalar cowsay

![alt text](assets/cowsay.png)


---

<!-- _class: inverse -->

# Chat Grupal

![alt text](assets/cliente-servidor.png)

## Trabajando con modulos

---

# Creando ambiente

1. En un nuevo directorio vamos a crear un ambiente virtual
2. Copiar desde el repositorio [cliente.py](../recursos/cliente.py) y [requirements_cliente.txt](../recursos/requirements_cliente.txt)
3. Ejecutar `pip install -r requirements_cliente.txt`

---

# Creando nuestros programas

1. Crear un programa python que permita enviar mensajes hasta que escribamos salir.
2. Crear un programa python que permita recibir mensajes e imprimirlos en pantalla.
3. Ejecutar ambos programas en diferentes terminales.

> Hay que modificar en cliente.py la variable `SERVIDOR` con datos que les voy a pasar.

---

<!-- _class: inverse -->

# Armado de grupos para TP Integrador
