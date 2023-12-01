# Write your solution here

numItemAdd = int(input("Please enter number of items to be added:"))
userList = []

count = 1
while count <= numItemAdd:
    itemX = int(input(f"Item {count}:"))
    userList.append(itemX)
    count += 1

print(userList)