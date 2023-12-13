from fractions import *

def fractionate(amount: int):
    fracList = []
    for i in range(amount):
        fracList.append(Fraction(1, amount))
    return fracList


if __name__ == "__main__":
    print(fractionate(5))
