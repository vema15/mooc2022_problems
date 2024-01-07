# Write your solution here
def prime_numbers():
    i = 2
    while i >= 2:
        isPrime = True
        for j in range(2, i-1):
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            yield i
        i += 1
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))