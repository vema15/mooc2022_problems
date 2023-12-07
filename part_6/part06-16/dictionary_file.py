# Write your solution here

while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    userInput = int(input("Function: "))
    if userInput == 1:
        finWord = input("The word in Finnish: ")
        engWord = input("The word in English: ")
        with open('dictionary.txt', 'a') as dictionary:
            dictionary.write(f'{finWord} - {engWord}')
        print('Dictionary entry added')
    elif userInput == 2:
        searchTerm = input("Search term: ")
        with open('dictionary.txt') as dictionary:
            for item in dictionary:
                if searchTerm in item:
                    print(item)
    else:
        print("Bye!") 
        break
