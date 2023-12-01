# Write your solution here

list = [1,2,3,4,5]


while True:
    userIndex = int(input("Please enter an index:"))
    if userIndex == -1:
        break
    userNewVal = int(input("Please enter a new integer value:"))
    list[userIndex] = userNewVal
    print(list)