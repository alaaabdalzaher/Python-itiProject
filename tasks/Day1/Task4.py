x = int(input ("Enter the height of the pyramid: "))

for i in range(1, x + 1):
    spaces = x - i
    blocks = i  
    print(" " * spaces + "*" * blocks)