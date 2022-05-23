#this script takes a list of numbers and returns only the even numbers that are greater than 0

numbers = [ int(item) for item in input("Enter the list items : ").split() ]

def filter_numbers(numbers):
    '''Take a list of numbers and return only the
        numbers that are greater than 0 and divisible by 2.'''
    
    return [ n for n in numbers if n>0 and n%2==0 ]

result = filter_numbers(numbers)
print(result)