# Write your solution here

def print_sudoku(chusoku: list):
    rowCount = 0
    while rowCount <= len(chusoku)-1:
        colCount = 0
        while colCount <= len(chusoku[rowCount])-1:
            if chusoku[rowCount][colCount] == 0:
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
                    print(chusoku[rowCount][colCount], end="  ")
                elif colCount == 8 and (rowCount == 2 or rowCount == 5):
                    print(chusoku[rowCount][colCount], end="\n"*2)
                elif colCount == 8: 
                    print(chusoku[rowCount][colCount], end="\n")
                else:
                    print(chusoku[rowCount][colCount], end=" ")
            colCount+=1
        rowCount += 1
    
def copy_and_add(chubloku: list, row_no: int, column_no: int, number: int):
    modifiedSudoku = []
    rowCounter = 0
    while rowCounter <= len(chubloku)-1:
        modifiedSudoku.append([])
        colCounter = 0
        while colCounter <= len(chubloku[rowCounter])-1:
            if rowCounter == row_no and colCounter == column_no:
                modifiedSudoku[rowCounter].append(number)
            else:
                modifiedSudoku[rowCounter].append(chubloku[rowCounter][colCounter])
            colCounter += 1
        rowCounter+=1
    return modifiedSudoku
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
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
