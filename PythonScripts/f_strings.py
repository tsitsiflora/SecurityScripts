#string formatting methods

name = "Bob"
age = 10

print("My name is %s. I am %s years old" % (name, age))

print("My name is {0}. I am {1} years old".format(name, age))

print("My name is {name}. I am {age} years old".format(name = name, age = age))

print(f"My name is {name}. I am {age} years old.")