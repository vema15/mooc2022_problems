# Write your solution here
my_list = []
uniqueCounter = 0

while True: 
    userWord = input("Word:")
    if userWord not in my_list:
        my_list.append(userWord)
        uniqueCounter += 1 
    else:
        print(f"You typed in {uniqueCounter} different words")
        break