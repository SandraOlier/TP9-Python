def dibujar_rectangulo(filas, columnas):
   
    for i in range(filas):
        print('*' * columnas)

filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
dibujar_rectangulo(filas, columnas)
