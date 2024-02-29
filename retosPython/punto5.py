# se ordena la palabra y se compara con las demas palabras ordenadas
def mismo_caracteres(lista):
    iguales=[]
    for palabra in lista:
        for palabra2 in lista:
            if palabra!=palabra2:
                if sorted(palabra)==sorted(palabra2):
                    iguales.append(palabra)
    return iguales
