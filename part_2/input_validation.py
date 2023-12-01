from math import sqrt
# Write your solution here

while True:
    userInput = int(input("Please type in a number:"))
    if userInput > 0:
        print(f"{sqrt(userInput)}")
    elif userInput < 0:
        print("Invalid number")
    elif userInput == 0:
        print("Exiting...")
        break

