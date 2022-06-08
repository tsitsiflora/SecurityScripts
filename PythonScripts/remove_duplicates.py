# this script removes duplicates from a sorted list

# using sets
def remove_duplicates(array):
    new_array = set(array)
    return new_array

# using loops
def remove_dups(array):
    new_list = []
    for i in array:
        if i not in new_list:
            new_list.append(i)
        else:
            pass
    return new_list

array = [1, 2, 3, 3, 4, 5, 5, 6, 5, 3, 0]
print(remove_duplicates(array))
print(remove_dups(array))