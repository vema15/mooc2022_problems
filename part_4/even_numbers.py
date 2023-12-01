# Write your solution here

def even_numbers(list):
    evenList = []
    count = 0
    while count <= len(list)-1:
        if list[count] % 2 == 0:
            evenList.append(list[count])
            count += 1
        else:
            count += 1
            continue
    return evenList

if __name__ == "__main__":
    list = [1,2,3,4,5]
    print(f"original {list}")
    print(f"new {even_numbers(list)}")
