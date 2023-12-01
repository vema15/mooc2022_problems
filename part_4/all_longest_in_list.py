# Write your solution here

def all_the_longest(list):
    itemLens = []
    counter = 0
    while counter <= len(list)-1:
        itemLens.append([counter, len(list[counter])])
        counter += 1
    sortedList = sorted(itemLens, key=lambda x: x[1])
    longestBenchmark = sortedList[len(sortedList)-1][1]
    longestList = []
    counter = 0
    while counter <= len(sortedList)-1:
        if sortedList[counter][1] == longestBenchmark:
            longestList.append(list[sortedList[counter][0]])
            counter += 1
        else:
            counter += 1
    return longestList
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)