import string

def run(gathered_code: list):
    resultList = []
    locationDict = {}
    currRam = {}
    for letter in string.ascii_uppercase:
        currRam[letter] = 0
    for line in range(len(gathered_code)):
        gathered_code[line] = gathered_code[line].split(" ")
        if gathered_code[line][0] == "END":
            return resultList
        elif gathered_code[line][0] == "PRINT":
            resultList.append(int(currRam[gathered_code[line][1]]))
        elif gathered_code[line][0] == "MOV":
            if gathered_code[line][2] in string.ascii_uppercase:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][2]])
            else:
                currRam[gathered_code[line][1]] = int(gathered_code[line][2])
        elif gathered_code[line][0] == "ADD":
            if gathered_code[line][2] in string.ascii_uppercase:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][1]]) + int(currRam[gathered_code[line][2]])
            else:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][1]]) + int(gathered_code[line][2])
        elif gathered_code[line][0] == "SUB":
            if gathered_code[line][2] in string.ascii_uppercase:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][1]]) - int(currRam[gathered_code[line][2]])
            else:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][1]]) - int(gathered_code[line][2])
        elif gathered_code[line][0] == "MUL":
            if gathered_code[line][2] in string.ascii_uppercase:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][1]]) * int(currRam[gathered_code[line][2]])
            else:
                currRam[gathered_code[line][1]] = int(currRam[gathered_code[line][1]]) * int(gathered_code[line][2])
    return resultList


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
