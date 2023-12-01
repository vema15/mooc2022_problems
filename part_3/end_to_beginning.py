# Write your solution here

userString = input("Please type in a string:")
currIndex = (len(userString) - 1)

while currIndex >= 0:
    print(userString[currIndex])
    currIndex -= 1
