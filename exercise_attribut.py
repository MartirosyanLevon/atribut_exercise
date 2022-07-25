class Person:
    def __init__(self, name='Jhon', surname='Smith'):
        self.name = name
        self.surname = surname
        self.__email = None

    @property
    def email(self):
        if self.__email is None:
            return f"{self.name}{self.surname}.@Matrix.com"
        else:
            return self.__email

    @email.setter
    def email(self, value):
        self.__email = value


p1 = Person()
print(p1.email)
