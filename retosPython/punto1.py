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
print(operaciones_basicas(2, 3, "+"))
print(operaciones_basicas(2, 3, "-"))
print(operaciones_basicas(2, 3, "x"))
print(operaciones_basicas(2, 3, "/"))
