class User:
    def __init__(self, user_name, pwd):
        self.user_name = user_name
        self.__pwd = pwd
        self.__pwd_bank = "1234"


user = User(user_name="pablo",pwd="123")


print(user.user_name)
print(user.__pwd_bank)