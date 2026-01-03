class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Ejemplo de uso
singleton1 = Singleton() # singleton
singleton2 = Singleton() # ya se reusa
print(singleton1 is singleton2)  # True (Ambos son la misma instancia)
