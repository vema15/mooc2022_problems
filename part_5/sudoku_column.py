# Write your solution here

def column_correct(sudoku: list, column_no: int):
    columnList = []
    counter = 0
    while counter <= len(sudoku)-1:
        columnList.append(sudoku[counter][column_no])
        counter += 1
    columnTruth = True
    counter2 = 0
    while counter2 <= len(columnList)-1:
        occurrenceCount = columnList.count(columnList[counter2])
        if columnList[counter2] == 0:
            counter2+=1
            continue
        elif occurrenceCount == 1:
            counter2 += 1
            continue
        elif occurrenceCount > 1:
            columnTruth = False
            break 
    return columnTruth

        




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

    print(column_correct(sudoku, 0))