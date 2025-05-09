x =int(input ("Enter a number: "))
result =[]

for i in range(1, x + 1):
    row=[]
    for j in range(1, i + 1):   
        row. append (i * j) 
    result.append(row)
print("Multiplication Table:")
print(result)