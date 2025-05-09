vowles = "aeiou"
x = 0

input_string = input("Enter a string: ")

for char in input_string. lower ():
    if char in vowles:
        x += 1

print("Number of vowels in the string:", x)