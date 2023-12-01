# Write your solution here
def everything_reversed(list):
    reverseList = list[::-1]
    fullReverseList = []
    count = 0 
    while count <= len(reverseList)-1:
        fullReverseList.append(reverseList[count][::-1])
        count += 1
    return fullReverseList




if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
