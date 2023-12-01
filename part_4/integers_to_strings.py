# Write your solution here

def formatted(floatList):
    stringList = []
    counter = 0
    while counter <= len(floatList)-1:
        currentIndexContent = floatList[counter]
        stringList.append(str(f'{currentIndexContent:.2f}'))
        counter += 1    
    return stringList    



if __name__ == "__main__":
    my_list = [1.222, 0.33333, 0.6666, 0.9999]
    new_list = formatted(my_list)
    print(new_list)