#this script accepts an age and returns whether the person is allowed to drive or not
min_driving_age = 18
name = input("Enter name: ")
age = int(input("Enter age: "))

def driver_check(name, age):
    '''Print {name} is allowed to drive or {name} is not allowed to drive
        based to the check against the constant min_driving_age'''
    is_allowed = 'is allowed' if age >= min_driving_age else 'is not allowed'
    print(f"{name} {is_allowed} to drive")

driver_check(name, age)