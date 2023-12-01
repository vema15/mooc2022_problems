# Write your solution here

def length_of_longest(list):
    count = 0
    while count <= len(list)-1:
        list[count] = len(list[count])
        count += 1
    sortedList = sorted(list)
    return sortedList[len(sortedList)-1]
    

if __name__ == "__main__":
    list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']
    print(length_of_longest(list))