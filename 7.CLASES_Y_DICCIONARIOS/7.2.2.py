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


def mostrar_datos(lista):
    """
    docstring
    """
    return [print(i) for i in lista]


def mostrar_grupo(lista, grupo):

    return [print(i) for i in lista if i.grupo == grupo]


def acta(lista):
    for estudiante in lista:
        print(estudiante.nombre, estudiante.calificación())


def nota_media(lista):
    suma = 0
    cantidad = 0
    for estudiante in lista:
        if estudiante.practica:
            suma += estudiante.nota
            cantidad += 1

    if cantidad != 0:
        return suma / cantidad
    else:
        return 0.0


def porcentaje_de_prácticasa_entregadas(lista):
    if len(lista) != 0:
        cantidad = 0
        for estudiante in lista:
            if estudiante.práctica:
                cantidad += 1
        return cantidad / len(lista)*100
    else:
        return 0.0


def nota_media_por_grupo(lista, grupo):
    cantidad = 0
    notas = 0
    for estudiante in lista:
        if estudiante.grupo == grupo and estudiante.aprobado() == 'aprobado':
            notas += estudiante.nota
            cantidad += 1
    return notas / cantidad

def mejores_estudiantes(lista):
    nota_más_alta = 0
    mejores = []
    for estudiante in lista:
        if estudiante.practica:
            if estudiante.nota > nota_más_alta:
                mejores = [estudiante]
                nota_más_alta = estudiante.nota
            elif estudiante.nota == nota_más_alta:
                mejores.append(estudiante)

    return mejores                


estud = []

while (option := input('añadir estudiante? ').lower()) != 'n':
    lee_y_añade_estudiante(estud)
