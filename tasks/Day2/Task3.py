name = input("Enter your name: ")

while name.strip() == '' or name.isdigit():
    print("Invalid name. Please enter a valid name.")
    name = input("Enter your name: ")

email = input("Enter your email: ")

print ("Email: ", email)

if "@" in email and "." in email:
    at_index = email. index("@")
    dot_index = email.rindex(".")
    if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
        print ("Email is valid.")
    else:
        print ("Email is invalid.")
else:
    print ("Email is invalid.")
