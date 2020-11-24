class Fecha:

    def __init__(self, day, month, year):
        """
        docstring
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """
        docstring
        """
        return f'{self.day}/{self.month}/{self.year}'

    def long_date(self):
        """
        exercise 400
        """
        months = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']

        month = months[self.month-1]

        return print(f'{month} {self.day} of {self.year}')

    def leap(self):
        """
        docstring
        """

        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def validate(self):
        '''
        exercise 401
        '''
        if self == Fecha(-1, -1, -1):
            return False

        thirty = [1, 4, 9, 11]
        months = range(1, 13)

        if self.month not in months and self.day > 31 or self.day < 0:
            return print(f'invalid date.\nthe number included in the day field'
                         f'it is the {self.day} and that month does not exist in the year')

        elif self.month in thirty and self.day > 30 or self.day < 0:
            return print(f'the indicated month: {self.month} has 30 days\n'
                         f'not on more, not one less')

        elif self.month == 2:

            if self.leap() and self.day > 29 or self.day < 0:
                return print(f'the indicated month: {self.month} has 29 days\n'
                             f'not on more, not one less')

            if not self.leap() and self.day > 28 or self.day < 0:

                return print(f'the indicated month: {self.month} has 28 days\n'
                             f'not on more, not one less')

            else:
                return print('the date has been entered correctly')
        else:

            return print('the date has been entered correctly'), True

    def is_minor(self, other_date):

        if self.year < other_date.year:
            return True
        elif self.year > other_date.year:
            return False

        if self.month < other_date.month:
            return True
        elif self.month > other_date.month:
            return False

        return self.day < other_date.day

    def is_equal(self, other_date):

        return self.year == other_date and \
            self.month == other_date.month and \
            self.day == other_date.day

    def add_one_day(self):

        thirty = [1, 4, 9, 11]

        if self.month == 2 and self.day == 29:

            if self.leap():
                return Fecha(1, 3, self.year)
            else:
                return print('Ese año no es bisiesto')

        elif self.month == 2 and self.day == 28:
            return Fecha(1, 3, self.year)

        elif self.month == 2 and self.day == 28:
            return Fecha(1, 3, self.year)

        elif self.month in thirty and self.day == 30:
            if self.month < 12:
                return Fecha(1, self.month+1, self.year)
            else:
                return Fecha(1, 1, self.year+1)

        elif self.day == 31 and self.month == 12:
            return Fecha(1, 1, self.year+1)

        elif self.day == 31:
            return Fecha(1, self.month+1, self.year)

        else:
            return Fecha(self.day+1, self.month, self.year)


def read_date():
    """
    docstring
    """

    fecha = Fecha(-1, -1, -1)
    while not fecha.validate():
        day = 0
        while day < 1 or day > 31:
            day = int(input('Day: '))
        month = 0
        while month < 1 or month > 12:
            month = int(input('month: '))
        year = int(input('year: '))

        fecha = Fecha(day, month, year)

        if fecha.validate():

            return Fecha(day, month, year)
        else:

            return print('date not valid')


fecha = Fecha(28, 2, 1988)

print(fecha.add_one_day())
