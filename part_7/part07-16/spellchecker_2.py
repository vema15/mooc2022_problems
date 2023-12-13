from difflib import get_close_matches

def dictList():
    dictList = []
    with open('wordlist.txt') as wordList:
        for line in wordList:
            line = line.replace("\n", "")
            dictList.append(line)
    return dictList
wordList = dictList()
userInput = input("Write text: ")
userInputSplit = userInput.split(" ")
correctedList = []
incorrectWords = []
for item in userInputSplit:
    if item.lower() not in wordList:
        correctedList.append(f"*{item}*")
        incorrectWords.append(item)
    else:
        correctedList.append(item)

matchesList = []
for item in incorrectWords:
        closeMatches = get_close_matches(item, wordList)
        matchesList.append(f'{item}: {", ".join(closeMatches)}')
if len(matchesList) > 0:
    print(" ".join(correctedList))
    print('suggestions:')
    for i in matchesList:
        print(i)
else: 
    print(" ".join(correctedList))