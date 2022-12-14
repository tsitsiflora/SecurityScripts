# Write a function that generates a username
# from the user’s email. The code should ask the user to input an
# email and the code should return everything before the @ sign
# as their user name.

def username_generator():
    email = input("Enter your email: ")
    return email.split("@")[0]
    

print(username_generator())