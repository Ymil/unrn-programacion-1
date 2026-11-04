# Fibonacci: material complementario

La sucesión de Fibonacci empieza con 0 y 1. Cada número siguiente es la suma de los dos anteriores:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Para índices enteros no negativos, llamamos `fib(n)` al número que está en la posición `n`:

| `n` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| `fib(n)` | 0 | 1 | 1 | 2 | 3 | 5 | 8 |

Para calcular `fib(4)` necesitamos sumar `fib(3)` y `fib(2)`. Esos resultados se calculan de la misma manera:

```text
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)
```

Los casos base son `fib(0) = 0` y `fib(1) = 1`.

```python
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))  # 3
```

Cada llamada que no llega a un caso base hace otras dos llamadas. Para `fibonacci(4)` ocurre esto:

```text
                fib(4)
              /        \
         fib(3)         fib(2)
        /     \         /     \
    fib(2)   fib(1)  fib(1)  fib(0)
    /    \
fib(1)  fib(0)
```

`fib(2)` se calcula dos veces y `fib(1)`, tres. Esta solución muestra el patrón recursivo, pero repite cálculos y se vuelve lenta cuando `n` crece.
