def encontrar_mayor(lista):
    maximo = float('-inf')
    for x in lista:
        if x >= maximo:
            maximo = x
    return maximo

def encontrar_menor(lista):
    minimo = float('inf')
    for x in lista:
        if x <= minimo:
            minimo = x
    return minimo

def calcular_promedio(lista):
    acumulador = 0
    for cantidad in lista:
        acumulador += cantidad
    promedio = acumulador / len(lista)
    return promedio
