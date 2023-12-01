# Write your solution here

upperLim = int(input("Upper limit:"))
base = int(input("Base:"))
count = 1
print(count)
while count <= upperLim:
    if count % base == 0:
        print(count)
        count = count * base
    else:
        count += 1