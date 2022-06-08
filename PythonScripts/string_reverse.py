# this script reverses a given string

#using reversed in Python
def reverse_string(sentence):
    words = sentence.split()
    words = list(reversed(words))
    return (" ".join(words))

# using just split and join
def string_reverse(sentence):
    s = sentence.split()[::-1]
    l = []
    for i in s:
        l.append(i)
    return (" ".join(l))



sentence = "the sky is blue"
print(reverse_string(sentence))
print(string_reverse(sentence))