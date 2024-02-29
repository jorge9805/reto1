#paliandromo
#primero formatea la palabra a minuscula luego recorre las letras de la palabra y compara si la letra en la posicion i es igual a la letra en la posicion -i-1 si no es igual retorna falso si todas las letras son iguales retorna verdadero
def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    for i in range(len(palabra)):
        if palabra[i] != palabra[-i-1]:
            return False
    return True
print(palindromo("Anita lava la tina"))
print(palindromo("mahalo"))
