# we store in a matrix of m x n elements the
# grade chosen by m students (whom we
# know by their list number) in the evaluation
# of n exercises delivered weekly (qhen an exercise has not
# been delivered, the grade is -1).
#
# desingsn functions and procedures that perform the following calculations:
#
# given the number of a student, return the
# number of exercises delivered
#
# given the number of a student, return the average over the
# exercises delivered.
#
# given the number of a student, return the average
# of the exercises submitted if they were submitted all,
# otherwise, the average is 0.
#
# return the number of all students who have submitted all
# the exerrcises and have an average of 3.5 or higer
#
# given the number of an exercise, return the number of
# students who have presented it.
#
# given the number of an exercise, return the
# highest grade obtained.
#
# given the number of an exercise, retun the
# lowest grade obtained.
#
# return the number of dropouts based on
# the week.
# we consider that a student dropped out in week s
# if he has not submitted any exercises since then.
# this procedure will display the number of dropouts for
# each week (if a student has never submitted any exercise,
# they dropped out on <<week zero>>)


import numpy as np


def total_exercises(student, qualis):
    """
    given a number of student, return
    a numebr of exercises delivered

    """
    delivered = [i for i in qualis[student-1] if i > 0]

    return len(delivered)


def median_total_exercises(student, qualis):
    return np.mean(qualis[student-1])


def absolute_mean(student, qualis, total_exercises):

    delivered = [i for i in qualis[student-1] if i > 0]

    if len(delivered) < total_exercises:
        return 0

    else:
        return np.mean(qualis[student-1])


def mean_all_student_delivered(qua):
    """
    docstring
    """
    return [index+1 for index, values in enumerate(qua) if -1 not in values and np.mean(values) > 3.5]


def delivered_exercise(num, quali):
    """
    docstring
    """
    return len([index for index, value in enumerate(quali) if quali[index][num] != -1])


def mean_exercises_delivered(num, quali):
    return round(np.mean([lis[num] for index, lis in enumerate(quali) if quali[index][num] != -1]), 2)


def max_grade(num, quali):
    return max([lis[num] for index, lis in enumerate(quali) if quali[index][num] != -1])


def min_grade(num, quali):
    return min([lis[num] for index, lis in enumerate(quali) if quali[index][num] != -1])


student1 = 1
student2 = 2
student3 = 3
student4 = 4
student5 = 5

total_exercises = 4

quali = [[5.5, 8.9, 6, -1], [-1, 5, 7.6, 6],
         [6, 6, 6.7, 6], [7, 8, 7.2, 8], [2, 7.6, .3, 1]]


print(min_grade(1, quali))
