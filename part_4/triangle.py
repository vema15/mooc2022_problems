# Copy here code of line function from previous exercise
def line(size):
    print("#" * size)

def triangle(size):
    # You should call function line here with proper parameters
    subAgainst = size - 1
    while subAgainst >= 0:
        line(size-subAgainst)
        subAgainst -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
