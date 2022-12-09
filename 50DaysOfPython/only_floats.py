# Write a function which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither
# argument is a float.

def only_floats(a, b):
    if isinstance(a or b, float):
        return 1
    elif isinstance(a and b, float):
        return 2
    else:
        return 0

print(only_floats(12, 8))