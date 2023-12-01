# Write your solution here

userSentence = input("Please type in a sentence:")
counter = 0

while counter <= len(userSentence)-1: 
    if counter == 0: 
        print(userSentence[counter])
    elif userSentence[counter] == " ":
        print(userSentence[counter+1])
    
    counter += 1