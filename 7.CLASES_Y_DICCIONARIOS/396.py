class estudiante:

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
            f'Nota: {self.nota}.'

        if self.práctica:
            cadena += 'Practica entregada.'
        else:
            cadena += 'Practica no entregada'

        return cadena

    def calificación(self):
        if not self.práctica:
            return 'suspenso'
        else:
            if self.nota < 5:
                return 'suspenso'
            elif self.nota < 7:
                return 'aprobado'
            elif self.nota < 8.5:
                return 'notable'
            elif self.nota < 10:
                return 'sobresaliente'
            else:
                return 'MATRICULA DE HONOR'

    def aprobado(self):
        if self.nota > 5:
            return 'aprobado'
        else:
            return 'suspenso'


def lee_estudiante():
    """
    docstring
    """
    nombre = input('Nombre: ')
    grupo = input('Grupo: ')
    nota = float(input('Nota: '))
    entregada = input('Practica entregada (s/n): ')
    practica = entregada == 's'

    return estudiante(nombre, grupo, nota, practica)

# nuevo_estudiante = lee_estudiante()


def lee_y_añade_estudiante(lista):
    """
    docstring
    """
    estudiante = lee_estudiante()
    lista.append(estudiante)


lista_de_estudiantes = []

lee_y_añade_estudiante(lista_de_estudiantes)

print(lista_de_estudiantes[0].aprobado())
