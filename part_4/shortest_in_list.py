# Write your solution here

def shortest(list):
    itemLens = []
    counter = 0
    while counter <= len(list)-1:
        itemLens.append([len(list[counter]), counter])
        counter += 1
    sortedList = sorted(itemLens, key=lambda x: x[0])
    print(sortedList)
    return list[sortedList[0][1]]
    

if __name__ == "__main__":
    my_list = ['ab', 'abc']
    result = shortest(my_list)
    print(result)
