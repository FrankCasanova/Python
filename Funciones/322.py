# uses the functions developed in exercise
# 295 and desings new functions to build a
# program that presents the following
# menu and allows executing the actions
# corresponding to each option

import numpy as np
from numpy.core.defchararray import count, index


def approved_list(name, note):

    for i, o in zip(name, note):
        if o > 5:
            print(f'{i} ha aprobado, ha sacado un {o}')


def number_passes(l):
    passes = [i for i in l if i > 5]
    return passes


def students_MaxMark(lstudents, lnotes):
    maxMark = [(i, o) for i, o in zip(lstudents, lnotes)
               if i in lstudents and o == 10]
    return maxMark


def higher_median_grade(lstudents, lnotes):
    median = np.median(lnotes)

    students_sup_median = [i for i, o in zip(lstudents, lnotes) if o >= median]

    return students_sup_median

    median = np.median(lnotes)

    students_sup_median = [i for i, o in zip(lstudents, lnotes) if o >= median]

    return students_sup_median


def student_exist(lstudents, lnotes, name):

    for i, o in zip(lstudents, lnotes):
        if name in i:
            return o
    return None


def add_student(lstudents, lnotes):
    """
    add a student or students and the grade they got
    """
    option = 'y'

    while option == 'y':

        try:
            name = input('Name: ')
            qualification = float(input('Qualification: '))
            lstudents.append(name)
            lnotes.append(qualification)

        except ValueError:
            print('wrong value')

        option = input(
            'if you want add more studets press: \'y\' otherwise press any key: ')


def show_students(lstudents, lnotes):
    for student, quali in zip(lstudents, lnotes):
        print(f'student: {student}, qulification: {quali}')


def calculate_med(lnotes):

    median = np.median(lnotes)

    return median


def passed(lnotes):
    passed = len([i for i in lnotes if i >= 5])
    return passed


def best_quali(lstudents, lnotes):
    return [i for i, o in zip(lstudents, lnotes) if o >= 7]


def check_quali(lstudents, lnotes):

    option = 'y'
    while option == 'y':
        name = input('Name of the student: ')
        name = name.title()

        if name in lstudents:
            print(lnotes[lstudents.index(name)])
            option = input(
                'if you want continue checking quialifications press \'y\' \n otherwise press enter.')

        else:
            print('The name doesn\'t exist in our DB, please try again with other name')
            option = input(
                'if you want continue checking quialifications press \'y\' \n otherwise press enter.')


students = ['Ana Pi', 'Pau López', 'Luis Sol', 'Mar Vega', 'Paz Mir']
test_notes = [10, 5.5, 2.2, 8.5, 7.0]

check_quali(students, test_notes)
