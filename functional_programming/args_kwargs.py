# def sumar(*args: int) -> int:
#     suma = 0
#     for num in args:
#         suma += num
#     return suma

# def info_estudiantes(**kwargs: str) -> None:
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# # print(sumar(1, 2, 3))  # 6
# # print(sumar(4, 5, 6, 7))  # 22

# info_estudiantes(nombre="Alice", edad="21", carrera="Ingeniería")



dict_aux = {"nombre" : "pablo"}
dict_aux2 = {"apellido" : "sandoval"}
print(dict_aux | dict_aux2)