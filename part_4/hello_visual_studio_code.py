# Write your solution here

while True:
    userInput = input("Please enter your editor:")
    if userInput.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif userInput.lower() == "word" or userInput.lower == "notepad":
        print("awful")
    else:
        print("not good")