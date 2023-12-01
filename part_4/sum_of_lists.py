# Write your solution here

def list_sum(a, b):
    newList = []
    counter = 0
    while counter <= len(a)-1:
        newList.append(a[counter] + b[counter])
        counter += 1
    return newList

if __name__ == "__main__":
    a = [1,2,3]
    b = [7,8,9]
    print(list_sum(a, b))