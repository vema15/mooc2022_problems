# Write your solution here

def who_won(game_board: list):
    p1Count = 0
    p2Count = 0
    counter = 0
    while counter <= len(game_board)-1:
        counter2 = 0
        while counter2 <= len(game_board[counter])-1:
            if game_board[counter][counter2] == 1:
                p1Count += 1
            elif game_board[counter][counter2] == 2:
                p2Count += 1
            counter2 += 1
        counter += 1
    winStatus = 0
    if p1Count > p2Count:
        winStatus = 1
    elif p1Count < p2Count:
        winStatus = 2
    else:
        winStatus = 0
    return winStatus

if __name__ == "__main__":
    goBoardList = [[0,1][1,2]]
    print(who_won(goBoardList))