# Public

class Public:
    def __init__(self):
        self.public_variable = 10


obj = Public()
print(obj.public_variable)  # Accessible outside the class


# Private
class Private:
    def __init__(self):
        self.__private_variable = 20

    @property
    def get_private_variable(self):
        return self.__private_variable

    @get_private_variable.setter
    def get_private_variable(self, value):
        self.__private_variable = value


obj = Private()
# print(obj.__private_variable)  # This would result in an error
print(obj.get_private_variable)  # Access through a method


# Protect
class Protect:
    def __init__(self):
        self._protected_variable = 30


class OpenProtect(Protect):
    def get_protected_variable(self):
        return self._protected_variable


obj = OpenProtect()
# print(obj._protected_variable)  # It can be accessed within subclasses
print(obj.get_protected_variable())  # Access through a method
