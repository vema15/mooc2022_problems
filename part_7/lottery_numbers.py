from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
    lottoNums = range(lower, upper+1)
    weekly_draw = sample(lottoNums, amount)
    return sorted(weekly_draw)


if __name__ == "__main__":
    lottery_numbers(7, 1, 40)