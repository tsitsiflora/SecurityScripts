# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary.

names = ["Joseph", "Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

def start_with(names):
    d = {}
    for name in names:
        if name.startswith("S"):
            d.update({name:names.count(name)})
    
    return d

print(start_with(names))