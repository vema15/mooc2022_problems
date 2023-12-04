# Write your solution here

def row_correct(sudoku: list, row_no: int):
    correctFill = True
    for i in sudoku[row_no]:
        occurrenceCheck = sudoku[row_no].count(i)
        if i == 0:
            continue
        elif occurrenceCheck == 1:
            continue
        elif occurrenceCheck != 1:
            correctFill = False
            break
    return correctFill
        

if __name__ == "__main__":
    sudokuTable = [[9, 0, 0, 0, 8, 0, 3, 0, 0], [2, 0, 0, 2, 5, 0, 7, 0, 0], [0, 2, 0, 3, 0, 0, 0, 0, 4], [2, 9, 4, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 3, 0, 5, 6, 0], [7, 0, 5, 0, 6, 0, 4, 0, 0], [0, 0, 7, 8, 0, 3, 9, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 3], [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(row_correct(sudokuTable, 0))