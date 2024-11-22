def es_color_primario(color):
    
    colores_primarios = ["rojo", "azul", "amarillo"]
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario")

es_color_primario("Rojo")
es_color_primario("Turquesa")
