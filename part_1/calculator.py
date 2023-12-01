# Write your solution here

num1 = float(input("Please enter first number:"))
num2 = float(input("Please enter second number:"))
operation = (input("Please enter operation:")).lower()

if operation == "add":
    print(f"{int(num1)} + {int(num2)} = {int(num1 + num2)}")
elif operation == "subtract":
    print(f"{int(num1)} - {int(num2)} = {int(num1 - num2)}")
elif operation == "multiply":
    print(f"{int(num1)} * {int(num2)} = {int(num1 * num2)}")