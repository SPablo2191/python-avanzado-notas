# Clase padre: Animal
class Animal:
    def __init__(self, especie, edad,respirar):
        self.especie = especie
        self.respirar = respirar
        self.edad = edad

    def describeme(self):
        print(f"Soy un {self.especie} y tengo {self.edad} años.")
    
    def hablar(self):
        pass

    def caminar(self):
        pass

class Carnivoro:
    def comer(self):
        print("que rico asado")

class Herbivoro:
    def comer(self):
        print("que rico pasto")

# # Clase hija: Perro (hereda de Animal)
class Perro(Animal,Carnivoro):
    def __init__(self, especie, edad,raza):
        super().__init__(especie, edad)
        self.raza = raza
    # Clase hija: Vaca
class Vaca(Animal,Herbivoro):
    def hablar(self):
        print("moo")
# Clase hija: Abeja
class Abeja(Animal):
    def hablar(self):
        print("bzzzz")


class Sverro(Animal):
    pass


class Humano(Animal):
    def hablar(self):
        print("hola")


# # # Crear un perro
mi_perro = Perro("mamífero", 5,"chihuahua")
# mi_perro.describeme()  # Salida: Soy un mamífero y tengo 5 años.

mi_vaca = Vaca("mamífero", 7)
mi_abeja = Abeja("insecto", 1)

# [animal.comer() for animal in [mi_perro,mi_vaca]]

granja : list[Animal] = [mi_perro,mi_abeja,mi_vaca, Humano()]


[animal.hablar() for animal in granja]


