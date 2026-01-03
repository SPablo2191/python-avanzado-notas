"""prinicpio open/close """

# class CalculadoraDeAreas:
#     def calcular(self, figura):
#         if figura["tipo"] == "rectangulo":
#             return figura["ancho"] * figura["alto"]
#         elif figura["tipo"] == "circulo":
#             return 3.14 * (figura["radio"] ** 2)


# class Figura:
#     def calcular_area(self):
#         pass

# class Rectangulo(Figura):
#     def __init__(self, ancho, alto):
#         self.ancho = ancho
#         self.alto = alto

#     def calcular_area(self):
#         return self.ancho * self.alto

# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio

#     def calcular_area(self):
#         return 3.14 * (self.radio ** 2)

# # Ejemplo de uso
# figuras = [Rectangulo(5, 10), Circulo(7)]
# for figura in figuras:
#     print(figura.calcular_area())


"""principio de sustitucion de liskov"""

# class Animal:
#     def hacer_sonido(self):
#         pass

# class Perro(Animal):
#     def hacer_sonido(self):
#         return "Guau"

# class Pez(Animal):
#     def hacer_sonido(self):
#         raise NotImplementedError("Los peces no hacen sonido")


# class Animal:
#     def hacer_sonido(self):
#         pass

# class Perro(Animal):
#     def hacer_sonido(self):
#         return "Guau"

# class Pez(Animal):
#     def hacer_sonido(self):
#         return "..."  # Un pez no hace sonido, pero no rompe el programa.

"""principio de segregacion de interfaces"""

# class Vehiculo:
#     def conducir(self):
#         pass

#     def volar(self):
#         pass

# class Coche(Vehiculo):
#     def conducir(self):
#         return "Conduciendo..."

#     def volar(self):
#         raise NotImplementedError("El coche no puede volar")


# class VehiculoTerrestre:
#     def conducir(self):
#         pass

# class VehiculoAereo:
#     def volar(self):
#         pass

# class Coche(VehiculoTerrestre):
#     def conducir(self):
#         return "Conduciendo..."

# class Avion(VehiculoAereo):
#     def volar(self):
#         return "Volando..."


"""principio de inversion de dependencias"""

class Motor:
    def arrancar(self):
        print("Motor arrancado")

class Coche:
    def __init__(self):
        self.motor = Motor()

    def encender(self):
        self.motor.arrancar()

# Ejemplo de uso

class Motor:
    def arrancar(self):
        pass

class MotorGasolina(Motor):
    def arrancar(self):
        print("Motor de gasolina arrancado")

class MotorElectrico(Motor):
    def arrancar(self):
        print("Motor eléctrico arrancado")

class Coche:
    def __init__(self, motor):
        self.motor = motor

    def encender(self):
        self.motor.arrancar()

# Ejemplo de uso
motor = MotorGasolina()  # O MotorElectrico()
coche = Coche(motor)
coche.encender()
