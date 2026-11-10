libro_principito = {
    "titulo": "el principito",
    "autor": "Antoni Hockis",
    "paginas": 100
}
# libro_principito[]
# print(type(libro_principito))
def es_extenso(libro):
    if libro["paginas"] > 300:
        return True
    return False

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def es_extenso(self):
        if self.paginas > 300:
            return True
        return False

    def __str__(self):
        return self.titulo

x = Libro("El Principito", "Antoni Hockis", 100)
y = Libro("El Principito 2", "Antoni Hockis", 100)
print(x, x.titulo)
print(x)
print(y)
print(__name__)