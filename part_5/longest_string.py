# Write your solution here

def longest(strings: list):
    lengthList = []
    counter = 0
    while counter <= len(strings)-1:
        lengthList.append([len(strings[counter]), counter])
        counter += 1
    sortedLengthList = sorted(lengthList, key=lambda x:x[0])
    return strings[sortedLengthList[len(sortedLengthList)-1][1]]

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))