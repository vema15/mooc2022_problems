# Write your solution here

normList = []


while True: 
    userItem = int(input("New item:"))
    if userItem == 0:
        print("Bye!")
        break
    else:
        normList.append(userItem)
        mutatedList = sorted(normList)
        print(f"The list now: {normList}")
        print(f"The list in order: {mutatedList}")