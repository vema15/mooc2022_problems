# Write your solution here

userString = input("Please type in a string:")
counter = len(userString)-1

while counter >= 0:
    print(userString[counter:])
    counter -= 1