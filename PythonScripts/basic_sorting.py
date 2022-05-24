#this script demonstrates basic sorting using python built ins

animals = [{'type': 'cat', 'name': 'Stephanie', 'age': 8},
 {'type': 'dog', 'name': 'Devon', 'age': 3},
 {'type': 'rhino', 'name': 'Moe', 'age': 5}]
print(sorted(animals, key=lambda animal: animal['age']))

numbers = [9, 20, 56, 12, 34, 4, 6, 18, 91, 28, 0, -2, 11, -8]
print(sorted(numbers))