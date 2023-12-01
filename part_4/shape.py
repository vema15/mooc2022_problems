# Copy here code of line function from previous exercise and use it in your solution
def line(userString, userInt):
        print(userString * userInt)

def shape(int1, string1, int2, string2):
    decrimentor = int1 - 1
    count = 0

    while decrimentor >= 0:
        line(string1, int1-decrimentor)
        decrimentor -= 1
    
    while count < int2:
        line(string2, int1)
        count += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")