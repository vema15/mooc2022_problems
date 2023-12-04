# Write your solution here

def phoneBook():
    pBook = {}
    while True:
        userInput = int(input("command(1 search, 2 add, 3 quit)"))
        if userInput == 1:
            searchInp = input("name:")
            if searchInp in pBook:
                print(pBook[searchInp])
            else:
                print("no number")
        elif userInput == 2:
            nameInp = input("name:")
            numInp = input("number:")
            pBook[nameInp] = numInp
            print("ok!")
            continue
        else:
            print("quitting...")
            break


phoneBook()