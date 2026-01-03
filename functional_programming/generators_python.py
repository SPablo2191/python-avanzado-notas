def contar():
    print("previo yield 1")
    yield 1
    print("previo yield 2")
    yield 2
    print("previo yield final")
    yield 3

# g = contar()

# print(next(g))  # 1
# print(next(g))  # 2
# print(next(g))  # 3
# print(next(g))  # Error: ya no hay más


# otra forma de leer un generador
# for num in contar():
#     print(num)



cuadrados = (i**2 for i in range(5))
for cuadrado in cuadrados:
    print(cuadrado)