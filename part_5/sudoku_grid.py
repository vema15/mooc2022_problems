# Write your solution here

def sudoku_grid_correct(sudoku: list):
    rowCount = 0
    while rowCount <= len(sudoku)-1:
        uniqueList = []
        colCount = 0
        while colCount <= len(sudoku[rowCount])-1:
            if sudoku[rowCount][colCount] in uniqueList and sudoku[rowCount][colCount] > 0:
                return False
            uniqueList.append(sudoku[rowCount][colCount])
            colCount += 1
        rowCount += 1
    colCount = 0
    while colCount <= len(sudoku[0])-1:
        columnList = []
        rowCount = 0
        while rowCount <= len(sudoku[0])-1:
            if sudoku[rowCount][colCount] in columnList and sudoku[rowCount][colCount] > 0:
                return False
            columnList.append(sudoku[rowCount][colCount])
            rowCount += 1
        colCount += 1
    def blockCheck(sudoku, row_no, column_no):
        totalBlock = []
        rowIndex = row_no
        while rowIndex < row_no+3:
            columnIndex = column_no
            while columnIndex < column_no+3:
                if sudoku[rowIndex][columnIndex] in totalBlock and sudoku[rowIndex][columnIndex] > 0:
                    return False
                totalBlock.append(sudoku[rowIndex][columnIndex])
                columnIndex += 1
            rowIndex += 1
        
    rowIterator = 0
    while rowIterator <= 6:
        colIterator = 0
        while colIterator <= 6:
            blockCheck(sudoku, rowIterator, colIterator)
            if blockCheck(sudoku, rowIterator, colIterator) == False:
                return False
            colIterator +=3 
        rowIterator += 3  
    return True

if __name__ == "__main__":
    sudoku1 = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku2 = [
      [2, 6, 7, 8, 3, 9, 5, 0, 4],
      [9, 0, 3, 5, 1, 0, 6, 0, 0],
      [0, 5, 1, 6, 0, 0, 8, 3, 9],
      [5, 1, 9, 0, 4, 6, 3, 2, 8],
      [8, 0, 2, 1, 0, 5, 7, 0, 6],
      [6, 7, 4, 3, 2, 0, 0, 0, 5],
      [0, 0, 0, 4, 5, 7, 2, 6, 3],
      [3, 2, 0, 0, 8, 0, 0, 5, 7],
      [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    sudoku3 = [
      [2, 6, 7, 8, 3, 9, 5, 0, 4],
      [9, 0, 3, 5, 1, 0, 6, 0, 0],
      [0, 5, 6, 0, 0, 0, 8, 3, 9],
      [5, 1, 9, 0, 4, 6, 3, 2, 8],
      [8, 0, 2, 1, 0, 5, 7, 0, 6],
      [6, 7, 4, 3, 2, 0, 0, 0, 5],
      [0, 0, 0, 4, 5, 7, 2, 6, 3],
      [3, 2, 0, 0, 8, 0, 0, 5, 7],
      [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku1))
    print(sudoku_grid_correct(sudoku2))
    print(sudoku_grid_correct(sudoku3))
