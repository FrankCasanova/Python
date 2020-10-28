# in the problem of the students and the notes it is requesd:
# 1) Desing a procedure that receives two lists and displays
# on the screen the names of all the students who passed
# the exam.
#
# 2)desing a function that receives the list of grades and returns
# the number of passes.
#
# 3) desing a procedure that receives two lists and display on the
# screen the name of all the students who obtained the maximun mark
#
# 4) desing a procedure that reveives the two lists and displays on
# the screen the name of all students whose grade is equal to or higher
# than the average grade
#
# 5) desing a function that reveives the two lists and a name (a string);
# if the name is in the student list, it will return your grade, if not
# it will return None.

import numpy as np


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


students = ['Ana Pi', 'Pau López', 'Luis Sol', 'Mar Vega', 'Paz Mir']
test_notes = [10, 5.5, 2.2, 8.5, 7.0]
