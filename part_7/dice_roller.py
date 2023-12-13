from random import *
def roll(die: str):
    if die == "A":
        sides = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        sides = [2, 2, 2, 5, 5, 5]
    else:
        sides = [1, 4, 4, 4, 4, 4]
    return choice(sides)

def play(die1: str, die2: str, times: int):
    p1Wins = 0
    p2Wins = 0
    ties = 0
    for i in range(1, times+1):
        p1Roll = roll(die1)
        p2Roll = roll(die2)
        if p1Roll > p2Roll:
            p1Wins += 1
        elif p1Roll < p2Roll:
            p2Wins += 1
        elif p1Roll == p2Roll:
            ties += 1
    return (p1Wins, p2Wins, ties)

if __name__ == "__main__":
    print(play("A", "C", 1000))