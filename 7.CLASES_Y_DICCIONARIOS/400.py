class MP3:

    def __init__(self, tittle, interpreter, duration, gender) -> None:

        self.tittle = tittle
        self.interpreter = interpreter
        self.duration = duration
        self.gender = gender

    def summary(self):
        return (self.tittle, self.interpreter)

    def __str__(self) -> str:
        datos = f'tittle: {self.tittle}\n'\
            f'interpreter: {self.interpreter}\n'\
                f'duration: {self.duration}\n'\
            f'gender: {self.gender}'
        return datos


def songs_per_interpreter(name, list1):
    """
    docstring
    """
    songs = [
        i.summary()
        for i in list1
        if i.interpreter == name
    ]
    # for i in list1:
    #     if i.interpreter == name:
    #         return i.summary()

    return print(songs)


def add_song(list1):
    """
    docstring
    """
    tittle = input('tittle: ')
    interpreter = input('interpreter: ')
    duration = input('duration: ')
    gender = input('gender: ')
    return list1.append(MP3(tittle, interpreter, duration, gender))


def songs_per_gender(gender, list1):
    """
    docstring
    """
    songs = [
        i.summary()
        for i in list1
        if i.gender == gender
    ]
    # for i in list1:
    #     if i.interpreter == name:
    #         return i.summary()

    return print(songs)


data_base = [
    MP3('quitate', 'maria montero', 3.30, 'copla'),
    MP3('cariño', 'pedrín', 2.10, 'latin'),
    MP3('muere perra', 'zurco', 1.50, 'rock'),
    MP3('bésame', 'pedrín', 2.20, 'latin'),
    MP3('cállate puta', 'zurco', 2.00, 'rock'),
    MP3('zorra dame de comer', 'zurco', 1.00, 'rock')
]

rock = 'copla'

songs_per_gender(rock, data_base)
