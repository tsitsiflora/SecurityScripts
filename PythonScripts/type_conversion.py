#this script takes input, tries to convert it to integer, raises value error and tries to divide

enumerator = input("Enter the enumerator: ")
denominator = input("Enter the denominator: ")

def type_conversion(enumerator, denominator):
    '''Take input from the user and try to convert it to integer.
        If it raises a ValueError, reraise it. Then try to divide the
        numbers, catch the Can't divide by 0 error.'''
    try:
        answer = int(enumerator)/int(denominator)
        return answer
    
    except ValueError:
        raise 
    except ZeroDivisionError:
        return 0
    
output = type_conversion(enumerator, denominator)
print(output)