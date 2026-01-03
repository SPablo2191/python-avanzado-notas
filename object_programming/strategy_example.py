class Delivery:
    """Estrategia de entrega abstracta."""
    def ejecutar(self):
        pass

class UberDelivery(Delivery):
    """Estrategia de entrega específica para Uber."""
    def ejecutar(self):
        return "Estrategia de entrega Uber"

class RappiDelivery(Delivery):
    """Estrategia de entrega específica para Rappi."""
    def ejecutar(self):
        return "Estrategia de entrega Rappi"

class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def ejecutar_estrategia(self):
        return self.estrategia.ejecutar()

# Ejemplo de uso
contexto = Contexto(UberDelivery())
print(contexto.ejecutar_estrategia())  # Estrategia A

contexto.estrategia = RappiDelivery()
print(contexto.ejecutar_estrategia())  # Estrategia B
