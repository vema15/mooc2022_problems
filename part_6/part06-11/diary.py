# Write your solution here
   
while True:
    print("1- add an entry, 2 - read entries, 0 - quit")
    inputChoice = int(input("Function: "))
    if inputChoice == 1:
        with open('diary.txt', "a") as diaryAdd:
            diaryEntry = input("Diary entry: ")
            diaryAdd.write(f'{diaryEntry}\n')
            print("Diary saved")
    elif inputChoice == 2:
        print("Entries:")
        with open('diary.txt') as totalDiary:
            for line in totalDiary:
                line = line.replace("\n", "")
                print(line)
    elif inputChoice == 0:
        print("Bye now!")
        break