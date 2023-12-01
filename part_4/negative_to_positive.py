# Write your solution here

userInt = int(input("Please type in a positive number"))

for i in range(-userInt, userInt+1):
    if i == 0:
        continue
    else:
        print(i)