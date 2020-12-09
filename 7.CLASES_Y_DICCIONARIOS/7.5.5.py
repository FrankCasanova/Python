# a phone book
class Listín:

    def __init__(self) -> None:
        self.listín = {}

    def añadir(self, nombre, teléfono):
        if nombre in self.listín:
            if not teléfono in self.listín[nombre]:
                self.listín[nombre].append(teléfono)
        else:
            self.listín[nombre] = [teléfono]

    def consultar(self, nombre):
        if nombre in self.listín:
            return self.listín[nombre]
        else:
            return []

    def eliminar(self, nombre):
        if nombre in self.listín:
            del self.listín[nombre]

    def __str__(self) -> str:
        return f'{self.listín}\n'

# fin de la clase


def monstrar_listín(listín):

    print(listín)


def menú():
    opción = 0

    while opción < 1 or opción > 5:
        print('1) Añadir teléfono')
        print('2) Consultar listín')
        print('3) Eliminar persona del listín')
        print('4) Mostrar listín.')
        print('5) Salir')
        opción = int(input('Escoge una opción: '))

    return opción


# programa principal
listín = Listín()

opción = 0


while opción != 4:

    opción = menú()

    if opción == 1:
        nombre = input('Nombre: ')
        teléfono = input('Teléfono: ')
        listín.añadir(nombre, teléfono)
        más = input(f'Deseas añadir otro teléfono a {nombre}? (s/n): ')

        while más == 's':
            teléfono = input('Teléfono: ')
            listín.añadir(nombre, teléfono)
            más = input(f'Deseas añadir otro teléfono a {nombre}? (s/n): ')

    elif opción == 2:
        nombre = input('Nombre: ')
        teléfonos = listín.consultar(nombre)
        for teléfono in teléfonos:
            print(teléfono)

    elif opción == 3:
        nombre = input('Nombre: ')
        listín.eliminar(nombre)

    elif opción == 4:
        monstrar_listín(listín)
