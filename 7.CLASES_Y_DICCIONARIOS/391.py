# desing a method to detemine if a
# person is older by returning true, if the
# age is less than 18, or false, otherwise

class perso:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def older(self):
        """
        docstring
        """
        if self.age < 18:
            return True
        else:
            return False


juan = perso('Juan', 34)
manuel = perso('Manuel', 12)

print(juan.older())
