# Write your solution here

userNum = int(input("Please type in a number:"))
upCount = 1
downCount = userNum

while upCount < downCount:
    print(upCount)
    upCount += 1
    print(downCount)
    downCount -= 1

if userNum % 2 != 0:
    print(upCount)