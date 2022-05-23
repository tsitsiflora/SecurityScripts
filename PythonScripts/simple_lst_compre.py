#a simple script to demonstrate list comprehensions

#normal for loop
squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

#in a list comprehension
squared = [x * x for x in range(10)]
print(squared)

#list comprehension with filtering
even_squares = [ x * x for x in range(10) if x % 2 ==0 ]
print(even_squares)

#even squares with a for loop
squares_even = []
for x in range(10):
    if x % 2 == 0:
        squares_even.append(x * x)

print(squares_even)