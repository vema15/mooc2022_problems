# Write your solution here

# Write your solution here

userWord = input("Please type in a string:")
userSubStr = input("Please type in a substring:")
initialSubStr = userWord.find(userSubStr)
subStrLen = len(userSubStr)
subStrCount = 0
count = 0

while count < len(userWord): 
    if userWord[count:count+subStrLen] == userSubStr:
        subStrCount += 1
        if subStrCount == 2:
            print(f"The second occurrence of the substring is at index {count}.")
        count += subStrLen
    else:
        count += 1

if subStrCount == 1 or subStrCount == 0:
    print("The substring does not occur twice in the string.")
