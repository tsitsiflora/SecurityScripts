#this script gives an introduction to sets

first_set = set(['foo', 'bar']) #converting a list into a set
second_set = set({"hello": 5}) #converting a dict into a list. It only takes the keys
third_set = set("Hello") #converting a string into a list. it splits the string into characters and removes duplicates
fourth_set = {'foo', 'bar'} #defining sets using curly braces
fifth_set = set() #defining an empty set
sixth_set = {'hello', 3, True, None, (1, 4)} #sets can contain any hashable values mixed together

x1 = {'a', 'b', 'c', 'd', 'e'}
x2 = {'c', 'e', 'f', 'g', 'h'}

print(len(x1))
print(x1 | x2)
print(x1 & x2)
print(x1 - x2)
print(x1 ^ x2)
