# Write your solution here

userString = input("Please type in a string:")

if userString[len(userString)-2] == userString[1]:
    print(f"The second and the second to last characters are {userString[1]}")
else:
    print("The second and the second to last characters are different")