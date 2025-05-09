L= []

for i in range(5):
    x = int ( input(f"Enter a number: ") )
    L.append (x)

print("Your list is: ", L)
print("Asecending sort of list is: ", sorted(L))
print("Desecending sort of List is: ", sorted (L,reverse=True))