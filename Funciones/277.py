# desings a function that, given a list of strins, returns a list with all the longest strins,
# that is, if two or more strings have the same length and are the longes,
# the listr will contain them all

def more_longests(names):

    candidates = []

    for i in names:

        if len(candidates) == 0:
            candidates.append(i)

        elif len(i) > len(candidates[0]):
            candidates[0] = i
        elif len(i) == len(candidates[0]):
            candidates.append(i)

    return candidates


i_list = ['ana', 'Pepe', 'Juan', 'Paz']

print(more_longests(i_list))
