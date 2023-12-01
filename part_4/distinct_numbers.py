# Write your solution here

def distinct_numbers(list):
    distinctList = []
    counter = 0
    while counter <= len(list)-1:
        if list[counter] in distinctList:
            counter += 1
        else:
            distinctList.append(list[counter])
            counter+=1
    return sorted(distinctList)



if __name__ == "__main__":
    list = [3,2,2,1,3,3,1]
    print(distinct_numbers(list))