# WRITE YOUR SOLUTION HERE:

class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        maxCount = 0
        mostFrequent = 0
        for i in range(len(my_list)):
            if my_list.count(my_list[i]) > maxCount:
                maxCount = my_list.count(my_list[i])
                mostFrequent = my_list[i]
        return mostFrequent
    
    @classmethod
    def doubles(cls, my_list: list):
        doublesList = []
        uniqueList = []
        for i in range(len(my_list)):
            if my_list[i] not in uniqueList:
                uniqueList.append(my_list[i])
                if my_list.count(my_list[i]) >= 2:
                    doublesList.append(my_list[i])
        return len(doublesList)
    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
