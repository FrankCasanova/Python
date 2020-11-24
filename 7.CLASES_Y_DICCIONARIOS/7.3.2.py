# exercise 410:

class Queue:

    def __init__(self):
        self.cola = []

    def add(self, element):
        self.cola.append(element)

    def first(self):
        if len(self.cola) == 0:
            return None
        else:
            return self.cola[0]

    def pop_first(self):
        if len(self.cola) > 0:
            del self.cola[0]

    def __str__(self):
        string = ''
        for element in self.cola:
            string += str(element)+' '

        return string

    def lenght(self):
        return len(self.cola)

    def is_empty(self):
        return len(self.cola) == 0

    def copy(self):
        return self.cola[:]


class Patient:

    def __init__(self, name, seg_number) -> None:

        self.name = name
        self.seg_number = seg_number

    def __str__(self) -> str:

        return f'Nombre: {self.name}.\nNúmero de la seguridad social: {self.seg_number}\n. '


def menu(cola):
    """
    docstring
    """

    print('Bienvenido al gestor de pacientes')
    option = 0
    while option != 3:
        print('Escoja una de las siguientes opciones')
        print('1) Añadir un paciente a la lista de espera')
        print('2) atender al primer paciente de la lista')
        print('3)finalizar la ejecución del programa')
        option = int(input('Seleccione una de las opciones: '))

        if option == 1:
            name = input('Nombre: ')
            seg_number = int(input('Número de la seguridad social: '))
            patient = Patient(name, seg_number)
            cola.add(patient)

        if option == 2:
            print(cola.first())
            print('será atendido')
            cola.pop_first()


cola = Queue()
menu(cola)

print(cola)
