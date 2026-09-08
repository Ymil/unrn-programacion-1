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

# Clonar el repositorio

Siempre que trabajemos con un repositorio, lo primero que tenemos que hacer es clonarlo.

```bash
git clone https://github.com/Ymil/unrn-programacion-1-repo-compartido.git
cd unrn-programacion-1-repo-compartido
```

`git clone` crea una copia local del repositorio remoto.

---

<!-- _class: compact -->

# Configurar nuestra identidad en Git

Antes del primer commit, configuramos quién firma nuestros cambios:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

La configuración global se realiza una sola vez para cada usuario de la computadora.

---

<!-- _class: compact -->

# Configuración inicial

Una vez dentro del repositorio:

```bash
git branch --set-upstream-to=origin/main main
git config pull.rebase true
```

Nuestra rama `main` se sincroniza con `origin/main`.

`origin/main` es la rama `main` que viene de GitHub.

`git pull` ya sabe cómo traer y acomodar cambios del grupo.

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

Aunque cada persona toque su archivo, el `push` puede rechazarse si alguien subió antes.

En ese caso hacemos `git pull`; Git suele resolver solo si son archivos distintos.

Los conflictos aparecen cuando dos cambios pisan el mismo lugar.

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

Necesita sincronizar:

```bash
git pull
```


---

<!-- _class: compact -->

# Cuando el `pull` se complica

A veces Git no puede decidir solo cómo juntar los cambios.

```text
<<<<<<< HEAD
Mensaje que vino de GitHub.
=======
Mensaje que escribí yo.
>>>>>>> abc1234 (mi cambio)
```

En este caso, arriba está lo que llegó de GitHub y abajo está mi cambio local.

Para resolverlo:

1. Revisar con `git status`;
2. editar el archivo y dejar la versión final;
3. borrar las marcas `<<<<<<<`, `=======`, `>>>>>>>`;
4. ejecutar `git add archivo`, `git rebase --continue` y `git push`.

---

<!-- _class: compact -->

# Ejercicio grupal masivo

```bash
# si todavia no tengo el repo:
git clone https://github.com/Ymil/unrn-programacion-1-repo-compartido.git

# entro a la carpeta del repo:
cd unrn-programacion-1-repo-compartido

# configuración inicial:
git switch main
git branch --set-upstream-to=origin/main main
git config pull.rebase true
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

Vamos a modificar masivamente la misma línea de `mensaje.txt`.

**Git permite trabajar en conjunto, pero no reemplaza la coordinación del equipo.**

---

# Flujo para el TP

```text
pull → acordar quién modifica qué → trabajar → add → commit → pull → push
```

Después de este ejercicio, cada grupo pasa a trabajar en el repositorio de su TP Integrador.

---

<!-- _class: compact -->

# Anexo: un `.gitignore` mínimo

En la raíz del repositorio creamos un archivo llamado `.gitignore`:

```gitignore
*.pyc
.venv
```

Así Git ignora los archivos compilados que Python puede generar al ejecutar el programa.
