def without_repeat(sList):
    result = []
    for i in sList:
        if i not in result:
            result.append(i)
    return result


a_list = without_repeat([1, 2, 1, 3, 2])
print(a_list)
