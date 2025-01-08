class UserAccount:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        if self.__password == password:
            print("Напишите новый пароль")
            return self.__password
        else:
            self.__password = password


Obj = UserAccount('Harold',"fhfheui2@gmail.com",hash("123"))
Obj.password = hash('1234')

