def calcular_promedio(notas):

    if not notas:
        return 0
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

notas = [41, 45, 98, 72, 58]
promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio}")
