def print_sudoku(sudoku: list):
    rowCount = 0
    while rowCount <= len(sudoku)-1:
        colCount = 0
        while colCount <= len(sudoku[rowCount])-1:
            if sudoku[rowCount][colCount] == 0:
                if colCount == 2 or colCount == 5:
                    print("_", end="  ")
                elif colCount == 8 and (rowCount == 2 or rowCount == 5):
                    print("_", end="\n"*2)
                elif colCount == 8: 
                    print("_", end="\n")
                else:
                    print("_", end=" ")
            else:
                if colCount == 2 or colCount == 5:
                    print(sudoku[rowCount][colCount], end="  ")
                elif colCount == 8 and (rowCount == 2 or rowCount == 5):
                    print(sudoku[rowCount][colCount], end="\n"*2)
                elif colCount == 8: 
                    print(sudoku[rowCount][colCount], end="\n")
                else:
                    print(sudoku[rowCount][colCount], end=" ")
            colCount+=1
        rowCount += 1
    
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
