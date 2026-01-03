class Dog:
    name = "Laika"
    def talk(self):
        """Esto es un metodo de instancia"""
        print("Woof!")

    @classmethod
    def class_method(cls):
        """Esto es un metodo de clase"""
        print("Esto es un metodo de clase")

    @staticmethod
    def static_method(a,b):
        """Esto es un metodo estatico - puede ser llamado desde una clase o instancia"""
        print("Esto es un metodo estatico")




dog =  Dog()
dog.static_method(1,2)

Dog.class_method()