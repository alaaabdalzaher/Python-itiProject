x =input ("Enter your string to find i character: ")

for i in range(len(x)):
    if x[i] == "i":
            print ("The i is at: ", i)
else:
    print("there is no i character in your input text")