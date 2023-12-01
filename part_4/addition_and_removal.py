# Write your solution here

list = []
numCount = 0

print(f"The list is now {list}")
while True:
    userChoice = input("a(d)d, (r)emove or e(x)it:")
    if userChoice == "d":
        numCount += 1
        list.append(numCount)
        print(f"The list is now {list}")
    elif userChoice == "r":
        list.pop(len(list)-1)
        numCount -= 1
        print(f"The list is now {list}")
    elif userChoice == "x":
        print("Bye!")
        break