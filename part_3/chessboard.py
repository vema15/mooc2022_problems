def chessboard(num):
    count = 1
    while count <= num:
        if count % 2 != 0:
            count2 = 1
            rowList = []
            while count2 <= num:
                if count2 % 2 == 0:
                    rowList.append("0")
                elif count2 % 2 != 0:
                    rowList.append("1")
                count2 += 1
            print(*rowList, sep="")
        elif count % 2 == 0:
            count2 = 1
            rowList = []
            while count2 <= num:
                if count2 % 2 == 0:
                    rowList.append("1")
                elif count2 % 2 != 0:
                    rowList.append("0")
                count2 += 1
            print(*rowList, sep="")
        count += 1



if __name__ == "__main__":
    chessboard(3)