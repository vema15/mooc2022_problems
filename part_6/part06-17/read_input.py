# Write your solution here

def read_input(question: str, lowerBound, upperBound):
    while True:
        try:
            userInput = int(input(question))
            if userInput > lowerBound and userInput < upperBound:
                return userInput
            else:
                print(f"You must type in an integer between {lowerBound} and {upperBound}")
                continue
        except ValueError:
            print(f"You must type in an integer between {lowerBound} and {upperBound}")



if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print(f"You typed in: {number}")