#this script goes in an infinite loop of asking for a color until the user presses quit
valid_colors = ['yellow','blue','green','red']

def check_color():
    '''Ask for a color from the user, lowercase it. Check if the color entered was quit.
    If yes, print quit and break. If not check the color against the valid_colors and print
    if they get it right'''
    while True:
        color = input("Enter color: ").lower()
        if color == "quit":
            print("Quitting")
            break

        if color not in valid_colors:
            print("Not a valid color!")
            continue

        print(color)

check_color()