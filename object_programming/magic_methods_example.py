class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
    
    def __eq__(self, value):
        print()
        return self.name == value

    def __dict__(self):
        return {
            "name": self.name,
            "age": self.age
        }
    

pablo01 = User("Pablo", 30)
pablo02 = User("Pablo", 30)
# print(pablo01 == pablo02)
print(pablo01.__dict__())
