# Write your solution here

numInput = float(input("Please type in a number:"))

if numInput >= 0: 
    print(f"The absolute value of this number is {int(numInput)}")

if numInput < 0:
    print(f"The absolute value of this number is {int(numInput * -1)}")
