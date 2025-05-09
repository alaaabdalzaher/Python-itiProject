h = int(input ("Enter the height of the Mario pyramid: "))
p=[]

for i in range (1, h + 1):
    spaces = h - i
    hashes = i
    row = [" "] * spaces + ["*"] * hashes
    p.append("'".join(row))


for row in p:
    print(row)