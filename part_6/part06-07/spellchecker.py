def dictList():
    dictList = []
    with open('wordlist.txt') as wordList:
        for line in wordList:
            line = line.replace("\n", "")
            dictList.append(line)
    return dictList

wordList = dictList()
userInput = input("Write text:")
userInputSplit = userInput.split(" ")
correctedList = []
for item in userInputSplit:
    if item.lower() not in wordList:
        correctedList.append(f"*{item}*")
    else:
        correctedList.append(item)
for item in correctedList:
    print(item, end=" ")

