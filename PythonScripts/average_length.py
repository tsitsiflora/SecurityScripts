# given a sentence, the function returns the average length of the words

import string

def average_length(sentence):
    for p in string.punctuation:
        sentence = sentence.replace(p, '')

    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words), 2)


print(average_length("My name is tsitsi."))
print(average_length("I am not so sure, is this python code or magic."))












