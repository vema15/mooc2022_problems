# Write your solution here
def spruce(height):
    whiteSpaceMax = 3 + (2 * (height-2))
    count = 0
    print("a spruce!")
    while count < height:
        spruceRow = 1 + (2 * count)
        iterWhiteSpace = int((whiteSpaceMax - spruceRow)/2)
        print((iterWhiteSpace*" ") + (spruceRow * "*") + iterWhiteSpace*" ")
        count += 1

        if count == (height):
            spruceRow = 1
            iterWhiteSpace = int((whiteSpaceMax - spruceRow)/2)
            print((iterWhiteSpace*" ") + (spruceRow * "*") + iterWhiteSpace*" ")




# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)