#retorna una lista con los primos de una lista de numeros, para esto primero halla la raiz del numero de la lista que se quiere verificar ya que por teorema un numero no se puede dividir por un numero mayor a su raiz cuadrada, luego recorre los numeros desde 2 hasta la raiz del numero y si el numero es divisible por alguno de estos numeros no es primo, si no es divisible por ninguno de estos numeros es primo
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
