def factorial(n):
    print(f"Llamado factorial: {n} ")
    if n == 0:
        return 1

    x = n * factorial(n - 1)

    print(f"Resultado factorial {n}: {x}")

    return x


print(factorial(4))