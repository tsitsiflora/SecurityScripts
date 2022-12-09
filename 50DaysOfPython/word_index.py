# Write a function that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero

def word_index(l: list):
    for word in l:
        for j in range(len(l)-1):
            if len(l[j]) == len(l[j+1]):
                return 0
            elif len(word) == len(max(l)):
                return l.index(word)

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]
print(word_index(words1))
print(word_index(words2))