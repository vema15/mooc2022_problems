# Write your solution here

def factorials(n: int):
    factorialDict = {}
    counter = 1
    while counter <= n:
        counter2 = 1
        prod = 1
        while counter2 <= counter:
            prod *= counter2
            counter2 += 1
        factorialDict[counter] = prod
        prod = 0
        counter += 1
    return factorialDict

if __name__ == "__main__":
    k = factorials(5)