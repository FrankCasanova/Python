def search_input(name, lastname):

    with open('agenda.txt', 'r') as file:

        line1 = file.readline()

        while line1 != '':

            line2 = file.readline()
            line3 = file.readline()

            if name == line1[:-1] and lastname == line2[:-1]:
                file.close()
                return line3[:-1]

            line1 = file.readline()

    return None


def add_input(name, lastname, number):

    with open('agenda.txt', 'a') as file:

        file.write(name + '\n')
        file.write(lastname + '\n')
        file.write(str(number) + '\n')


def remove_input(name, lastname):

    with open('agenda.txt', 'r') as file, open('agenda.txt.copia', 'w') as fcopy:

        line1 = file.readline()

        while line1 != '':

            line2 = file.readline()
            line3 = file.readline()

            if name != line1[:-1] or lastname != line2[:-1]:

                fcopy.write(line1)
                fcopy.write(line2)
                fcopy.write(line3)

            line1 = file.readline()

    with open('agenda.txt', 'w') as file, open('agenda.txt.copia', 'r') as fcopy:

        for line in fcopy:
            file.write(line)


def menu():

    print('Bienvenido a la aplicación de agenda.')
    print('Qué desea realizar?')
    print('a) buscar en la agenda.')
    print('b) añadir un usuario a la agenda.')
    print('c) borrar un usuario de la agenda.')

    option = input('Elija una opción: ')

    while option != '':

        if option.lower() > 'c' or option.lower() < 'a':
            print('Elija solo una de las opciones: a, b o c.')

        if option.lower() == 'a':

            name = input('Nombre que desea buscar: ')
            lastname = input('Apellido: ')

            search_input(name=name, lastname=lastname)
            print('gracias por usar nuestra aplicación')
            break

        if option.lower() == 'b':

            name = input('Nombre: ')
            lastname = input('Apellido: ')
            number = int(input('Número: '))

            add_input(name=name, lastname=lastname, number=number)
            print('gracias por usar nuestra aplicación')
            break

        if option.lower() == 'c':

            name = input('Nombre del usuario que desea borrar de la agenda: ')
            lastname = input(
                'Apellido del usuario que desea borrar de la agenda')

            remove_input(name=name, lastname=lastname)
            print('gracias por usar nuestra aplicación')
            break


menu()
