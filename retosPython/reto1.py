#funcion operaciones basicas (suma, resta, multiplicacion, division)
#recibe dos numeros y un operador luego atraves de un condicional se mira que operacion se va a realizar y se retorna los dos numeros operados
def operaciones_basicas(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "x":
        return a * b
    elif operacion == "/":
        return a / b
    else:
        return "Operacion no valida"
    
#paliandromo
#primero formatea la palabra a minuscula luego recorre las letras de la palabra y compara si la letra en la posicion i es igual a la letra en la posicion -i-1 si no es igual retorna falso si todas las letras son iguales retorna verdadero
def palindromo(palabra):
    palabra = palabra.lower()
    for i in range(len(palabra)):
        if palabra[i] != palabra[-i-1]:
            return False
    return True
print(palindromo("Anita lava la tina"))


#primos
from math import sqrt
def primos(numeros):
    primos=[]
    for num in numeros:
        raiz=sqrt(num)
        entero_raiz=int(raiz)
        esPrimo=True
        for i in range(2,entero_raiz+1):
            if  num%i==0: esPrimo=False
            if num==1: esPrimo=False
        if esPrimo==True: primos.append(num)
    return primos
print(primos([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

# mayor suma dos elementos consecutivos

def mayor_suma(numeros):
    mayor=0
    for i in range(len(numeros)-1):
        suma=numeros[i]+numeros[i+1]
        if suma>mayor:
            mayor=suma
    return mayor
#random list
print(mayor_suma([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,17,18,11,]))

#mismos caracteres
# def mismos_caracteres(strings):
    
