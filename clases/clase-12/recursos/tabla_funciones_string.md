# Tabla de funciones para manipulacion de strings

Referencia oficial: [Python - Text Sequence Type str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

| Metodo | Para que sirve | Devuelve | Ejemplo | Resultado |
| --- | --- | --- | --- | --- |
| [`upper`](https://docs.python.org/3/library/stdtypes.html#str.upper) | Convierte letras a mayusculas. | `str` | `"hola".upper()` | `"HOLA"` |
| [`lower`](https://docs.python.org/3/library/stdtypes.html#str.lower) | Convierte letras a minusculas. | `str` | `"HOLA".lower()` | `"hola"` |
| [`isupper`](https://docs.python.org/3/library/stdtypes.html#str.isupper) | Verifica si las letras estan en mayusculas. | `bool` | `"HOLA".isupper()` | `True` |
| [`islower`](https://docs.python.org/3/library/stdtypes.html#str.islower) | Verifica si las letras estan en minusculas. | `bool` | `"hola".islower()` | `True` |
| [`partition`](https://docs.python.org/3/library/stdtypes.html#str.partition) | Separa el string en 3 partes usando el primer separador encontrado. | `tuple` | `"PROG-101".partition("-")` | `("PROG", "-", "101")` |
| [`split`](https://docs.python.org/3/library/stdtypes.html#str.split) | Divide el string en varias partes usando un separador. | `list` | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| [`title`](https://docs.python.org/3/library/stdtypes.html#str.title) | Pone en mayuscula la primera letra de cada palabra. | `str` | `"mara gomez".title()` | `"Mara Gomez"` |
| [`strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) | Quita caracteres al principio y al final. Si no se indica nada, quita espacios. | `str` | `"  hola  ".strip()` | `"hola"` |
| [`replace`](https://docs.python.org/3/library/stdtypes.html#str.replace) | Reemplaza apariciones de un texto por otro. | `str` | `"hola mundo".replace("mundo", "Python")` | `"hola Python"` |

## Diferencias importantes

- `upper` y `lower` transforman el texto. `isupper` e `islower` solo preguntan si el texto cumple una condicion.
- `split` devuelve una lista con todas las partes que encuentra. `partition` devuelve siempre una tupla de 3 elementos: antes del separador, el separador y despues del separador.
- `strip` limpia los bordes del string. No toca espacios o caracteres que esten en el medio.
- `title` cambia el formato de las palabras. No valida nombres: solo transforma texto.
- `replace` cambia coincidencias dentro del string. No separa el texto en partes.

## Ejemplo con f-string

Referencia: [Python - formatted string literals](https://docs.python.org/3/library/stdtypes.html#formatted-string-literals-f-strings)

```python
nombre = "  mara gomez  ".strip().title()
codigo = "prog-101".upper()

print(f"{nombre} esta anotada en {codigo}")
```

Salida:

```text
Mara Gomez esta anotada en PROG-101
```
