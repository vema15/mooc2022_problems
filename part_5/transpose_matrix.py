def transpose(matrix: list):
    refList = []
    rowCount = 0
    while rowCount <= len(matrix)-1:
        refList.append([])
        colCount = 0
        while colCount <= len(matrix[rowCount])-1:
            refList[rowCount].append(matrix[colCount][rowCount])
            colCount += 1
        rowCount += 1
    counter = len(matrix)-1
    while counter >= 0:
        matrix.remove(matrix[counter])
        counter -= 1
    for i in refList:
        matrix.append(i)



if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    transpose(matrix)
    print(matrix)
