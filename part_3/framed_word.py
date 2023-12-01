# Write your solution here
userWord = input("Word:")

stars = 30 * "*"
whiteSpaceOdd1 = (int((28 - len(userWord))/2)+1) * " "
whiteSpaceOdd2 = (int((28 - len(userWord))/2)) * " "
whiteSpaceEven = (int((28 - len(userWord))/2)) * " "


print(stars)
if len(userWord) % 2 == 0:
    print("*" + whiteSpaceEven + userWord + whiteSpaceEven + "*")
else: 
    print("*" + whiteSpaceOdd2 + userWord + whiteSpaceOdd1 + "*")
print(stars)