# Write your solution here

userNum = int(input("Please type in a number:"))

count1 = 1

while count1 <= userNum:
    count2 = 1
    while count2 <= userNum:
        print(f"{count1} x {count2} = {count1 * count2}")
        count2 += 1
    count1 += 1