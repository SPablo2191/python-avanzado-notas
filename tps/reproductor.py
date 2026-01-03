# Clase base para las fuentes de sonido - "Interfaz informal"
class FuenteSonido:
    def reproducir(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")
















# Subclase para fuente MP3
class MP3(FuenteSonido):
    def reproducir(self):
        print("Sonando MP3")

# Subclase para fuente CD
class CD(FuenteSonido):
    def reproducir(self):
        print("Sonando CD")

# Subclase para fuente Consola
class Consola(FuenteSonido):
    def reproducir(self):
        print("Sonando Consola")

class Mp4(FuenteSonido):
    pass

# Clase Reproductor
class Reproductor:
    def __init__(self):
        self.fuente : FuenteSonido = MP3()  # Fuente por defecto

    def reproducir(self):
        self.fuente.reproducir()

    def cambiar_fuente(self, nueva_fuente : FuenteSonido):
        self.fuente = nueva_fuente

# Ejemplo de uso
if __name__ == "__main__":
    reproductor = Reproductor()
    reproductor.reproducir()  # Sonando MP3

    reproductor.cambiar_fuente(CD())
    reproductor.reproducir()  # Sonando CD

    reproductor.cambiar_fuente(Consola())
    reproductor.reproducir()  # Sonando Consola
