# Write your solution here

def most_common_character(userString):
    counter = 0
    occurenceList = []
    while counter <= len(userString)-1:
        if [userString.count(userString[counter]), userString[counter]] not in occurenceList:
            occurenceList.append([userString.count(userString[counter]), userString[counter]])
            counter+=1
        else:
            counter+=1
            continue
    sortedOccurList = sorted(occurenceList, key=lambda x:x[0])
    highestOccurence = sortedOccurList[len(sortedOccurList)-1][0]
    counter = 0
    while counter <= len(sortedOccurList)-1:
        if sortedOccurList[counter][0] == highestOccurence:
            return sortedOccurList[counter][1]
        else:
            counter += 1

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))