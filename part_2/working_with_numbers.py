# Write your solution here
sum = 0
count = 0
negCount = 0
posCount = 0


print("Please type in integer numbers. Type in 0 to finish.")
while True:
    userNum = int(input("Number:"))
    if userNum == 0:
        break
    elif userNum != 0:
        sum += userNum
        count += 1
    if userNum < 0:
        negCount += 1
    elif userNum > 0:
        posCount += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/count}")
print(f"Positive numbers {posCount}")
print(f"Negative numbers {negCount}")
