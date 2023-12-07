# write your solution here
def read_fruits():
    with open('fruits.csv') as fruitsCSV:
        fruitDict = {}
        for line in fruitsCSV:
            line = line.replace("\n", "")
            sepdLine = line.split(";")
            fruitDict[sepdLine[0]] = float(sepdLine[1])
        return fruitDict


if __name__ == "__main__":
    print(read_fruits())