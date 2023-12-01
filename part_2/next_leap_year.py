# Write your solution here

userYearInput = int(input("Year:"))
yearCounter = userYearInput
while True:
    if yearCounter == userYearInput:
        yearCounter += 1
    elif yearCounter % 4 == 0 and yearCounter % 100 != 0:
        break
    elif yearCounter % 4 == 0 and yearCounter % 100 == 0 and yearCounter % 400 == 0:
        break
    elif yearCounter % 4 == 0 and yearCounter % 100 == 0 and yearCounter % 400 != 0:
        yearCounter += 1
    else: 
        yearCounter += 1
print(f"The next leap year after {userYearInput} is {yearCounter}")