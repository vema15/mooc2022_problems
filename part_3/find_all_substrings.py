
userWord = input("Please type in a word:")
userChar = input("Please type in a character:")
count = 0

while count < len(userWord)-2:
    if userWord[count] == userChar:
        print(userWord[count:count+3])
        count +=1
    else:
        count += 1