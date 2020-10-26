# in a program that we design, we ask the
# user nmerous questions that requier an
# affirmative or negative answer. design a
# function called yes_or_no that receives a string
# (the question). this string will be displayed on the
# screen and the user will be asked to respond.
# we will only accept as valid answers yes, s, Yes YES
# and the same for nose. every time the user makes a mistake,
# a message will appear on the screen to remind him of the
# acceptable answers. the function will return true if the
# answer is affirmative and false otherwise


def yes_or_no(quest):

    print(quest)

    possibles_answr = ['yes', 'y', 'Yes', 'YES', 'no', 'n', 'No', 'NO']
    affirmative_answr = ['yes', 'y', 'Yes', 'YES']
    negative_answr = ['no', 'n', 'No', 'NO']

    answer = ''

    while answer not in possibles_answr:

        answer = input('Write your answer: \n')

        if answer not in possibles_answr:

            print('You can only answer whit: yes, y, Yes, YES, no, n, No, NO')

    if answer in affirmative_answr:
        return True
    else:
        return False


question = 'Are you male?'

print(yes_or_no(question))
