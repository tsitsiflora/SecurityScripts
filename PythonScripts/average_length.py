# given a sentence, the function returns the average length of the words

import string

def average_length(sentence):
    words = sentence.split()
    return round(sum(len(word) for word in words if word not in string.punctuation)/len(words))


print(average_length("My name is tsitsi."))
print(average_length("I am not so sure, is this python code or magic."))












