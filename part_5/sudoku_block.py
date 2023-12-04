# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    totalBlock = []
    rowIndex = row_no
    while rowIndex < row_no+3:
        columnIndex = column_no
        while columnIndex < column_no+3:
            if sudoku[rowIndex][columnIndex] == 0:
                columnIndex += 1
            elif sudoku[rowIndex][columnIndex] not in totalBlock:
                totalBlock.append(sudoku[rowIndex][columnIndex])
                columnIndex += 1
            else:
                return False   
        rowIndex += 1
    return True

if __name__ == "__main__":
    sudoku = [
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

    print(block_correct(sudoku, 1, 2))