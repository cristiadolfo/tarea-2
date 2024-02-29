def numeroRango (numeros):
    contador = 0
    for numero in numeros:
        if numero >= 10 and numero <=20:
            contador += 1
    return contador
        
cantiNumerosInt = int(input("ingrese la cantidad de numeros que quiere registrar :"))
numeros = []
for i in range(cantiNumerosInt):
    numero = int(input("ingrese un numero :"))
    numeros.append(numero)
NumeroEnRango = numeroRango(numeros)
print ("numeros en rango :", NumeroEnRango)
    