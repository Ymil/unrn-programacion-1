def saludo():
    print("hola")

def ret_saludo():
    return "hola"

def saludo_argumento(nombre = ""):
    if(nombre == ""):
        return "hola"
    return f"hola {nombre}"

saludo()
print(ret_saludo())
print(saludo_argumento("lauti"))
print(saludo_argumento())