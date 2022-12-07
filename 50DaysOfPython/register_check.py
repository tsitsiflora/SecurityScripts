# Write a function that checks how many
# students are in school. The function takes a dictionary as a
# parameter. Your
# function should return the number of students in school.

def register_check(d: dict):
    count = 0
    for value in d.values():
        if value == 'yes':
            count += 1
    return count


register = {'Michael':'yes','John': 'no','Peter':'yes', 'Mary': 'yes'}
print(register_check(register))