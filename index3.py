def encontrar_numero_mayor(numeros):
   
    if not numeros:
        return None  
    numero_mayor = numeros[0]
    for numero in numeros:
        if numero > numero_mayor:
            numero_mayor = numero
    return numero_mayor


numeros = [18, 27, 3, 58, 70, 2, 99, 44]
mayor = encontrar_numero_mayor(numeros)
print(f"El número mayor de la serie es: {mayor}")
