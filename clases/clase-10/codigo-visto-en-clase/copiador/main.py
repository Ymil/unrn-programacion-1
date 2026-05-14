archivo_entrada = open("entrada/frase.txt", "r")
contenido_entrada = archivo_entrada.read()
archivo_entrada.close()

archivo_salida = open("salida/frase_copia.txt", "w")
archivo_salida.write(contenido_entrada)
archivo_salida.close()