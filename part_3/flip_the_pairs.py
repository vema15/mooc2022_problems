
userNum = int(input("Please type in a number:"))
counter = 1

while counter <= userNum:
    if counter+1 > userNum:
        print(counter)
        break
    print(counter+1)
    print(counter)
    counter+= 2

