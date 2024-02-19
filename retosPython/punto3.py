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
