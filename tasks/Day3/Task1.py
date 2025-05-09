count = 0
def mailvalidation(email):
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            d1, d2 = domain.split('.')
            if d1 and d2:
                return True
        
            
usermail = input("Enter your email address: ")
while not mailvalidation(usermail):
    count += 1
    usermail = input("Enter a valid email address:")
    if count == 3:
        print("You entered 4 incorrect email addresses!")
        break
    continue
else:
        print("your email address is correct")