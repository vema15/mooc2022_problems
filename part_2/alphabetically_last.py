# Write your solution here

wordOne = input("Please type in the 1st word:")
wordTwo = input("Please type in the 2nd word:")

if wordOne < wordTwo:
    print(f"{wordTwo} comes alphabetically last")
elif wordOne > wordTwo:
    print(f"{wordOne} comes alphabetically last")
else:
    print("You gave the same word twice.")
