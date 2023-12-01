# Write your solution here

# Write your solution here
def squared(userString, num):
    stringList = list(userString)
    stringLength = len(stringList)
    listPosition = 0
    rowCount = 0
    while rowCount <= num-1:
        rowList = []
        unitCount = 0
        while unitCount <= num-1:
            if listPosition > stringLength-1:
                listPosition = 0
            rowList.append(stringList[listPosition])
            listPosition += 1
            unitCount += 1
        print(*rowList, sep="")
        rowCount+=1


if __name__ == "__main__":
    squared("ab", 3)