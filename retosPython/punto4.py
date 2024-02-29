# mayor suma dos elementos consecutivos, para esto se guarde el mayor valor de la suma de dos elementos consecutivos y se compara con el siguiente par de elementos, si la suma de estos es mayor que el mayor valor de la suma de dos elementos consecutivos se actualiza el valor del mayor valor de la suma de dos elementos consecutivos


def mayor_suma(numeros):
    mayor=0
    for i in range(len(numeros)-1):
        suma=numeros[i]+numeros[i+1]
        if suma>mayor:
            mayor=suma
    return mayor
#random list
print(mayor_suma([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,17,18,11,]))
