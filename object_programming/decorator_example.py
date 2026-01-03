class Componente:
    def operar(self):
        return "Componente base"

class Decorador(Componente):
    def __init__(self, componente):
        self.componente = componente

    def operar(self):
        return f"{self.componente.operar()} con Decorador"
    
    def describir(self):
        print("")

# Ejemplo de uso
componente = Componente()
decorado = Decorador(componente)
print(decorado.operar())  # Componente base con Decorador
