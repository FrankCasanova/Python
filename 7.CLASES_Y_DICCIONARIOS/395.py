# designs a procedure that, given a list of
# students, displays the data of all of tham
# on the screen

class Estudiantes:

    def __init__(self, nombre, grupo, nota, práctica):
        """
        docstring
        """
        self.nombre = nombre
        self.grupo = grupo
        self.nota = nota
        self.práctica = práctica

    def __str__(self):
        """
        docstring
        """
        cadena = f'Nombre: {self.nombre}.\nGrupo: {self.grupo}.\n'\
            f'Nota: {self.nota}.\n'

        if self.práctica:
            cadena += 'Practica entregada.'
        else:
            cadena += 'Practica no entregada'

        return cadena


def lee_estudiante():
    """
    docstring
    """
    nombre = input('Nombre: ')
    grupo = input('Grupo: ')
    nota = float(input('Nota: '))
    entregada = input('Practica entregada (s/n): ')
    practica = entregada == 's'

    return Estudiantes(nombre, grupo, nota, practica)

# nuevo_estudiante = lee_estudiante()


def lee_y_añade_estudiante(lista):
    """
    docstring
    """
    estudiante = lee_estudiante()
    lista.append(estudiante)


def mostrar_datos(lista):
    """
    docstring
    """
    return [print(i) for i in lista]


def mostrar_grupo(lista, grupo):

    return [print(i) for i in lista if i.grupo == grupo]


estud = []

while (option := input('añadir estudiante? ').lower()) != 'n':
    lee_y_añade_estudiante(estud)

print('.................')
print('.................')
print('.................')
mostrar_grupo(estud, 'c')
print('.................')
print('.................')
print('.................')
print('.................')
