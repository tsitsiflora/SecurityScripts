# given an array containing None values, fill in the None 
# values with the most recent non-None value


def none_values(array):
    valid = 0
    res = []
    for i in array:
        if i != None:
            valid = i
            res.append(i)
        else:
            res.append(valid)

    return res


print(none_values([1, 2, None, 4, None, None, 7, None]))
