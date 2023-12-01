# Write your solution here

def longest_series_of_neighbours(userList):
    hasNeighborList = []
    counter = 0
    while counter <= len(userList)-2:
        if userList[counter+1] == userList[counter]+1 or userList[counter+1] == userList[counter]-1:
            hasNeighborList.append([True, counter])
            counter += 1
        else:
            hasNeighborList.append([False, counter])
            counter += 1
    counter = 0
    trueCount = 0
    neighborLengthList = []
    while counter <= len(hasNeighborList)-1:
        if hasNeighborList[counter][0] == True:
            trueCount += 1
            counter += 1
        elif hasNeighborList[counter][0] == False:
            neighborLengthList.append(trueCount+1)
            trueCount = 0
            counter += 1
    
    neighborLengthList.append(trueCount+1)
    sortedNLL = sorted(neighborLengthList)
    return sortedNLL[len(sortedNLL)-1]


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))