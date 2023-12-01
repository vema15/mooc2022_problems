# Write your solution here

def no_shouting(userList):
    counter = 0
    scrubbedList = []
    while counter <= len(userList)-1:
        if userList[counter].isupper():
            counter += 1
            continue
        else:
            scrubbedList.append(userList[counter])
            counter += 1
    return scrubbedList

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)