# Write your solution here

def count_matching_elements(my_matrix: list, element: int):
    matchCount = 0
    counter = 0
    while counter <= len(my_matrix)-1:
        counter2 = 0
        while counter2 <= len(my_matrix[counter])-1:
            if my_matrix[counter][counter2] == element:
                matchCount += 1
            counter2+=1
        counter+=1
    return matchCount

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))