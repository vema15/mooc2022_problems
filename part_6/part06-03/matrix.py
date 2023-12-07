# write your solution here

def matrix_sum():
    sumOfMatrix = 0
    with open('matrix.txt') as matrixTxt:
        for line in matrixTxt:
            line = line.replace("\n", "")
            sepdLine = line.split(",")
            for item in sepdLine:
                sumOfMatrix += int(item)
    return sumOfMatrix
def matrix_max():
    maxIndex = 0
    with open('matrix.txt') as matrixTxt:
        for line in matrixTxt:
            line = line.replace("\n", "")
            splitLine = line.split(",")
            for item in splitLine:
                if int(item) > maxIndex:
                    maxIndex = int(item)
    return maxIndex
def row_sums():
    rowSumList = []
    with open('matrix.txt') as matrixTxt:
        for line in matrixTxt:
            lineSum = 0
            line = line.replace("\n", "")
            splitLine = line.split(",")
            for item in splitLine:
                lineSum += int(item)
            rowSumList.append(lineSum)
    return rowSumList
if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())