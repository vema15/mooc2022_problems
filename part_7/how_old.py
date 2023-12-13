from datetime import *
# Write your solution here

birthDay = int(input("Day: "))
birthMonth = int(input("Month: "))
birthYear = int(input("Year: "))

userBirthDate = datetime(birthYear, birthMonth, birthDay)
distFrom = datetime(1999, 12, 31) - userBirthDate

if distFrom.days >= 0:
    print(f'You were {distFrom.days} days old on the eve of the new millennium.')
else:
    print("You weren't born yet on the eve of the new millennium.")



