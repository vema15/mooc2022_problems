
storyConcat = ""
lastValue = ""

while True:
    wordInput = input("Please type in a word:")
    if wordInput == "end":
        break
    elif lastValue == wordInput:
        break
    else:
        storyConcat += wordInput + " "
    lastValue = wordInput
print(storyConcat)