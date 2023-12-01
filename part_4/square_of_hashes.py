# Copy here code of line function from previous exercise

def line(userString, userInt):
    if userString == "":
        print("*" * userInt)
    else:
        print(userString * userInt)


def square_of_hashes(height):
    count = 0
    while count < height:
        line(height, "#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
