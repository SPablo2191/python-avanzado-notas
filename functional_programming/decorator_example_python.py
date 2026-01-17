def saludar():
    print("Hola")



# saludar()






















# Decoradores en Python


def mi_decorador(funcion_original):
    def nueva_funcion():
        print("👉 Antes de la función")
        funcion_original()
        print("👈 Después de la función")
    return nueva_funcion

# # Decoramos la función
saludo_decorado = mi_decorador(saludar) # nueva_funcion

# # Llamamos a la función decorada
saludo_decorado()


# forma de usar el decorador directamente



@mi_decorador
def saludar():
    print("Hola")

saludar()
