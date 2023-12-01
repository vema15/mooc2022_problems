def line(size, character):
    if character == "":
        print("*" * size)
    else:
        print(character * size)

def square(size, character):
    # You should call function line here with proper parameters
    count = 0
    while count < size:
        line(size, character)
        count += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")