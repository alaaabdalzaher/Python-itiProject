# tasks_module.py

def task1():
    vowels = "aeiou"
    count = 0
    input_string = input("Task1 - Enter a string: ").lower()
    for char in input_string:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)

def task2():
    text = input("Task2 - Enter a string to find 'i': ")
    found = False
    for index, char in enumerate(text):
        if char == 'i':
            print("The 'i' is at:", index)
            found = True
    if not found:
        print("No 'i' character found.")

def task3():
    num = int(input("Task3 - Enter a number: "))
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(f"{i} * {j} = {i * j}", end="\t")
        print()

def task4():
    height = int(input("Task4 - Enter pyramid height: "))
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * i)

def task5():
    numbers = []
    for i in range(5):
        x = int(input(f"Task5 - Enter number {i+1}: "))
        numbers.append(x)
    print("List:", numbers)
    print("Ascending:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))

def task6():
    x = int(input("Task6 - Enter a number: "))
    result = []
    for i in range(1, x + 1):
        row = [i * j for j in range(1, i + 1)]
        result.append(row)
    print("Multiplication Table:")
    for row in result:
        print(row)

def task7():
    name = input("Task7 - Enter your name: ").strip()
    while not name.isalpha():
        name = input("Invalid. Enter a valid name: ").strip()
    email = input("Enter your email: ").strip()
    if "@" in email and "." in email:
        at = email.index("@")
        dot = email.rindex(".")
        if at > 0 and dot > at + 1 and dot < len(email) - 1:
            print("Valid email.")
        else:
            print("Invalid email.")
    else:
        print("Invalid email.")

def task8():
    height = int(input("Task8 - Enter Mario pyramid height: "))
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * i)

def task9():
    def is_valid(email):
        if "@" in email and "." in email:
            try:
                user, domain = email.split("@")
                parts = domain.split(".")
                return user and len(parts) >= 2 and all(parts)
            except:
                return False
        return False

    attempts = 0
    email = input("Task9 - Enter your email: ")
    while not is_valid(email):
        attempts += 1
        if attempts == 3:
            print("Too many invalid attempts.")
            return
        email = input("Invalid email. Try again: ")
    print("Email is valid.")

def task10():
    users = [{"name": "omar", "pass": "123"}, {"name": "ahmed", "pass": "456"}]
    uname = input("Task10 - Enter username: ")
    for user in users:
        if uname == user["name"]:
            pwd = input("Enter password: ")
            if pwd == user["pass"]:
                print("Authorized!")
            else:
                print("Incorrect password!")
            break
    else:
        print("Incorrect username!")
