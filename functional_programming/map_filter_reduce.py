from functools import reduce

def es_par(num: int) -> bool:
    return num % 2 == 0

def sumar(x: int, y: int) -> int:
    return x + y

def cuadrado_numero(num : int) -> int:
    return num ** 2

numeros = [1, 2, 3, 4, 5]


# Aplicando map para elevar al cuadrado cada número en la lista
# cuadrados = map(cuadrado_numero, numeros)

# print(list(cuadrados))

# Aplicando filter para obtener solo los números pares
# pares = filter(es_par, numeros)

# print(list(pares))

# print(sum(numeros))
# # Aplicando reduce para sumar todos los números
suma_total = reduce(sumar, numeros)

print(suma_total)