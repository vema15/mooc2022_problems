# Write your solution here

userNum = int(input("Please type in a number:"))

if userNum >= 1000:
    print("Thank you!")
if userNum < 1000 and userNum >= 100:
    print("This number is smaller than 1000")
    print("Thank you!")
if userNum < 100 and userNum >= 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
if userNum < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")