mylist = [{"name":"omar", "pass":"123"},{"name":"ahmed", "pass":"456"}]
username = input("Enter your username: ")

for i in range(len(mylist)):
    if username == mylist[i]["name"]:
        password = input("Enter your password: ")
        if password == mylist[i]["pass"]:
            print("You are authorized!")
            break
        else: 
            print("You entered an uncorrect password!")
            break
else:
    print("You entered an uncorrect username!")