---
marp: true
theme: unrn-programacion
size: 16:9
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# 18. Trabajo colaborativo con Git

## Flujo compartido para el TP Integrador

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

1. ¿Para qué nos servía usar `try` / `except`?
2. ¿Por qué validamos datos que vienen de archivos o argumentos?
3. ¿Qué excepciones esperables aparecían al trabajar con archivos?

---

# Repositorio GIT

<div class="columns">
<div>

## Remoto

Repositorio compartido en GitHub.

Es la versión que usa el grupo como punto común.

</div>
<div>

## Local

Copia en la computadora de cada integrante.

Ahí se editan archivos y se preparan commits.

</div>
</div>

Trabajamos directamente sobre `main`.

---

<!-- _class: compact -->

# Flujo recomendado

```bash
git pull

# acordamos quien modifica que
# trabajamos en los archivos

git status
git add archivo.py
git commit -m "Agrega lectura de sensores"

git pull
git push
```

`pull` antes de empezar trae cambios del grupo.

`pull` antes de `push` evita subir desde una version vieja.

---

# Commits propios y coordinación

Cada integrante debe hacer commits con sus propios cambios.

Eso permite saber:

- quién modificó cada parte;
- qué cambió en cada paso;
- cuándo se integró una solución;
- qué revisar si aparece un problema.

Antes de editar, acuerden quién toca cada archivo o función.

---

<!-- _class: compact -->

# Ejemplo: archivos distintos

```text
repositorio-tp/
├── sofia.txt
├── bruno.txt
├── camila.txt
└── mensaje.txt
```

| Integrante | Archivo | Commit |
|---|---|---|
| Sofia | `sofia.txt` | `Agrega avance de Sofia` |
| Bruno | `bruno.txt` | `Agrega avance de Bruno` |
| Camila | `camila.txt` | `Agrega avance de Camila` |

Si modificamos solo nuestro propio archivo, git integra sin problemas.

Si dos personas tocamos el mismo archivo y el mismo bloque de codigo vamos a tener conflictos.

---

<!-- _class: compact -->

# Cuando el `push` se rechaza

1. X hace `push` con su commit.
2. Y todavía tiene una copia vieja.
3. Y intenta hacer `push`.

```text
! [rejected] main -> main
error: failed to push some refs
hint: Updates were rejected because the remote contains work
```

Git no deja pisar cambios que Y todavía no tiene.

Primero necesita sincronizar:

```bash
git pull
git push
```

---

<!-- _class: compact -->

# Conflicto de merge

Un conflicto ocurre cuando Git encuentra cambios incompatibles en el mismo lugar y no puede decidir automáticamente cuál conservar.

```text
<<<<<<< HEAD
Mensaje escrito por X.
=======
Mensaje escrito por Y.
>>>>>>> origin/main
```

Para resolverlo:

1. Tenemos que editar el archivo;
2. dejar el texto final;
3. borrar las marcas `<<<<<<<`, `=======`, `>>>>>>>`;
4. hacer `add`, `commit` y `push`.

---

<!-- _class: compact -->

# Ejercicio grupal masivo

Vamos a clonar todos el repositorio.
Crear un archivo con nuestro nombre y subirlo nuevamente.

```bash
# si todavia no tengo el repo:
git clone URL_DEL_REPOSITORIO

# si ya lo tengo:
git pull

# editar mi_nombre.txt

git add mi_nombre.txt
git commit -m "Agrega aporte de mi_nombre"
git pull
git push
```

---

<!-- _class: compact -->

# Segunda etapa

Vamos a modificar masivamente el archivo mensaje.txt

**Git permite trabajar en conjunto, pero no reemplaza la coordinación del equipo.**

---

# Flujo para el TP

```text
pull → acordar quién modifica qué → trabajar → add → commit → pull → push
```

Después de este ejercicio, cada grupo pasa a trabajar en el repositorio de su TP Integrador.
