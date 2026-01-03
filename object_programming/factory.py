class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

class AnimalFactory:
    @staticmethod
    def crear_animal(tipo: str) -> Animal:
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()

# Ejemplo de uso
animal : Animal = AnimalFactory.crear_animal("perro")
print(animal.hablar())  # Guau
