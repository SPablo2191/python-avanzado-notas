import re 

class EmailValidationException(Exception):
    pass


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

email = input()


while True:
    try:
        if email == "":
            raise EmailValidationException("No se acepta email vacio")
        if(not(re.fullmatch(regex, email))):
            raise EmailValidationException("Formato invalido")
    except Exception as e:
        print(e)
    else:
        print("Email valido <3")
        break