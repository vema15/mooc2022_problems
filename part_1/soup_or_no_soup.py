# Write your solution here

userName = input("Please tell me your name:")

if userName == "Jerry":
    print("Next please!")

if userName != "Jerry":
    soupPortion = int(input("How many portions of soup?"))
    print(f"The total cost is {float(soupPortion * 5.90)}")
    print("Next please!")