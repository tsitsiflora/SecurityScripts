# counter: It is used to keep the count of the elements in an iterable in the form
#  of an unordered dictionary where the key represents the element in the iterable 
# and value represents the count of that element in the iterable.

from collections import Counter, defaultdict, namedtuple, deque

def counter_func(text):
    return (Counter(text).most_common(3))

# a defaultdict is used to provide some default values for the key that does 
# not exist and never raises a KeyError

def default_dictionary():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(sorted(d.items()))

# a namedtuple returns a tuple object with names for each position 
# which the ordinary tuples lack

def named_tuple():
    Student = namedtuple('Student', ['fname', 'lname', 'age', 'classes'])
    s = Student('mary', 'joe', 14, 'math')
    print(f"The student's name is {s.fname} {s.lname}. She is {s.age} and is taking {s.classes}.")

# a deque (double ended queue) is the optimized list for quicker append 
# and pop operations from both sides of the container. It provides O(1) time 
# complexity for append and pop operations as compared to list with O(n) time
# complexity

def deque_function():
    de = deque([7, 3, 6, 9, 2, 0])
    de.append(6)
    print(de)
    de.appendleft(14)
    print(de)
    print(de.pop())
    print(de.popleft())



def main():
    count = counter_func("abracadabra")
    print(count)
    default_dictionary()
    named_tuple()
    deque_function()

if __name__ == '__main__':
    main()