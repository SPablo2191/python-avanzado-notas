class Perro:
    # Constructor (inicializa los atributos)
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre  # Atributo de la clase
        self.raza = raza      # Atributo de la clase
        self.edad = edad      # Atributo de la clase

    # Método que hace que el perro ladre
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    # Método que hace que el perro camine
    def caminar(self):
        print(f"{self.nombre} está caminando...")


        
# Crear objetos (instancias) de la clase Perro
perro1 = Perro("Toby", "Labrador", 3)
perro2 = Perro("Laika", "Beagle", 5)

# Llamar a los métodos de los objetos
perro1.ladrar()
perro2.caminar()
