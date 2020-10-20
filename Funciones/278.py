# desing a function that receives a list of strings and returns
# the longest common prefix. for example, the string pol is the longest
# common prefix in this list [ pliedro, policia, polifona, polinizar, polo, politica]


def detect_longest_prefix(strings):

    prefix = ''

    max_sentense = max(strings, key=len)
    min_sentense = min(strings, key=len)

    for i, o in zip(max_sentense, min_sentense):

        if i == o:
            prefix += i
        else:
            break

    return prefix


list_strings = ['poliedro', 'policía',
                'polifona', 'polinizar', 'polo', 'política']

print(detect_longest_prefix(list_strings))
