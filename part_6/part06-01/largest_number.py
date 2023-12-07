# write your solution here
def largest():
    numList = []
    with open('numbers.txt') as numTxt:
        for line in numTxt:
            numList.append(int(line))
    sortedNumList = sorted(numList)
    return sortedNumList[len(sortedNumList)-1]
if __name__ == "__main__":
    print(largest())
