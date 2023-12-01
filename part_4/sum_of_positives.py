# Write your solution here

def sum_of_positives(list):
    sum = 0
    counter = 0
    while counter <= len(list)-1:
        if list[counter] < 0:
            counter += 1
            continue
        else:
            sum += list[counter]
            counter += 1

    return sum

if __name__ == "__main__":
    result = sum_of_positives([1,2])
    print(f"The result is {result}")
