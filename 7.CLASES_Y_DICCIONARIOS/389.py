# desing a prgram dthat prompts for two
# data form several people and adds it to
# an initially empty list. every time a
# person's data is read into the program, it
# will ask if you want to continue introducing
# new people. when the user says no, the program will stop

personas = []

while (persona := input('Escriba el nombre de la persona que quiera añadir, si no quiere añadir a nadie escriba \'salir\':').lower()) \
        != 'salir':
    personas.append(persona.title())


print(personas)
