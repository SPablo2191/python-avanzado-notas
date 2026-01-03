class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self):
        print("hhice algo")
        for observador in self.observadores:
            observador.actualizar()

class Observador:
    def actualizar(self):
        print("El observador ha sido notificado")

# Ejemplo de uso
sujeto = Sujeto()
observador1 = Observador()
observador2 = Observador()

sujeto.agregar_observador(observador1)
sujeto.agregar_observador(observador2)

sujeto.notificar()
# Salida:
# El observador ha sido notificado
# El observador ha sido notificado
