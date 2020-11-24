# design a stack_name method that returns a person's first name.print
# we sill assume that the given name is the forst woed
# of the name attribute(that is, there
# are no compound names)

class person:

    def __init__(self, name, age):
        """
        docstring
        """
        self.name = name
        self.age = age

    def stack_name(self):
        """
        docstring
        """
        return self.name.split()[0]


juan = person('Juan Martinez', 18)

print(juan.stack_name())
