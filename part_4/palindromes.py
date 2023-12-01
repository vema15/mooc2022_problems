# Write your solution here

def palindromes(userInput):
    while True:
        counter = 0
        reverseCounter = len(userInput)-1

        while counter <= len(userInput)-1 and reverseCounter >= 0:
            if userInput[counter] == userInput[reverseCounter]:
                counter += 1
                reverseCounter -= 1
                continue
            else:
                return False
        
        return True

while True:
        palindromeInput = input("Please type in a palindrome:")

        if palindromes(palindromeInput) == True:
            print(f"{palindromeInput} is a palindrome!")
            break
        else:
            print(f"that wasn't a palindrome")


if __name__ == "__main__":
    palindromes(palindromeInput)




# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
