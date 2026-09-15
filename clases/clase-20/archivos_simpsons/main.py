from pathlib import Path

carpeta = Path.cwd() # DIRECTORIO DE TRABAJO ACTUAL
print(carpeta) # C:\.......\archivos_simpsons\

def recorrer(carpeta, nivel=0):
    nivel = nivel + 1
    for elemento in carpeta.iterdir():
        print("\t" * nivel + elemento.name)
        if elemento.is_dir():
            recorrer(elemento, nivel)

recorrer(carpeta)