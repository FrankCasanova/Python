class sets():
    def __init__(self) -> None:
        """
        docstring
        """
        self.elements = []

    def insert(self, element):
        if not (element in self.elements):
            self.elements.append(element)

    def erase(self, element):
        if (element in self.elements):
            self.elements.remove(element)

    def __str__(self) -> str:
        cadena = '{'
        if len(self.elements) > 0:
            for elemento in self.elements[:-1]:
                cadena = cadena + str(elemento) + ', '
            cadena = cadena + str(self.elements[-1])
            return cadena + '}'

    def talla(self):
        return len(self.elements)

    def pertenece(self, elemento):
        return elemento in self.elements

    def is_empty(self):
        return len(self.elements) == 0

    def union(self, otro):
        c = sets()
        c.elements = self.elements[:]
        for elemento in otro.elements:
            c.insert(elemento)
        return c

    def interseccion(self, otro):
        c = sets()
        for element in self.elements[:]:
            if element in otro.elements:
                c.insert(element)

        return c

    def diferencia(self, otro):
        c = sets()
        for element in self.elements[:]:
            if element not in otro.elements:
                c.insert(element)

        return c

    def incluye(self, otro):
        for elemento in otro.elements:
            if not (elemento in self.elements):
                return False
        return True


a = sets()
a.insert(3)
a.insert(5)
a.insert(3)
a.insert(7)
a.insert(6)
a.insert(3)

b = sets()
b.insert(8)
b.insert(2)
b.insert(6)
b.insert(1)
b.insert(7)
b.insert(3)


print(a.diferencia(b))
print(a.interseccion(b))


print(a)
print(a.talla())
print(a.pertenece(5))
print(a.is_empty())
