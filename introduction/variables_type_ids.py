class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_dog = Dog("Buddy", 3)
dog2 = Dog("Buddy", 3)
# print(my_dog)
# print(type(5)) 
x = [1,2,3]
y = x

print(x is y)