class Socio:

    def __init__(self, dni, nombre, teléfono, domicilio) -> None:

        self.dni = dni
        self.nombre = nombre
        self.teléfono = teléfono
        self.domicilio = domicilio

    def __str__(self) -> str:
        return f'DNI: {self.dni}\nNombre: {self.nombre}\n'\
            f'Teléfono: {self.teléfono}\nDomicilio: {self.domicilio}.'


class Película:

    def __init__(self, título, género) -> None:

        self.título = título
        self.género = género
        self.alquilada = None

    def __str__(self) -> str:
        cadena = f'Título: {self.título}\nGénero: {self.género}.'

        if self.alquilada == None:
            cadena = cadena + 'Disponible\n'
        else:
            cadena = cadena + f'Alquilada a: {self.alquilada}.'

        return cadena


class Videoclub:

    def __init__(self) -> None:
        self.socios = {}
        self.películas = {}

    def cotiene_socio(self, dni):
        for socio in self.socios:
            if socio.dni == dni:
                return True
            else:
                return False

    def contiene_película(self, título):
        for película in self.películas:
            if película.título == título:
                return True
        return False

    def alta_socio(self, socio):
        """
        docstring
        """
        self.socios[socio.dni] = socio

    def baja_socio(self, dni):
        """
        docstring
        """
        del self.socios[dni]

    def alta_película(self, película, ejemplares):
        """
        docstring
        """
        for i in range(ejemplares):
            nuevo_ejemplar = Película(película.título, película.género)
            self.películas.append(nuevo_ejemplar)

            if película.título in self.películas:
                self.películas[película.título].append(nuevo_ejemplar)
            else:
                self.películas[película.título] = [ nuevo_ejemplar ]        

    def baja_película(self, película, ejemplares):
        """
        docstring
        """
        bajas_efectivas = 0
        i = 0
        while i < len(self.películas) and bajas_efectivas < ejemplares:
            if self.películas[i].título == título and self.película[i].alquilada == None:
                del película[i]
                bajas_efectivas += 1
        else:
            i += 1

        return bajas_efectivas

    def alquilar_película(self, título, dni):
        """
        docstring
        """
        for película in self.películas:
            if película.título == título:
                if película.alquilada == None:
                    película.alquilada = dni
                    return True
        return False

    def devolver_película(self, título, dni):

        for película in self.películas:
            if película.título == título and película.alquilada == dni:
                película.alquilada == None

    def listado_por_género(self, género):

        disponibles = []
        alquiladas = []
        for película in self.películas:
            if película.género == género:
                if película.alquilada == None and not (película.título in disponibles):
                    disponibles.append(película.título)
            if película.alquilada != None and not (película.título in alquiladas):
                alquiladas.append(película.título)

        for título in disponibles:
            print(f'{título} DISPONIBLE')

        for título in alquiladas:
            print(f'{título} NO DISPONIBLE')


def menú():

    print('*** VIDEOCLUB ***')
    print('1) Dar de alta nuevo socio')
    print('2) Dar de baja un socio')
    print('3) Dar de alta nueva película')
    print('4) Dar de baja una película')
    print('5) Alquilar una película')
    print('6) Devolver película')
    print('7) salir')

    while (opción := int(input('Escoge opción: '))) < 1 or (opción := int(input('Escoge opción: '))) > 6:

        return opción


def nuevo_socio():
    dni = input('DNI: ')
    nombre = input('Nombre: ')
    teléfono = input('Teléfono: ')
    domicilio = input('Domicilio: ')
    return Socio(dni, nombre, teléfono, domicilio)


def nueva_película():
    título = input('Título: ')
    género = input('Género: ')


videoclub = Videoclub()


while (opción := menú()) != 8:

    if opción == 1:
        print('Alta nuevo socio')
        socio = nuevo_socio()
        if videoclub.contiene_socio(socio_dni):
            print('Ya existía un socio con DNI', dni)
        else:
            videoclub.alta_socio(socio)

    elif opción == 2:
        print('Baja de socio')
        dni = input('DNI: ')
        if videoclub.contiene_socio(dni):
            videoclub.baja_socio(dni)
        else:
            print('No existe ningún socio con DNI: ', dni)

    elif opción == 3:
        print('Alta de película')
        película = nueva_película()
        ejemplares = int(input('Ejemplares: '))
        videoclub.alta_película(película, ejemplares)

    elif opción == 4:
        print('Baja de película')
        título = input('Título: ')
        ejemplares = int(input('Ejemplares: '))
        bajas = videoclub.baja_película(título, ejemplares)
        if bajas < ejemplares:
            print(f'Solo pude dar de baja {bajas} ejemplares')
        else:
            print('Operación realizada')

    elif opción == 5:
        print('Alquiler de película')

        título = input('Título de la película: ')
        dni = input('DNI del socio: ')
        hay_película = videoclub.contiene_película(título)
        hay_socio = videoclub.cotiene_socio(dni)

        if hay_película and hay_socio:
            if videoclub.alquilar_película(título, dni):
                print('Operación realizada con éxito')
            else:
                print('La película no está disponible')
        else:
            if not hay_película:
                print('No hay película títulada', título)

            if not hay_socio:
                print('No hay socio con DNI', dni)

    elif opción == 6:
        print('Devolver película')
        título = input('Nombre de la película que desea devolver')
        dni = input('DNI del socio: ')
        hay_película = videoclub.contiene_película(título)
        hay_socio = videoclub.cotiene_socio(dni)
        if hay_película and hay_socio:
            resultado = videoclub.devolver_película(título, dni)
            if resultado == 0:
                print('Operación realizada')
            elif resultado > 0:
                print('Película entregada con un retraso')
            else:
                print(f'La película {título} no está alquilada al socio {dni}')
        else:
            if not hay_película:
                print(f'No hay película titulada {título}')

            if not hay_socio:
                print(f'No hay socio con DNI {dni}')

    elif opción == 7:
        print('Listado por género')
        género = input('Género: ')
        videoclub.listado_por_género(género)


opción = menú
