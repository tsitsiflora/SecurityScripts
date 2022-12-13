# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list.

def sex_numbers(l: list):
    new_list = []
    student_count = []

    for name in l:
        new_list.append(name.lower())

    for sex in new_list:
        if sex == "male":
            student_count.append((sex, new_list.count(sex)))
            break
    
    for fsex in new_list:
        if fsex == "female":
            student_count.append((fsex, new_list.count(fsex)))
            break

    return student_count

print(sex_numbers(['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']))