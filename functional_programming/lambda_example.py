es_mayor_edad : bool = lambda edad: edad >= 18
edad = int(input("ingrese su edad"))
if es_mayor_edad(edad):
    print("puede salir a bailar")
