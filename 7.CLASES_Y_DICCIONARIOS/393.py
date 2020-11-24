class person:

    def __init__(self, name, age, sex):
        """
        docstring
        """
        self.name = name
        self.age = age
        self.sex = sex

    def stack_name(self):
        """
        docstring
        """
        return self.name.split()[0]

    def __str__(self) -> str:
        """
        docstring
        """
        return f'Name: {self.name}.\nAge: {self.age}.\n'\
            f'gender: {self.sex}.'


juan = person('Juan', 12, 'M')

print(juan)
