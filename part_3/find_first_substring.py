# Write your solution here

userWord = input("Please type in a word:")
userChar = input("Please type in a character:")
charIndex = userWord.find(userChar)


if userChar in userWord and charIndex < len(userWord)-2:
    print(userWord[charIndex:charIndex+3])
