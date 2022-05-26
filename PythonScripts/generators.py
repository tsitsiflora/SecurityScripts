#this script gives an introduction to generators

def odds(start, stop):
    '''Take a start and stop integer and 
        return only the odd numbers in that
        range using generators.'''
    for odd in range(start, stop + 1, 2):
        yield odd

def main():
    odd_values = [odd for odd in odds(3, 17)]
    print(odd_values)
    odd_v = tuple(odds(5, 29))
    print(odd_v)

if __name__ == "__main__":
    main()