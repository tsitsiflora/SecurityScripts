# write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order.

def lowercase_names(l: list):
    d = []
    for name in sorted(names, reverse=True):
        if name.islower():
            d.append(name)
            name_tuple = tuple(d)

    return name_tuple

names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]
print(lowercase_names(names))