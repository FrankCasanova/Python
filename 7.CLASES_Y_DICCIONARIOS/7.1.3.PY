class Persona:

    def __init__(self, nombre, dni, edad) -> None:
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def iniciales(self) -> str:
        cadena = ''
        for carácter in self.nombre:
            if carácter >= 'A' and carácter <= 'Z':
                cadena = cadena + carácter + '. '
        return cadena

    def __str__(self) -> str:
        cadena = f'nombre: {self.nombre}\n'
        cadena = cadena + f'DNI: {self.dni}\n'
        cadena = cadena + f'Edad: {self.edad}'
        return cadena

    def copia(self):
        """
        docstring
        """
        nuevo = Persona(self.nombre[:], self.dni[:], self.edad)
        return nuevo


def nada_util(persona1, persona2):
    """
    docstring
    """
    persona1.edad += 1
    persona3 = persona2
    persona4 = persona2.copia()
    persona3.edad -= 1
    persona4.edad -= 2

    return persona4


juan = Persona('Juan Pérez', '18273645E', 22)
pedro = Persona('Pedro López', '23456789A', 19)

otro = nada_util(juan, pedro)

print(juan)
print(pedro)
print(otro)
