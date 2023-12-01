# Write your solution here

userString = input("Please type in a string:")
counter = 0

while counter <= len(userString):
    print(userString[:counter])
    counter += 1